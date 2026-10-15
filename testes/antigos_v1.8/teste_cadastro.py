# Cadastro padrão Escola São Pedro: 8 bichinhos oficiais em UMA linha, em pé/deitado, com teclado.
import threading, http.server, socketserver, functools, json
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.ThreadingTCPServer(('127.0.0.1',8793),functools.partial(Q,directory='/home/claude/z'))
threading.Thread(target=srv.serve_forever,daemon=True).start()
BASE='http://127.0.0.1:8793/index.html'
OFICIAIS=['🦉','🦊','🐰','🐼','🦋','🐨','🐯','🐴']
NOMES=['Coruja','Raposa','Coelho','Panda','Borboleta','Coala','Tigre','Pônei']
R=[]
def ok(n,c,x=''): R.append(bool(c)); print('✅' if c else '❌', n, x if not c else '')
INIT="try{localStorage.setItem('escola_conviteVisto',String(Date.now()))}catch(e){}"
MEDIR='''()=>{
  const W=innerWidth,H=innerHeight;
  const bs=[...document.querySelectorAll('#nuEmojis .nuEmoji')].map(b=>{const r=b.getBoundingClientRect();
     const cx=r.left+r.width/2, cy=r.top+r.height/2; const el=document.elementFromPoint(cx,cy);
     return {l:r.left,r:r.right,t:r.top,b:r.bottom,w:r.width,clic:!!el&&(el===b||b.contains(el))};});
  const box=id=>{const r=document.getElementById(id).getBoundingClientRect();return {l:r.left,r:r.right,t:r.top,b:r.bottom};};
  const p=document.querySelector('.nuPronto').getBoundingClientRect();
  return {W,H,bs,nome:box('nuNome'),pronto:{l:p.left,r:p.right,t:p.top,b:p.bottom}};
}'''
TAMANHOS=[('deitado 740x360',740,360),('deitado 640x360',640,360),('deitado pequeno 568x320',568,320),
          ('deitado tablet 1024x600',1024,600),('em pé 360x740',360,740),('em pé 320x568',320,568),('em pé 412x915',412,915)]
TECLADO=[('deitado + teclado 740x170',740,170),('deitado + teclado 640x150',640,150),('deitado + teclado 568x140',568,140),
         ('em pé + teclado 360x420',360,420),('em pé + teclado 320x300',320,300)]
with sync_playwright() as p:
    b=p.chromium.launch()
    def abre(w,h):
        c=b.new_context(viewport={'width':w,'height':h},service_workers='block',has_touch=True,is_mobile=True)
        c.add_init_script(INIT); pg=c.new_page(); er=[]; pg.on('pageerror',lambda e: er.append(str(e)))
        pg.on('dialog',lambda d:d.accept()); pg.goto(BASE); pg.wait_for_timeout(500); return c,pg,er
    # ---------- 1ª conferência: funcionamento ----------
    c,pg,er=abre(740,360)
    lista=pg.evaluate("[...document.querySelectorAll('#nuEmojis .nuEmoji')].map(b=>b.textContent)")
    ok('1.1 exatamente os 8 bichinhos oficiais, na ordem oficial', lista==OFICIAIS, lista)
    nomes=pg.evaluate("[...document.querySelectorAll('#nuEmojis .nuEmoji')].map(b=>b.getAttribute('aria-label'))")
    ok('1.2 nomes dos bichinhos corretos', nomes==NOMES, nomes)
    ok('1.3 lista vem do arquivo compartilhado escola-pwa.js', pg.evaluate("JSON.stringify(EscolaPWA.BICHINHOS.map(b=>b.e))")==json.dumps(OFICIAIS, ensure_ascii=False).replace(' ',''))
    ok('1.4 nenhum bichinho vem escolhido sozinho', pg.locator('.nuEmoji.on').count()==0)
    pg.fill('#nuNome','Renata'); pg.click('.nuPronto'); pg.wait_for_timeout(200)
    ok('1.5 sem bichinho não cadastra', pg.is_visible('#novoUser') and pg.evaluate('U.us.length')==0)
    pg.fill('#nuNome',''); pg.click('.nuEmoji >> nth=4'); pg.click('.nuPronto'); pg.wait_for_timeout(200)
    ok('1.6 sem nome não cadastra', pg.evaluate('U.us.length')==0)
    ok('1.7 mostra o bichinho escolhido por extenso', 'Borboleta' in pg.inner_text('#nuEscolhido'), pg.inner_text('#nuEscolhido'))
    pg.fill('#nuNome','  Renata  '); pg.click('.nuPronto'); pg.wait_for_timeout(400)
    u=pg.evaluate('U.us[0]')
    ok('1.8 cadastro: nome e bichinho gravados certos', u['nome']=='Renata' and u['av']=='🦋', u)
    ok('1.9 depois do cadastro vai para a tela inicial', pg.is_visible('#home'))
    pg.evaluate('abrirNovoUser()'); pg.fill('#nuNome','renata'); pg.click('.nuEmoji >> nth=4'); pg.click('.nuPronto'); pg.wait_for_timeout(300)
    ok('1.10 "renata"+🦋 de novo não cria repetido (abre a Renata)', pg.evaluate('U.us.length')==1 and pg.evaluate('userAtual().nome')=='Renata')
    pg.evaluate('abrirNovoUser()'); pg.fill('#nuNome','Renata'); pg.click('.nuEmoji >> nth=6'); pg.click('.nuPronto'); pg.wait_for_timeout(300)
    ok('1.11 mesmo nome com OUTRO bichinho é outra criança', pg.evaluate('U.us.length')==2)
    pg.evaluate('abrirNovoUser()'); pg.fill('#nuNome','Ana'); pg.click('.nuEmoji >> nth=0')
    pg.press('#nuNome','Enter'); pg.wait_for_timeout(300)
    ok('1.12 Enter no teclado confirma quando já tem bichinho', pg.evaluate('U.us.length')==3)
    pg.reload(); pg.wait_for_timeout(600)
    ok('1.13 reabrir o app: cadastros continuam (3) e pede "Quem vai estudar hoje?"', pg.evaluate('U.us.length')==3 and pg.is_visible('#users') and 'estudar' in pg.inner_text('#usersTop'))
    pg.click('#usersGrid .userCard >> nth=0'); pg.wait_for_timeout(300)
    ok('1.14 acesso: tocar no nome entra no progresso dela', pg.evaluate('userAtual().nome')=='Renata' and pg.evaluate('userAtual().av')=='🦋')
    pg.evaluate("abrirUsers()"); pg.evaluate("editarUser()"); pg.fill('#nuNome','Ana'); pg.click('.nuEmoji >> nth=0'); pg.click('.nuPronto'); pg.wait_for_timeout(200)
    ok('1.15 editar para um nome+bichinho que já é de outra criança é bloqueado', pg.evaluate("U.us.filter(u=>u.nome==='Ana').length")==1)
    ok('1.16 sem erros', not er, er); c.close()
    # ---------- 2ª conferência: celular ----------
    def confere(nome,w,h,teclado=False):
        c,pg,er=abre(w,h)
        if teclado:
            pg.focus('#nuNome'); pg.wait_for_timeout(500)
        m=pg.evaluate(MEDIR); bs=m['bs']
        uma_linha = max(x['t'] for x in bs)-min(x['t'] for x in bs) < 2
        dentro = all(x['l']>=-0.5 and x['r']<=m['W']+0.5 and x['t']>=-0.5 and x['b']<=m['H']+0.5 for x in bs)
        sem_encostar = all(bs[i]['r']<=bs[i+1]['l']+0.5 for i in range(7))
        clicaveis = all(x['clic'] for x in bs)
        tam = min(x['w'] for x in bs)
        nome_ok = m['nome']['t']>=-0.5 and m['nome']['b']<=m['H']+0.5 and m['nome']['r']<=m['W']+0.5
        pronto_ok = m['pronto']['t']>=-0.5 and m['pronto']['b']<=m['H']+0.5
        ok(f'2 {nome}: 8 numa linha, inteiros na tela, clicáveis (≥30px: {tam:.0f}px), nome visível, Pronto visível',
           len(bs)==8 and uma_linha and dentro and sem_encostar and clicaveis and tam>=29.5 and nome_ok and pronto_ok,
           dict(uma_linha=uma_linha,dentro=dentro,sem_encostar=sem_encostar,clicaveis=clicaveis,tam=tam,nome_ok=nome_ok,pronto_ok=pronto_ok,m=m['nome'],p=m['pronto']))
        # tocar num bichinho de verdade funciona
        pg.tap('.nuEmoji >> nth=7'); pg.wait_for_timeout(100)
        ok(f'2 {nome}: tocar no 🐴 escolhe o Pônei', pg.evaluate('nuEmoji')=='🐴')
        pg.screenshot(path='/home/claude/t/cad_'+nome.replace(' ','_').replace('+','').replace('é','e')+'.png')
        c.close()
    for n,w,h in TAMANHOS: confere(n,w,h)
    for n,w,h in TECLADO: confere(n,w,h,teclado=True)
    # em pé: a tela de cadastro não é girada (o teclado funciona normal)
    c,pg,er=abre(360,740)
    ok('2.x em pé: cadastro fica em pé (não gira)', pg.evaluate("getComputedStyle(document.getElementById('novoUser')).transform")=='none')
    c.close()
    b.close()
print('RESULTADO %d/%d'%(sum(R),len(R)))
