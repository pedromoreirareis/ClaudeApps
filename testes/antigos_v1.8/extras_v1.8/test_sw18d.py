import threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.ThreadingTCPServer(('127.0.0.1',8799),functools.partial(Q,directory='/home/claude/z18'))
threading.Thread(target=srv.serve_forever,daemon=True).start()
print('server up', flush=True)

with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={'width':390,'height':844})
    pg=ctx.new_page()
    pg.set_default_timeout(8000)
    err=[]; pg.on('pageerror', lambda e: err.append(str(e)))
    pg.goto('http://localhost:8799/index.html'); pg.wait_for_timeout(2500)
    print('cache keys before offline:', pg.evaluate("caches.keys()"), flush=True)
    ctx.set_offline(True)
    print('now offline, reloading...', flush=True)
    pg.reload(timeout=8000)
    pg.wait_for_timeout(1000)
    print('reload done offline', flush=True)
    visible = pg.is_visible('#novoUser') or pg.is_visible('#users') or pg.is_visible('#reader') or pg.is_visible('#home')
    print('alguma tela visível offline:', visible, 'erros JS:', err, flush=True)
    b.close()
print('DONE', flush=True)
