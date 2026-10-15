import sys, json
from lib import *
sys.path.insert(0,'/home/claude/revisor/v20/testes/navegador')
import ef
P18=int(os.environ.get('P18','8970')); P20=int(os.environ.get('P20','8971'))
d18=preparar(RAIZ+'/v20/testes/versao_anterior_v1.8', RAIZ+'/meus/srv18k')
d20=preparar(RAIZ+'/v20/pacote-netlify', RAIZ+'/meus/srv20k')
s18=Servidor(P18,d18); s20=Servidor(P20,d20)
HIN='p1790243541621'
r=R('H9 um celular na v1.8 e outro na v2.0, mesma família, ao mesmo tempo')
def nl(fb): 
    d=fb.dados_app('hinata_1f98b',familia='pmrtestes'); return (ef.conta_lidas(json.loads(d['lidas'])), d.get('seqDias')) if d else None
with sync_playwright() as pw:
    fb=FakeFirebase(); er=[]
    # A: v1.8
    stA=storage_do_backup('pmrtestes')
    cA,_=ctx_novo(pw,fb,storage=stA); pA=abrir(cA,s18.url,er)
    for _ in range(20):
        pA.wait_for_timeout(500)
        if nl(fb): break
    pA.wait_for_timeout(2500)
    print('  v1.8 subiu:',nl(fb)); r.t('v1.8 subiu 33', nl(fb) and nl(fb)[0]==33)
    # B: v2.0 traz a criança pela nuvem (T2 "já tenho cadastro")
    cB,_=ctx_novo(pw,fb); pB=abrir(cB,s20.url,er)
    pB.click('.ef-t1-ja'); pB.wait_for_timeout(300); pB.fill('#efRaiz input','pmrtestes'); pB.click('#efRaiz button.ef-procurar:not(.ef-procurar-mini)'); pB.wait_for_timeout(2500)
    print('  T2 achou:', pB.text_content('#efRaiz')[:160].replace('\n',' '))
    pB.click('text=TRAZER TODAS'); pB.wait_for_timeout(3500)
    ids=[u['id'] for u in json.loads(ef.chaves_brutas(pB)['mundo_usuarios'])['us']]
    r.t('v2.0 trouxe a Hinata (33)', len(ids)==1 and ef.conta_lidas(ef.lidas(pB,ids[0]))==33, ids)
    # B marca +2
    if not ef.aberta(pB,'ef-t4'): pass
    ef.escolher(pB,ids[0]) if ef.aberta(pB,'ef-t4') else None
    ef.marcar_lida(pB,1,1); ef.marcar_lida(pB,1,2); pB.wait_for_timeout(2000); ef.esperar_ok(pB,10000)
    print('  nuvem depois de B:',nl(fb)); r.t('nuvem 35', nl(fb)[0]==35, nl(fb))
    # A (v1.8) marca +1 e envia (sem antes receber): trava de versão => junta
    pA.evaluate("()=>{ paisIdx=2; curIdx=1; openReader(); toggleLida(); }"); pA.wait_for_timeout(500)
    pA.evaluate("NuvemSync.sincronizar()"); pA.wait_for_timeout(5000)
    print('  nuvem depois de A (v1.8):',nl(fb)); r.t('nuvem 36 (união; v1.8 não derrubou as do v2.0)', nl(fb)[0]==36, nl(fb))
    # B atualiza
    pB.evaluate("EscolaFamilia.abrir('quem')"); pB.wait_for_timeout(400)
    pB.click('.ef-atualizar'); pB.wait_for_timeout(5000)
    n=ef.conta_lidas(ef.lidas(pB,ids[0])); print('  B depois de atualizar:',n)
    r.t('v2.0 recebe a marcação do v1.8 (36)', n==36, n)
    # B muda o bichinho (Hinata 🦋 -> 🐨); A (v1.8) continua sem quebrar
    pB.click('.ef-arrumar'); pB.locator('.ef-t4 .ef-mudar').first.click(); pB.wait_for_timeout(400)
    pB.locator('#efRaiz .ef-bicho').nth(5).click(); vis=pB.evaluate("(()=>{const b=document.querySelector('#efRaiz .ef-pronto'); return !!(b&&b.offsetParent)})()")
    pB.click('#efRaiz .ef-pronto' if vis else '#efRaiz .ef-pronto-mini'); pB.wait_for_timeout(3000); ef.esperar_ok(pB,10000)
    fichas=[k for k in fb.docs if k.count('/')==3 and k.startswith('familias/pmrtestes/usuarios/')]
    print('  fichas:',fichas)
    old=fb.ficha('hinata_1f98b',familia='pmrtestes'); print('  campos da ficha antiga:', list(old.keys()))
    r.t('ficha antiga continua na nuvem com movidoPara', 'movidoPara' in old)
    pA.evaluate("NuvemSync.sincronizar()"); pA.wait_for_timeout(3000)
    r.t('v1.8 continua funcionando (sem erro JS)', not [e for e in er if 'pageerror' in e], er)
    ln=nl(fb); print('  ficha antiga:',ln); r.t('ficha antiga intacta (36)', ln[0]==36, ln)
    nov=fb.dados_app('hinata_1f428',familia='pmrtestes'); print('  ficha nova:', ef.conta_lidas(json.loads(nov['lidas'])) if nov else None)
    r.t('ficha nova com 36', nov and ef.conta_lidas(json.loads(nov['lidas']))==36)
    print('  erros:',er)
    cA.close(); cB.close()
f=r.fim(); sys.exit(1 if f else 0)
