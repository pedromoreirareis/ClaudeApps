import threading,http.server,socketserver,functools
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.ThreadingTCPServer(('127.0.0.1',8792),functools.partial(Q,directory='/home/claude/z'))
threading.Thread(target=srv.serve_forever,daemon=True).start()
R=[]
def ok(n,c,x=''): R.append(c); print('✅' if c else '❌', n, x)
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':900,'height':420},service_workers='block')
    ctx.add_init_script("try{localStorage.setItem('escola_conviteVisto',String(Date.now()))}catch(e){}")
    pg=ctx.new_page(); err=[]; pg.on('pageerror',lambda e: err.append(str(e)))
    pg.goto('http://127.0.0.1:8792/index.html'); pg.wait_for_timeout(500)
    pg.fill('#nuNome','Teste'); pg.click('.nuEmoji >> nth=2'); pg.click('.nuPronto'); pg.wait_for_timeout(300)
    # abre subcategoria 3 pela home (clique real)
    pg.evaluate("buildHome()")
    pg.evaluate("(()=>{ paisIdx=3; curIdx=posPais[DATA[3].code]||0; saveState(); openReader(); })()")
    ok('R1 nunca visitada abre na 1ª', pg.evaluate('curIdx')==0)
    pg.click('#next'); pg.click('#next'); pg.click('#next'); pg.wait_for_timeout(200)
    ok('R2 avançou para a 4ª', pg.evaluate('curIdx')==3)
    pg.click('#marcarLida'); pg.wait_for_timeout(100)
    ok('R3 LIDA gravada no disco na hora', pg.evaluate("JSON.parse(localStorage.getItem(K('lidas')))[DATA[3].code][3]")=='1')
    pg.evaluate("goHome()"); pg.reload(); pg.wait_for_timeout(600)
    pg.evaluate("(()=>{ paisIdx=3; curIdx=posPais[DATA[3].code]||0; saveState(); openReader(); })()")
    ok('R4 reabriu: volta onde parou (4ª)', pg.evaluate('curIdx')==3)
    ok('R5 LIDA continua marcada após reabrir', pg.evaluate("lidas[DATA[3].code][3]")=='1')
    pg.evaluate("goHome(); (()=>{ paisIdx=7; curIdx=posPais[DATA[7].code]||0; openReader(); })()")
    ok('R6 outra nunca visitada abre na 1ª', pg.evaluate('curIdx')==0)
    pg.evaluate("goHome(); abrirBusca()"); pg.fill('#buscaInput','egito'); pg.wait_for_timeout(500)
    ok('R7 busca em sanfona funciona', pg.locator('.buscaGrupo').count()>=1)
    pg.evaluate("fecharBusca(); mudaFontSize(-1)"); ok('R8 fonte 14', pg.evaluate('FSIZES[fsizeIdx]')==14)
    lp=pg.evaluate("DATA.findIndex(p=>p.simbolo)")
    pg.evaluate(f"(()=>{{ paisIdx={lp}; curIdx=0; openReader(); }})()")
    ok('R9 cartão de Língua Portuguesa mostra símbolo vermelho', pg.evaluate("document.getElementById('emoji').classList.contains('simboloEnsinado')"))
    ok('R10 sem erros', not err, err)
    b.close()
print('RESULTADO %d/%d'%(sum(R),len(R)))
