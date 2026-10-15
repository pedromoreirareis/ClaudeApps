"""🌍 Curiosidades v2.0 — desenho das telas da família (copiado do teste_desenho.py do
Alfabetização v123 e adaptado; parte 4.12 do plano, itens 7 a 10): respiro e uso da largura deitado.
Seção 8 (nova): as barras de cima do Curiosidades com o chip ao lado da ⚙️.

1) Teclado aberto: a caixa do código fica NO MEIO entre o topo e o teclado,
   sem sobra vazia dentro do cartão (T2, T3 e T5).
2) "🎉 ACHEI A SUA FAMÍLIA!": pop-up largo, cartões em grade com espaço,
   botões embaixo e sempre à vista, com 1, 3 e 6 crianças.
3) Configurações: pop-up usa a largura deitado; em "☁️ Família e nuvem"
   o texto fica à esquerda e os botões numa linha à direita, sem encostar.
4) "Quem vai estudar hoje?": cartões no meio, rodapé sem texto cortado.
5) Famílias neste celular: cada família numa linha só.
6) Site de teste reconhecido em escolasaopedrotestes.netlify.app.
7) Tela cheia: o app pede a tela cheia de verdade também quando aberto pelo
   ícone (v123 voltou ao jeito da v122, a pedido do Pedro: sem as barras do
   Android; o aviso do Chrome é do Chrome) e o ⛶ da aba entra e sai.

Tamanhos: 984x432 (o Motorola do Pedro), 937x411, 740x360, 640x360 e 568x320
deitado; 1280x800 (tablet). Chromium + Firebase de mentira."""
from base import *
from ef import *
import json, os

DEITADO = [(984,432),(937,411),(740,360),(640,360),(568,320)]
NOMES = [('Hina','🐰','1f430'),('Renata','🦋','1f98b'),('Bia','🐱','1f431'),('Caio','🐯','1f42f'),('Lu','🐼','1f43c'),('Ana','🦊','1f98a')]

def fb_com(n, fam='pmrtestes'):
    fb = FakeFirebase()
    for nome, av, cod in NOMES[:n]:
        fb.gravar_app(nome.lower()+'_'+cod, nome, av, {'lidas':json.dumps({'AL1':'1'*5})}, familia=fam)
    return fb

def caixas(p, sel):
    return p.evaluate("s=>Array.from(document.querySelectorAll(s)).filter(e=>e.offsetParent||getComputedStyle(e).position==='fixed').map(e=>{const r=e.getBoundingClientRect(); return {x:r.left,y:r.top,w:r.width,h:r.height,b:r.bottom,r:r.right,sw:e.scrollWidth,cw:e.clientWidth,fs:parseFloat(getComputedStyle(e).fontSize)}})", sel)

def sobrepoe(a, b, folga=0):
    return not (a['r'] <= b['x']+folga or b['r'] <= a['x']+folga or a['b'] <= b['y']+folga or b['b'] <= a['y']+folga)

def main():
    servidor()
    res = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()

        # ================= 1) teclado: no meio, sem sobra =================
        r = R('1) Teclado aberto: a caixa do código fica no meio entre o topo e o teclado')
        for (W,H) in [(984,432),(740,360),(568,320)]:
            ctx, _ = novo_contexto(b, fb=fb_com(1), largura=W, altura=H)
            p = abrir(ctx); p.wait_for_timeout(1000)
            p.click('.ef-t1-ja'); p.wait_for_timeout(300)
            p.click('.ef-t2 .ef-codigo'); p.keyboard.type('pmrtestes')
            for kh in (int(H*0.28), int(H*0.42)):
                p.set_viewport_size({'width':W,'height':kh}); p.wait_for_timeout(450)
                c = caixas(p, '.ef-t2 .ef-card')[0]; campo = caixas(p, '.ef-t2 .ef-codigo')[0]
                cima, baixo = c['y'], kh - c['b']
                foco = p.evaluate("document.activeElement && document.activeElement.classList.contains('ef-codigo')")
                r.t('T2 %dx%d, teclado deixa %d px: cartão no meio (sobra em cima %d, embaixo %d) e campo com foco' % (W,H,kh,cima,baixo),
                    abs(cima-baixo) <= 12 and cima >= 2 and baixo >= 2 and foco and campo['y'] >= 0 and campo['b'] <= kh, (cima, baixo, foco))
                r.t('...sem sobra vazia dentro do cartão (altura %d ≤ campo %d + 30)' % (c['h'], campo['h']), c['h'] <= campo['h'] + 30)
            p.set_viewport_size({'width':W,'height':H}); p.wait_for_timeout(300)
            fechar_tudo(p)
            p.evaluate("EscolaFamilia.abrir('boasvindas')"); p.wait_for_timeout(300)
            p.click('.ef-t1-novo'); p.wait_for_timeout(300); p.click('.ef-t3 .ef-codigo')
            kh = int(H*0.30); p.set_viewport_size({'width':W,'height':kh}); p.wait_for_timeout(450)
            c = caixas(p, '.ef-t3 .ef-card')[0]
            r.t('T3 %dx%d com teclado: cartão no meio (%d / %d)' % (W,H,c['y'],kh-c['b']), abs(c['y']-(kh-c['b'])) <= 12)
            p.set_viewport_size({'width':W,'height':H}); p.wait_for_timeout(300)
            ctx.close()
        # T5 (nome da criança)
        ctx, _ = novo_contexto(b, fb=fb_com(0), largura=740, altura=360,
                               storage={'mundo_usuarios':us_json([('p1','Hina','🐰')]),
                                        'escola_familia':familia_json(['pmrtestes'],{'p1':'pmrtestes'},'pmrtestes')})
        p = abrir(ctx); p.wait_for_timeout(2000); fechar_tudo(p)
        p.evaluate("EscolaFamilia.abrir('nova')"); p.wait_for_timeout(300)
        p.click('#efRaiz .ef-nome-campo'); p.set_viewport_size({'width':740,'height':150}); p.wait_for_timeout(450)
        m = caixas(p, '#efRaiz .ef-t5 .ef-miolo')[0]
        bichos = caixas(p, '#efRaiz .ef-t5 .ef-bicho')
        r.t('T5 com teclado: nome + 8 bichinhos no meio da área visível (%d / %d)' % (m['y'], 150-m['b']),
            abs(m['y']-(150-m['b'])) <= 14 and len(bichos)==8 and all(x['b'] <= 150 for x in bichos))
        ctx.close()
        res.append(r.fim())

        # ================= 2) "Achei a sua família" =================
        r = R('2) "Achei a sua família": largo, com respiro, botões sempre à vista')
        for (W,H) in DEITADO + [(1280,800)]:
            for n in (1,3,6):
                ctx, _ = novo_contexto(b, fb=fb_com(n), largura=W, altura=H)
                p = abrir(ctx); p.wait_for_timeout(1000)
                p.click('.ef-t1-ja'); p.wait_for_timeout(300)
                p.fill('.ef-t2 .ef-codigo','pmrtestes'); p.click('.ef-t2 .ef-procurar'); p.wait_for_timeout(1300)
                card = caixas(p, '.ef-t2 .ef-card')[0]
                bts = caixas(p, '.ef-t2 .ef-botoes-achei .ef-btn')
                gr = caixas(p, '.ef-t2 .ef-cartoes')[0]
                minis = caixas(p, '.ef-t2 .ef-mini')
                esperado = min(960, 0.96*W)
                ok_larg = card['w'] >= 0.9*esperado
                ok_bts = len(bts)==3 and all(x['y']>=0 and x['b']<=H and x['h']>=48 for x in bts)
                ok_sep = all(not sobrepoe(a,c,-8) for i,a in enumerate(bts) for c in bts[i+1:])   # 8 px ou mais entre eles
                ok_cartoes = gr['b'] <= min(x['y'] for x in bts) - 4 and len(minis)==n
                ok_nomes = all(x['sw'] <= x['cw']+1 for x in caixas(p, '.ef-t2 .ef-mini .ef-nome'))
                # o que não cabe rola dentro da grade, nunca some: a grade inteira cabe ou rola
                rola = p.evaluate("(()=>{const g=document.querySelector('.ef-t2 .ef-cartoes'); return g.scrollHeight<=g.clientHight+2 || getComputedStyle(g).overflowY==='auto';})()".replace('clientHight','clientHeight'))
                some = p.is_visible('.ef-t2 .ef-codigo') or p.is_visible('.ef-t2 .ef-cancelar') or p.is_visible('.ef-t2 .ef-procurar')
                r.t('%dx%d, %d criança(s): pop-up largo (%d px), cartões sem encostar nos botões, 3 botões inteiros e separados, nomes inteiros' % (W,H,n,card['w']),
                    ok_larg and ok_bts and ok_sep and ok_cartoes and ok_nomes and rola and not some,
                    dict(larg=ok_larg, bts=ok_bts, sep=ok_sep, cartoes=ok_cartoes, nomes=ok_nomes, rola=rola, some=some))
                if n==6 and W>=740:
                    fileiras = len(set(round(x['y']) for x in minis))
                    r.t('%dx%d: as 6 crianças cabem em até 2 fileiras (sem rolar)' % (W,H), fileiras <= 2, fileiras)
                ctx.close()
        # nomes compridos: nunca cortados (podem ir para 2 linhas)
        import unicodedata, re
        CHAVE = lambda n: re.sub(r'[^a-z0-9]+','-', unicodedata.normalize('NFD', n).encode('ascii','ignore').decode().lower()).strip('-')
        LONGOS = [('Maria Eduarda','🐰','1f430'),('Maria Clara','🦋','1f98b'),('Pedro Henrique','🐱','1f431'),('João Pedro','🐯','1f42f')]
        for (W,H) in [(984,432),(740,360),(568,320),(1280,800)]:
            fb = FakeFirebase()
            for nome, av, cod in LONGOS:
                fb.gravar_app(CHAVE(nome)+'_'+cod, nome, av, {'lidas':json.dumps({'AL1':'11'})}, familia='pmrtestes')
            fb.gravar_app('maria-eduarda_1f430','Maria Eduarda','🐰',{'x':'1'}, app='matematica', familia='pmrtestes')
            ctx, _ = novo_contexto(b, fb=fb, largura=W, altura=H)
            p = abrir(ctx); p.wait_for_timeout(1000); p.click('.ef-t1-ja'); p.wait_for_timeout(300)
            p.fill('.ef-t2 .ef-codigo','pmrtestes'); p.click('.ef-t2 .ef-procurar'); p.wait_for_timeout(1300)
            nomes = p.evaluate("Array.from(document.querySelectorAll('.ef-t2 .ef-mini .ef-nome')).map(e=>({t:e.textContent, sw:e.scrollWidth, cw:e.clientWidth, sh:e.scrollHeight, ch:e.clientHeight, ell:getComputedStyle(e).textOverflow}))")
            r.t('%dx%d: nomes compridos inteiros no "Achei" (MARIA EDUARDA, PEDRO HENRIQUE…)' % (W,H),
                len(nomes)==4 and all(x['sw']<=x['cw']+1 and x['sh']<=x['ch']+1 and x['ell']!='ellipsis' for x in nomes), nomes)
            bts = caixas(p, '.ef-t2 .ef-botoes-achei .ef-btn')
            r.t('%dx%d: ...e os botões continuam inteiros na tela' % (W,H), len(bts)==3 and all(x['b']<=H for x in bts))
            ctx.close()
        # 4 crianças numa fileira nos 2 Motorolas do Pedro; ✕ sem encostar no título também em pé
        for (W,H) in [(984,432),(937,411)]:
            ctx, _ = novo_contexto(b, fb=fb_com(4), largura=W, altura=H)
            p = abrir(ctx); p.wait_for_timeout(1000); p.click('.ef-t1-ja'); p.wait_for_timeout(300)
            p.fill('.ef-t2 .ef-codigo','pmrtestes'); p.click('.ef-t2 .ef-procurar'); p.wait_for_timeout(1300)
            ys = set(round(x['y']) for x in caixas(p, '.ef-t2 .ef-mini'))
            r.t('%dx%d: 4 crianças numa fileira só no "Achei"' % (W,H), len(ys)==1, ys)
            ctx.close()
        for (W,H) in [(360,740),(568,320),(984,432)]:
            ctx, _ = novo_contexto(b, fb=fb_com(3), largura=W, altura=H)
            p = abrir(ctx); p.wait_for_timeout(1000); p.click('.ef-t1-ja'); p.wait_for_timeout(300)
            p.fill('.ef-t2 .ef-codigo','pmrtestes'); p.click('.ef-t2 .ef-procurar'); p.wait_for_timeout(1300)
            folga = p.evaluate("(()=>{const a=document.querySelector('.ef-t2 .ef-x-achei').getBoundingClientRect(); const rg=document.createRange(); rg.selectNodeContents(document.querySelector('.ef-t2 .ef-achei')); const t=rg.getBoundingClientRect(); return Math.min(a.left - t.right, a.bottom <= t.top ? 99 : 999);})()")
            r.t('%dx%d: o ✕ fica a 8 px ou mais do título "ACHEI A SUA FAMÍLIA!"' % (W,H), folga >= 8, folga)
            ctx.close()
        # Enter (lupa do teclado) no campo: o "Achei" aparece e o campo perde o foco (o teclado fecha)
        ctx, _ = novo_contexto(b, fb=fb_com(3), largura=984, altura=432)
        p = abrir(ctx); p.wait_for_timeout(1000); p.click('.ef-t1-ja'); p.wait_for_timeout(300)
        p.click('.ef-t2 .ef-codigo'); p.keyboard.type('pmrtestes'); p.keyboard.press('Enter'); p.wait_for_timeout(1300)
        r.t('Enter no campo: aparece o "Achei" e o foco sai do campo (no celular, o teclado fecha)', p.is_visible('.ef-t2 .ef-trazer-todas') and not p.evaluate("document.activeElement && document.activeElement.classList.contains('ef-codigo')"))
        ctx.close()
        # o ✕ do "Achei" (cancelar) fica no canto, sem cobrir o título
        ctx, _ = novo_contexto(b, fb=fb_com(3), largura=568, altura=320)
        p = abrir(ctx); p.wait_for_timeout(1000); p.click('.ef-t1-ja'); p.wait_for_timeout(300)
        p.fill('.ef-t2 .ef-codigo','pmrtestes'); p.click('.ef-t2 .ef-procurar'); p.wait_for_timeout(1300)
        x = caixas(p, '.ef-t2 .ef-x-achei'); tit = caixas(p, '.ef-t2 .ef-achei')[0]
        r.t('"Achei": ✕ (cancelar) no canto, com 48 px, sem cobrir o título', len(x)==1 and x[0]['h']>=48 and not sobrepoe(x[0], tit))
        p.click('.ef-t2 .ef-x-achei'); p.wait_for_timeout(300)
        r.t('...tocar no ✕ fecha e volta para a tela de boas-vindas, sem guardar nada', not aberta(p,'ef-t2') and aberta(p,'ef-t1') and estado_familia(p)['familias']==[])
        ctx.close()
        # letras e botões do "Achei"
        ctx, _ = novo_contexto(b, fb=fb_com(3), largura=740, altura=360)
        p = abrir(ctx); p.wait_for_timeout(1000); p.click('.ef-t1-ja'); p.wait_for_timeout(300)
        p.fill('.ef-t2 .ef-codigo','pmrtestes'); p.click('.ef-t2 .ef-procurar'); p.wait_for_timeout(1300)
        fs = p.evaluate("Array.from(document.querySelectorAll('.ef-t2 .ef-card *')).filter(e=>e.offsetParent && e.childNodes.length && Array.from(e.childNodes).some(n=>n.nodeType===3&&n.textContent.trim())).map(e=>parseFloat(getComputedStyle(e).fontSize))")
        r.t('"Achei": todas as letras com 14 px ou mais', min(fs) >= 14, min(fs))
        r.t('"Achei": o código procurado aparece embaixo do título', 'PMRTESTES' in p.text_content('.ef-t2 .ef-codigo-achado'))
        ordem = p.evaluate("Array.from(document.querySelectorAll('.ef-t2 .ef-botoes-achei .ef-btn')).map(e=>e.className)")
        r.t('"Achei": botões na ordem ← OUTRO CÓDIGO · ESCOLHER · TRAZER TODAS (o verde à direita)', 'ef-outro-codigo' in ordem[0] and 'ef-escolher' in ordem[1] and 'ef-trazer-todas' in ordem[2], ordem)
        ctx.close()
        res.append(r.fim())

        # ================= 3) Configurações =================
        r = R('3) Configurações: largura deitado e "Família e nuvem" com respiro')
        st = {'mundo_usuarios':us_json([('p1','Hina','🐰'),('p2','Renata','🦋')],'p1'),
              'escola_familia':familia_json(['pmrtestes'],{'p1':'pmrtestes','p2':'pmrtestes'},'pmrtestes')}
        for (W,H) in DEITADO + [(1280,800),(360,740)]:
            ctx, _ = novo_contexto(b, fb=fb_com(2), largura=W, altura=H, storage=st)
            p = abrir(ctx); p.wait_for_timeout(2200); fechar_tudo(p)
            p.evaluate("openCfg()"); p.wait_for_timeout(400)
            card = caixas(p, '#cfgCard')[0]
            deitado = W > H
            if deitado:
                r.t('%dx%d: pop-up das Configurações usa a largura (%d px de %d)' % (W,H,card['w'],W), card['w'] >= 0.9*min(980, 0.94*W))
            if deitado and W >= 700:
                cols = p.evaluate("getComputedStyle(document.querySelector('#cfgOv .cfgBody')).gridTemplateColumns.split(' ').length")
                r.t('%dx%d: as opções do app ficam em 2 colunas' % (W,H), cols == 2, cols)
            linhas = p.evaluate("""Array.from(document.querySelectorAll('#cfgFamilia .ef-cfg-linha')).map(l=>{
                const r=l.getBoundingClientRect(); const bs=Array.from(l.querySelectorAll('.ef-btn')).map(b=>b.getBoundingClientRect());
                const t=l.querySelector('.ef-cfg-txt').getBoundingClientRect();
                return {cls:l.className, h:r.height, dentro: bs.every(b=>b.left>=r.left-1&&b.right<=r.right+1),
                        alt: bs.every(b=>b.height>=48), bs: bs.map(b=>[b.left,b.right,b.top,b.bottom]), t:[t.left,t.right,t.top,t.bottom]}; })""")
            sep = True
            for l in linhas:
                bs = l['bs']
                for i in range(len(bs)):
                    for j in range(i+1, len(bs)):
                        a, c = bs[i], bs[j]
                        if not (a[1]+8 <= c[0] or c[1]+8 <= a[0] or a[3]+8 <= c[2] or c[3]+8 <= a[2]): sep = False
            r.t('%dx%d: "Família e nuvem": botões dentro da linha, com 48 px ou mais e com 8 px ou mais entre eles' % (W,H),
                linhas and all(l['dentro'] and l['alt'] for l in linhas) and sep, linhas)
            if deitado and W >= 740:
                r.t('%dx%d: cada linha fica numa linha só (texto à esquerda, botões à direita)' % (W,H), all(l['h'] <= 84 for l in linhas), [round(l['h']) for l in linhas])
            sobra = p.evaluate("(()=>{const e=document.querySelector('#cfgOv .cfgBody'); return e.scrollWidth - e.clientWidth;})()")
            r.t('%dx%d: nada sai para o lado (sem rolar na horizontal)' % (W,H), sobra <= 1, sobra)
            ctx.close()
        # trava do adulto continua: toque rápido não abre, 3 s abre
        ctx, _ = novo_contexto(b, fb=fb_com(2), largura=984, altura=432, storage=st)
        p = abrir(ctx); p.wait_for_timeout(2200); fechar_tudo(p)
        p.evaluate("openCfg()"); p.wait_for_timeout(400)
        r.t('Botões do adulto numa linha só: "◯ 👨 ABRIR ▶" e "◯ 👨 👁 MOSTRAR"', p.evaluate("['.ef-cfg-copias-bt','.ef-cfg-mostrar'].every(s=>{const e=document.querySelector(s); return e && e.classList.contains('ef-adulto-curto') && e.textContent.indexOf('👨')>=0 && !e.querySelector('small');})"))
        p.click('.ef-cfg-mostrar'); p.wait_for_timeout(300)
        r.t('...toque rápido em MOSTRAR não mostra o código e explica "PEÇA PARA UM ADULTO SEGURAR"', '••••' in p.text_content('.ef-cfg-cod') and 'ADULTO' in toast(p))
        segurar(p, '.ef-cfg-mostrar')
        r.t('...segurando 3 s mostra o código', p.text_content('.ef-cfg-cod').strip().lower()=='pmrtestes')
        segurar(p, '.ef-cfg-copias-bt')
        r.t('...segurando 3 s em ABRIR abre as Cópias de cada dia', aberta(p, 'ef-copias'))
        ctx.close()
        res.append(r.fim())

        # ================= 4) Quem vai estudar hoje? / 5) Famílias =================
        r = R('4) "Quem vai estudar hoje?" e "Famílias neste celular": no meio e com respiro')
        st1 = {'mundo_usuarios':us_json([('p1','Hina','🐰')]),
               'escola_familia':familia_json(['pmrtestes'],{'p1':'pmrtestes'},'pmrtestes')}
        for (W,H) in DEITADO + [(1280,800)]:
            ctx, _ = novo_contexto(b, fb=fb_com(4), largura=W, altura=H, storage=st1)
            p = abrir(ctx); p.wait_for_timeout(2200); fechar_tudo(p)
            p.evaluate("EscolaFamilia.abrir('quem')"); p.wait_for_timeout(1500)
            cards = caixas(p, '.ef-t4 .ef-grade .ef-crianca')
            meio = caixas(p, '.ef-t4 .ef-meio')[0]
            esq = min(c['x'] for c in cards) - meio['x']; dir_ = meio['r'] - max(c['r'] for c in cards)
            r.t('%dx%d: os cartões ficam no meio (sobra à esquerda %d, à direita %d)' % (W,H,esq,dir_), abs(esq-dir_) <= 24, (esq,dir_))
            if W >= 937:
                r.t('%dx%d: Hina + 3 da nuvem + ➕ numa fileira só' % (W,H), len(set(round(c['y']) for c in cards))==1 and len(cards)==5, len(cards))
            stt = caixas(p, '.ef-t4 .ef-status-txt')[0]
            r.t('%dx%d: o texto da nuvem no rodapé não fica cortado' % (W,H), stt['sw'] <= stt['cw']+1 and stt['r'] <= W)
            fl = caixas(p, '.ef-t4 .ef-familia-link')[0]
            r.t('%dx%d: "🔑 FAMÍLIA PMR••••" inteiro, com 48 px, longe do texto da nuvem' % (W,H), fl['r'] <= W and fl['h'] >= 48 and (fl['x'] - stt['r'] >= 8 or fl['y'] >= stt['b']))
            fechar_tudo(p)
            p.evaluate("EscolaFamilia.abrir('familias')"); p.wait_for_timeout(600)
            fl = caixas(p, '.ef-t8 .ef-fam-linha')[0]
            if W >= 740:
                r.t('%dx%d: Famílias: cada família numa linha só (%d px)' % (W,H,fl['h']), fl['h'] <= 84)
            r.t('%dx%d: Famílias: o código aparece em CAIXA ALTA como nas outras telas (PMR••••)' % (W,H), p.evaluate("getComputedStyle(document.querySelector('.ef-t8 .ef-cod')).textTransform")=='uppercase')
            ctx.close()
        res.append(r.fim())

        # ================= 6) site de teste =================
        r = R('6) Site de teste: escolasaopedrocuriosidadestestes.netlify.app (o site novo do Pedro)')
        def no_host(host):
            ctx, _ = novo_contexto(b, fb=fb_com(1))
            pasta = os.path.abspath(PASTA)
            def h(route):
                u = route.request.url.split('?')[0]; cam = u[len(host):] or 'index.html'
                if cam=='nuvem-config.js': return route.fallback()
                arq = os.path.join(pasta, cam)
                if not os.path.isfile(arq): return route.fulfill(status=404, body='')
                tipo = 'text/html' if arq.endswith('.html') else ('application/javascript' if arq.endswith('.js') else 'application/octet-stream')
                route.fulfill(status=200, content_type=tipo+'; charset=utf-8', body=open(arq,'rb').read())
            ctx.route(host+'**', h)
            p = ctx.new_page(); p.goto(host, wait_until='load'); p.wait_for_timeout(800)
            return ctx, p
        ctx, p = no_host('https://escolasaopedrocuriosidadestestes.netlify.app/')
        r.t('No site de teste do Pedro aparece a faixa roxa "🧪 SITE DE TESTE" nas telas da família', p.is_visible('.ef-teste'))
        f = caixas(p, '.ef-teste')[0]; bt = caixas(p, '.ef-t1 .ef-btn')
        tit = caixas(p, '.ef-t1 .ef-titulo')[0]
        r.t('...sem cobrir o título nem os botões da tela', all(not sobrepoe(f, x) for x in bt + [tit]))
        p.click('.ef-t1-novo'); p.wait_for_timeout(300); p.click('.ef-t3 .ef-criar'); p.wait_for_timeout(1500)
        p.click('.ef-ja-anotei'); p.wait_for_timeout(800)
        cadastrar_t5(p, 'Teste Bia', 2); fechar_tudo(p); p.wait_for_timeout(300)
        r.t('...e some quando a criança está no app (nunca por cima da barra de cima do app)', not p.is_visible('.ef-teste') and p.is_visible('#cfgGearHome'))
        ctx.close()
        ctx, p = no_host('https://escolasaopedrocuriosidades.netlify.app/')
        r.t('No site de verdade NÃO aparece a faixa', not p.is_visible('.ef-teste'))
        ctx.close()
        res.append(r.fim())

        # ================= 7) tela cheia =================
        r = R('7) Tela cheia: como o app já fazia (D18): pede a tela cheia de verdade, também no app instalado')
        CONTA = """(function(){ window.__pedidos=0; const f=function(){ window.__pedidos++; return Promise.resolve(); };
          Element.prototype.requestFullscreen=f; Element.prototype.webkitRequestFullscreen=f; })();"""
        INSTALADO = """(function(){ const mm=window.matchMedia.bind(window);
          window.matchMedia=function(q){ if(/display-mode:\\s*fullscreen/.test(q)) return {matches:true,media:q,addListener(){},removeListener(){},addEventListener(){},removeEventListener(){}}; return mm(q); }; })();"""
        for instalado in (False, True):
            ctx, _ = novo_contexto(b, fb=fb_com(0), storage=st1)
            ctx.add_init_script(CONTA)
            if instalado: ctx.add_init_script(INSTALADO)
            p = abrir(ctx); p.wait_for_timeout(2000); fechar_tudo(p)
            antes = p.evaluate("window.__pedidos")
            p.mouse.click(370, 200); p.wait_for_timeout(300); p.mouse.click(370, 200); p.wait_for_timeout(300)
            n = p.evaluate("window.__pedidos")
            if instalado:
                r.t('Aberto pelo ícone: pede a tela cheia de verdade, como na v1.8 (sem as barras do Android) (%d pedidos)' % n, n >= 1)
            else:
                r.t('No navegador: continua pedindo a tela cheia ao tocar (como antes)', n > antes or n >= 1, (antes, n))
            ctx.close()
        # tela cheia de verdade (sem imitação), na aba do navegador: o ⛶ entra e SAI como antes
        ctx, _ = novo_contexto(b, fb=fb_com(0), storage=st1)
        p = abrir(ctx); p.wait_for_timeout(2000); fechar_tudo(p)
        p.evaluate("document.exitFullscreen && document.fullscreenElement && document.exitFullscreen()"); p.wait_for_timeout(300)
        FS = '#homeTop button[title="Tela cheia"]'
        p.click(FS); p.wait_for_timeout(500)
        dentro = p.evaluate("!!document.fullscreenElement")
        p.click(FS); p.wait_for_timeout(500)
        fora = p.evaluate("!document.fullscreenElement")
        r.t('Na aba do navegador: o ⛶ da tela inicial entra na tela cheia e, tocado de novo, sai (como na v1.8)', dentro and fora, (dentro, fora))
        ctx.close()
        res.append(r.fim())
        # ================= 8) barras de cima do Curiosidades =================
        r = R('8) Barras de cima (tela inicial e leitura): chip ao lado da ⚙️, nada fora da tela, botões do mesmo tamanho da v1.8')
        V18 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'versao_anterior_v1.8')
        def medir_barra(p, barra):
            return p.evaluate("""b=>{ const t=document.getElementById(b); const W=innerWidth;
              const els=Array.from(t.querySelectorAll('button,.ef-chip,#meta,h1')).filter(e=>e.offsetParent || getComputedStyle(e).position==='fixed');
              const mc=t.querySelector('#meta .mCont'), mt=t.querySelector('#meta');
              const lista=els.map(e=>{ const r=e.getBoundingClientRect(); return {id:e.id||e.className, x:r.left, r:r.right, y:r.top, b:r.bottom, w:r.width, h:r.height, chip:e.classList.contains('ef-chip')}; });
              lista.push({id:'__barra', x:0, r:0, y:0, b:0, w:0, h:t.getBoundingClientRect().height, chip:false,
                          contador: mc ? (mc.getBoundingClientRect().right <= mt.getBoundingClientRect().right+0.5 && mc.getBoundingClientRect().width>0) : null});
              return lista; }""", barra)
        larg18 = {}
        for (W,H) in DEITADO:
            for gaveta in (False, True):
                stg = {'mundo_usuarios':us_json([('p1','Hinata','🦋')]), 'mundo_p1_ajustes':'1' if gaveta else '0',
                       'escola_familia':familia_json(['pmrtestes'],{'p1':'pmrtestes'},'pmrtestes'), 'nuvem_familia':'pmrtestes'}
                medidas = {}
                for versao in ('v1.8','v2.0'):
                    ctx, _ = novo_contexto(b, fb=fb_com(0), largura=W, altura=H, storage=stg)
                    if versao=='v1.8':
                        pasta = os.path.abspath(V18)
                        def h(route):
                            u = route.request.url.split('?')[0]; cam = u[len(URL):] or 'index.html'
                            if cam=='nuvem-config.js': return route.fallback()
                            arq = os.path.join(pasta, cam)
                            if not os.path.isfile(arq): return route.fulfill(status=404, body='')
                            tipo = 'text/html' if arq.endswith('.html') else ('application/javascript' if arq.endswith('.js') else 'application/octet-stream')
                            route.fulfill(status=200, content_type=tipo+'; charset=utf-8', body=open(arq,'rb').read())
                        ctx.route(URL+'**', h)
                    p = abrir(ctx); p.wait_for_timeout(1500)
                    if versao=='v2.0': p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1500)
                    p.evaluate("goHome()"); p.wait_for_timeout(300)
                    casa = medir_barra(p, 'homeTop')
                    p.evaluate("paisIdx=5; curIdx=0; openReader();"); p.wait_for_timeout(400)
                    leit = medir_barra(p, 'top')
                    if versao=='v2.0':
                        p.screenshot(path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','capturas','barra_leitura_%dx%d%s.png' % (W,H,'_gaveta' if gaveta else '')))
                    medidas[versao] = (casa, leit)
                    ctx.close()
                for nome_b, k in (('tela inicial',0),('leitura',1)):
                    v20 = [x for x in medidas['v2.0'][k] if x['id']!='__barra']; v18 = [x for x in medidas['v1.8'][k] if x['id']!='__barra']
                    b20 = [x for x in medidas['v2.0'][k] if x['id']=='__barra'][0]; b18 = [x for x in medidas['v1.8'][k] if x['id']=='__barra'][0]
                    chip = [x for x in v20 if x['chip']]
                    bts = [x for x in v20 if not x['chip'] and x['id'] not in ('meta','homeTitle') and 'h1' not in x['id']]
                    dentro = all(x['x'] >= -0.5 and x['r'] <= W+0.5 for x in v20)
                    sobre = [ (a['id'],c['id']) for i,a in enumerate(v20) for c in v20[i+1:] if not (a['r'] <= c['x']+0.5 or c['r'] <= a['x']+0.5 or a['b'] <= c['y']+0.5 or c['b'] <= a['y']+0.5) and 'h1' not in (a['id']+c['id']) ]
                    w18 = {x['id']: round(x['w']) for x in v18 if x['id'] and x['id'] not in ('meta','userChip','homeTitle')}
                    w20 = {x['id']: round(x['w']) for x in v20 if x['id'] and x['id'] not in ('meta','homeTitle')}
                    iguais = all(w20.get(i)==w for i,w in w18.items() if i in w20)
                    gear = 'cfgGearHome' if k==0 else 'gear'
                    ladoalado = chip and [x for x in v20 if x['id']==gear] and abs([x for x in v20 if x['id']==gear][0]['x'] - chip[0]['r']) <= 20
                    meta = [x for x in v20 if x['id']=='meta']
                    alt_ok = b20['h'] <= b18['h'] + 2
                    cont_ok = (k==0) or b20['contador']
                    r.t('%dx%d %s%s: chip visível colado à ⚙️, tudo dentro da tela, nada encavalado, botões do mesmo tamanho da v1.8, barra da mesma altura (%d / %d px)%s' % (W,H,nome_b,' (gaveta aberta)' if gaveta else '', b20['h'], b18['h'], (', o número da curiosidade inteiro no selo (%d px)' % meta[0]['w']) if meta else ''),
                        chip and chip[0]['h'] >= 44 and dentro and not sobre and iguais and ladoalado and alt_ok and cont_ok,
                        dict(chip=chip[:1], dentro=dentro, sobre=sobre, iguais=iguais, w18=w18, w20=w20, meta=meta, alt=(b20['h'],b18['h']), cont=cont_ok))
        # em pé (a tela inicial e a leitura são giradas pelo app): o chip continua dentro da tela
        for (W,H) in [(360,740),(412,915)]:
            ctx, _ = novo_contexto(b, fb=fb_com(0), largura=W, altura=H, storage={'mundo_usuarios':us_json([('p1','Hinata','🦋')]),
                     'escola_familia':familia_json(['pmrtestes'],{'p1':'pmrtestes'},'pmrtestes'),'nuvem_familia':'pmrtestes'})
            p = abrir(ctx); p.wait_for_timeout(1500); p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1500)
            for tela, sel in (('tela inicial','#efChipHome .ef-chip'),('leitura','#efChipLeitura .ef-chip')):
                if tela=='leitura': p.evaluate("paisIdx=5; curIdx=0; openReader();"); p.wait_for_timeout(400)
                bb = p.locator(sel).bounding_box()
                r.t('em pé %dx%d %s: o chip fica dentro da tela (a barra é girada junto com o app)' % (W,H,tela), bb and bb['x']>=-0.5 and bb['y']>=-0.5 and bb['x']+bb['width']<=W+0.5 and bb['y']+bb['height']<=H+0.5, bb)
            ctx.close()
        res.append(r.fim())
        b.close()
    return res

if __name__=='__main__':
    res = main()
    ok = sum(a for a,_ in res); tot = sum(t for _,t in res)
    print('\nDESENHO: %d/%d' % (ok,tot))
    sys.exit(0 if ok==tot else 1)
