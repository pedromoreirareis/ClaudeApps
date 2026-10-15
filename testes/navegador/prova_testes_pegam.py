"""PROVA de que os testes novos pegam os problemas (parte 9-A, etapa 1, item 2).
Monta cópias do pacote v2.0 com UMA correção desfeita de cada vez (e usa a v1.8
publicada) e roda a conferência correspondente. Em cada linha, o esperado é:
  v2.0 de verdade → ✅   ·   versão sem a correção → ❌ (o teste pegou)."""
from base import *
from ef import *
import os, shutil, json, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
V20 = os.path.abspath(PASTA)
V18 = os.path.join(AQUI, '..', 'versao_anterior_v1.8')
BACKUP = os.path.join(AQUI, '..', 'dados', 'backup_pedro_2026-10-08.json')
TMP = tempfile.mkdtemp(prefix='mutantes_')

def mutante(nome, trocas):
    d = os.path.join(TMP, nome); shutil.copytree(V20, d)
    s = open(os.path.join(d, 'index.html'), encoding='utf-8').read()
    for a, b in trocas:
        assert s.count(a) == 1, (nome, a[:60]); s = s.replace(a, b)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(s)
    return d

def servir(ctx, pasta):
    def h(route):
        u = route.request.url.split('?')[0]; cam = u[len(URL):] or 'index.html'
        if cam == 'nuvem-config.js': return route.fallback()
        arq = os.path.join(pasta, cam)
        if not os.path.isfile(arq): return route.fulfill(status=404, body='')
        tipo = 'text/html' if arq.endswith('.html') else ('application/javascript' if arq.endswith('.js') else 'application/octet-stream')
        route.fulfill(status=200, content_type=tipo + '; charset=utf-8', body=open(arq, 'rb').read())
    ctx.route(URL + '**', h)

# ---- as conferências (cada uma devolve True quando o app está CERTO) ----
def leitor1_fantasma(b, pasta):
    """lista de crianças VAZIA + chave antiga mundo_lidas: abrir 2 vezes não pode criar 'Leitor 1'"""
    ctx, fb = novo_contexto(b, familia='familiateste', storage={'mundo_usuarios': json.dumps({'us': [], 'atual': None}), 'mundo_lidas': json.dumps({'AL1': '111'})})
    servir(ctx, pasta); p = abrir(ctx); p.reload(); p.wait_for_timeout(900)
    ok = json.loads(ls(p, 'mundo_usuarios'))['us'] == []
    ctx.close(); return ok

def sem_chaves_p0(b, pasta):
    """sem criança: abrir o app não grava nenhuma chave mundo_p0_*"""
    ctx, fb = novo_contexto(b, familia='familiateste', storage={'mundo_usuarios': json.dumps({'us': [], 'atual': None})})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(800)
    # v2.1: abrir já não grava o dia (novidade da v1.9); então a conferência também troca as cores
    # pelas Configurações sem criança escolhida (o saveState gravaria mundo_p0_theme etc.)
    try: p.evaluate("(()=>{ openCfg(); themeIdx=2; saveState(); closeCfg(); })()"); p.wait_for_timeout(300)
    except Exception: pass
    ok = not [k for k in chaves_brutas(p) if k.startswith('mundo_p0_')]
    ctx.close(); return ok

def mesclar_estragado(b, pasta):
    """dados estragados da nuvem não param a junção no meio (cores e dias seguidos ainda entram)"""
    ctx, fb = novo_contexto(b, familia='familiateste', storage={'mundo_usuarios': us_json([('p1', 'Hana', '🦊')]), 'mundo_p1_lidas': json.dumps({'AL1': '1'})})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(800)
    try:
        p.evaluate("nuvemMesclar('p1', {lidas:'{}', ultimasLidas:'{}', theme:'6', seqDias:'9'}, true)")
    except Exception:
        pass
    ok = ls(p, 'mundo_p1_theme') == '6' and ls(p, 'mundo_p1_seqDias') == '9'
    ctx.close(); return ok

def mesclar_crianca_fora(b, pasta):
    """juntar numa criança que não está no celular não grava nada"""
    ctx, fb = novo_contexto(b, familia='familiateste', storage={'mundo_usuarios': us_json([('p1', 'Hana', '🦊')])})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(800)
    p.evaluate("nuvemMesclar('p9', {lidas:'{\"AL1\":\"1\"}'}, false)")
    ok = not [k for k in chaves_brutas(p) if k.startswith('mundo_p9_')]
    ctx.close(); return ok

def backup_junta(b, pasta):
    """celular com a Hinata lendo MAIS que o backup real do Pedro: importar não pode perder nada (40 continua 40)"""
    st = storage_do_backup(BACKUP, 'familiateste')
    l = json.loads(st['mundo_p1790243541621_lidas']); assert 'BR' not in l; l['BR'] = '1111111'; st['mundo_p1790243541621_lidas'] = json.dumps(l)
    ctx, fb = novo_contexto(b, storage=st)
    servir(ctx, pasta)
    p = ctx.new_page(); p.on('dialog', lambda d: d.accept()); p.goto(URL); p.wait_for_timeout(1200)
    try: p.evaluate("EscolaFamilia.fecharTudo()")
    except Exception: pass
    with p.expect_file_chooser() as fc: p.evaluate("importarBackup()")
    fc.value.set_files(BACKUP); p.wait_for_timeout(600)
    if p.is_visible('#perguntaOv'): p.click('#perguntaSim')
    p.wait_for_timeout(2500); p.wait_for_load_state('load'); p.wait_for_timeout(800)
    n = conta_lidas(json.loads(ls(p, 'mundo_p1790243541621_lidas') or '{}'))
    ctx.close(); return n == 40

def sem_caixinha_ao_tirar(b, pasta):
    """tirar/apagar uma criança não usa caixinha do navegador (confirm)"""
    caixas = []
    ctx, fb = novo_contexto(b, familia='familiateste', storage={'mundo_usuarios': us_json([('p1', 'Hana', '🦊'), ('p2', 'Bia', '🐰')])})
    servir(ctx, pasta)
    p = ctx.new_page(); p.on('dialog', lambda d: (caixas.append(d.message), d.dismiss())); p.goto(URL); p.wait_for_timeout(1500)
    if p.evaluate("!!window.EscolaFamilia"):
        p.click('#efRaiz .ef-arrumar'); p.locator('#efRaiz .ef-crianca[data-id="p2"] .ef-tirar').click(); p.wait_for_timeout(400)
    else:
        p.evaluate("apagarUser()"); p.wait_for_timeout(400)
    ctx.close(); return not caixas

def barra_cabe(b, pasta):
    """568x320, leitura com a gaveta aberta: a ⚙️ fica inteira dentro da tela"""
    ctx, fb = novo_contexto(b, largura=568, altura=320, familia='pmrtestes', storage={'mundo_usuarios': us_json([('p1', 'Hinata', '🦋')]), 'mundo_p1_ajustes': '1',
                            'escola_familia': familia_json(['pmrtestes'], {'p1': 'pmrtestes'}, 'pmrtestes')})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(1200)
    try: p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1500)
    except Exception: pass
    p.evaluate("paisIdx=5; curIdx=0; openReader();"); p.wait_for_timeout(400)
    bb = p.locator('#gear').bounding_box()
    ctx.close(); return bb['x'] + bb['width'] <= 568.5

def preferencia_fica(b, pasta):
    """criança sem lida neste celular: ligar o 'destaque por linha' (v2.3: era 'sílabas') e a nuvem juntar dados de outro celular → continua ligado"""
    fb = FakeFirebase(); fb.gravar_app('haha_1f42f','Haha','🐯',{'modoLinha':'0'},familia='pmrtestes')
    ctx, _ = novo_contexto(b, fb=fb, largura=984, altura=432, storage={'mundo_usuarios': us_json([('p2','Haha','🐯')]), 'nuvem_familia':'pmrtestes',
                           'escola_familia': familia_json(['pmrtestes'], {'p2':'pmrtestes'}, 'pmrtestes')})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(3500)
    try: p.click('#efRaiz .ef-crianca[data-id="p2"]'); p.wait_for_timeout(1500)
    except Exception: pass
    p.evaluate("goHome(); openCfg();"); p.wait_for_timeout(300); p.click('#cfgLinha'); p.evaluate("closeCfg()")
    fb.gravar_app('haha_1f42f','Haha','🐯',{'modoLinha':'0'},familia='pmrtestes')
    p.evaluate("(()=>{ NuvemSync.sincronizar(); })()"); p.wait_for_timeout(3000)
    ok = p.evaluate("modoLinha") == True
    ctx.close(); return ok

# ---- v2.1 (as novidades da v1.9 em cima do novo cadastro) ----
V20B_INDEX = os.path.join(AQUI, '..', '..', 'trabalho', 'base_v2.0b', 'index.html')
def pasta_v20b():
    """o pacote atual com o index.html da v2.0b (a versão anterior à v2.1)"""
    d = os.path.join(TMP, 'v2.0b')
    if not os.path.isdir(d):
        shutil.copytree(V20, d); shutil.copy(V20B_INDEX, os.path.join(d, 'index.html'))
    return d

def _hinata(b, pasta):
    ctx, fb = novo_contexto(b, largura=900, altura=420, storage={'mundo_usuarios': us_json([('p1','Hinata','🦋')]), 'nuvem_familia':'pmrtestes',
                           'escola_familia': familia_json(['pmrtestes'], {'p1':'pmrtestes'}, 'pmrtestes')})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(1500)
    try: p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1200)
    except Exception: pass
    return ctx, p

def seta_com_t4(b, pasta):
    """com "Quem vai estudar hoje?" aberta por cima da leitura, a seta → não mexe na leitura"""
    ctx, p = _hinata(b, pasta)
    p.evaluate("(()=>{ paisIdx=3; curIdx=2; openReader(); EscolaFamilia.abrir('quem'); })()"); p.wait_for_timeout(400)
    p.keyboard.press('ArrowRight'); p.wait_for_timeout(200)
    ok = p.evaluate("curIdx") == 2
    ctx.close(); return ok

def ler_ao_tocar_lembrado(b, pasta):
    """desligar "ler ao tocar", fechar e abrir o app → continua desligado"""
    ctx, p = _hinata(b, pasta)
    p.evaluate("(()=>{ paisIdx=3; curIdx=0; openReader(); toggleSayTap(); })()"); p.wait_for_timeout(200)
    p.reload(); p.wait_for_timeout(1500)
    try: p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1200)
    except Exception: pass
    ok = p.evaluate("sayTapOn") is False
    ctx.close(); return ok

def dia_so_com_leitura(b, pasta):
    """abrir o app e entrar na criança NÃO conta o dia; só marcar LIDA conta"""
    ctx, p = _hinata(b, pasta)
    ok = ls(p, 'mundo_p1_ultimoDia') is None
    ctx.close(); return ok

def entrar_traz_nuvem(b, pasta):
    """dois celulares: escolher a Bia no B (aberto na Hinata) traz as 2 leituras do A"""
    import teste_v21
    def sv(ctx): servir(ctx, pasta)
    return teste_v21.dois_celulares(b, servir_em=sv)

def antigas_iguais(b, pasta):
    """v2.2/v2.3: cada curiosidade que já existia continua igual e no mesmo lugar (dados comparados com a v2.1;
    só as 3 correções autorizadas da v2.3 — Júpiter #11, Netuno #8 e Nosso Cerrado #3 — podem ter outro texto;
    Brasil Colônia #5 e Idade Média #17 só podem ter perdido o hífen invisível)"""
    def D(arq):
        s = open(arq, encoding='utf-8').read(); i = s.index('const DATA='); j = s.index('[', i); k = s.index('\n', j)
        return json.loads(s[j:k].rstrip().rstrip(';'))
    d0 = D(os.path.join(AQUI, '..', '..', 'trabalho', 'base_v2.1', 'index.html')); d1 = D(os.path.join(pasta, 'index.html'))
    CORRIGIDAS = {('JUP', 10), ('NET', 7), ('F4', 2)}
    # revisor-chefe da v2.3: Brasil Colônia #5 e Idade Média #17 só perderam o hífen invisível (e "NUMA ARMAÇÃO")
    SO_HIFEN = {('HBR', 4), ('HID', 16)}
    def limpo(x): return dict(x, d=x['d'].replace('\u00ad', '').replace('NUM ARMAÇÃO', 'NUMA ARMAÇÃO'))
    return all(len(d1[i]['items']) >= len(c['items']) and
               all((limpo(d1[i]['items'][n]) == limpo(x)) if (c['code'], n) in SO_HIFEN else d1[i]['items'][n] == x
                   for n, x in enumerate(c['items']) if (c['code'], n) not in CORRIGIDAS)
               for i, c in enumerate(d0))

def destaque_duplo(b, pasta):
    """v2.3: com o destaque por linha, segurar o dedo numa palavra dá a ela o segundo destaque"""
    ctx, fb = novo_contexto(b, largura=984, altura=432, storage={'mundo_usuarios': us_json([('p1','Hinata','🦋')]), 'nuvem_familia':'pmrtestes',
                           'escola_familia': familia_json(['pmrtestes'], {'p1':'pmrtestes'}, 'pmrtestes'), 'mundo_p1_modoLinha':'1', 'mundo_p1_cfgAudio':'0'})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(1500)
    try: p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1200)
    except Exception: pass
    p.evaluate("(()=>{ paisIdx=0; curIdx=0; openReader(); })()"); p.wait_for_timeout(400)
    bb = p.locator('#text .w').nth(1).bounding_box()
    p.mouse.move(bb['x']+bb['width']/2, bb['y']+bb['height']/2); p.mouse.down(); p.wait_for_timeout(700); p.mouse.up(); p.wait_for_timeout(300)
    ok = p.locator('#text .w.pal').count() == 1
    ctx.close(); return ok

def silabas_lermais(b, pasta):
    """v2.3: com "✂️ Sílabas", o Ler Mais ganha os pontos de corte e a margem é ajustada"""
    ctx, fb = novo_contexto(b, largura=984, altura=432, storage={'mundo_usuarios': us_json([('p1','Hinata','🦋')]), 'nuvem_familia':'pmrtestes',
                           'escola_familia': familia_json(['pmrtestes'], {'p1':'pmrtestes'}, 'pmrtestes'), 'mundo_p1_margem':'silabas'})
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(1500)
    try: p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1200)
    except Exception: pass
    i = p.evaluate("DATA.findIndex(x=>x.code==='C2')")
    p.evaluate("i=>{ paisIdx=i; curIdx=0; openReader(); abrirDetalhes(); }", i); p.wait_for_timeout(800)
    ok = p.evaluate("document.getElementById('detTexto').textContent.indexOf('\u00AD')>=0") and p.locator('#detTexto .wsp.aj').count() > 0
    ctx.close(); return ok

V23_ANTES = os.path.join(AQUI, '..', '..', 'trabalho', 'v23_rodada7_antes', 'index.html')
def pasta_v23_antes():
    """o pacote atual com o index.html da v2.3 ANTES das correções da rodada 7 do conferente"""
    d = os.path.join(TMP, 'v23antes')
    if not os.path.isdir(d):
        shutil.copytree(V20, d); shutil.copy(V23_ANTES, os.path.join(d, 'index.html'))
    return d

def _hin(b, pasta, extra):
    st = {'mundo_usuarios': us_json([('p1','Hinata','🦋')]), 'nuvem_familia':'pmrtestes',
          'escola_familia': familia_json(['pmrtestes'], {'p1':'pmrtestes'}, 'pmrtestes')}
    st.update(extra)
    ctx, fb = novo_contexto(b, largura=984, altura=432, storage=st)
    servir(ctx, pasta); p = abrir(ctx); p.wait_for_timeout(1500)
    try: p.click('#efRaiz .ef-crianca[data-id="p1"]'); p.wait_for_timeout(1200)
    except Exception: pass
    return ctx, p

def linha_com_silabas(b, pasta):
    """v2.3 (rodada 7): com "✂️ Sílabas" e destaque por linha, o marca-texto tem a altura de UMA linha e o Ler Mais não rola de lado"""
    ctx, p = _hin(b, pasta, {'mundo_p1_modoLinha':'1', 'mundo_p1_cfgAudio':'0', 'mundo_p1_margem':'silabas'})
    i = p.evaluate("DATA.findIndex(x=>x.code==='C17')")
    p.evaluate("i=>{ paisIdx=i; curIdx=0; openReader(); abrirDetalhes(); }", i); p.wait_for_timeout(800)
    alt = p.evaluate("parseFloat(getComputedStyle(document.querySelector('#detTexto p')).lineHeight)")
    n = p.evaluate("document.querySelectorAll('#detTexto .w').length"); ok = True
    for k in range(n):
        p.evaluate("k=>document.querySelectorAll('#detTexto .w')[k].click()", k)
        m = p.evaluate("(()=>{ const b=document.querySelector('#detTexto .lineHi.on'); const t=document.getElementById('detTexto'); return b?[b.offsetHeight,t.scrollWidth,t.clientWidth]:null; })()")
        if not m or m[0] > alt * 1.5 or m[1] > m[2] + 1: ok = False; break
    ctx.close(); return ok

def segurar_sem_linha_fala(b, pasta):
    """v2.3 (rodada 7): sem o destaque por linha (voz ligada), segurar o dedo 600 ms numa palavra: ela fala e não fica escura"""
    ctx, p = _hin(b, pasta, {'mundo_p1_voz':'1', 'mundo_p1_cfgAudio':'1'})
    p.evaluate("(()=>{ window.__falou=[]; const fake={ speaking:false, pending:false, cancel(){}, getVoices(){return [];}, speak(u){ window.__falou.push(u.text); } }; Object.defineProperty(window,'speechSynthesis',{configurable:true, value:fake}); })()")
    i = p.evaluate("DATA.findIndex(x=>x.code==='C17')")
    p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
    bb = p.locator('#text .w').nth(2).bounding_box()
    p.mouse.move(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 2); p.mouse.down(); p.wait_for_timeout(600); p.mouse.up(); p.wait_for_timeout(300)
    ok = p.locator('#text .w.pal').count() == 0 and len(p.evaluate("window.__falou")) >= 1
    ctx.close(); return ok

V23_R8 = os.path.join(AQUI, '..', '..', 'trabalho', 'v23_rodada8_antes', 'index.html')
def pasta_v23_r8():
    """o pacote atual com o index.html da v2.3 aprovado na rodada 8, ANTES das correções do revisor-chefe"""
    d = os.path.join(TMP, 'v23r8')
    if not os.path.isdir(d):
        shutil.copytree(V20, d); shutil.copy(V23_R8, os.path.join(d, 'index.html'))
    return d

def segurar_muito(b, pasta):
    """v2.3 (revisor-chefe): com o destaque por linha, segurar a palavra 3,5 s e soltar: o segundo destaque continua"""
    ctx, p = _hin(b, pasta, {'mundo_p1_modoLinha':'1', 'mundo_p1_cfgAudio':'0'})
    i = p.evaluate("DATA.findIndex(x=>x.code==='C17')")
    p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
    bb = p.locator('#text .w').nth(2).bounding_box()
    p.mouse.move(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 2); p.mouse.down(); p.wait_for_timeout(3500); p.mouse.up(); p.wait_for_timeout(300)
    ok = p.locator('#text .w.pal').count() == 1
    ctx.close(); return ok

def toque_depois_do_cancel(b, pasta):
    """v2.3 (revisor-chefe): sem o clique do soltar (pointercancel), um toque de propósito 1,2 s depois vale"""
    ctx, p = _hin(b, pasta, {'mundo_p1_modoLinha':'1', 'mundo_p1_cfgAudio':'0'})
    i = p.evaluate("DATA.findIndex(x=>x.code==='C17')")
    p.evaluate("i=>{ paisIdx=i; curIdx=1; openReader(); }", i); p.wait_for_timeout(400)
    p.evaluate("""(()=>{ const w=document.querySelectorAll('#text .w')[2]; const r=w.getBoundingClientRect();
        const o={bubbles:true, cancelable:true, clientX:r.x+r.width/2, clientY:r.y+r.height/2, pointerId:7, pointerType:'touch', isPrimary:true};
        w.dispatchEvent(new PointerEvent('pointerdown', o)); window.__o=o; })()""")
    p.wait_for_timeout(700); marcou = p.locator('#text .w.pal').count() == 1
    p.evaluate("document.dispatchEvent(new PointerEvent('pointercancel', window.__o))"); p.wait_for_timeout(1200)
    p.locator('#text .w').nth(2).click(); p.wait_for_timeout(300)
    ok = marcou and p.locator('#text .w.pal').count() == 0
    ctx.close(); return ok

PROVAS = [
    ('"Leitor 1" fantasma com a lista vazia', leitor1_fantasma,
     [('if(!d.us.length){ U={us:[],atual:null}; return; }', '')]),
    ('sem criança, nenhuma chave mundo_p0_*', sem_chaves_p0,
     [('''function instalarTravaSemCrianca(){''', '''function instalarTravaSemCrianca(){ return;''')]),
    ('juntar numa criança que saiu não grava', mesclar_crianca_fora,
     [("  if(!U.us.some(u=>u.id===id)) return;\n  if(!dn || typeof dn!=='object') dn={};", "  if(!dn || typeof dn!=='object') dn={};")]),
    ('barra da leitura cabe com o chip (568x320, gaveta aberta)', barra_cabe,
     [("    if(aperto()) b.classList.add('efBarraApertada');\n", "")]),
    ('v2.3: destaque duplo (segurar o dedo numa palavra)', destaque_duplo,
     [("    if(!w || !palavraOn || !linhaAtiva()) return;", "    return;")]),
    ('v2.3: Ler Mais com sílabas no fim da linha e margem ajustada', silabas_lermais,
     [("  if(modoMargem!=='silabas') return t;\n  return hifenizarTexto(t)", "  return t;\n  return hifenizarTexto(t)")]),
    ('v2.2: as curiosidades antigas continuam iguais e no mesmo lugar', antigas_iguais,
     [('MARIE CURIE NASCEU NA POLÔNIA EM 1867 E FOI ESTUDAR CIÊNCIAS NA FRANÇA.', 'MARIE CURIE NASCEU NA POLÔNIA E FOI ESTUDAR NA FRANÇA.')]),
    ('v2.1: escolher a criança traz o progresso do outro celular', entrar_traz_nuvem,
     [('''    if(id!==antes || !(opc && opc.naAbertura===false)){''', '''    if(false){''')]),
    ('v2.1: seta não mexe na leitura com a tela do cadastro por cima', seta_com_t4,
     [('''    if(!leitorAberto()) return;
    if(document.querySelector('.ov.open') || document.querySelector('#efRaiz.ef-ativo')) return;''', '''    if(!leitorAberto()) return;
    if(document.querySelector('.ov.open')) return;''')]),
]

def main():
    servidor()
    linhas = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for nome, fn, trocas in PROVAS:
            certo = fn(b, V20)
            errado = fn(b, mutante(nome[:12].replace(' ', '_').replace('"', ''), trocas))
            linhas.append((nome, certo, errado, 'v2.0 sem esta correção'))
        # contra a v1.8 publicada
        for nome, fn in (('importar backup JUNTA (backup real do Pedro, 40 lidas no celular)', backup_junta),
                         ('juntar com dados estragados da nuvem não para no meio', mesclar_estragado),
                         ('preferência mudada neste celular não volta sozinha (achado do Pedro)', preferencia_fica),
                         ('tirar/apagar criança sem caixinha do navegador', sem_caixinha_ao_tirar)):
            linhas.append((nome, fn(b, V20), fn(b, V18), 'v1.8 publicada'))
        # v2.1: contra a v2.0b (a versão anterior, sem as novidades da v1.9)
        for nome, fn in (('v2.1: "ler ao tocar" fica lembrado ao reabrir', ler_ao_tocar_lembrado),
                         ('v2.1: abrir o app não conta o dia (só ler conta)', dia_so_com_leitura)):
            linhas.append((nome, fn(b, V20), fn(b, pasta_v20b()), 'v2.0b'))
        # v2.3: contra a v2.3 ANTES das correções da rodada 7 do conferente
        for nome, fn in (('v2.3: marca-texto de uma linha só com "✂️ Sílabas" (rodada 7)', linha_com_silabas),
                         ('v2.3: segurar o dedo sem o destaque por linha: a palavra fala (rodada 7)', segurar_sem_linha_fala)):
            linhas.append((nome, fn(b, V20), fn(b, pasta_v23_antes()), 'v2.3 antes da rodada 7'))
        # v2.3: contra a v2.3 aprovada na rodada 8, antes das correções do revisor-chefe
        linhas.append(('v2.3: segurar 3,5 s mantém o segundo destaque (revisor-chefe)', segurar_muito(b, V20), segurar_muito(b, pasta_v23_r8()), 'v2.3 rodada 8'))
        linhas.append(('v2.3: sem o clique do soltar, toque de propósito 1,2 s depois vale (revisor)', toque_depois_do_cancel(b, V20), toque_depois_do_cancel(b, pasta_v23_r8()), 'v2.3 rodada 8'))
        b.close()
    tudo = True
    print('\n%-70s %-8s %-8s %s' % ('conferência', 'atual', 'anterior', 'versão anterior'))
    for nome, certo, errado, qual in linhas:
        pegou = certo and not errado
        tudo = tudo and pegou
        print('%-70s %-8s %-8s %s  → %s' % (nome, '✅' if certo else '❌', '✅' if errado else '❌', qual, 'O TESTE PEGA' if pegou else 'NÃO PROVA'))
    shutil.rmtree(TMP, ignore_errors=True)
    print('\nPROVA: %d/%d conferências pegam o problema' % (sum(1 for l in linhas if l[1] and not l[2]), len(linhas)))
    sys.exit(0 if tudo else 1)

if __name__ == '__main__':
    main()
