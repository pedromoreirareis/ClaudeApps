"""🌍 Curiosidades v2.2 — curiosidades novas (17 cartões + extras de Marie Curie e Leonardo).

1) Dados (sem navegador): cada cartão antigo continua IGUAL item por item (as novas só no fim de C2/C7),
   os 17 cartões novos estão no fim, todo emoji tem descrição, todo cartão novo tem a frase do símbolo.
2) No navegador, com o retrato do celular do Pedro (backup real: 🦋 Hinata, 33 lidas, inclusive em C2 e C7):
   as lidas continuam 33 e no mesmo lugar; as seções mostram os cartões novos no fim; abrir um cartão
   novo, tocar no símbolo e no emoji, "Ler Mais", marcar LIDA; as extras de C2 aparecem depois das antigas;
   a busca acha os cartões novos; marcos até o total novo.
Chromium + Firebase de mentira (nunca o Firebase real)."""
from base import *
from ef import *
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE21 = os.path.join(AQUI, '..', '..', 'trabalho', 'base_v2.1', 'index.html')
FINAL = os.path.join(AQUI, '..', '..', 'trabalho', 'v22', 'CARTOES_V22_FINAL.json')
BACKUP = os.path.join(AQUI, '..', 'dados', 'backup_pedro_2026-10-08.json')
HIN = 'p1790243541621'
NOVOS = ['C12', 'C13', 'C14', 'C17', 'C15', 'C16', 'C18', 'C19', 'C20', 'C21', 'MET', 'PLAN', 'EST', 'GALX', 'BN', 'TEL', 'SON']

def obj(s, nome, abre):
    i = s.index('const %s=' % nome); j = s.index(abre, i); k = s.index('\n', j)
    return json.loads(s[j:k].rstrip().rstrip(';'))

def main():
    res = []
    # ================= 1) dados =================
    r = R('1) Dados: o que existia continua igual; o novo entra só no fim')
    # v2.3: a parte 1 confere a ENTREGA da v2.2 (trabalho/base_v2.2), que já é história; o pacote atual (v2.3)
    # mudou de propósito 3 curiosidades e o código — isso é conferido no teste_v23.py
    s0 = open(BASE21, encoding='utf-8').read(); s1 = open(os.path.join(AQUI, '..', '..', 'trabalho', 'base_v2.2', 'index.html'), encoding='utf-8').read()
    D0, D1 = obj(s0, 'DATA', '['), obj(s1, 'DATA', '[')
    E1, P0, P1 = obj(s1, 'EMOJI_DESC', '{'), obj(s0, 'PAIS_DESC', '{'), obj(s1, 'PAIS_DESC', '{')
    fin = json.load(open(FINAL, encoding='utf-8'))
    r.t('Os 278 cartões antigos continuam na mesma ordem, com o mesmo código, nome, símbolo e seção',
        [(c['code'], c['name'], c['flag'], c['sec']) for c in D0] == [(c['code'], c['name'], c['flag'], c['sec']) for c in D1[:278]])
    r.t('Cada curiosidade antiga continua igual e no mesmo lugar (as lidas são guardadas por posição)',
        all(D1[i]['items'][:len(c['items'])] == c['items'] for i, c in enumerate(D0)))
    cresceram = {c['code']: len(D1[i]['items']) - len(c['items']) for i, c in enumerate(D0) if len(D1[i]['items']) != len(c['items'])}
    r.t('Só Marie Curie (C2) e Leonardo (C7) ganharam curiosidades, 5 cada, no fim', cresceram == {'C2': 5, 'C7': 5}, cresceram)
    r.t('Os 17 cartões novos estão no fim, na ordem combinada', [c['code'] for c in D1[278:]] == NOVOS, [c['code'] for c in D1[278:]])
    r.t('Hipátia tem 15 curiosidades e Mulheres Na Ciência 15; os outros cartões novos, 12',
        {c['code']: len(c['items']) for c in D1[278:]} == {k: (15 if k in ('C17', 'C18') else 12) for k in NOVOS})
    tot = sum(len(c['items']) for c in D1)
    r.t('Total: 4.034 + 220 = 4.254 curiosidades em 295 cartões', tot == 4254 and len(D1) == 295, (tot, len(D1)))
    r.t('Os cartões novos são exatamente os conferidos (CARTOES_V22_FINAL.json)', [{k: c[k] for k in ('code', 'name', 'flag', 'sec', 'items')} for c in fin['cartoes']] == D1[278:])
    r.t('Todo emoji usado tem descrição (o toque no emoji nunca fica sem explicação)', not ({it['e'] for c in D1 for it in c['items']} - set(E1)))
    r.t('Todo cartão novo tem a frase do símbolo grande (e as antigas não mudaram)', all(k in P1 for k in NOVOS) and all(P1[k] == v for k, v in P0.items()))
    novos_itens = [it for c in D1[278:] for it in c['items']] + D1[[c['code'] for c in D1].index('C2')]['items'][15:] + D1[[c['code'] for c in D1].index('C7')]['items'][15:]
    r.t('Tudo em CAIXA ALTA e com 3 parágrafos no "Ler Mais"',
        all(it['c'] == it['c'].upper() and it['d'] == it['d'].upper() and it['d'].count('\n\n') == 2 for it in novos_itens))
    temas_antigos = {it['t'] for c in D0 for it in c['items']}
    r.t('Todo tema (t) das curiosidades novas já é usado no app', all(it['t'] in temas_antigos for it in novos_itens))
    antigas = [it['c'] for c in D0 for it in c['items']]
    r.t('Nenhuma frase curta nova repete outra (do app ou nova)', len({it['c'] for it in novos_itens}) == len(novos_itens) and not ({it['c'] for it in novos_itens} & set(antigas)))
    linhas0, linhas1 = s0.split('\n'), s1.split('\n')
    dif = [i for i, (a, b) in enumerate(zip(linhas0, linhas1)) if a != b]
    r.t('Fora as linhas de dados (DATA, PAIS_DESC, EMOJI_DESC), o código do app é idêntico ao da v2.1',
        len(linhas0) == len(linhas1) and all(linhas0[i].startswith(('const DATA=', 'const PAIS_DESC=', 'const EMOJI_DESC=')) for i in dif), dif)
    res.append(r.fim())

    # ================= 2) no navegador, com o celular do Pedro =================
    servidor()
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        r = R('2) No app, com o retrato do celular do Pedro (Hinata, 33 lidas)')
        st = storage_do_backup(BACKUP, 'pmrtestes')
        st['escola_familia'] = familia_json(['pmrtestes'], {HIN: 'pmrtestes'}, 'pmrtestes')
        antes = {k: v for k, v in st.items() if k.startswith('mundo_%s_' % HIN)}
        ctx, fb = novo_contexto(b, largura=984, altura=432, storage=st)
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1800)
        txt = p.text_content('.ef-t4 .ef-crianca[data-id="%s"]' % HIN) or ''
        r.t('"Quem vai estudar hoje?" mostra a Hinata com 33 de 4254', '33 de 4254' in txt, txt)
        escolher(p, HIN)
        r.t('Depois de entrar, as lidas da Hinata são as mesmas, no mesmo lugar (inclusive C2 e C7)', ls(p, 'mundo_%s_lidas' % HIN) == antes['mundo_%s_lidas' % HIN])
        r.t('...e são 33', conta_lidas(lidas(p, HIN)) == 33)
        p.evaluate("abrirSecao('🔬 Cientistas E Inventores')"); p.wait_for_timeout(300)
        nomes = p.evaluate("[...document.querySelectorAll('#homeGrid .pais .nm')].map(x=>x.textContent)")
        r.t('Seção Cientistas: os 10 cartões novos aparecem depois dos 11 antigos', nomes[:11] == [c['name'] for c in D0 if c['sec'] == '🔬 Cientistas E Inventores'] and
            nomes[11:] == ['Sócrates', 'Platão', 'Aristóteles', 'Hipátia De Alexandria', 'Galileu Galilei', 'Louis Pasteur', 'Mulheres Na Ciência', 'Químicos Famosos', 'Físicos Famosos', 'Astrônomos'], nomes)
        p.evaluate("abrirSecao('🚀 Espaço')"); p.wait_for_timeout(300)
        nomes = p.evaluate("[...document.querySelectorAll('#homeGrid .pais .nm')].map(x=>x.textContent)")
        r.t('Seção Espaço: os 7 cartões novos aparecem depois dos 14 antigos', nomes[14:] == ['Meteoros E Meteoritos', 'Planetas Anões', 'Estrelas', 'Galáxias', 'Buracos Negros', 'Telescópios', 'Sondas Espaciais'], nomes)
        # abrir Hipátia
        p.evaluate("abrirSecao('🔬 Cientistas E Inventores')"); p.wait_for_timeout(300)
        p.locator('#homeGrid .pais:has-text("Hipátia")').first.click(); p.wait_for_timeout(500)
        r.t('Tocar em "Hipátia De Alexandria" abre a 1ª curiosidade dela', p.evaluate("leitorAberto() && DATA[paisIdx].code==='C17' && curIdx===0"))
        p.click('#flag'); p.wait_for_timeout(300)
        info = (p.text_content('#infoTitle') or '') + ' | ' + (p.text_content('#infoText') or p.text_content('#infoOv') or '')
        r.t('Tocar no símbolo grande mostra quem foi Hipátia (e não "é um país do mundo")', 'HIPÁTIA' in info.upper() and 'PAÍS DO MUNDO' not in info.upper(), info[:200])
        p.evaluate("closeInfo()"); p.wait_for_timeout(150)
        p.click('#emoji'); p.wait_for_timeout(300)
        r.t('Tocar no emoji mostra a explicação dele', p.evaluate("document.getElementById('infoOv').classList.contains('open')") and len(p.text_content('#infoTitle') or '') > 2)
        p.evaluate("closeInfo()"); p.wait_for_timeout(150)
        p.evaluate("abrirDetalhes()"); p.wait_for_timeout(400)
        det = p.evaluate("(document.getElementById('detOv')||{}).textContent||''")
        r.t('"Ler Mais" abre o texto longo da curiosidade', p.evaluate("document.getElementById('detOv').classList.contains('open')") and len(det) > 200)
        p.evaluate("fecharDet()"); p.wait_for_timeout(150)
        p.evaluate("toggleLida()"); p.wait_for_timeout(300)
        r.t('Marcar LIDA num cartão novo grava e soma (34)', lidas(p, HIN).get('C17', '')[:1] == '1' and conta_lidas(lidas(p, HIN)) == 34)
        # extras de Marie Curie
        c2 = p.evaluate("DATA.findIndex(c=>c.code==='C2')")
        p.evaluate("i=>{ paisIdx=i; curIdx=15; openReader(); }", c2); p.wait_for_timeout(300)
        r.t('Marie Curie: a 16ª curiosidade é a primeira nova (Manya), depois das 15 antigas', 'MANYA' in (p.text_content('#text') or '').upper() and p.evaluate("DATA[paisIdx].items.length") == 20)
        lc2 = lidas(p, HIN).get('C2', '')
        p.evaluate("toggleLida()"); p.wait_for_timeout(300)
        lc2b = lidas(p, HIN).get('C2', '')
        r.t('Marcar a 16ª de Marie Curie não mexe nas lidas antigas dela', lc2b[:15] == (lc2 + '0' * 15)[:15] and lc2b[15:16] == '1', (lc2, lc2b))
        n = p.evaluate("procuraCuriosidades('hipatia').totalReal")
        r.t('A busca acha Hipátia (sem acento também)', n >= 15, n)
        r.t('Marcos e medalhas vão até o novo total (4254)', p.evaluate("TOTAL_CUR===4254 && MARCOS[MARCOS.length-1]===4254"))
        r.t('Nenhum erro de JavaScript', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())
        b.close()
    ok = sum(a for a, _ in res); tot_ = sum(t for _, t in res)
    print('\nV22: %d/%d' % (ok, tot_))
    return ok == tot_

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
