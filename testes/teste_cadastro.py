# Cadastro padrão Escola São Pedro: 8 bichinhos oficiais em UMA linha, em pé/deitado, com teclado.
# v2.0: as mesmas 41 conferências da v1.8, agora na tela "🌟 QUAL É O SEU NOME?" do escola-familia.js
# (os seletores mudaram; o que cada conferência prova continua igual).
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
T5='#efRaiz .ef-t5'
MEDIR='''()=>{
  const W=innerWidth,H=innerHeight;
  const bs=[...document.querySelectorAll('#efRaiz .ef-t5 .ef-bicho')].map(b=>{const r=b.getBoundingClientRect();
     const cx=r.left+r.width/2, cy=r.top+r.height/2; const el=document.elementFromPoint(cx,cy);
     return {l:r.left,r:r.right,t:r.top,b:r.bottom,w:r.width,clic:!!el&&(el===b||b.contains(el))};});
  const box=s=>{const r=document.querySelector(s).getBoundingClientRect();return {l:r.left,r:r.right,t:r.top,b:r.bottom};};
  const vis=s=>{const e=document.querySelector(s); return e && e.offsetParent ? e : null;};
  const pe=vis('#efRaiz .ef-t5 .ef-pronto')||vis('#efRaiz .ef-t5 .ef-pronto-mini');
  const p=pe.getBoundingClientRect();
  return {W,H,bs,nome:box('#efRaiz .ef-t5 .ef-nome-campo'),pronto:{l:p.left,r:p.right,t:p.top,b:p.bottom}};
}'''
TAMANHOS=[('deitado 740x360',740,360),('deitado 640x360',640,360),('deitado pequeno 568x320',568,320),
          ('deitado tablet 1024x600',1024,600),('em pé 360x740',360,740),('em pé 320x568',320,568),('em pé 412x915',412,915)]
TECLADO=[('deitado + teclado 740x170',740,170),('deitado + teclado 640x150',640,150),('deitado + teclado 568x140',568,140),
         ('em pé + teclado 360x420',360,420),('em pé + teclado 320x300',320,300)]
def us(pg): return pg.evaluate('U.us')
with sync_playwright() as p:
    b=p.chromium.launch()
    def abre(w,h):
        c=b.new_context(viewport={'width':w,'height':h},service_workers='block',has_touch=True,is_mobile=True)
        c.add_init_script(INIT); pg=c.new_page(); er=[]; pg.on('pageerror',lambda e: er.append(str(e)))
        pg.on('dialog',lambda d:(er.append('CAIXINHA DO NAVEGADOR: '+d.message), d.dismiss())); pg.goto(BASE); pg.wait_for_timeout(600)
        pg.evaluate("EscolaFamilia.abrir('nova')"); pg.wait_for_timeout(400)
        return c,pg,er
    def nova(pg):
        pg.evaluate("EscolaFamilia.abrir('nova')"); pg.wait_for_timeout(300)
    def pronto(pg, ms=1600):
        pg.click(T5+' .ef-pronto'); pg.wait_for_timeout(ms)
    # ---------- 1ª conferência: funcionamento ----------
    c,pg,er=abre(740,360)
    lista=pg.evaluate("[...document.querySelectorAll('#efRaiz .ef-t5 .ef-bicho')].map(b=>b.textContent)")
    ok('1.1 exatamente os 8 bichinhos oficiais, na ordem oficial', lista==OFICIAIS, lista)
    nomes=pg.evaluate("[...document.querySelectorAll('#efRaiz .ef-t5 .ef-bicho')].map(b=>b.getAttribute('aria-label'))")
    ok('1.2 nomes dos bichinhos corretos', nomes==NOMES, nomes)
    ok('1.3 lista vem do arquivo compartilhado escola-pwa.js', pg.evaluate("JSON.stringify(EscolaPWA.BICHINHOS.map(b=>b.e))")==json.dumps(OFICIAIS, ensure_ascii=False).replace(' ',''))
    ok('1.4 nenhum bichinho vem escolhido sozinho', pg.locator(T5+' .ef-bicho.ef-on').count()==0)
    pg.fill(T5+' .ef-nome-campo','Renata'); pronto(pg, 300)
    ok('1.5 sem bichinho não cadastra', pg.is_visible(T5) and len(us(pg))==0)
    pg.fill(T5+' .ef-nome-campo',''); pg.click(T5+' .ef-bicho >> nth=4'); pronto(pg, 300)
    ok('1.6 sem nome não cadastra', len(us(pg))==0)
    ok('1.7 mostra o bichinho escolhido por extenso', 'Borboleta' in pg.text_content(T5+' .ef-escolhido'), pg.text_content(T5+' .ef-escolhido'))
    pg.fill(T5+' .ef-nome-campo','  Renata  '); pronto(pg)
    u=us(pg)[0] if us(pg) else {}
    ok('1.8 cadastro: nome e bichinho gravados certos', u.get('nome')=='Renata' and u.get('av')=='🦋', u)
    ok('1.9 depois do cadastro vai para a tela inicial', pg.is_visible('#home') and not pg.evaluate("EscolaFamilia.estaAberto()"))
    nova(pg); pg.fill(T5+' .ef-nome-campo','renata'); pg.click(T5+' .ef-bicho >> nth=4'); pronto(pg)
    ok('1.10 "renata"+🦋 de novo não cria repetido (abre a Renata)', len(us(pg))==1 and pg.evaluate('userAtual().nome')=='Renata')
    nova(pg); pg.fill(T5+' .ef-nome-campo','Renata'); pg.click(T5+' .ef-bicho >> nth=6'); pronto(pg, 400)
    # v2.0: mesmo nome com outro bichinho → o app pergunta "JÁ EXISTE 🦋 Renata NA FAMÍLIA. É VOCÊ?"
    perg=pg.is_visible('#efRaiz .ef-pergunta') and 'É VOCÊ?' in (pg.text_content('#efRaiz .ef-pergunta') or '')
    pg.click('#efRaiz .ef-pergunta .ef-nao'); pg.wait_for_timeout(1600)
    ok('1.11 mesmo nome com OUTRO bichinho é outra criança (depois de responder "NÃO, SOU OUTRA CRIANÇA")', perg and len(us(pg))==2)
    nova(pg); pg.fill(T5+' .ef-nome-campo','Ana'); pg.click(T5+' .ef-bicho >> nth=0')
    pg.press(T5+' .ef-nome-campo','Enter'); pg.wait_for_timeout(1600)
    ok('1.12 Enter no teclado confirma quando já tem bichinho', len(us(pg))==3)
    pg.reload(); pg.wait_for_timeout(800)
    ok('1.13 reabrir o app: cadastros continuam (3) e pede "Quem vai estudar hoje?"', len(us(pg))==3 and pg.is_visible('#efRaiz .ef-t4') and 'ESTUDAR' in pg.text_content('#efRaiz .ef-t4 .ef-titulo'))
    rid=[x['id'] for x in us(pg) if x['nome']=='Renata' and x['av']=='🦋'][0]
    pg.click('#efRaiz .ef-t4 .ef-crianca[data-id="%s"]' % rid); pg.wait_for_timeout(1500)
    ok('1.14 acesso: tocar no nome entra no progresso dela', pg.evaluate('userAtual().nome')=='Renata' and pg.evaluate('userAtual().av')=='🦋')
    pg.evaluate("EscolaFamilia.abrir('mudar')"); pg.wait_for_timeout(300)
    pg.fill(T5+' .ef-nome-campo','Ana'); pg.click(T5+' .ef-bicho >> nth=0'); pronto(pg, 400)
    ok('1.15 mudar para um nome+bichinho que já é de outra criança é bloqueado', pg.evaluate("U.us.filter(u=>u.nome==='Ana').length")==1)
    ok('1.16 sem erros', not er, er); c.close()
    # ---------- 2ª conferência: celular ----------
    def confere(nome,w,h,teclado=False):
        c,pg,er=abre(w,h)
        if teclado:
            pg.focus(T5+' .ef-nome-campo'); pg.wait_for_timeout(500)
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
        pg.tap(T5+' .ef-bicho >> nth=7'); pg.wait_for_timeout(150)
        ok(f'2 {nome}: tocar no 🐴 escolhe o Pônei', pg.locator(T5+' .ef-bicho.ef-on').count()==1 and pg.locator(T5+' .ef-bicho.ef-on').text_content()=='🐴')
        pg.screenshot(path='/home/claude/t/cad_'+nome.replace(' ','_').replace('+','').replace('é','e')+'.png')
        c.close()
    for n,w,h in TAMANHOS: confere(n,w,h)
    for n,w,h in TECLADO: confere(n,w,h,teclado=True)
    # em pé: a tela de cadastro não é girada (o teclado funciona normal)
    c,pg,er=abre(360,740)
    ok('2.x em pé: cadastro fica em pé (não gira)', pg.evaluate("getComputedStyle(document.querySelector('#efRaiz .ef-t5')).transform")=='none' and pg.evaluate("getComputedStyle(document.getElementById('efRaiz')).transform")=='none')
    c.close()
    b.close()
print('RESULTADO %d/%d'%(sum(R),len(R)))
