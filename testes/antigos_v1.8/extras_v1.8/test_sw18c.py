import threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.ThreadingTCPServer(('127.0.0.1',8798),functools.partial(Q,directory='/home/claude/z18'))
threading.Thread(target=srv.serve_forever,daemon=True).start()
print('server up', flush=True)

with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={'width':390,'height':844})
    pg=ctx.new_page()
    pg.set_default_timeout(8000)
    err=[]; pg.on('pageerror', lambda e: err.append(str(e)))
    pg.goto('http://localhost:8798/index.html'); pg.wait_for_timeout(500)
    print('sw regs:', pg.evaluate("navigator.serviceWorker.getRegistrations().then(r=>r.length)"), flush=True)
    pg.wait_for_timeout(2000)
    print('sw regs after wait:', pg.evaluate("navigator.serviceWorker.getRegistrations().then(r=>r.length)"), flush=True)
    keys = pg.evaluate("caches.keys()")
    print('cache keys:', keys, flush=True)
    b.close()
print('DONE', flush=True)
