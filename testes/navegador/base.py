"""(Copiado do Alfabetização v123 e adaptado ao Curiosidades: pasta do pacote e cadastrar.)
Base comum dos testes com navegador de verdade (Chromium via Playwright).
Sobe um servidor local com a pasta do pacote e oferece ajudantes."""
import os, sys, json, threading, functools, http.server, socketserver, time
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(__file__))
from fakefb import FakeFirebase

PASTA = os.environ.get('PASTA_PACOTE', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'pacote-netlify'))
PORTA = int(os.environ.get('PORTA', '8775'))   # v2.0: 8775 (o teste_nuvem_v20.py usa 8765 e 8766)

CFG_TESTE = """window.NUVEM_CONFIG={apiKey:'chave-de-teste',projectId:'projeto-teste',familia:''};"""
CFG_VAZIA = """const firebaseConfig={apiKey:"",projectId:""};const codigoDaFamilia="";
window.NUVEM_CONFIG={apiKey:'',projectId:'',familia:''};"""

class _H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

_srv = None
def servidor():
    global _srv
    if _srv: return
    h = functools.partial(_H, directory=os.path.abspath(PASTA))
    socketserver.TCPServer.allow_reuse_address = True
    _srv = socketserver.ThreadingTCPServer(('127.0.0.1', PORTA), h)
    threading.Thread(target=_srv.serve_forever, daemon=True).start()

URL = 'http://localhost:%d/' % PORTA

class R:
    def __init__(self, nome):
        self.nome = nome; self.ok = 0; self.falhas = []
        print('\n=== ' + nome)
    def t(self, desc, cond, extra=''):
        if cond: self.ok += 1; print('  OK    ' + desc)
        else: self.falhas.append(desc); print('  FALHA ' + desc + ('  :: ' + str(extra) if extra else ''))
    def fim(self):
        tot = self.ok + len(self.falhas)
        print('%d/%d passou' % (self.ok, tot))
        return self.ok, tot

def novo_contexto(browser, fb=None, config='teste', largura=740, altura=360, offline=False, familia=None, storage=None, service_worker='block', convite=False):
    ctx = browser.new_context(viewport={'width': largura, 'height': altura}, service_workers=service_worker,
                              has_touch=True, is_mobile=False)
    # NUNCA falar com o Firebase de verdade nos testes
    if fb is None: fb = FakeFirebase()
    fb.instalar(ctx)
    if config == 'teste':
        ctx.route('**/nuvem-config.js', lambda r: r.fulfill(status=200, content_type='application/javascript', body=CFG_TESTE))
    elif config == 'vazia':
        ctx.route('**/nuvem-config.js', lambda r: r.fulfill(status=200, content_type='application/javascript', body=CFG_VAZIA))
    elif config == 'falta':
        ctx.route('**/nuvem-config.js', lambda r: r.fulfill(status=404, body='nao existe'))
    init = []
    # o convite de instalar aparece sozinho em 2,5 s; fora dos testes dele, marca como 'visto agora'
    if not convite: init.append("localStorage.setItem('escola_conviteVisto', String(Date.now()));")
    if familia: init.append("localStorage.setItem('nuvem_familia', %s);" % json.dumps(familia))
    if storage:
        for k, v in storage.items(): init.append("localStorage.setItem(%s,%s);" % (json.dumps(k), json.dumps(v)))
    if init:
        # só na 1ª carga (marca própria), pra não repetir a cada reload
        ctx.add_init_script("if(!sessionStorage.getItem('__ini')){sessionStorage.setItem('__ini','1');" + ''.join(init) + "}")
    return ctx, fb

def abrir(ctx, erros=None):
    p = ctx.new_page()
    if erros is not None:
        p.on('pageerror', lambda e: erros.append(str(e)))
        p.on('dialog', lambda d: (erros.append('CAIXINHA NATIVA DO NAVEGADOR: '+d.message), d.dismiss()))
        p.on('console', lambda m: erros.append('console.error: ' + m.text) if m.type == 'error' and 'favicon' not in m.text and 'net::ERR' not in m.text else None)
    p.goto(URL, wait_until='load')
    p.wait_for_timeout(600)
    return p

def ls(p, k):
    return p.evaluate("k=>{ return Storage.prototype.getItem.call(localStorage,k) }", k)

def ls_bruto(p):
    return p.evaluate("""()=>{ const o={}; for(let i=0;i<localStorage.length;i++){ const k=localStorage.key(i); o[k]=localStorage.getItem.call? null:null; }
      const r={}; const n=localStorage.length; for(let i=0;i<n;i++){ const k=localStorage.key(i); r[k]=window._rawGet?_rawGet(k):null; } return r; }""")

def cadastrar(p, nome, bicho_idx):
    """cadastra pela T5 do escola-familia.js (o Curiosidades não recarrega a página)"""
    p.fill('#efRaiz .ef-nome-campo', nome)
    p.locator('#efRaiz .ef-bicho').nth(bicho_idx).click()
    p.click('#efRaiz .ef-pronto')
    p.wait_for_timeout(1500)
