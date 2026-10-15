"""🌍 Curiosidades v2.1 — as novidades da v1.9 levadas para cima do novo cadastro (v2.0b).

Adaptado do trabalho/v1.9-pendente/testes/teste_v19_novidades.py (que usava as telas antigas),
mais as conferências próprias da v2.1 (setas/Esc/arrastar com as telas do cadastro por cima,
"ler ao tocar" na nuvem e no backup, karaokê com os avisos da voz).
Chromium + Firebase de mentira (nunca o Firebase real)."""
from base import *
from ef import *
import json, datetime, tempfile, os

def st_criancas(lista, fam='pmrtestes', atual=None, extra=None):
    st = {'mundo_usuarios': us_json(lista, atual), 'escola_familia': familia_json([fam], {i: fam for i,_,_ in lista}, fam), 'nuvem_familia': fam}
    if extra: st.update(extra)
    return st

def dia(d):  # mesmo formato do app: AAAA-M-D sem zero à esquerda
    return '%d-%d-%d' % (d.year, d.month, d.day)

def cfg_aberta(p):
    return p.evaluate("document.getElementById('cfgOv').classList.contains('open')")

def dois_celulares(b, servir_em=None):
    """celular B aberto na Hinata; no celular A, a Bia lê 2; no B, escolher a Bia → chegam as 2 (sem recarregar)"""
    fb = FakeFirebase()
    st = st_criancas([('p1','Hinata','🦋'),('p2','Bia','🐰')])
    ctxB, _ = novo_contexto(b, fb=fb, largura=900, altura=420, storage=st)
    if servir_em: servir_em(ctxB)
    pB = abrir(ctxB); pB.wait_for_timeout(1500); escolher(pB, 'p1'); pB.wait_for_timeout(3500)
    ctxA, _ = novo_contexto(b, fb=fb, largura=900, altura=420, storage=st)
    if servir_em: servir_em(ctxA)
    pA = abrir(ctxA); pA.wait_for_timeout(1500); escolher(pA, 'p2')
    marcar_lida(pA, 0, 0); marcar_lida(pA, 0, 1)
    okA = esperar_ok(pA); ctxA.close()
    pB.evaluate("EscolaFamilia.abrir('quem')"); pB.wait_for_timeout(400); escolher(pB, 'p2', ms=300)
    n = 0
    for _ in range(16):
        n = conta_lidas(lidas(pB, 'p2'))
        if n >= 2: break
        pB.wait_for_timeout(250)
    ctxB.close()
    return okA and n >= 2

def main():
    servidor()
    res = []
    hoje = datetime.date.today()
    with sync_playwright() as pw:
        b = pw.chromium.launch()

        # ================= 1) Continuar de onde parei + setas + Esc =================
        r = R('1) ▶️ Continuar de onde parei, setas ← → e Esc (com as telas do cadastro)')
        ctx, fb = novo_contexto(b, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("voltarMenu()"); p.wait_for_timeout(200)
        r.t('Criança sem leitura ainda: sem o botão "Continuar"', p.locator('.pais.continuar').count() == 0)
        p.evaluate("(()=>{ favMode=false; diaMode=false; paisIdx=3; curIdx=2; saveState(); openReader(); })()"); p.wait_for_timeout(200)
        p.evaluate("goHome(); voltarMenu();"); p.wait_for_timeout(300)
        txt = p.text_content('.pais.continuar') if p.locator('.pais.continuar').count() else ''
        nome3 = p.evaluate('DATA[3].name'); tot3 = p.evaluate('DATA[3].items.length')
        r.t('O botão mostra o cartão e "3 de N"', 'Continuar de onde parei' in txt and nome3 in txt and ('3 de %d' % tot3) in txt, txt)
        bb = p.locator('.pais.continuar').bounding_box()
        r.t('O botão aparece na tela inicial com a barra de cima no lugar (chip e ⚙️ visíveis)', bb and bb['height'] >= 40 and p.is_visible('#efChipHome') and p.is_visible('#cfgGearHome'), bb)
        p.evaluate("(()=>{ paisIdx=0; curIdx=0; })()")
        p.click('.pais.continuar'); p.wait_for_timeout(300)
        r.t('Tocar nele abre a mesma curiosidade', p.evaluate('paisIdx===3 && curIdx===2 && leitorAberto()'))
        p.keyboard.press('ArrowRight'); p.wait_for_timeout(150)
        r.t('Seta → passa para a próxima', p.evaluate('curIdx') == 3)
        p.keyboard.press('ArrowLeft'); p.wait_for_timeout(150)
        r.t('Seta ← volta', p.evaluate('curIdx') == 2)
        p.evaluate("EscolaFamilia.abrir('quem')"); p.wait_for_timeout(400)
        p.keyboard.press('ArrowRight'); p.wait_for_timeout(150)
        r.t('Com "Quem vai estudar hoje?" aberta por cima, a seta NÃO mexe na leitura de baixo', p.evaluate('curIdx') == 2 and aberta(p, 'ef-t4'))
        fechar_tudo(p); p.wait_for_timeout(300)
        p.evaluate("openCfg()"); p.wait_for_timeout(200)
        p.keyboard.press('Escape'); p.wait_for_timeout(200)
        r.t('Esc fecha as Configurações', not cfg_aberta(p))
        p.evaluate("openCfg()"); p.wait_for_timeout(200)
        p.evaluate("(()=>{ window.__resp='?'; perguntaApp({titulo:'Teste', texto:'Teste', sim:'Sim', nao:'Não'}).then(v=>{window.__resp=v;}); })()"); p.wait_for_timeout(300)
        p.keyboard.press('Escape'); p.wait_for_timeout(200)
        r.t('Com uma pergunta do app aberta, o Esc não fecha as Configurações por baixo dela',
            cfg_aberta(p) and p.evaluate("document.getElementById('perguntaOv').classList.contains('open')"))
        fechar_tudo(p)
        r.t('Nenhuma caixinha do navegador e nenhum erro de JavaScript', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())

        # ================= 2) Arrastar o dedo =================
        r = R('2) 👉 Arrastar o dedo para passar de curiosidade')
        ctx, fb = novo_contexto(b, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        p = abrir(ctx); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("(()=>{ favMode=false; diaMode=false; paisIdx=3; curIdx=2; openReader(); })()"); p.wait_for_timeout(300)
        ARRASTA = """([x0,x1,ms])=>new Promise(res=>{ const st=document.getElementById('stage');
          const t=(x)=>new Touch({identifier:1,target:st,clientX:x,clientY:200});
          st.dispatchEvent(new TouchEvent('touchstart',{touches:[t(x0)],changedTouches:[t(x0)],bubbles:true}));
          setTimeout(()=>{ st.dispatchEvent(new TouchEvent('touchend',{touches:[],changedTouches:[t(x1)],bubbles:true})); res(); }, ms); })"""
        p.evaluate(ARRASTA, [600, 400, 150]); p.wait_for_timeout(200)
        r.t('Arrastar para a esquerda passa para a próxima', p.evaluate('curIdx') == 3)
        p.evaluate(ARRASTA, [400, 600, 150]); p.wait_for_timeout(200)
        r.t('Arrastar para a direita volta', p.evaluate('curIdx') == 2)
        p.evaluate(ARRASTA, [500, 470, 150]); p.wait_for_timeout(200)
        r.t('Um movimento curto (toque) não passa', p.evaluate('curIdx') == 2)
        p.evaluate(ARRASTA, [600, 400, 1200]); p.wait_for_timeout(200)
        r.t('Arrasto lento demais não passa', p.evaluate('curIdx') == 2)
        p.evaluate("openCfg()"); p.wait_for_timeout(200)
        p.evaluate(ARRASTA, [600, 400, 150]); p.wait_for_timeout(200)
        r.t('Com as Configurações abertas, arrastar não mexe na leitura', p.evaluate('curIdx') == 2)
        ctx.close()
        res.append(r.fim())

        # ================= 3) Dias seguidos =================
        r = R('3) 🔥 Dias seguidos só contam com leitura de verdade')
        ctx, fb = novo_contexto(b, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        p = abrir(ctx); p.wait_for_timeout(1500)
        nova_crianca(p, 'TESTE ANA', 3)
        uid = p.evaluate('U.atual')
        r.t('Criança nova: abrir e entrar NÃO grava o dia (ultimoDia vazio)', uid and uid != 'p1' and ls(p, 'mundo_%s_ultimoDia' % uid) is None, uid)
        r.t('Abrir com a Hinata também não grava o dia dela', ls(p, 'mundo_p1_ultimoDia') is None)
        marcar_lida(p, 0, 0)
        r.t('Marcar LIDA grava o dia de hoje e 1 dia seguido', ls(p, 'mundo_%s_ultimoDia' % uid) == dia(hoje) and ls(p, 'mundo_%s_seqDias' % uid) == '1')
        ontem = hoje - datetime.timedelta(days=1)
        p.evaluate("([a,b])=>{ localStorage.setItem(K('ultimoDia'),a); localStorage.setItem(K('seqDias'),b); }", [dia(ontem), '4'])
        marcar_lida(p, 0, 1)
        r.t('Leu ontem e hoje: vira 5 dias seguidos', ls(p, 'mundo_%s_seqDias' % uid) == '5')
        marcar_lida(p, 0, 2)
        r.t('Mais uma leitura no mesmo dia: continua 5', ls(p, 'mundo_%s_seqDias' % uid) == '5')
        antes = hoje - datetime.timedelta(days=3)
        p.evaluate("([a,b])=>{ localStorage.setItem(K('ultimoDia'),a); localStorage.setItem(K('seqDias'),b); }", [dia(antes), '7'])
        p.evaluate("abrirConquistas()"); p.wait_for_timeout(200)
        r.t('Sem ler há 3 dias: Conquistas mostra 0 (sem apagar as chaves)', p.evaluate('streakDias') == 0 and ls(p, 'mundo_%s_seqDias' % uid) == '7')
        p.evaluate("fecharConquistas()")
        r.t('Nenhuma chave mundo_p0_* criada', not [k for k in chaves_brutas(p) if k.startswith('mundo_p0_')])
        ctx.close()
        res.append(r.fim())

        # ================= 4) Marcos e medalhas =================
        r = R('4) 🏅 Marcos e medalhas até o total do app')
        ctx, fb = novo_contexto(b, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        r.t('Marcos vão até o total (1.500, 2.000, 3.000 e todas)', p.evaluate('MARCOS[MARCOS.length-1]===TOTAL_CUR && MARCOS.includes(1500) && MARCOS.includes(2000) && MARCOS.includes(3000)'))
        p.evaluate("abrirConquistas()"); p.wait_for_timeout(300)
        t = p.text_content('#conquistas') or ''
        r.t('Minhas Conquistas mostra as medalhas novas', all(x in t for x in ['Astronauta do Saber', 'Coruja Sábia', 'Arco-Íris do Saber', 'Leu o Mundo Inteiro']), t[:200])
        r.t('Sem erros', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())

        # ================= 5) "Ler ao tocar" lembrado (celular, nuvem, backup) =================
        r = R('5) 🔊 "Ler ao tocar" lembrado — no celular, na nuvem e no backup')
        fb = FakeFirebase()
        ctx, _ = novo_contexto(b, fb=fb, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        p = abrir(ctx); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("(()=>{ paisIdx=3; curIdx=0; openReader(); toggleSayTap(); })()"); p.wait_for_timeout(200)
        r.t('Desligar grava mundo_p1_sayTap = 0', ls(p, 'mundo_p1_sayTap') == '0')
        r.t('sayTap está nas listas do backup, da nuvem e das preferências locais',
            p.evaluate("CHAVES_DADOS.includes('sayTap') && CHAVES_NUVEM.includes('sayTap') && CHAVES_SIMPLES_NUVEM.includes('sayTap')"))
        r.t('Exportar a criança (backup e nuvem) leva o sayTap', (p.evaluate("ADAPTADOR_CRIANCAS.exportar('p1')") or {}).get('sayTap') == '0')
        r.t('A criança tem agora 26 chaves possíveis (24 do backup + dias seguidos; v2.3 somou margem, recuo e palavra)', p.evaluate("ADAPTADOR_CRIANCAS.chavesDaCrianca('p1').length") == 26)
        ok_nuvem = esperar_ok(p)
        dn = fb.dados_app('hinata_1f98b', familia='pmrtestes') or {}
        r.t('Chega na nuvem (Firebase de mentira) com sayTap = 0', ok_nuvem and dn.get('sayTap') == '0', (ok_nuvem, dn.get('sayTap')))
        p.reload(); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("(()=>{ paisIdx=3; curIdx=0; openReader(); })()"); p.wait_for_timeout(200)
        r.t('Depois de reabrir o app continua desligado (e o botão aparece desligado)', p.evaluate('sayTapOn') is False and p.evaluate("document.getElementById('sayWord').classList.contains('off')"))
        ctx.close()
        # criança trazida da nuvem para outro celular adota o "ler ao tocar" de lá
        fb2 = FakeFirebase()
        fb2.gravar_app('bia_1f430', 'Bia', '🐰', {'lidas': json.dumps({'AL1': '111'}), 'sayTap': '0', 'theme': '5'}, familia='pmrtestes')
        ctx, _ = novo_contexto(b, fb=fb2, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        p = abrir(ctx); p.wait_for_timeout(1500)
        p.evaluate("EscolaFamilia.abrir('nuvem')"); p.wait_for_timeout(2000)
        tem = p.locator('#efRaiz .ef-t6 .ef-mini[data-chave="bia_1f430"]')
        if tem.count():
            tem.first.click(); p.wait_for_timeout(3000)
        bia = [u for u in usuarios(p)['us'] if u['nome'].lower() == 'bia']
        r.t('Criança trazida da nuvem adota o "ler ao tocar" desligado e o tema de lá',
            bool(bia) and ls(p, 'mundo_%s_sayTap' % bia[0]['id']) == '0' and ls(p, 'mundo_%s_theme' % bia[0]['id']) == '5', bia)
        ctx.close()
        # backup antigo (sem sayTap) entra e fica ligado
        f = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False)
        json.dump({'app': 'Curiosidades do Mundo', 'usuarios': {'us': [{'id': 'p7', 'nome': 'Zeca', 'av': '🐶'}], 'atual': 'p7'},
                   'dados': {'p7': {'lidas': json.dumps({'AL1': '1'})}}}, f); f.close()
        ctx, _ = novo_contexto(b, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("openCfg()"); p.set_input_files('#backupFileInput', f.name); p.wait_for_timeout(600)
        p.click('#perguntaOv button:has-text("Juntar")'); p.wait_for_timeout(2500)
        zeca = [u for u in usuarios(p)['us'] if u['nome'] == 'Zeca']
        r.t('Backup antigo sem sayTap entra (Zeca) e o "ler ao tocar" dele fica ligado (padrão)',
            bool(zeca) and ls(p, 'mundo_%s_sayTap' % zeca[0]['id']) in (None, '1'), zeca)
        r.t('Nenhuma caixinha do navegador', not [e for e in erros if 'CAIXINHA' in e], erros)
        os.unlink(f.name)
        ctx.close()
        res.append(r.fim())

        # ================= 6) Desafio com placar =================
        r = R('6) 🎯 Desafio com placar e mensagem gentil')
        lid = json.dumps({})
        ctx, fb = novo_contexto(b, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')]))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("(()=>{ const l=JSON.parse(localStorage.getItem(K('lidas'))||'{}'); l[DATA[0].code]='1111111111'; localStorage.setItem(K('lidas'),JSON.stringify(l)); resincronizarDoDisco(); })()")
        p.evaluate("abrirDesafio()"); p.wait_for_timeout(300)
        r.t('Mostra o placar e a dica', '🎯 Vamos lá!' in (p.text_content('.desafioPlacar') or '') and 'Qual figura combina' in (p.text_content('.desafioDica') or ''))
        certo = p.evaluate("desafioAtual.opts.indexOf(desafioAtual.alvo)")
        errado = 0 if certo != 0 else 1
        p.click('.desafioOpt >> nth=%d' % errado); p.wait_for_timeout(300)
        r.t('Errar mostra "Boa tentativa" e o placar "0 de 1"', 'Boa tentativa' in (p.text_content('#desafioBody') or '') and '0 de 1' in (p.text_content('.desafioPlacar') or ''), p.text_content('#desafioBody'))
        p.evaluate("fecharDesafio()")
        r.t('Sem erros', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())

        # ================= 7) Karaokê com a voz, busca, Últimas Lidas =================
        r = R('7) 🎤 Karaokê no ritmo da voz, 🔍 busca e 🕒 Últimas Lidas')
        ctx, fb = novo_contexto(b, largura=900, altura=420, storage=st_criancas([('p1','Hinata','🦋')], extra={'mundo_p1_voz': '1', 'mundo_p1_cfgAudio': '1', 'mundo_p1_cfgHi': '1'}))
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(1500); escolher(p, 'p1')
        p.evaluate("(()=>{ paisIdx=3; curIdx=0; openReader(); })()"); p.wait_for_timeout(300)
        # a "voz" de mentira avisa que começou a 3ª palavra
        p.evaluate("""(()=>{ window.__falou=[]; const fake={ speaking:false, pending:false, cancel(){}, getVoices(){return [];},
              speak(u){ window.__falou.push(u.text); const ini=[]; const re=/\\S+/g; let m; while((m=re.exec(u.text))) ini.push(m.index);
                setTimeout(()=>{ if(u.onboundary) u.onboundary({name:'word', charIndex: ini[2]}); }, 30); } };
              Object.defineProperty(window,'speechSynthesis',{configurable:true, value:fake}); vozOn=true; cfgAudio=true; cfgHi=true; })()""")
        p.evaluate("speakText()"); p.wait_for_timeout(120)
        idx = p.evaluate("[...document.querySelectorAll('#text .w')].findIndex(w=>w.classList.contains('on') || w.querySelector('.s.on'))")
        r.t('Quando a voz avisa a palavra, é ela que acende (a 3ª)', idx == 2, idx)
        p.wait_for_timeout(400)
        idx2 = p.evaluate("[...document.querySelectorAll('#text .w')].findIndex(w=>w.classList.contains('on') || w.querySelector('.s.on'))")
        r.t('...e o ritmo antigo não passa por cima (continua a 3ª)', idx2 == 2, idx2)
        n = p.evaluate("procuraCuriosidades('dinossauro').totalReal")
        conta = p.evaluate("(()=>{ const q=normaliza('dinossauro'); let t=0; DATA.forEach(pa=>{ const ok=normaliza(pa.name).indexOf(q)>=0||normaliza(pa.sec).indexOf(q)>=0; pa.items.forEach(it=>{ if(ok||normaliza(it.c).indexOf(q)>=0) t++; }); }); return t; })()")
        r.t('Busca acha os mesmos resultados de antes, com o índice preparado uma vez só', n and n == conta and p.evaluate("indiceBusca()===indiceBusca()"), (n, conta))
        marcar_lida(p, 3, 0); marcar_lida(p, 3, 1)
        p.evaluate("abrirUltimasLidas()"); p.wait_for_timeout(300)
        r.t('Últimas Lidas mostra as curiosidades marcadas', p.locator('#ultimasLidasTela .uFrase').count() >= 2)
        r.t('Sem erros', not [e for e in erros if 'console.error' not in e], erros)
        ctx.close()
        res.append(r.fim())

        # ================= 8) dois celulares: escolher a criança traz o progresso do outro celular =================
        r = R('8) Dois celulares: escolher a criança com o app aberto traz o que ela leu no outro celular (achado do conferente)')
        r.t('Escolher a Bia no celular B traz as 2 leituras feitas no celular A em até 4 s', dois_celulares(b), '')
        res.append(r.fim())

        b.close()
    ok = sum(a for a, _ in res); tot = sum(t for _, t in res)
    print('\nV21: %d/%d' % (ok, tot))
    return ok == tot

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
