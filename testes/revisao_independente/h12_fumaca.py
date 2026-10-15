import sys, json
from lib import *
sys.path.insert(0,'/home/claude/revisor/v20/testes/navegador')
import ef
PORTA=int(os.environ.get('PORTA','8975'))
d20=preparar(RAIZ+'/v20/pacote-netlify', RAIZ+'/meus/srv20o')
srv=Servidor(PORTA, d20)
HIN='p1790243541621'
r=R('H12 fumaça do app antigo com toques de verdade (v2.0)')
with sync_playwright() as pw:
    fb=FakeFirebase(); er=[]
    ctx,_=ctx_novo(pw,fb,w=984,h=432,storage=storage_do_backup('pmrtestes')); p=abrir(ctx,srv.url,er); ef.esperar_ok(p,10000)
    ef.escolher(p,HIN)
    r.t('estante abre após escolher', p.evaluate("!document.getElementById('home').classList.contains('hidden')") and not ef.aberta(p,'ef-t4'))
    # Cantinhos
    for txt,screen in [('Dicionário','palavras'),('Minhas Conquistas','conquistas'),('Desafio Rápido','desafio'),('Últimas Lidas','ultimasLidasTela')]:
        p.locator('#home button:has-text("%s")'%txt).first.click(); p.wait_for_timeout(700)
        vis=p.evaluate("s=>!document.getElementById(s).classList.contains('hidden')",screen)
        r.t('%s abre'%txt, vis)
        p.screenshot(path=RAIZ+'/meus/caps/f_%s.png'%screen)
        p.evaluate("goHome(); voltarMenu()"); p.wait_for_timeout(400)
    # abre a primeira seção, lê, marca lida, favorita
    p.locator('#home button.secBtn').first.click(); p.wait_for_timeout(700); p.locator('#home button.pais:not(.secBtn):not(.ult)').first.click(); p.wait_for_timeout(900)
    print('  tela:', p.evaluate("['home','reader','palavras','conquistas','desafio','ultimasLidasTela','buscaTela'].filter(s=>document.getElementById(s)&&!document.getElementById(s).classList.contains('hidden'))"))
    antes=ef.conta_lidas(ef.lidas(p,HIN))
    if p.evaluate("!document.getElementById('reader').classList.contains('hidden')"):
        p.click('#marcarLida'); p.wait_for_timeout(500)
        p.click('#fav'); p.wait_for_timeout(300)
        p.click('#next') if p.locator('#next').count() else None
        depois=ef.conta_lidas(ef.lidas(p,HIN))
        r.t('LIDA grava na hora', depois!=antes, (antes,depois))
    # busca
    p.evaluate("goHome(); voltarMenu()"); p.wait_for_timeout(400)
    p.click('text=🔍') if p.locator('text=🔍').count() else p.evaluate("abrirBusca&&abrirBusca()")
    p.wait_for_timeout(600)
    print('  busca visível:', p.evaluate("!document.getElementById('buscaTela').classList.contains('hidden')"))
    # engrenagem da estante abre config com seção família
    p.evaluate("goHome(); voltarMenu()"); p.wait_for_timeout(400)
    p.click('#cfgGearHome'); p.wait_for_timeout(600)
    r.t('Config: seção ☁️ FAMÍLIA E NUVEM é a última', p.evaluate("(()=>{const c=document.getElementById('cfgFamilia'); const b=c.closest('.cfgBody')||c.parentElement; const f=[...b.children].filter(e=>e.offsetParent); return f[f.length-1]===c || b.lastElementChild===c;})()"))
    r.t('Config: textos antigos de nuvem sumiram', not p.evaluate("/Recuperar leitores|Código da família|Enviar agora/i.test(document.getElementById('cfgCard').innerText)"))
    r.t('sem erros JS / diálogos', not er, er)
    ctx.close()
f=r.fim(); sys.exit(1 if f else 0)
