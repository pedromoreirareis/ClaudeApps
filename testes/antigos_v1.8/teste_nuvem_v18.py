import json, threading, http.server, socketserver, functools, time, sys, re, urllib.parse
from playwright.sync_api import sync_playwright

PORTA = 8765
def servir(pasta, porta):
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self,*a): pass
    socketserver.TCPServer.allow_reuse_address=True
    srv = socketserver.ThreadingTCPServer(('127.0.0.1', porta), functools.partial(Q, directory=pasta))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv
srv1 = servir('/home/claude/t/site', PORTA)          # com nuvem configurada
srv2 = servir('/home/claude/z', PORTA+1)             # sem configurar (como vai para o Pedro)

# ---------------- Firebase de mentira ----------------
NUVEM = {}      # caminho -> fields
UPD = {}        # caminho -> updateTime
CONT = {'n':0}
INJETAR = {}    # caminho -> função chamada logo depois de um GET desse doc (simula outro celular)
def carimbo():
    CONT['n'] += 1
    return '2026-09-23T12:00:%02d.%06dZ' % (CONT['n'] % 60, CONT['n'])
def erro(status, cod, msg):
    return dict(status=status, content_type='application/json', body=json.dumps({'error':{'code':status,'message':msg,'status':cod}}))
LOG = []
FALHAR = {'on': False}
def fake(route, request):
    url = request.url; m = request.method
    LOG.append((m, url.split('?')[0][-90:]))
    if FALHAR['on']:
        return route.abort('internetdisconnected')
    if 'identitytoolkit' in url or 'securetoken' in url:
        return route.fulfill(status=200, content_type='application/json',
            body=json.dumps({'idToken':'tok','refreshToken':'ref','expiresIn':'3600','id_token':'tok','refresh_token':'ref','expires_in':'3600'}))
    if 'firestore.googleapis.com' in url:
        assert request.headers.get('authorization') == 'Bearer tok'
        u = urllib.parse.urlparse(url)
        cam = urllib.parse.unquote(u.path.split('/documents/')[1])
        qs = urllib.parse.parse_qs(u.query)
        partes = cam.split('/')
        if m == 'PATCH':
            corpo = json.loads(request.post_data)
            campos = corpo['fields']
            if 'currentDocument.exists' in qs and qs['currentDocument.exists'][0]=='false' and cam in NUVEM:
                return route.fulfill(**erro(409,'ALREADY_EXISTS','Document already exists'))
            if 'currentDocument.updateTime' in qs and UPD.get(cam) != qs['currentDocument.updateTime'][0]:
                return route.fulfill(**erro(400,'FAILED_PRECONDITION','the stored version does not match the required base version'))
            if 'updateMask.fieldPaths' in qs:
                atual = NUVEM.get(cam, {})
                for fp in qs['updateMask.fieldPaths']:
                    if '.' in fp:
                        a, b = fp.split('.',1)
                        mp = atual.setdefault(a, {'mapValue':{'fields':{}}})
                        mp['mapValue'].setdefault('fields',{})[b] = campos[a]['mapValue']['fields'][b]
                    else:
                        atual[fp] = campos[fp]
                NUVEM[cam] = atual
            else:
                NUVEM[cam] = campos
            UPD[cam] = carimbo()
            return route.fulfill(status=200, content_type='application/json', body=json.dumps({'name':cam,'fields':NUVEM[cam],'updateTime':UPD[cam]}))
        if m == 'GET':
            if len(partes) % 2 == 1:   # coleção
                docs = [{'name':'projects/x/databases/(default)/documents/'+k, 'fields':v} for k,v in NUVEM.items()
                        if k.startswith(cam+'/') and k.count('/') == cam.count('/')+1]
                return route.fulfill(status=200, content_type='application/json', body=json.dumps({'documents':docs} if docs else {}))
            if cam in NUVEM:
                resp = json.dumps({'name':cam,'fields':NUVEM[cam],'updateTime':UPD.get(cam,'')})
                f = INJETAR.pop(cam, None)
                if f: f(cam)
                return route.fulfill(status=200, content_type='application/json', body=resp)
            return route.fulfill(status=404, content_type='application/json', body=json.dumps({'error':{'code':404,'message':'not found','status':'NOT_FOUND'}}))
    return route.continue_()

def doc_app(chave):
    for k,v in NUVEM.items():
        if k.endswith('/usuarios/'+chave+'/apps/curiosidades'):
            return v
    return None
def lidas_nuvem(chave):
    d = doc_app(chave)
    if not d: return None
    return json.loads(json.loads(d['dados']['stringValue']).get('lidas','{}'))

RES = []
def ok(nome, cond, extra=''):
    RES.append((nome, bool(cond)))
    print(('✅' if cond else '❌'), nome, extra)

WAKE = '''
window.__wake={pedidos:0,soltos:0};
try{
 Object.defineProperty(navigator,'wakeLock',{configurable:true,value:{request:function(t){
   window.__wake.pedidos++;
   const ls=[]; const s={released:false,type:t,addEventListener:(e,f)=>{ if(e==='release') ls.push(f); },
     release:function(){ if(s.released) return Promise.resolve(); s.released=true; window.__wake.soltos++; ls.forEach(f=>f()); return Promise.resolve(); }};
   window.__wakeAtual=s; return Promise.resolve(s);
 }}});
}catch(e){}
'''

def novo_ctx(browser, url_base):
    ctx = browser.new_context(viewport={'width':900,'height':420}, service_workers='block')
    ctx.add_init_script(WAKE + "try{ localStorage.setItem('escola_conviteVisto',String(Date.now())); }catch(e){}")
    ctx.route(re.compile(r'https://(identitytoolkit|securetoken|firestore)\.googleapis\.com/.*'), fake)
    pg = ctx.new_page()
    erros = []
    pg.on('pageerror', lambda e: erros.append(str(e)))
    pg.on('dialog', lambda d: d.accept('Familia Teste 2026') if d.type=='prompt' else d.accept())
    pg.goto(url_base + '/index.html'); pg.wait_for_timeout(600)
    return ctx, pg, erros

def marcar(pg, code, idx):
    pg.evaluate('''([code,idx])=>{ paisIdx=DATA.findIndex(p=>p.code===code); curIdx=idx; openReader(); toggleLida(); goHome(); }''', [code, idx])

with sync_playwright() as p:
    br = p.chromium.launch()

    # ===== A) SEM configuração: app funciona igual, nuvem escondida =====
    ctx, pg, erros = novo_ctx(br, 'http://127.0.0.1:%d' % (PORTA+1))
    ok('A1 sem config: abre o cadastro sem erros', pg.is_visible('#novoUser') and not erros, erros)
    ok('A2 sem config: botão "recuperar" escondido', not pg.is_visible('#nuNuvem'))
    pg.fill('#nuNome','Ana'); pg.click('.nuEmoji >> nth=1'); pg.click('.nuPronto'); pg.wait_for_timeout(300)
    marcar(pg, DATA_CODE := pg.evaluate('DATA[0].code'), 0)
    ok('A3 sem config: marcar LIDA continua salvando', '1' in (pg.evaluate("localStorage.getItem(K('lidas'))") or ''))
    st = pg.evaluate("NuvemSync.status()")
    ok('A4 sem config: estado desligada', st['estado']=='desligada', st)
    ok('A5 sem config: ponto da nuvem escondido', not pg.is_visible('#nuvemPonto'))
    ok('A6 sem config: nenhuma chamada ao Firebase', len(LOG)==0, LOG[:3])
    ok('A7 tela acesa pedida ao abrir', pg.evaluate('window.__wake.pedidos')>=1, pg.evaluate('window.__wake'))
    # voltar do segundo plano pede de novo
    pg.evaluate("window.__wakeAtual.release()"); pg.wait_for_timeout(1200)
    ok('A8 tela acesa: se o sistema soltar, pede de novo', pg.evaluate('window.__wake.pedidos')>=2, pg.evaluate('window.__wake'))
    pg.evaluate("openCfg()"); pg.wait_for_timeout(100)
    ok('A9 config mostra "Tela sempre acesa" ligada', pg.evaluate("document.getElementById('cfgTela').classList.contains('on')"))
    txt = pg.inner_text('#cfgNuvemSt')
    ok('A10 config explica que falta nuvem-config', 'nuvem-config' in txt, txt)
    pg.evaluate("alternaTelaAcesa()"); pg.wait_for_timeout(100)
    ok('A11 desligar tela acesa solta o pedido', pg.evaluate('window.__wake.soltos')>=2 and pg.evaluate("localStorage.getItem('mundo_telaAcesa')")=='0')
    ctx.close()

    # ===== B) COM configuração — celular 1 =====
    base = 'http://127.0.0.1:%d' % PORTA
    ctx, pg, erros = novo_ctx(br, base)
    ok('B1 com config, sem código: abre sem erros', not erros, erros)
    ok('B2 botão "já li antes" aparece', pg.is_visible('#nuNuvem'))
    pg.fill('#nuNome','Renata'); pg.evaluate("nuEmoji='🦋'"); pg.click('.nuPronto'); pg.wait_for_timeout(300)
    c0 = pg.evaluate('DATA[0].code'); c5 = pg.evaluate('DATA[5].code')
    marcar(pg, c0, 0); marcar(pg, c0, 2); marcar(pg, c5, 1)
    ok('B3 sem código da família: nada enviado ainda', not any('firestore' in u for _,u in LOG))
    st = pg.evaluate("NuvemSync.status()")
    ok('B4 pendências guardadas no celular', st['pendentes']>=1 and st['estado']=='sem-codigo', st)
    pg.evaluate("pedirCodigoFamilia(false)"); pg.fill('#codigoInput','Familia Teste 2026'); pg.click('#codigoOkBtn')   # v1.8: popup próprio
    pg.wait_for_timeout(2500)
    chave = pg.evaluate("NuvemSync.chaveUsuario('Renata','🦋')")
    ok('B5 chave do leitor = nome + bichinho', chave=='renata_1f98b', chave)
    ln = lidas_nuvem(chave)
    ok('B6 progresso subiu para a nuvem', ln and ln.get(c0,'').startswith('101') and ln.get(c5,'')[1:2]=='1', ln)
    ok('B7 caminho usa o código da família', any('familias/familia-teste-2026/usuarios/renata_1f98b' in k for k in NUVEM), list(NUVEM)[:3])
    perfil = NUVEM.get('familias/familia-teste-2026/usuarios/renata_1f98b')
    ok('B8 perfil do leitor com nome/bichinho/app', perfil and perfil['nome']['stringValue']=='Renata' and 'curiosidades' in perfil['apps']['mapValue']['fields'], perfil)
    ok('B9 estado ok e sem pendências', pg.evaluate("NuvemSync.status().estado")=='ok' and pg.evaluate("NuvemSync.status().pendentes")==0, pg.evaluate("NuvemSync.status()"))
    ok('B10 ponto verde no ⚙️', 'ok' in (pg.get_attribute('#nuvemPonto','class') or ''))

    # --- offline: fila de pré-sincronização ---
    ctx.set_offline(True); FALHAR['on']=True
    pg.evaluate("window.dispatchEvent(new Event('offline'))")
    marcar(pg, c0, 4); marcar(pg, c0, 5)
    pg.wait_for_timeout(5000)
    st = pg.evaluate("NuvemSync.status()")
    ok('B11 offline: marcação salva no celular', pg.evaluate("JSON.parse(localStorage.getItem(K('lidas')))['%s']" % c0).startswith('101011'))
    ok('B12 offline: fica na fila (pendente) e estado offline', st['pendentes']>=1 and st['estado']=='offline', st)
    ok('B13 offline: nuvem ainda sem as novas', not lidas_nuvem(chave)[c0].startswith('101011'))
    ctx.set_offline(False); FALHAR['on']=False
    pg.evaluate("window.dispatchEvent(new Event('online'))"); pg.wait_for_timeout(2500)
    ok('B14 voltou a internet: fila enviada sozinha', lidas_nuvem(chave)[c0].startswith('101011') and pg.evaluate("NuvemSync.status().pendentes")==0, lidas_nuvem(chave)[c0])
    # desmarcar também sobe
    marcar(pg, c0, 5); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(2500)
    ok('B15 desmarcar também vai para a nuvem', lidas_nuvem(chave)[c0].startswith('101010'), lidas_nuvem(chave)[c0])
    # favorita
    pg.evaluate("favs['%s:3']=1; saveState();" % c5); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(2500)
    ok('B16 favoritas vão para a nuvem', '%s:3' % c5 in json.loads(json.loads(doc_app(chave)['dados']['stringValue'])['favs']))
    ok('B17 nenhum erro de página no celular 1', not erros, erros)
    # tempo de desmarcar em segundo plano (visibilitychange hidden) não quebra
    ctx.close()

    # ===== C) Dados do navegador APAGADOS — recuperar pela tela =====
    ctx, pg, erros = novo_ctx(br, base)
    ok('C1 celular limpo: abre no cadastro', pg.is_visible('#novoUser'))
    pg.click('#nuNuvem'); pg.wait_for_timeout(300)
    ok('C2 tela "recuperar" pede o código', 'código da família' in pg.inner_text('#nuvemMsg'), pg.inner_text('#nuvemMsg'))
    pg.click('text=🔑 Código da família'); pg.fill('#codigoInput','Familia Teste 2026'); pg.click('#codigoOkBtn'); pg.wait_for_timeout(2000)   # v1.8: popup próprio
    cards = pg.locator('#nuvemGrid .userCard')
    ok('C3 lista mostra Renata 🦋 da nuvem', cards.count()==1 and 'Renata' in cards.first.inner_text(), pg.inner_text('#nuvemGrid'))
    cards.first.click(); pg.wait_for_timeout(1500)
    lid = pg.evaluate("lidas['%s']" % c0)
    ok('C4 progresso de Renata recuperado', lid and lid.startswith('10101') and pg.evaluate("lidas['%s'][1]" % c5)=='1', lid)
    ok('C5 favorita recuperada', pg.evaluate("!!favs['%s:3']" % c5))
    ok('C6 usuário local criado com o mesmo nome/bichinho', pg.evaluate("U.us.length===1 && U.us[0].nome==='Renata' && U.us[0].av==='🦋'"))
    ok('C7 está na tela inicial', pg.is_visible('#home'))
    # neste celular marca uma nova
    marcar(pg, c5, 7); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(2500)
    ok('C8 nova marcação no celular 2 sobe sem apagar as antigas', lidas_nuvem(chave)[c0].startswith('10101') and lidas_nuvem(chave)[c5][7]=='1', lidas_nuvem(chave))
    ok('C9 sem erros', not erros, erros)
    ctx.close()

    # ===== D) Outro celular cadastra "Renata 🦋" de novo — volta sozinho =====
    ctx, pg, erros = novo_ctx(br, base)
    pg.evaluate("localStorage.setItem('nuvem_familia','familia-teste-2026')"); pg.reload(); pg.wait_for_timeout(600)
    pg.fill('#nuNome','Renata'); pg.evaluate("nuEmoji='🦋'"); pg.click('.nuPronto'); pg.wait_for_timeout(2500)
    ok('D1 cadastro com mesmo nome+bichinho recupera sozinho', pg.evaluate("(lidas['%s']||'').startsWith('10101') && lidas['%s'][7]==='1'" % (c0,c5)), pg.evaluate("lidas"))
    pg.wait_for_timeout(5000)
    ok('D2 nuvem continua com tudo (não foi apagada pelo cadastro novo)', lidas_nuvem(chave)[c0].startswith('10101') and lidas_nuvem(chave)[c5][7]=='1', lidas_nuvem(chave))
    # leitor novo diferente não herda nada
    pg.evaluate("abrirNovoUser()"); pg.fill('#nuNome','Pedro'); pg.evaluate("nuEmoji='🐯'"); pg.click('.nuPronto'); pg.wait_for_timeout(2500)
    ok('D3 leitor diferente começa do zero', pg.evaluate("Object.keys(lidas).length")==0)
    ok('D4 sem erros', not erros, erros)
    ctx.close()

    # ===== E) Mistura entre celulares ao abrir =====
    # celular E1 já tem Renata com X; nuvem tem Y (de outro aparelho) -> junta
    ctx, pg, erros = novo_ctx(br, base)
    pg.evaluate("localStorage.setItem('nuvem_familia','familia-teste-2026')")
    pg.evaluate("""()=>{ const id='p111'; localStorage.setItem('mundo_usuarios',JSON.stringify({us:[{id:id,nome:'Renata',av:'🦋'}],atual:id}));
       const l={}; l['%s']='0000000001'; localStorage.setItem('mundo_'+id+'_lidas',JSON.stringify(l)); localStorage.setItem('mundo_'+id+'_theme','3'); }""" % c0)
    pg.reload(); pg.wait_for_timeout(4500)
    loc = pg.evaluate("JSON.parse(localStorage.getItem('mundo_p111_lidas'))['%s']" % c0)
    ok('E1 abrir junta o que tinha no celular com o da nuvem', loc.startswith('1010100001'), loc)
    ok('E2 preferência do celular (cores) é mantida', pg.evaluate("localStorage.getItem('mundo_p111_theme')")=='3')
    pg.wait_for_timeout(4500)
    ok('E3 nuvem recebe o resultado juntado', lidas_nuvem(chave)[c0].startswith('1010100001'), lidas_nuvem(chave)[c0])
    ok('E4 sem erros', not erros, erros)

    # ===== F) Regressão básica =====
    pg.evaluate("abrirBusca()"); pg.fill('#buscaInput','egito'); pg.wait_for_timeout(500)
    ok('F1 busca continua funcionando', pg.locator('.buscaGrupo').count()>=1)
    pg.evaluate("fecharBusca()")
    pg.evaluate("mudaFontSize(1)"); ok('F2 tamanho da letra muda', pg.evaluate("FSIZES[fsizeIdx]")==18)
    pg.evaluate("openCfg()"); pg.wait_for_timeout(200)
    ok('F3 config mostra situação da nuvem', 'nuvem' in pg.inner_text('#cfgNuvemSt').lower() or '✅' in pg.inner_text('#cfgNuvemSt'), pg.inner_text('#cfgNuvemSt'))
    ok('F4 código aparece mascarado', '•••' in pg.inner_text('#cfgNuvemFam'), pg.inner_text('#cfgNuvemFam'))
    pg.screenshot(path='/home/claude/t/cfg.png')
    pg.evaluate("closeCfg(); abrirNuvemTela()"); pg.wait_for_timeout(1500)
    pg.screenshot(path='/home/claude/t/nuvemtela.png')
    ok('F5 sem erros no fim', not erros, erros)
    ctx.close()

    # ===== G) Erro de regra (PERMISSION_DENIED) aparece em português =====
    def negar(route, request):
        if 'firestore' in request.url:
            return route.fulfill(status=403, content_type='application/json', body=json.dumps({'error':{'code':403,'message':'Missing or insufficient permissions.','status':'PERMISSION_DENIED'}}))
        return fake(route, request)
    ctx = br.new_context(viewport={'width':900,'height':420}, service_workers='block')
    ctx.route(re.compile(r'https://(identitytoolkit|securetoken|firestore)\.googleapis\.com/.*'), negar)
    pg = ctx.new_page(); pg.goto(base+'/index.html'); pg.wait_for_timeout(400)
    pg.evaluate("localStorage.setItem('nuvem_familia','familia-teste-2026')"); pg.reload(); pg.wait_for_timeout(400)
    pg.fill('#nuNome','Zé'); pg.click('.nuEmoji >> nth=6'); pg.click('.nuPronto'); pg.wait_for_timeout(300)
    marcar(pg, c0, 0); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(2500)
    st = pg.evaluate("NuvemSync.status()")
    ok('G1 erro de regras explicado em português', st['estado']=='erro' and 'Regras' in st['detalhe'], st)
    ok('G2 marcação continua salva no celular mesmo com erro', '1' in pg.evaluate("localStorage.getItem(K('lidas'))"))
    ctx.close()
    # ===== H) Dois celulares gravando ao mesmo tempo (trava de versão) =====
    ctx, pg, erros = novo_ctx(br, base)
    pg.evaluate("localStorage.setItem('nuvem_familia','familia-teste-2026')"); pg.reload(); pg.wait_for_timeout(600)
    pg.fill('#nuNome','Renata'); pg.evaluate("nuEmoji='🦋'"); pg.click('.nuPronto'); pg.wait_for_timeout(3000)
    caminho = 'familias/familia-teste-2026/usuarios/renata_1f98b/apps/curiosidades'
    def outro_celular_grava(cam):
        d = json.loads(NUVEM[cam]['dados']['stringValue'])
        l = json.loads(d.get('lidas','{}')); c = DATA_C9
        l[c] = '0000000000001'
        d['lidas'] = json.dumps(l)
        NUVEM[cam] = dict(NUVEM[cam]); NUVEM[cam]['dados'] = {'stringValue': json.dumps(d)}
        NUVEM[cam]['dispositivo'] = {'stringValue': 'celular-do-meio'}
        UPD[cam] = carimbo()
    DATA_C9 = pg.evaluate('DATA[9].code')
    INJETAR[caminho] = outro_celular_grava
    marcar(pg, c0, 8); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(3000)
    ln = lidas_nuvem(chave)
    ok('H1 outro celular gravou no meio: nada se perdeu na nuvem', ln.get(DATA_C9,'').endswith('1') and ln[c0][8]=='1', {DATA_C9: ln.get(DATA_C9), c0: ln[c0]})
    ok('H2 e este celular também recebeu a do outro', pg.evaluate("(lidas['%s']||'').slice(-1)" % DATA_C9)=='1')
    # relógio errado no outro celular (data antiga) não impede de juntar
    d = json.loads(NUVEM[caminho]['dados']['stringValue']); l = json.loads(d['lidas'])
    c11 = pg.evaluate('DATA[11].code'); l[c11] = '01'; d['lidas'] = json.dumps(l)
    NUVEM[caminho] = dict(NUVEM[caminho]); NUVEM[caminho]['dados'] = {'stringValue': json.dumps(d)}
    NUVEM[caminho]['dispositivo'] = {'stringValue':'celular-relogio-atrasado'}; NUVEM[caminho]['atualizadoEm'] = {'integerValue':'1000'}
    UPD[caminho] = carimbo()
    marcar(pg, c0, 9); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(3000)
    ln = lidas_nuvem(chave)
    ok('H3 celular com relógio atrasado: junta mesmo assim', ln.get(c11)=='01' and ln[c0][9]=='1', {c11: ln.get(c11), c0: ln[c0]})
    ok('H4 sem erros', not erros, erros)
    ctx.close()

    # ===== P) PWA: convite para instalar, tela cheia e modo reserva da tela acesa =====
    SPY = """
    window.__fs=0;
    const _rf=Element.prototype.requestFullscreen;
    Element.prototype.requestFullscreen=function(){ window.__fs++; return _rf ? _rf.apply(this,arguments).catch(()=>{}) : Promise.resolve(); };
    """
    def ctx_pwa(init_extra='', online_base=base):
        c = br.new_context(viewport={'width':900,'height':420}, service_workers='block')
        c.add_init_script(SPY + init_extra)
        c.route(re.compile(r'https://(identitytoolkit|securetoken|firestore)\.googleapis\.com/.*'), fake)
        p_ = c.new_page(); er = []; p_.on('pageerror', lambda e: er.append(str(e)))
        p_.on('dialog', lambda d: d.accept())
        p_.goto(online_base + '/index.html'); p_.wait_for_timeout(400)
        return c, p_, er
    # P1: sem o evento do Chrome → instruções manuais
    ctx, pg, erros = ctx_pwa()
    pg.wait_for_timeout(2800)
    ok('P1 abriu pelo navegador: convite aparece sozinho', pg.is_visible('#escolaConvite'))
    ok('P2 sem botão nativo: mostra os passos (⋮ → Instalar app)', 'Instalar app' in pg.inner_text('#escolaConvite'))
    pg.screenshot(path='/home/claude/t/convite_passos.png')
    fsA = pg.evaluate('window.__fs')
    pg.click('#ecAgoraNao'); pg.wait_for_timeout(200)
    ok('P3 "Entendi" fecha', not pg.is_visible('#escolaConvite'))
    fs0 = pg.evaluate('window.__fs') - fsA
    ok('P4 tocar no botão do convite NÃO pediu tela cheia (não atrapalha)', fs0==0, fs0)
    pg.reload(); pg.wait_for_timeout(2800)
    ok('P4b reabriu logo em seguida: não fica insistindo depois do "Entendi"', not pg.is_visible('#escolaConvite'))
    pg.evaluate("localStorage.setItem('escola_conviteVisto', String(Date.now()-11*60*1000))"); pg.reload(); pg.wait_for_timeout(2800)
    ok('P4c abriu de novo mais tarde, ainda sem instalar: oferece de novo', pg.is_visible('#escolaConvite'))
    pg.click('#ecAgoraNao'); pg.wait_for_timeout(200)
    pg.click('.nuPronto'); pg.wait_for_timeout(300)   # botão comum
    ok('P5 toque comum pede tela cheia', pg.evaluate('window.__fs')>=1, pg.evaluate('window.__fs'))
    n = pg.evaluate('window.__fs'); pg.click('#nuNome'); pg.wait_for_timeout(200)
    ok('P6 tocar no campo de digitar não força tela cheia', pg.evaluate('window.__fs')==n)
    ctx.close()
    # nova visita (abriu o app de novo pelo navegador) e o Chrome libera a instalação
    ctx, pg, erros = ctx_pwa()
    pg.evaluate("""()=>{ const e=new Event('beforeinstallprompt',{cancelable:true});
       window.__promptou=0; e.prompt=()=>{ window.__promptou++; return Promise.resolve(); };
       e.userChoice=Promise.resolve({outcome:'accepted'}); window.dispatchEvent(e); }""")
    pg.wait_for_timeout(2800)
    ok('P7 nova visita + Chrome liberou: convite aparece com botão "Instalar agora"', pg.is_visible('#ecInstalar'))
    pg.screenshot(path='/home/claude/t/convite_botao.png')
    pg.click('#ecInstalar'); pg.wait_for_timeout(400)
    ok('P8 "Instalar agora" chama a instalação do Chrome', pg.evaluate('window.__promptou')==1)
    ok('P9 depois de instalar, convite some e fica marcado', not pg.is_visible('#escolaConvite') and pg.evaluate("localStorage.getItem('escola_instalado')")=='1')
    ok('P10 sem erros', not erros, erros)
    ctx.close()
    # P11: aberto como app instalado (display-mode fullscreen) → nunca convida
    FAKEMM = """
    const _mm=window.matchMedia.bind(window);
    window.matchMedia=function(q){ if(/display-mode:\\s*fullscreen/.test(q)) return {matches:true,media:q,addListener(){},removeListener(){},addEventListener(){},removeEventListener(){}}; return _mm(q); };
    """
    ctx, pg, erros = ctx_pwa(FAKEMM)
    pg.wait_for_timeout(2800)
    ok('P11 aberto pelo ícone (instalado): sem convite', not pg.is_visible('#escolaConvite'))
    pg.evaluate("openCfg()"); pg.wait_for_timeout(100)
    ok('P12 instalado: linha "Instalar" some das Configurações', not pg.is_visible('#cfgInstRow'))
    ctx.close()
    # P13: Wake Lock recusado → modo reserva (vídeo)
    REJ = """Object.defineProperty(navigator,'wakeLock',{configurable:true,value:{request:()=>Promise.reject(Object.assign(new Error('x'),{name:'NotAllowedError'}))}});"""
    ctx, pg, erros = ctx_pwa(REJ)
    pg.wait_for_timeout(800); pg.click('body', position={'x':5,'y':400}); pg.wait_for_timeout(800)
    tem_video = pg.evaluate("!!document.querySelector('video')")
    st = pg.evaluate("EscolaPWA.estado().telaAcesa")
    ok('P13 celular recusou o Wake Lock: liga o modo reserva (vídeo mudo)', tem_video, st)
    ok('P14 vídeo reserva está tocando', st['modo']=='reserva', st)
    pg.evaluate("openCfg()"); pg.wait_for_timeout(100)
    ok('P15 config mostra modo reserva', 'reserva' in pg.inner_text('#cfgTelaSt'), pg.inner_text('#cfgTelaSt'))
    ok('P16 sem erros', not erros, erros)
    ctx.close()
    # P17: sem Wake Lock nenhum no navegador → modo reserva também
    NOWL = """try{ delete Navigator.prototype.wakeLock; }catch(e){} Object.defineProperty(navigator,'wakeLock',{configurable:true,get:()=>undefined}); try{ delete navigator.wakeLock; }catch(e){}"""
    ctx, pg, erros = ctx_pwa(NOWL)
    pg.wait_for_timeout(600); pg.click('body', position={'x':5,'y':400}); pg.wait_for_timeout(800)
    ok('P17 navegador sem Wake Lock: usa o modo reserva', pg.evaluate("EscolaPWA.estado().telaAcesa.modo")=='reserva', pg.evaluate("EscolaPWA.estado().telaAcesa"))
    ctx.close()

    # ===== V) Histórico de versões, envio rápido, armazenamento persistente =====
    PERS = """window.__persist=0; try{ navigator.storage.persisted=()=>Promise.resolve(false); navigator.storage.persist=()=>{ window.__persist++; return Promise.resolve(true); }; }catch(e){}"""
    ctx = br.new_context(viewport={'width':900,'height':420}, service_workers='block')
    ctx.add_init_script(WAKE + PERS + "try{ localStorage.setItem('escola_conviteVisto',String(Date.now())); }catch(e){}")
    ctx.route(re.compile(r'https://(identitytoolkit|securetoken|firestore)\.googleapis\.com/.*'), fake)
    pg = ctx.new_page(); erros=[]; pg.on('pageerror', lambda e: erros.append(str(e))); pg.on('dialog', lambda d: d.accept())
    pg.goto(base+'/index.html'); pg.wait_for_timeout(400)
    pg.evaluate("localStorage.setItem('nuvem_familia','familia-teste-2026')"); pg.reload(); pg.wait_for_timeout(500)
    ok('V1 pede armazenamento persistente ao navegador', pg.evaluate('window.__persist')>=1)
    pg.fill('#nuNome','Renata'); pg.evaluate("nuEmoji='🦋'"); pg.click('.nuPronto'); pg.wait_for_timeout(3500)
    c15 = pg.evaluate('DATA[15].code')
    marcar(pg, c15, 2); pg.wait_for_timeout(2600)
    ok('V2 envio rápido: ~1,5 s depois de marcar já está na nuvem', (lidas_nuvem(chave).get(c15,'')+'000')[2]=='1', lidas_nuvem(chave).get(c15))
    import datetime
    hoje = pg.evaluate("(()=>{const d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');})()")
    cam_v = caminho + '/versoes/' + hoje
    ok('V3 cópia do dia guardada em versoes/'+hoje, cam_v in NUVEM and c15 in json.loads(json.loads(NUVEM[cam_v]['dados']['stringValue'])['lidas']))
    # versão antiga com uma leitura que não existe mais em lugar nenhum
    c20 = pg.evaluate('DATA[20].code')
    velho = json.loads(NUVEM[cam_v]['dados']['stringValue']); lv = json.loads(velho['lidas']); lv[c20]='0001'; velho['lidas']=json.dumps(lv)
    NUVEM[caminho+'/versoes/2026-01-10'] = dict(NUVEM[cam_v]); NUVEM[caminho+'/versoes/2026-01-10']['dados']={'stringValue':json.dumps(velho)}
    UPD[caminho+'/versoes/2026-01-10'] = carimbo()
    vs = pg.evaluate("NuvemSync.listarVersoes('Renata','🦋').then(l=>l.map(v=>v.dia))")
    ok('V4 lista as versões, da mais nova para a mais antiga', vs[:1]==[hoje] and '2026-01-10' in vs, vs)
    pg.evaluate("abrirNuvemTela()"); pg.wait_for_timeout(800); pg.click('#nuvemVersoesBt'); pg.wait_for_timeout(1200)
    ok('V5 tela mostra as versões guardadas', pg.locator('#nuvemGrid .userCard').count()>=2 and '10/01/2026' in pg.inner_text('#nuvemGrid'), pg.inner_text('#nuvemGrid'))
    pg.screenshot(path='/home/claude/t/versoes.png')
    pg.locator('#nuvemGrid .userCard', has_text='10/01/2026').click(); pg.wait_for_timeout(2500)
    ok('V6 juntar versão antiga traz de volta a leitura que faltava', pg.evaluate("(lidas['%s']||'')[3]" % c20)=='1')
    ok('V7 e não apagou a leitura de hoje', pg.evaluate("(lidas['%s']||'')[2]" % c15)=='1')
    pg.wait_for_timeout(2500)
    ok('V8 resultado juntado sobe para a nuvem', (lidas_nuvem(chave).get(c20,'')+'0000')[3]=='1')
    ok('V9 sem erros', not erros, erros)
    ctx.close()
    # V10: regras antigas (sem "versoes") não impedem o envio principal
    def sem_versoes(route, request):
        if 'firestore' in request.url and '/versoes' in request.url:
            return route.fulfill(**erro(403,'PERMISSION_DENIED','Missing or insufficient permissions.'))
        return fake(route, request)
    ctx = br.new_context(viewport={'width':900,'height':420}, service_workers='block')
    ctx.add_init_script("try{ localStorage.setItem('escola_conviteVisto',String(Date.now())); }catch(e){}")
    ctx.route(re.compile(r'https://(identitytoolkit|securetoken|firestore)\.googleapis\.com/.*'), sem_versoes)
    pg = ctx.new_page(); pg.on('dialog', lambda d: d.accept())
    pg.goto(base+'/index.html'); pg.wait_for_timeout(400)
    pg.evaluate("localStorage.setItem('nuvem_familia','familia-teste-2026')"); pg.reload(); pg.wait_for_timeout(500)
    pg.fill('#nuNome','Lia'); pg.evaluate("nuEmoji='🐼'"); pg.click('.nuPronto'); pg.wait_for_timeout(300)
    marcar(pg, c0, 0); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(2000)
    st = pg.evaluate("NuvemSync.status()")
    ok('V10 regras sem "versoes": progresso principal sobe mesmo assim', st['estado']=='ok' and doc_app('lia_1f43c') is not None, st)
    pg.evaluate("openCfg()"); pg.wait_for_timeout(100)
    ok('V11 e o app avisa para conferir as Regras', 'Regras' in pg.inner_text('#cfgNuvemSt'), pg.inner_text('#cfgNuvemSt'))
    ctx.close()

    # ===== K) Trocar nome/bichinho leva a ficha da nuvem junto =====
    ctx = br.new_context(viewport={'width':900,'height':420}, service_workers='block')
    ctx.add_init_script("try{ localStorage.setItem('escola_conviteVisto',String(Date.now())); }catch(e){}")
    ctx.route(re.compile(r'https://(identitytoolkit|securetoken|firestore)\.googleapis\.com/.*'), fake)
    pg = ctx.new_page(); erros=[]; pg.on('pageerror', lambda e: erros.append(str(e))); pg.on('dialog', lambda d: d.accept())
    pg.goto(base+'/index.html'); pg.wait_for_timeout(400)
    pg.evaluate("localStorage.setItem('nuvem_familia','familia-teste-2026')"); pg.reload(); pg.wait_for_timeout(500)
    pg.fill('#nuNome','Bia'); pg.click('.nuEmoji >> nth=2'); pg.click('.nuPronto'); pg.wait_for_timeout(2500)
    marcar(pg, c0, 3); pg.evaluate("NuvemSync.sincronizar()"); pg.wait_for_timeout(2500)
    ok('K1 Bia 🐰 subiu para a nuvem', (lidas_nuvem('bia_1f430') or {}).get(c0,'')[3:4]=='1', lidas_nuvem('bia_1f430'))
    pg.evaluate("editarUser()"); pg.wait_for_timeout(200); pg.click('.nuEmoji >> nth=5'); pg.click('.nuPronto'); pg.wait_for_timeout(3500)
    ok('K2 trocou para Bia 🐨: a ficha nova tem o progresso', (lidas_nuvem('bia_1f428') or {}).get(c0,'')[3:4]=='1', lidas_nuvem('bia_1f428'))
    ok('K3 a ficha antiga continua na nuvem (nada apagado)', lidas_nuvem('bia_1f430') is not None)
    # bichinho antigo (fora dos 8): continua funcionando e, ao trocar, leva o progresso
    NUVEM['familias/familia-teste-2026/usuarios/lua_1f984/apps/curiosidades'] = {'nome':{'stringValue':'Lua'},'av':{'stringValue':'🦄'},
       'dados':{'stringValue':json.dumps({'lidas':json.dumps({c5:'00001'})})},'atualizadoEm':{'integerValue':'5'},'dispositivo':{'stringValue':'velho'}}
    UPD['familias/familia-teste-2026/usuarios/lua_1f984/apps/curiosidades'] = carimbo()
    pg.evaluate("""()=>{ U.us.push({id:'p999',nome:'Lua',av:'🦄'}); salvarUsers(); trocarUser('p999'); }"""); pg.wait_for_timeout(3500)
    ok('K4 leitora com bichinho antigo 🦄 continua abrindo e recebe o progresso', pg.evaluate("(lidas['%s']||'')[4]" % c5)=='1')
    pg.evaluate("editarUser()"); pg.wait_for_timeout(200)
    ok('K5 ao editar, avisa que o bichinho mudou e pede um dos 8', 'escolha um dos 8' in pg.inner_text('#nuEscolhido'), pg.inner_text('#nuEscolhido'))
    pg.click('.nuPronto'); pg.wait_for_timeout(200)
    ok('K6 sem escolher, não salva', pg.evaluate("userAtual().av")=='🦄')
    pg.click('.nuEmoji >> nth=4'); pg.click('.nuPronto'); pg.wait_for_timeout(3500)
    ok('K7 trocou para Lua 🦋: a ficha nova recebeu o progresso da antiga', (lidas_nuvem('lua_1f98b') or {}).get(c5,'')[4:5]=='1', lidas_nuvem('lua_1f98b'))
    ok('K8 sem erros', not erros, erros)
    ctx.close()

    br.close()

print()
print('RESULTADO: %d/%d' % (sum(1 for _,v in RES if v), len(RES)))
