"""🌍 Curiosidades v2.0 — testes do que o Alfabetização ensinou na v123 (teste_v123.py), adaptados:

1) ⚙️ na "Quem vai estudar hoje?" (D17) em 4 tamanhos, e sem nenhuma criança no celular.
2) C1 (nuvem-sync 4.1): uma leitura da nuvem que já estava a caminho quando a criança
   foi tirada NÃO regrava as chaves dela (recuperar e checar a nuvem).
3) C2 (escola-familia 1.2): criança tirada com "guardar uma cópia neste celular"
   deixa a bolinha 🟡 até voltar.
4) Abertura (D2): sempre "Quem vai estudar hoje?", mesmo com 1 criança; depois a estante.
Chromium + Firebase de mentira (nunca o Firebase real)."""
from base import *
from ef import *
import json

def st_criancas(lista, fam='pmrtestes', atual=None):
    return {'mundo_usuarios': us_json(lista, atual), 'escola_familia': familia_json([fam], {i: fam for i,_,_ in lista}, fam), 'nuvem_familia': fam}

def cfg_aberta(p):
    return p.evaluate("document.getElementById('cfgOv').classList.contains('open')")

def raiz_visivel(p):
    return p.evaluate("getComputedStyle(document.getElementById('efRaiz')).visibility") == 'visible'

def chaves_de(p, pre):
    return [k for k in p.evaluate("Object.keys(localStorage)") if k.startswith(pre)]

def main():
    servidor()
    res = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()

        # ================= 1) ⚙️ na T4 =================
        r = R('1) ⚙️ na "Quem vai estudar hoje?"')
        for (W,H) in [(984,432),(740,360),(568,320),(360,740)]:
            ctx, fb = novo_contexto(b, largura=W, altura=H, storage=st_criancas([('p1','Hinata','🦋')]))
            erros = []
            p = abrir(ctx, erros); p.wait_for_timeout(2000)
            g = p.locator('#efRaiz .ef-t4-config')
            bb = g.bounding_box() if g.count() else None
            pt = p.evaluate("(document.querySelector('#efRaiz .ef-t4-config .ef-ponto')||{}).className||''")
            r.t('%dx%d: ao abrir, a T4 tem a ⚙️ (48 px ou mais, dentro da tela) com a bolinha' % (W,H),
                aberta(p,'ef-t4') and bb and bb['width']>=48 and bb['height']>=48 and bb['x']+bb['width']<=W and 'ef-p-' in pt, (bb, pt))
            fs = p.evaluate("(()=>{const a=document.querySelector('#efRaiz .ef-t4-config').getBoundingClientRect(), b=document.querySelector('#efRaiz .ef-t4 .ef-topo .ef-icone:last-child').getBoundingClientRect(); return [a.right, b.left];})()")
            r.t('%dx%d: a ⚙️ fica antes do ⛶, sem encostar' % (W,H), fs[0] <= fs[1] - 2, fs)
            g.click(); p.wait_for_timeout(500)
            r.t('%dx%d: tocar na ⚙️ abre as Configurações do app por cima (a T4 fica escondida, sem fechar)' % (W,H), cfg_aberta(p) and not raiz_visivel(p) and aberta(p,'ef-t4'))
            p.click('#cfgOv .cfgX'); p.wait_for_timeout(700)
            r.t('%dx%d: fechar as Configurações volta para a T4' % (W,H), not cfg_aberta(p) and raiz_visivel(p) and aberta(p,'ef-t4'))
            r.t('%dx%d: nenhum erro de JavaScript' % (W,H), not [e for e in erros if 'console.error' not in e], erros)
            ctx.close()
        # sem nenhuma criança: mexer nas Configurações não cria criança nem chave
        ctx, fb = novo_contexto(b, largura=984, altura=432, storage={'escola_familia': familia_json(['pmrtestes'], {}, 'pmrtestes'), 'nuvem_familia':'pmrtestes',
                                                                      'mundo_usuarios': json.dumps({'us':[],'atual':None})})
        erros = []
        p = abrir(ctx, erros); p.wait_for_timeout(2000)
        p.click('#efRaiz .ef-t4-config'); p.wait_for_timeout(400)
        for s in ['#cfgOv .cfgBt:has-text("🎨 Trocar")','#cfgOv .cfgBt:has-text("✒️ Trocar")','#cfgOv .cfgBt:has-text("A+ Maior")','#cfgHi','#cfgLinha']:
            p.click(s); p.wait_for_timeout(150)
        p.click('#cfgOv .cfgX'); p.wait_for_timeout(700)
        r.t('Sem nenhuma criança: a ⚙️ abre e fecha as Configurações, mudar cores/letra não dá erro e não cria criança nem chave mundo_p0_*',
            aberta(p,'ef-t4') and raiz_visivel(p) and not [e for e in erros if 'console.error' not in e] and usuarios(p)['us']==[] and not chaves_de(p,'mundo_p0_'), (erros, chaves_de(p,'mundo_p')))
        ctx.close()
        res.append(r.fim())

        # ================= 2) C1 =================
        r = R('2) C1: resposta da nuvem que chega depois de a criança sair não regrava as chaves dela')
        for modo in ('recuperar', 'checar'):
            fb = FakeFirebase()
            fb.gravar_app('bia_1f430', 'Bia', '🐰', {'lidas':json.dumps({'AL1':'111'})}, familia='pmrtestes')
            ctx, _ = novo_contexto(b, fb=fb, storage=st_criancas([('p1','Hinata','🦋'),('p2','Bia','🐰')]))
            segurados = []; estado = {'segurar': False}
            def segura(route):
                if estado['segurar'] and route.request.method == 'GET' and 'bia_1f430' in route.request.url and '/versoes' not in route.request.url:
                    segurados.append(route); return
                route.fallback()
            ctx.route('**/firestore.googleapis.com/**', segura)
            p = abrir(ctx); p.wait_for_timeout(2500); fechar_tudo(p)
            p.wait_for_timeout(1500)
            estado['segurar'] = True
            if modo == 'recuperar':
                p.evaluate("(()=>{ window.__r = null; NuvemSync.recuperar('p2','Bia','🐰',false).then(v=>window.__r=v, e=>window.__r='erro'); })()")
            else:
                p.evaluate("(()=>{ const m=JSON.parse(localStorage.getItem('nuvem_curiosidades_meta')||'{}'); delete m['p2']; localStorage.setItem('nuvem_curiosidades_meta', JSON.stringify(m)); window.__r=null; NuvemSync.sincronizar({checarNuvem:true}).then(v=>window.__r=v); })()")
            for _ in range(20):
                if segurados: break
                p.wait_for_timeout(150)
            pegou = len(segurados) > 0
            p.evaluate("(()=>{ const f=()=>ADAPTADOR_CRIANCAS.tirar('p2'); if(NuvemSync.semVigiar) NuvemSync.semVigiar(f); else f(); NuvemSync.limparPendencia && NuvemSync.limparPendencia('p2'); })()")
            antes = chaves_de(p, 'mundo_p2_')
            estado['segurar'] = False
            for rt in segurados:
                try: rt.fallback()
                except Exception: pass
            p.wait_for_timeout(2500)
            depois = chaves_de(p, 'mundo_p2_')
            r.t('%s: a resposta chegou depois de a Bia sair e as chaves mundo_p2_* NÃO voltaram' % modo, pegou and not antes and not depois, (pegou, antes, depois))
            if modo == 'recuperar':
                r.t('recuperar: devolve "não juntou" (false)', p.evaluate("window.__r") is False, p.evaluate("window.__r"))
            r.t('%s: a ficha da Bia na nuvem continua lá' % modo, json.loads((fb.dados_app('bia_1f430', familia='pmrtestes') or {}).get('lidas','{}')).get('AL1') == '111')
            ctx.close()
        res.append(r.fim())

        # ================= 3) C2 =================
        r = R('3) C2: criança guardada só na lixeira deste celular deixa a bolinha 🟡')
        fb = FakeFirebase()
        ctx, _ = novo_contexto(b, fb=fb, storage=st_criancas([('p1','Hinata','🦋'),('p2','Bia','🐰')]))
        instalar_offline(ctx)
        p = abrir(ctx); p.wait_for_timeout(3000); fechar_tudo(p)
        p.evaluate("NuvemSync.sincronizar()"); p.wait_for_timeout(2500)
        cor0 = status_txt(p)['cor']
        lix = [{"id":"p2","nome":"Bia","av":"🐰","fam":"pmrtestes","quando":1,"dados":{"lidas":json.dumps({'AL1':'1111'})},"soAqui":True}]
        p.evaluate("v=>{ localStorage.setItem('escola_lixeira_curiosidades', v); }", json.dumps(lix))
        p.evaluate("(()=>{ const f=()=>ADAPTADOR_CRIANCAS.tirar('p2'); NuvemSync.semVigiar(f); NuvemSync.limparPendencia('p2'); })()")
        s = status_txt(p)
        r.t('Com uma criança só na lixeira: bolinha 🟡 "…GUARDADA(S) SÓ NESTE CELULAR…" (antes estava %s)' % cor0,
            cor0=='verde' and s['cor']=='amarelo' and 'SÓ NESTE CELULAR' in s['txt'], s)
        p.evaluate("EscolaFamilia.abrir('nuvem')"); p.wait_for_timeout(1500)
        p.locator('.ef-lixeira .ef-mini').first.click(); p.wait_for_timeout(1500)
        fechar_tudo(p); p.evaluate("NuvemSync.sincronizar()"); p.wait_for_timeout(2500)
        s2 = status_txt(p)
        nid = [u['id'] for u in usuarios(p)['us'] if u['nome']=='Bia']
        r.t('Trazendo a criança de volta, ela volta com tudo e a bolinha volta a 🟢', s2['cor']=='verde' and nid and lidas(p, nid[0]).get('AL1')=='1111', s2)
        ctx.close()
        res.append(r.fim())

        # ================= 4) abertura (D2) =================
        r = R('4) Abertura: sempre "Quem vai estudar hoje?", mesmo com 1 criança (D2)')
        ctx, fb = novo_contexto(b, storage=dict(st_criancas([('p1','Hinata','🦋')]), **{'mundo_p1_secAtual':'🌍 Países do Mundo'}))
        p = abrir(ctx); p.wait_for_timeout(1500)
        r.t('Com 1 criança, abre na "Quem vai estudar hoje?" (antes entrava direto)', aberta(p,'ef-t4') and p.locator('.ef-t4 .ef-crianca[data-id]').count()==1)
        p.go_back(); p.wait_for_timeout(400)
        r.t('Ao abrir, o voltar do Android não fecha a T4 sem escolher (nunca marca na criança errada)', aberta(p,'ef-t4'))
        escolher(p, 'p1')
        r.t('Tocar na criança: vai para a estante dela (o "passo próprio" do app), com o chip dela', p.is_visible('#home') and not aberta(p,'ef-t4') and '🦋' in p.text_content('#efChipHome'))
        p.reload(); p.wait_for_timeout(1500)
        r.t('Reabrir o app: de novo a "Quem vai estudar hoje?"', aberta(p,'ef-t4'))
        ctx.close()
        res.append(r.fim())

        # ================= 5) achados 🟡 do conferente (rodada 1) =================
        r = R('5) Conferente A1/A2: de quem são as Configurações; botões da pergunta do backup com 48 px')
        ctx, fb = novo_contexto(b, largura=984, altura=432, storage=st_criancas([('p1','Hinata','🦋'),('p2','Bia','🐰')], atual='p1'))
        p = abrir(ctx); p.wait_for_timeout(1500)
        p.click('#efRaiz .ef-t4-config'); p.wait_for_timeout(400)
        r.t('⚙️ na "Quem vai estudar hoje?": o título diz de quem são as cores e a letra ("⚙️ Configurações de 🦋 Hinata")', p.text_content('#cfgTitulo')=='⚙️ Configurações de 🦋 Hinata', p.text_content('#cfgTitulo'))
        p.click('#cfgOv .cfgX'); p.wait_for_timeout(700); escolher(p,'p2'); p.evaluate("openCfg()"); p.wait_for_timeout(300)
        r.t('...e muda quando a criança muda ("de 🐰 Bia")', p.text_content('#cfgTitulo')=='⚙️ Configurações de 🐰 Bia', p.text_content('#cfgTitulo'))
        p.evaluate("(()=>{ closeCfg(); perguntaApp({titulo:'x', linhas:['y'], sim:'✅ Juntar', nao:'Cancelar'}); })()"); p.wait_for_timeout(300)
        hs = p.evaluate("Array.from(document.querySelectorAll('#perguntaOv .btnrow button')).map(b=>b.getBoundingClientRect().height)")
        r.t('Pergunta do backup: botões com 48 px ou mais (%s)' % hs, len(hs)==2 and min(hs)>=48, hs)
        ctx.close()
        ctx, fb = novo_contexto(b, largura=984, altura=432, storage={'escola_familia': familia_json(['pmrtestes'], {}, 'pmrtestes'), 'nuvem_familia':'pmrtestes', 'mundo_usuarios': json.dumps({'us':[],'atual':None})})
        p = abrir(ctx); p.wait_for_timeout(1500); p.click('#efRaiz .ef-t4-config'); p.wait_for_timeout(400)
        r.t('Sem nenhuma criança: o título fica só "⚙️ Configurações"', p.text_content('#cfgTitulo')=='⚙️ Configurações', p.text_content('#cfgTitulo'))
        ctx.close()
        res.append(r.fim())

        # ================= 6) v2.0b: preferência mudada não volta sozinha =================
        r = R('6) v2.0b (achado do Pedro no site de teste): preferência mudada neste celular não volta ao valor do outro celular')
        fb = FakeFirebase(); fb.gravar_app('haha_1f42f','Haha','🐯',{'modoLinha':'0','theme':'0'},familia='pmrtestes')
        ctx, _ = novo_contexto(b, fb=fb, largura=984, altura=432, storage=st_criancas([('p2','Haha','🐯')]))
        p = abrir(ctx); p.wait_for_timeout(3500); escolher(p,'p2')
        p.evaluate("goHome()"); p.click('#cfgGearHome'); p.wait_for_timeout(300); p.click('#cfgLinha'); p.click('#cfgOv .cfgX'); p.wait_for_timeout(300)
        fb.gravar_app('haha_1f42f','Haha','🐯',{'modoLinha':'0','theme':'0'},familia='pmrtestes')   # o outro celular grava de novo
        p.evaluate("(()=>{ NuvemSync.sincronizar(); })()"); p.wait_for_timeout(3000)
        r.t('Criança SEM curiosidade lida neste celular: ligar o "destaque por linha" e a nuvem juntar dados do outro celular → continua LIGADO (v2.3: era "sílabas", que saiu do app)', p.evaluate("modoLinha")==True and ls(p,'mundo_p2_modoLinha')=='1')
        r.t('...e a nuvem fica com o que foi escolhido aqui', (fb.dados_app('haha_1f42f', familia='pmrtestes') or {}).get('modoLinha')=='1')
        p.reload(); p.wait_for_timeout(1500); escolher(p,'p2')
        r.t('...e continua ligado depois de fechar e abrir o app', p.evaluate("modoLinha")==True)
        ctx.close()
        # o que essa regra existe para fazer continua: criança trazida da nuvem / do backup adota as preferências dela
        fb = FakeFirebase(); fb.gravar_app('lia_1f43c','Lia','🐼',{'theme':'5','modoLinha':'1','lidas':json.dumps({'AL1':'1'})},familia='pmrtestes')
        ctx, _ = novo_contexto(b, fb=fb, largura=984, altura=432, storage=st_criancas([('p1','Hinata','🦋')]))
        p = abrir(ctx); p.wait_for_timeout(2500)
        p.locator('#efRaiz .ef-t4 .ef-nuvemcard').first.click(); p.wait_for_timeout(3500)
        r.t('Criança trazida da nuvem continua chegando com as cores e o "destaque por linha" dela', p.evaluate("userAtual().nome")=='Lia' and p.evaluate("themeIdx")==5 and p.evaluate("modoLinha")==True)
        ctx.close()
        res.append(r.fim())
        b.close()
    return res

if __name__=='__main__':
    res = main()
    ok = sum(a for a,_ in res); tot = sum(t for _,t in res)
    print('\nV20: %d/%d' % (ok,tot))
    sys.exit(0 if ok==tot else 1)
