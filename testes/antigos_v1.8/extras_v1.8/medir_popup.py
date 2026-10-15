import threading, http.server, socketserver, functools, json, sys
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.ThreadingTCPServer(('127.0.0.1',8811),functools.partial(Q,directory='/home/claude/t/site'))
threading.Thread(target=srv.serve_forever,daemon=True).start()
MED='''()=>{const r=e=>{const b=document.getElementById(e).getBoundingClientRect();return [Math.round(b.top),Math.round(b.bottom)]};
 const H=innerHeight; const x=['codigoInput','codigoOkBtn','codigoCancelBtn'].map(id=>{const [t,b]=r(id);return id+':'+t+'-'+b+(t>=0&&b<=H?' visível':' FORA')});
 return H+'px | '+x.join(' | ');}'''
with sync_playwright() as p:
    b=p.chromium.launch()
    for (w,h) in [(740,360),(740,170),(640,150),(568,140),(360,740),(360,420),(320,300)]:
        ctx=b.new_context(viewport={'width':w,'height':h},service_workers='block')
        ctx.add_init_script("try{localStorage.setItem('escola_conviteVisto',String(Date.now()))}catch(e){}")
        pg=ctx.new_page(); pg.goto('http://127.0.0.1:8811/index.html'); pg.wait_for_timeout(500)
        pg.evaluate("pedirCodigoFamilia(false)"); pg.wait_for_timeout(300)
        print(f"{w}x{h}:", pg.evaluate(MED))
        if (w,h)==(740,170): pg.screenshot(path=sys.argv[1]+'/popup_740x170.png')
        ctx.close()
    b.close()
