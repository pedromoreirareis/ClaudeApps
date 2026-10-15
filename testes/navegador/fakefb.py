"""(Copiado do Alfabetização v123; o app padrão passou a ser "curiosidades".)
Firebase de mentira para os testes (Playwright intercepta as chamadas).
Imita: login anônimo (identitytoolkit), renovação (securetoken) e o
Firestore REST (GET doc, GET coleção, PATCH com updateMask e com
currentDocument.exists / currentDocument.updateTime)."""
import json, time, threading
from urllib.parse import urlparse, parse_qs, unquote

class FakeFirebase:
    def __init__(self):
        self.docs = {}          # caminho relativo -> {"fields":..., "updateTime":...}
        self.lock = threading.RLock()   # v122: RLock — dois pedidos ao mesmo tempo travavam o teste (o fulfill de um deixa o outro entrar)
        self.chamadas = []      # (metodo, caminho)
        self.negar_versoes = False
        self.negar_tudo = False
        self.antes_de_gravar = None   # gancho: fn(caminho) chamado antes de um PATCH (simula outro celular)
        self.falhar_get_app = False
        self.offline = False          # v122: simula "sem internet" (sem precisar desligar a página toda)   # v122: simula erro ao BAIXAR a ficha de um app (recuperação que falha)
        self._t = 0

    def _now(self):
        self._t += 1
        return '2026-09-23T12:00:%02d.%06dZ' % (self._t // 1000000 % 60, self._t % 1000000)

    def instalar(self, page_or_ctx):
        page_or_ctx.route('**/identitytoolkit.googleapis.com/**', self._auth)
        page_or_ctx.route('**/securetoken.googleapis.com/**', self._auth)
        page_or_ctx.route('**/firestore.googleapis.com/**', self._fs)

    def _auth(self, route):
        if self.offline: return route.abort('internetdisconnected')
        body = {"idToken": "tok", "refreshToken": "ref", "expiresIn": "3600",
                "id_token": "tok", "refresh_token": "ref", "expires_in": "3600"}
        route.fulfill(status=200, content_type='application/json', body=json.dumps(body))

    def _resp(self, route, status, obj):
        route.fulfill(status=status, content_type='application/json',
                      headers={'Access-Control-Allow-Origin': '*'}, body=json.dumps(obj))

    def _fs(self, route):
        req = route.request
        if req.method == 'OPTIONS':
            route.fulfill(status=200, headers={'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': '*'}, body='')
            return
        if self.offline: return route.abort('internetdisconnected')
        u = urlparse(req.url)
        pref = '/documents/'
        caminho = unquote(u.path[u.path.index(pref) + len(pref):])
        qs = parse_qs(u.query)
        self.chamadas.append((req.method, caminho))
        if self.negar_tudo or (self.negar_versoes and '/versoes' in caminho):
            return self._resp(route, 403, {"error": {"code": 403, "message": "Missing or insufficient permissions.", "status": "PERMISSION_DENIED"}})
        with self.lock:
            partes = caminho.split('/')
            if req.method == 'GET':
                if len(partes) % 2 == 1:   # coleção
                    docs = []
                    for k, d in self.docs.items():
                        if k.rsplit('/', 1)[0] == caminho:
                            docs.append({"name": "projects/x/databases/(default)/documents/" + k, "fields": d["fields"], "updateTime": d["updateTime"]})
                    return self._resp(route, 200, {"documents": docs} if docs else {})
                if self.falhar_get_app and '/apps/' in caminho and '/versoes' not in caminho:
                    return self._resp(route, 503, {"error": {"code": 503, "message": "The service is currently unavailable.", "status": "UNAVAILABLE"}})
                d = self.docs.get(caminho)
                if not d:
                    return self._resp(route, 404, {"error": {"code": 404, "message": "not found", "status": "NOT_FOUND"}})
                return self._resp(route, 200, {"name": "projects/x/databases/(default)/documents/" + caminho, "fields": d["fields"], "updateTime": d["updateTime"]})
            if req.method == 'PATCH':
                if self.antes_de_gravar:
                    g = self.antes_de_gravar; self.antes_de_gravar = None
                    g(self, caminho)
                corpo = json.loads(req.post_data or '{}')
                atual = self.docs.get(caminho)
                if 'currentDocument.exists' in qs and qs['currentDocument.exists'][0] == 'false' and atual:
                    return self._resp(route, 400, {"error": {"code": 400, "message": "Document already exists", "status": "ALREADY_EXISTS"}})
                if 'currentDocument.exists' in qs and qs['currentDocument.exists'][0] == 'true' and not atual:
                    return self._resp(route, 404, {"error": {"code": 404, "message": "No document to update", "status": "NOT_FOUND"}})
                if 'currentDocument.updateTime' in qs:
                    if not atual or atual['updateTime'] != qs['currentDocument.updateTime'][0]:
                        return self._resp(route, 400, {"error": {"code": 400, "message": "precondition", "status": "FAILED_PRECONDITION"}})
                campos = corpo.get('fields', {})
                mascara = qs.get('updateMask.fieldPaths')
                if mascara:
                    novo = json.loads(json.dumps(atual['fields'])) if atual else {}
                    for m in mascara:
                        if '.' in m:
                            a, b = m.split('.', 1)
                            novo.setdefault(a, {"mapValue": {"fields": {}}})
                            novo[a].setdefault('mapValue', {}).setdefault('fields', {})
                            novo[a]['mapValue']['fields'][b] = campos[a]['mapValue']['fields'][b]
                        else:
                            novo[m] = campos[m]
                    campos = novo
                ut = self._now()
                self.docs[caminho] = {"fields": campos, "updateTime": ut}
                return self._resp(route, 200, {"name": "projects/x/databases/(default)/documents/" + caminho, "fields": campos, "updateTime": ut})
        route.fulfill(status=405, body='')

    # ajudantes para os testes
    def dados_app(self, chave_usuario, app='curiosidades', familia='familiateste'):
        d = self.docs.get('familias/%s/usuarios/%s/apps/%s' % (familia, chave_usuario, app))
        if not d: return None
        return json.loads(d['fields']['dados']['stringValue'])

    def ficha(self, chave_usuario, familia='familiateste'):
        d = self.docs.get('familias/%s/usuarios/%s' % (familia, chave_usuario))
        return d['fields'] if d else None

    def gravar_app(self, chave_usuario, nome, av, dados, app='curiosidades', familia='familiateste', dispositivo='outroCelular'):
        base = 'familias/%s/usuarios/%s' % (familia, chave_usuario)
        ut = self._now()
        self.docs[base + '/apps/' + app] = {"updateTime": ut, "fields": {
            "nome": {"stringValue": nome}, "av": {"stringValue": av}, "app": {"stringValue": app},
            "dados": {"stringValue": json.dumps(dados)}, "atualizadoEm": {"integerValue": str(int(time.time() * 1000))},
            "dispositivo": {"stringValue": dispositivo}, "versao": {"stringValue": "3"}}}
        perfil = self.docs.get(base, {"fields": {"nome": {"stringValue": nome}, "av": {"stringValue": av}, "apps": {"mapValue": {"fields": {}}}}})
        perfil["fields"]["apps"]["mapValue"]["fields"][app] = {"integerValue": "1"}
        perfil["updateTime"] = self._now()
        self.docs[base] = perfil
