import threading,http.server,socketserver,functools
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.ThreadingTCPServer(('127.0.0.1',8791),functools.partial(Q,directory='/home/claude/t/site'))
threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':900,'height':420}); pg=ctx.new_page()
    err=[]; pg.on('pageerror',lambda e: err.append(str(e)))
    pg.goto('http://localhost:8791/index.html'); pg.wait_for_timeout(500)
    pg.evaluate("navigator.serviceWorker.ready"); pg.wait_for_timeout(1500)
    keys=pg.evaluate("caches.keys().then(ks=>Promise.all(ks.map(k=>caches.open(k).then(c=>c.keys()).then(r=>[k,r.map(x=>x.url.split('/').pop())]))))")
    print(keys)
    ctx.set_offline(True); pg.reload(); pg.wait_for_timeout(1200)
    # v2.0: sem internet o app abre nas boas-vindas do escola-familia.js (T1), com a nuvem configurada
    print('offline ok:', pg.is_visible('#efRaiz .ef-t1'), pg.evaluate("!!window.NuvemSync && NuvemSync.configurada() && !!window.EscolaFamilia"), err)
    b.close()
