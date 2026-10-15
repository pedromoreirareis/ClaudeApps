"""Ajudantes para as telas do escola-familia.js no 🌍 Curiosidades
(adaptado do ef.py do Alfabetização v123)."""
import json

def aberta(p, cls):
    return p.evaluate("c=>!!document.querySelector('#efRaiz .'+c)", cls)

def toast(p):
    return (p.evaluate("(document.getElementById('efToast')||{}).textContent||''") or '') + ' | ' + (p.text_content('#toast') or '')

def textos(p):
    return p.evaluate("EscolaFamilia.TEXTOS")

def usuarios(p):
    from base import ls
    return json.loads(ls(p, 'mundo_usuarios') or '{"us":[],"atual":null}')

def ids(p):
    return [u['id'] for u in usuarios(p)['us']]

def estado_familia(p):
    from base import ls
    return json.loads(ls(p, 'escola_familia') or 'null')

def fechar_tudo(p):
    p.evaluate("""()=>{ try{ EscolaFamilia.fecharTudo(); }catch(e){}
      ['cfgOv','perguntaOv','infoOv','detOv','transOv'].forEach(i=>{const e=document.getElementById(i); if(e) e.classList.remove('open');}); }""")
    p.wait_for_timeout(250)

def segurar(p, seletor, ms=3300):
    """trava do adulto: segura o botão por 3 s"""
    loc = p.locator(seletor).first
    loc.scroll_into_view_if_needed()
    bb = loc.bounding_box()
    p.mouse.move(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 2)
    p.mouse.down(); p.wait_for_timeout(ms); p.mouse.up()
    p.wait_for_timeout(300)

def cadastrar_t5(p, nome, bicho_idx, esperar=1600):
    p.fill('#efRaiz .ef-nome-campo', nome)
    p.locator('#efRaiz .ef-bicho').nth(bicho_idx).click()
    vis = p.evaluate("(()=>{const b=document.querySelector('#efRaiz .ef-pronto'); return !!(b && b.offsetParent);})()")
    p.click('#efRaiz .ef-pronto' if vis else '#efRaiz .ef-pronto-mini')
    p.wait_for_timeout(esperar)

def nova_crianca(p, nome, bicho_idx, fam=None):
    if fam is None:
        p.evaluate("EscolaFamilia.abrir('nova')")
    else:
        p.evaluate("f=>EscolaFamilia.abrir('nova', f)", fam)
    p.wait_for_timeout(300)
    cadastrar_t5(p, nome, bicho_idx)

def escolher(p, id_, ms=1500):
    p.click('#efRaiz .ef-t4 .ef-crianca[data-id="%s"]' % id_)
    p.wait_for_timeout(ms)

def familia_json(fams, criancas, atual, extra=None):
    st = {"v": 1, "familias": [{"c": c, "desde": 1, "conferida": True, "origem": "teste"} for c in fams],
          "criancas": criancas, "atual": atual, "ultimoNuvemFamilia": atual, "primeiraAberturaEm": 1,
          "liberouSegundaFamilia": False, "mudancasPendentes": [], "recusas": {}}
    if extra: st.update(extra)
    return json.dumps(st)

def us_json(lista, atual=None):
    """mundo_usuarios: lista de (id, nome, bichinho)"""
    return json.dumps({"us": [{"id": i, "nome": n, "av": a} for i, n, a in lista],
                       "atual": atual if atual is not None else (lista[0][0] if lista else None)})

def lidas(p, id_):
    from base import ls
    return json.loads(ls(p, 'mundo_%s_lidas' % id_) or '{}')

def conta_lidas(d):
    return sum(str(v).count('1') for v in (d or {}).values())

def marcar_lida(p, pais, cur):
    """abre o cartão 'pais' na curiosidade 'cur' e marca LIDA (a mesma função do botão;
    o toque de verdade no botão é testado no regressao.py)"""
    p.evaluate("([a,b])=>{ paisIdx=a; curIdx=b; openReader(); toggleLida(); }", [pais, cur])
    p.wait_for_timeout(150)

def ponto(p, sel):
    return p.evaluate("s=>(document.querySelector(s+' .ef-ponto')||{}).className||''", sel)

def status_txt(p):
    return p.evaluate("EscolaFamilia.situacao()")

OFFLINE_INIT = """(function(){ const g=Storage.prototype.getItem, st=Storage.prototype.setItem;
  Object.defineProperty(Navigator.prototype,'onLine',{configurable:true,get(){ try{ return g.call(sessionStorage,'__off')!=='1'; }catch(e){ return true; } }});
  window.__offline=function(v){ st.call(sessionStorage,'__off',v?'1':'0'); window.dispatchEvent(new Event(v?'offline':'online')); };
})();"""
def instalar_offline(ctx):
    """'sem internet' que sobrevive ao recarregar a página"""
    ctx.add_init_script(OFFLINE_INIT)

def offline(p, fb, sim):
    fb.offline = bool(sim)
    p.evaluate("v=>window.__offline(v)", bool(sim))
    p.wait_for_timeout(200)

def esperar_ok(p, ms=8000):
    for _ in range(ms // 250):
        st = p.evaluate("NuvemSync.status()")
        if st['estado'] == 'ok' and st['pendentes'] == 0: return True
        p.wait_for_timeout(250)
    return False

def chaves_brutas(p):
    return p.evaluate("()=>{ const g=Storage.prototype.getItem; const o={}; for(let i=0;i<localStorage.length;i++){ const k=localStorage.key(i); o[k]=g.call(localStorage,k); } return o; }")

def storage_do_backup(arq, familia=None):
    """monta o localStorage de um celular a partir de um backup exportado (como estava na v1.8)"""
    b = json.load(open(arq, encoding='utf-8'))
    st = {'mundo_usuarios': json.dumps(b['usuarios'])}
    for uid, ch in b['dados'].items():
        for k, v in ch.items(): st['mundo_%s_%s' % (uid, k)] = v
    if familia: st['nuvem_familia'] = familia
    return st
