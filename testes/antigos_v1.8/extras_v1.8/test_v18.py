import threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.ThreadingTCPServer(('127.0.0.1',8794),functools.partial(Q,directory='/home/claude/z18'))
threading.Thread(target=srv.serve_forever,daemon=True).start()

R=[]
def ok(n,c,x=''): R.append(bool(c)); print('✅' if c else '❌', n, x if not c else '')

with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={'width':390,'height':844}, service_workers='block')
    ctx.add_init_script("try{localStorage.setItem('escola_conviteVisto',String(Date.now()))}catch(e){}")
    pg=ctx.new_page(); err=[]; pg.on('pageerror', lambda e: err.append(str(e)))
    pg.on('console', lambda m: err.append('console:'+m.text) if m.type=='error' else None)
    pg.goto('http://127.0.0.1:8794/index.html')
    pg.wait_for_timeout(700)
    ok('sem erro de JS ao carregar', len(err)==0, str(err))

    # cadastro básico ainda funciona
    pg.fill('#nuNome','Teste18')
    pg.click('.nuEmoji >> nth=2')
    pg.click('.nuPronto')
    pg.wait_for_timeout(300)
    ok('cadastro concluído (estante visível ou reader)', pg.evaluate("!!U.us.length"))

    # mock NuvemSync para testar o popup sem depender do Firebase de verdade
    pg.evaluate("""() => {
        window.NuvemSync = {
            pronta: () => false,
            configurada: () => true,
            status: () => ({configurada:true, estado:'sem-codigo', temFamiliaNoArquivo:false}),
            definirFamilia: (c) => {
                const norm = c.toLowerCase().trim().replace(/\\s+/g,'-').replace(/[^a-z0-9-]/g,'');
                if (norm.length < 6) return false;
                return norm;
            }
        };
        window.__nuvemCfgArq = 'ok';
    }""")
    dialogs=[]
    pg.on('dialog', lambda d: (dialogs.append(d.message), d.dismiss()))
    pg.evaluate("pedirCodigoFamilia(false)")
    pg.wait_for_timeout(200)
    ok('popup abre (não é prompt nativo)', pg.eval_on_selector('#codigoOv','el=>el.classList.contains("open")'))
    ok('nenhum dialog nativo disparado', len(dialogs)==0, str(dialogs))
    pg.fill('#codigoInput','familia123')
    pg.click('#codigoOkBtn')
    pg.wait_for_timeout(300)
    ok('popup fecha após confirmar', pg.eval_on_selector('#codigoOv','el=>!el.classList.contains("open")'))

    ok('sem erros JS depois do fluxo todo', len(err)==0, str(err))
    b.close()

print()
print(f'{sum(R)}/{len(R)} testes passaram')
