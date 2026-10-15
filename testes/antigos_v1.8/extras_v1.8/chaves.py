import threading, http.server, socketserver, functools, json
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
for porta,pasta in [(8821,'/home/claude/z'),(8822,'/home/claude/t/site')]:
    srv=socketserver.ThreadingTCPServer(('127.0.0.1',porta),functools.partial(Q,directory=pasta))
    threading.Thread(target=srv.serve_forever,daemon=True).start()
KEYS="()=>Object.keys(localStorage).sort()"
with sync_playwright() as p:
    b=p.chromium.launch()
    for porta in (8821,8822):
        ctx=b.new_context(viewport={'width':900,'height':420},service_workers='block')
        ctx.route('**/*googleapis.com/**', lambda r: r.abort())
        pg=ctx.new_page(); pg.on('dialog',lambda d:d.accept())
        pg.goto('http://127.0.0.1:%d/index.html'%porta); pg.wait_for_timeout(600)
        print(porta,'ABERTURA 0 crianças:',pg.evaluate(KEYS), 'tela cadastro?', pg.is_visible('#novoUser'))
        pg.fill('#nuNome','Bia'); pg.click('.nuEmoji >> nth=2'); pg.click('.nuPronto'); pg.wait_for_timeout(300)
        pg.evaluate("(()=>{ paisIdx=0; curIdx=0; openReader(); toggleLida(); toggleFav(); })()"); pg.wait_for_timeout(300)
        print(porta,'DEPOIS:',pg.evaluate(KEYS))
        print(porta,'mundo_usuarios=',pg.evaluate("localStorage.getItem('mundo_usuarios')"))
        print(porta,'p0:',pg.evaluate("Object.keys(localStorage).filter(k=>k.startsWith('mundo_p0_')).map(k=>k+'='+localStorage.getItem(k))"))
        pg.reload(); pg.wait_for_timeout(500)
        print(porta,'reabre com 1 criança -> home?',pg.is_visible('#home'),'secAtual=',pg.evaluate('secAtual'))
        ctx.close()
    b.close()
