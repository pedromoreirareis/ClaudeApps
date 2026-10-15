"""🌍 Curiosidades v2.3 — versão final desta rodada.

1) Dados: só as 3 correções autorizadas mudaram (Júpiter #11, Netuno #8, Nosso Cerrado #3); todo cartão tem a
   frase do símbolo grande; nenhuma frase curta repetida no app.
2) "Destacar por sílabas" saiu (Configurações e barra de baixo); o valor antigo guardado é ignorado; o dicionário
   volta a aparecer na frase do cartão.
3) Ler Mais: margem direita (Normal / Sílabas / Espaços) e recuo, como no Coruja Explica; ajustes por criança
   (celular, nuvem, backup); ⚙️ no Ler Mais e nas Configurações; Esc; o pop-up cabe em vários tamanhos.
4) Destaque duplo: com o destaque por linha, segurar o dedo numa palavra dá a ela um segundo destaque.
Chromium + Firebase de mentira (nunca o Firebase real)."""
from base import *
from ef import *
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE22 = os.path.join(AQUI, '..', '..', 'trabalho', 'base_v2.2', 'index.html')

def obj(s, nome, abre):
    i = s.index('const %s=' % nome); j = s.index(abre, i); k = s.index('\n', j)
    return json.loads(s[j:k].rstrip().rstrip(';'))

def st_criancas(lista, fam='pmrtestes', atual=None, extra=None):
    st = {'mundo_usuarios': us_json(lista, atual), 'escola_familia': familia_json([fam], {i: fam for i, _, _ in lista}, fam), 'nuvem_familia': fam}
    if extra: st.update(extra)
    return st

def abre_lermais(p, code='C17', cur=0):
    i = p.evaluate("c=>DATA.findIndex(x=>x.code===c)", code)
    p.evaluate("([i,c])=>{ paisIdx=i; curIdx=c; openReader(); }", [i, cur]); p.wait_for_timeout(300)
    p.evaluate("abrirDetalhes()"); p.wait_for_timeout(700)

SHY = "document.getElementById('detTexto').textContent.split('\\u00AD').length-1"

def segura(p, loc, ms=700):
    bb = loc.bounding_box()
    p.mouse.move(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 2)
    p.mouse.down(); p.wait_for_timeout(ms); p.mouse.up(); p.wait_for_timeout(300)

def _lum(rgb):
    import re
    v = [int(x) / 255 for x in re.findall(r'\d+', rgb)[:3]]
    v = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in v]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]
def contraste(a, b):
    la, lb = sorted([_lum(a), _lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)

def main():
    res = []
    # ================= 1) dados =================
    r = R('1) Dados: só as correções autorizadas; frase do símbolo em todos os cartões')
    s0 = open(BASE22, encoding='utf-8').read(); s1 = open(os.path.join(PASTA, 'index.html'), encoding='utf-8').read()
    D0, D1 = obj(s0, 'DATA', '['), obj(s1, 'DATA', '[')
    mud = [(c['code'], n + 1) for c, c0 in zip(D1, D0) for n, (a, b) in enumerate(zip(c['items'], c0['items'])) if a != b]
    r.t('Mesmos cartões, mesma ordem, mesmo número de curiosidades (4.254)', [c['code'] for c in D0] == [c['code'] for c in D1] and
        [len(c['items']) for c in D0] == [len(c['items']) for c in D1] and sum(len(c['items']) for c in D1) == 4254)
    r.t('Só mudaram Júpiter #11 (Juno), Netuno #8 (Voyager 2), Nosso Cerrado #3 (frase repetida) e os 2 hífens escondidos (Brasil Colônia #5, Idade Média #17)',
        sorted(mud) == [('F4', 3), ('HBR', 5), ('HID', 17), ('JUP', 11), ('NET', 8)], mud)
    def _it(D, code, n): return [c for c in D if c['code'] == code][0]['items'][n - 1]
    a, b = _it(D0, 'HBR', 5), _it(D1, 'HBR', 5)
    a2, b2 = _it(D0, 'HID', 17), _it(D1, 'HID', 17)
    r.t('...e nessas duas só saiu o hífen invisível (e "NUM ARMAÇÃO" → "NUMA ARMAÇÃO")',
        dict(a, d=a['d'].replace('\u00ad', '')) == b and dict(a2, d=a2['d'].replace('\u00ad', '').replace('NUM ARMAÇÃO', 'NUMA ARMAÇÃO')) == b2)
    todas = [it['c'] for c in D1 for it in c['items']]
    r.t('Nenhuma frase curta repetida no app inteiro (a do Cerrado era a única)', len(set(todas)) == len(todas))
    P0, P1 = obj(s0, 'PAIS_DESC', '{'), obj(s1, 'PAIS_DESC', '{')
    r.t('Todo cartão (menos os 4 de Língua Portuguesa, que não mostram símbolo) tem a frase do símbolo grande',
        not [c['code'] for c in D1 if c['code'] not in P1 and not c.get('simbolo')])
    r.t('As frases antigas do símbolo não mudaram; nenhuma diz "é um país do mundo"', all(P1[k] == v for k, v in P0.items()) and not [v for v in P1.values() if v.endswith('é um país do mundo.')])
    r.t('Os emojis e as fontes não mudaram', obj(s0, 'EMOJI_DESC', '{') == obj(s1, 'EMOJI_DESC', '{') and
        [l for l in s0.split('\n') if l.startswith('@font-face')] == [l for l in s1.split('\n') if l.startswith('@font-face')])
    res.append(r.fim())

    servidor()
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        # ================= 2) sílabas fora =================
        r = R('2) "Destacar por sílabas" saiu do app')
        ctx, fb = novo_contexto(b, largura=984, altura=432, storage=st_criancas([('p1', 'Hinata', '🦋')], extra={'mundo_p1_cfgSyl': '1', 'mundo_p1_cfgHi': '1'}))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        r.t('Criança que tinha "sílabas" ligado: o app ignora (cfgSyl = falso)', p.evaluate('cfgSyl') is False)
        # cartão com palavra do dicionário
        achou = p.evaluate("""(()=>{ for(let i=0;i<DATA.length;i++){ const it=DATA[i].items; for(let c=0;c<it.length;c++){
             if(it[c].c.split(/\\s+/).some(w=>buscaGlossario(w))) return [i,c]; } } return null; })()""")
        p.evaluate("([i,c])=>{ paisIdx=i; curIdx=c; openReader(); }", achou); p.wait_for_timeout(400)
        r.t('A frase do cartão não é mais dividida em sílabas', p.locator('#text .s').count() == 0)
        r.t('...e as palavras do dicionário voltam a aparecer nela (antes, "sílabas" ligado escondia)', p.locator('#text .gloss').count() >= 1)
        r.t('A chavinha "SÍLABAS" da barra de baixo sumiu (o 🔊 "ler ao tocar" continua)', not p.is_visible('#sylSw') and
            p.evaluate("getComputedStyle(document.querySelector('#sylToggle>span')).display") == 'none')
        p.evaluate("openCfg()"); p.wait_for_timeout(300)
        txt = p.text_content('#cfgOv') or ''
        r.t('Nas Configurações não aparece mais "Destacar por sílabas"', not p.is_visible('#cfgSylRow') and 'sílaba que a criança' not in txt)
        r.t('...e aparece "Destacar palavra (segurar o dedo)" e a seção "📖 Ler Mais"', p.is_visible('#cfgPalavraRow') and '📖 Ler Mais' in txt and p.is_visible('#cfgLMName'))
        r.t('Sem erros de JavaScript', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())

        # ================= 3) Ler Mais: margem e recuo =================
        r = R('3) Ler Mais: margem direita (Normal / Sílabas / Espaços) e recuo — como no Coruja Explica')
        fb = FakeFirebase()
        ctx, _ = novo_contexto(b, fb=fb, largura=984, altura=432, storage=st_criancas([('p1', 'Hinata', '🦋'), ('p2', 'Bia', '🐰')], extra={'mundo_p1_voz': '1', 'mundo_p1_cfgAudio': '1'}))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        r.t('Padrão: margem Normal e recuo ligado', p.evaluate("modoMargem") == 'normal' and p.evaluate("recuoOn") is True)
        abre_lermais(p)
        gl_normal = p.locator('#detTexto .gloss').count()
        r.t('Normal: nenhum corte de sílaba e nenhum espaço esticado', p.evaluate(SHY) == 0 and p.locator('#detTexto .wsp.aj').count() == 0)
        ind = p.evaluate("parseFloat(getComputedStyle(document.querySelector('#detTexto p')).textIndent)")
        r.t('Recuo ligado: o parágrafo começa com um espacinho', ind > 5, ind)
        p.click('#detOv .detAj'); p.wait_for_timeout(400)
        r.t('A ⚙️ do Ler Mais abre "⚙️ Ajustes da leitura" (com Normal marcado)', p.evaluate("document.getElementById('ajLMOv').classList.contains('open')") and
            p.locator('#opcoesMargem .opcaoMargem.sel').get_attribute('data-modo') == 'normal')
        p.click('#opcoesMargem .opcaoMargem[data-modo="silabas"]'); p.wait_for_timeout(900)
        r.t('✂️ Sílabas: as palavras ganham os pontos de corte (hífens invisíveis)', p.evaluate(SHY) > 20, p.evaluate(SHY))
        aj = p.evaluate("ultimoAjuste")
        r.t('...e as linhas do parágrafo chegam à margem (sobra dividida entre os espaços)', aj['ajustadas'] > 0 and aj['rentes'] > 0, aj)
        r.t('...as palavras do dicionário continuam marcadas', p.locator('#detTexto .gloss').count() == gl_normal, (gl_normal, p.locator('#detTexto .gloss').count()))
        r.t('Escolha guardada para a criança (mundo_p1_margem = silabas)', ls(p, 'mundo_p1_margem') == 'silabas')
        # tocar numa palavra com ponto de corte: a voz recebe a palavra limpa
        p.keyboard.press('Escape'); p.wait_for_timeout(300)
        r.t('Esc fecha só os Ajustes (o Ler Mais continua aberto)', not p.evaluate("document.getElementById('ajLMOv').classList.contains('open')") and p.evaluate("lerMaisAberto()"))
        p.evaluate("(()=>{ window.__falou=[]; window.speak=(t)=>window.__falou.push(t); cfgAudio=true; sayTapOn=true; vozOn=true; modoLinha=false; })()")
        w = p.locator('#detTexto .w').filter(has_text='­').first
        if w.count():
            w.click(); p.wait_for_timeout(300)
        fal = p.evaluate("window.__falou")
        r.t('Tocar numa palavra que tem ponto de corte: a voz recebe a palavra sem o hífen invisível', fal and '­' not in fal[-1], fal)
        p.evaluate("abrirAjustesLM()"); p.wait_for_timeout(300)
        p.click('#opcoesMargem .opcaoMargem[data-modo="espacos"]'); p.wait_for_timeout(900)
        r.t('↔️ Espaços: nenhuma palavra cortada', p.evaluate(SHY) == 0)
        teto = p.evaluate("""(()=>{ const sp=[...document.querySelectorAll('#detTexto .wsp')]; const n=sp.filter(x=>!x.classList.contains('aj')).map(x=>x.getBoundingClientRect().width).sort((a,b)=>a-b);
             const normal=n[n.length>>1]||0; const ex=sp.filter(x=>x.classList.contains('aj')).map(x=>parseFloat(x.style.marginRight)||0); return [normal, Math.max(0,...ex), ex.length]; })()""")
        r.t('...os espaços crescem no máximo 75% do espaço normal (sem buracos)', teto[2] > 0 and teto[1] <= teto[0] * 0.75 + 0.6, teto)
        p.click('#chaveRecuo'); p.wait_for_timeout(400)
        ind2 = p.evaluate("parseFloat(getComputedStyle(document.querySelector('#detTexto p')).textIndent)")
        r.t('Recuo desligado: o parágrafo começa rente à margem (e fica guardado)', ind2 == 0 and ls(p, 'mundo_p1_recuo') == '0', ind2)
        bb = p.locator('#ajLMOv .ok').bounding_box()
        r.t('984×432: o "Pronto 👍" dos Ajustes aparece inteiro na tela', bb and bb['y'] + bb['height'] <= 432, bb)
        p.click('#ajLMOv .ok'); p.wait_for_timeout(300)
        p.keyboard.press('Escape'); p.wait_for_timeout(300)
        r.t('Esc depois fecha o Ler Mais', not p.evaluate("lerMaisAberto()"))
        r.t('Exportar a criança (backup e nuvem) leva margem, recuo e palavra', all(k in (p.evaluate("ADAPTADOR_CRIANCAS.exportar('p1')") or {}) for k in ('margem', 'recuo', 'palavra')))
        r.t('A criança tem 26 chaves (era 23)', p.evaluate("ADAPTADOR_CRIANCAS.chavesDaCrianca('p1').length") == 26)
        ok_n = esperar_ok(p); dn = fb.dados_app('hinata_1f98b', familia='pmrtestes') or {}
        r.t('Chega na nuvem (Firebase de mentira): margem espacos, recuo 0', ok_n and dn.get('margem') == 'espacos' and dn.get('recuo') == '0', (ok_n, dn.get('margem'), dn.get('recuo')))
        p.evaluate("EscolaFamilia.abrir('quem')"); p.wait_for_timeout(400); escolher(p, 'p2')
        r.t('Outra criança (Bia) continua com o padrão: Normal e recuo ligado', p.evaluate("modoMargem") == 'normal' and p.evaluate("recuoOn") is True)
        p.reload(); p.wait_for_timeout(1500); escolher(p, 'p1')
        r.t('Hinata, depois de fechar e abrir o app: Espaços e recuo desligado', p.evaluate("modoMargem") == 'espacos' and p.evaluate("recuoOn") is False)
        p.evaluate("goHome(); openCfg();"); p.wait_for_timeout(300)
        r.t('Configurações mostram o resumo do Ler Mais', 'Espaços' in (p.text_content('#cfgLMName') or '') and 'desligado' in (p.text_content('#cfgLMName') or ''), p.text_content('#cfgLMName'))
        p.click('#cfgOv .cfgBt:has-text("⚙️ Ajustar")'); p.wait_for_timeout(400)
        r.t('"⚙️ Ajustar" das Configurações abre os mesmos Ajustes, por cima', p.evaluate("document.getElementById('ajLMOv').classList.contains('open')") and p.evaluate("document.getElementById('cfgOv').classList.contains('open')"))
        p.keyboard.press('Escape'); p.wait_for_timeout(300)
        r.t('Esc fecha os Ajustes e as Configurações continuam abertas', not p.evaluate("document.getElementById('ajLMOv').classList.contains('open')") and p.evaluate("document.getElementById('cfgOv').classList.contains('open')"))
        r.t('Sem erros de JavaScript', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        # tamanhos
        for (W, H) in [(568, 320), (740, 360), (360, 740)]:
            ctx, _ = novo_contexto(b, largura=W, altura=H, storage=st_criancas([('p1', 'Hinata', '🦋')], extra={'mundo_p1_margem': 'silabas'}))
            erros = []
            p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
            abre_lermais(p)
            aj = p.evaluate("ultimoAjuste")
            sobra = p.evaluate("""(()=>{ const b=document.getElementById('detTexto'); return b.scrollWidth-b.clientWidth; })()""")
            r.t('%dx%d: Sílabas funciona no Ler Mais e o texto não passa da borda (sem rolar para o lado)' % (W, H), p.evaluate(SHY) > 0 and aj['linhas'] > 0 and sobra <= 1, (aj, sobra))
            p.evaluate("abrirAjustesLM()"); p.wait_for_timeout(400)
            bb = p.locator('#ajLMOv .ok').bounding_box(); vis = p.evaluate("(()=>{ const c=document.querySelector('#ajLMOv .pcard'); return c.scrollHeight<=c.clientHeight+1; })()")
            r.t('%dx%d: os Ajustes cabem (o "Pronto 👍" fica na tela, rolando o cartão se preciso)' % (W, H), bb is not None and (bb['y'] + bb['height'] <= H or not vis), (bb, vis))
            p.screenshot(path=os.path.join(AQUI, '..', '..', 'capturas', 'v23_ajustes_%dx%d.png' % (W, H)))
            r.t('%dx%d: sem erros de JavaScript' % (W, H), not [e for e in erros if 'console.error' not in e], erros)
            ctx.close()
        res.append(r.fim())

        # ================= 4) destaque duplo =================
        r = R('4) Destaque duplo: com o destaque por linha, segurar o dedo numa palavra')
        ctx, _ = novo_contexto(b, largura=984, altura=432, storage=st_criancas([('p1', 'Hinata', '🦋')], extra={'mundo_p1_modoLinha': '1', 'mundo_p1_cfgAudio': '0'}))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        i = p.evaluate("DATA.findIndex(x=>x.code==='C17')"); p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
        w2 = p.locator('#text .w').nth(2)
        segura(p, w2)
        r.t('Segurar o dedo numa palavra: a linha fica marcada E a palavra ganha o segundo destaque', p.locator('#text .w.pal').count() == 1 and
            p.evaluate("!!document.querySelector('#text .lineHi.on')") and 'pal' in (w2.get_attribute('class') or ''))
        cs = p.evaluate("(()=>{ const c=getComputedStyle(document.querySelector('#text .w.pal')); return [c.color, c.backgroundColor]; })()")
        r.t('...com letra clara num fundo escuro (diferente do marca-texto da linha)', contraste(cs[0], cs[1]) >= 4.5, cs)
        p.screenshot(path=os.path.join(AQUI, '..', '..', 'capturas', 'v23_destaque_duplo.png'))
        p.locator('#text .w').last.click(); p.wait_for_timeout(300)
        r.t('Um toque normal em outra palavra tira o destaque da palavra (a linha continua funcionando)', p.locator('#text .w.pal').count() == 0 and p.evaluate("!!document.querySelector('#text .lineHi.on')"))
        segurou_curto = p.locator('#text .w').nth(1); segura(p, segurou_curto, ms=150)
        r.t('Um toque rápido não dá o segundo destaque', p.locator('#text .w.pal').count() == 0)
        menu = p.evaluate("(()=>{ const w=document.querySelector('#text .w'); const e=new MouseEvent('contextmenu',{bubbles:true,cancelable:true}); w.dispatchEvent(e); return e.defaultPrevented; })()")
        r.t('Segurar o dedo não abre o menu do navegador (copiar/selecionar)', menu is True)
        p.evaluate("abrirDetalhes()"); p.wait_for_timeout(700)
        segura(p, p.locator('#detTexto .w').nth(5))
        r.t('No Ler Mais também: linha marcada + palavra com o segundo destaque', p.locator('#detTexto .w.pal').count() == 1 and p.evaluate("!!document.querySelector('#detTexto .lineHi.on')"))
        p.evaluate("fecharDet(); goHome(); openCfg();"); p.wait_for_timeout(300)
        p.click('#cfgPalavra'); p.wait_for_timeout(200); p.evaluate("closeCfg()")
        r.t('Desligar "Destacar palavra" nas Configurações fica guardado', ls(p, 'mundo_p1_palavra') == '0' and p.evaluate("palavraOn") is False)
        p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
        segura(p, p.locator('#text .w').nth(2))
        r.t('...e com ele desligado, segurar o dedo não dá o segundo destaque', p.locator('#text .w.pal').count() == 0)
        r.t('Sem erros de JavaScript', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())

        # ================= 5) correções da rodada 7 do conferente =================
        r = R('5) Correções da rodada 7: marca-texto com Sílabas, segurar sem o destaque por linha, tema Noite, nomes estrangeiros')
        ctx, _ = novo_contexto(b, largura=984, altura=432, storage=st_criancas([('p1', 'Hinata', '🦋')], extra={'mundo_p1_modoLinha': '1', 'mundo_p1_cfgAudio': '0', 'mundo_p1_margem': 'silabas'}))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        ruins = 0; testadas = 0
        for code in ('C17', 'C1', 'GALX'):
            abre_lermais(p, code, 0)
            n = p.evaluate("document.querySelectorAll('#detTexto .w').length")
            alt = p.evaluate("parseFloat(getComputedStyle(document.querySelector('#detTexto p')).lineHeight)")
            for k in range(0, n, 3):
                p.evaluate("k=>{ const w=document.querySelectorAll('#detTexto .w')[k]; w.click(); }", k)
                m = p.evaluate("(()=>{ const b=document.querySelector('#detTexto .lineHi.on'); const t=document.getElementById('detTexto'); return b?[b.offsetHeight,b.offsetWidth,t.scrollWidth,t.clientWidth]:null; })()")
                testadas += 1
                if not m or m[0] > alt * 1.5 or m[2] > m[3] + 1: ruins += 1
            p.evaluate("fecharDet()")
        r.t('Com "✂️ Sílabas" e destaque por linha, o marca-texto tem a altura de UMA linha e o Ler Mais não rola de lado (%d palavras tocadas)' % testadas, ruins == 0 and testadas > 60, ruins)
        abre_lermais(p, 'C17', 0)
        shy = p.evaluate(SHY)
        segura(p, p.locator('#detTexto .w').nth(7))
        m = p.evaluate("(()=>{ const b=document.querySelector('#detTexto .lineHi.on'); const t=document.getElementById('detTexto'); return b?[b.offsetHeight,t.scrollWidth,t.clientWidth]:null; })()")
        r.t('...e segurar o dedo (destaque duplo) também marca uma linha só', shy > 0 and m and m[0] < 80 and m[1] <= m[2] + 1, (shy, m))
        nomes = p.evaluate("comSilabasLM('ALBERT EINSTEIN E LOUIS PASTEUR, COM MARIE CURIE, ESTUDARAM CIÊNCIAS NATURALMENTE.')")
        r.t('Nomes de outras línguas não são cortados (EINSTEIN, PASTEUR, LOUIS, CURIE); o português continua com sílabas',
            all('\u00AD' not in x for x in ('EINSTEIN', 'PASTEUR', 'LOUIS', 'CURIE') if True) and
            all(w in nomes for w in ('EINSTEIN', 'PASTEUR', 'LOUIS', 'CURIE')) and '\u00AD' in nomes, nomes.replace('\u00AD', '-'))
        p.evaluate("fecharDet()")
        # tema Noite
        noite = p.evaluate("THEMES.findIndex(t=>t.name==='Noite')")
        p.evaluate("t=>{ themeIdx=t; applyTheme(); }", noite)
        i = p.evaluate("DATA.findIndex(x=>x.code==='C17')"); p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
        segura(p, p.locator('#text .w').nth(2))
        cs = p.evaluate("(()=>{ const w=document.querySelector('#text .w.pal'); if(!w) return null; const c=getComputedStyle(w); return [c.color, c.backgroundColor]; })()")
        r.t('Tema Noite: o segundo destaque aparece com bom contraste', cs and contraste(cs[0], cs[1]) >= 4.5, cs)
        r.t('Sem erros de JavaScript', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        # segurar o dedo SEM o destaque por linha (voz ligada): a palavra fala, sem segundo destaque
        ctx, _ = novo_contexto(b, largura=984, altura=432, storage=st_criancas([('p1', 'Hinata', '🦋')], extra={'mundo_p1_voz': '1', 'mundo_p1_cfgAudio': '1'}))
        p = abrir(ctx); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("(()=>{ window.__falou=[]; const fake={ speaking:false, pending:false, cancel(){}, getVoices(){return [];}, speak(u){ window.__falou.push(u.text); } }; Object.defineProperty(window,'speechSynthesis',{configurable:true, value:fake}); })()")
        p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
        for ms in (150, 600, 900):
            p.evaluate("window.__falou=[]")
            segura(p, p.locator('#text .w').nth(2), ms=ms)
            r.t('Sem o destaque por linha, segurar %d ms: a palavra FALA e não ganha o fundo escuro' % ms,
                p.locator('#text .w.pal').count() == 0 and len(p.evaluate("window.__falou")) >= 1, p.evaluate("window.__falou"))
        ctx.close()
        res.append(r.fim())

        # ================= 6) correções do revisor-chefe =================
        r = R('6) Revisor-chefe: segurar muito tempo, emoji do Cerrado, hífens escondidos, laticínios')
        ctx, _ = novo_contexto(b, largura=984, altura=432, storage=st_criancas([('p1', 'Hinata', '🦋')], extra={'mundo_p1_modoLinha': '1', 'mundo_p1_cfgAudio': '0'}))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
        for ms in (3500, 6000):
            p.locator('#text .w').last.click(); p.wait_for_timeout(1200)
            w2 = p.locator('#text .w').nth(2); segura(p, w2, ms=ms)
            r.t('Segurar %.1f s e soltar: a palavra CONTINUA com o segundo destaque' % (ms / 1000), p.locator('#text .w.pal').count() == 1 and 'pal' in (w2.get_attribute('class') or ''))
        # celular que NÃO manda o "clique" depois de segurar (o dedo sai por pointercancel): um toque de propósito
        # 1,2 s depois de soltar tem que valer (na v2.3 da rodada 8 a janela de 2,5 s contava do destaque e engolia esse toque)
        p.locator('#text .w').last.click(); p.wait_for_timeout(1200)
        p.evaluate("""(()=>{ const w=document.querySelectorAll('#text .w')[2]; const r=w.getBoundingClientRect();
            const o={bubbles:true, cancelable:true, clientX:r.x+r.width/2, clientY:r.y+r.height/2, pointerId:7, pointerType:'touch', isPrimary:true};
            w.dispatchEvent(new PointerEvent('pointerdown', o)); window.__w=w; window.__o=o; })()""")
        p.wait_for_timeout(700)
        marcou = p.locator('#text .w.pal').count() == 1
        p.evaluate("document.dispatchEvent(new PointerEvent('pointercancel', window.__o))"); p.wait_for_timeout(1200)
        p.locator('#text .w').nth(2).click(); p.wait_for_timeout(300)
        r.t('Sem o "clique" do soltar (pointercancel): um toque de propósito na mesma palavra, 1,2 s depois, tira o destaque (não é engolido)',
            marcou and p.locator('#text .w.pal').count() == 0, marcou)
        p.evaluate("abrirDetalhes()"); p.wait_for_timeout(700)
        segura(p, p.locator('#detTexto .w').nth(5), ms=3500)
        r.t('No Ler Mais: segurar 3,5 s também mantém o segundo destaque', p.locator('#detTexto .w.pal').count() == 1)
        p.evaluate("fecharDet()"); p.wait_for_timeout(300)
        dados = p.evaluate("""(()=>{ const c=k=>DATA.find(x=>x.code===k);
            return { e: c('F4').items[2].e, shy: JSON.stringify(DATA).split('\\u00AD').length-1,
                     hid: c('HID').items[16].d, al5: PAIS_DESC['AL5'] }; })()""")
        r.t('Nosso Cerrado #3 agora tem o emoji do mapa 🗺️ (a gota era da frase antiga)', dados['e'] == '🗺️', dados['e'])
        r.t('Nenhum hífen invisível escondido nas curiosidades (OREL-HAS, MIS-CIGENAÇÃO)', dados['shy'] == 0 and 'ORELHAS' in dados['hid'] and 'NUMA ARMAÇÃO' in dados['hid'], dados['shy'])
        r.t('Símbolo dos Laticínios: "a turma dos laticínios" (o leite não é derivado dele mesmo)', 'laticínios' in dados['al5'] and 'derivados' not in dados['al5'], dados['al5'])
        r.t('Sem erros de JavaScript', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())
        b.close()
    ok = sum(a for a, _ in res); tot = sum(t for _, t in res)
    print('\nV23: %d/%d' % (ok, tot))
    return ok == tot

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
