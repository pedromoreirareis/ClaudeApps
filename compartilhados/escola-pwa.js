/* =====================================================================
   escola-pwa.js — Escola São Pedro
   O MESMO arquivo para todos os aplicativos. Não precisa editar.

   Versão 2: também guarda a lista dos 8 BICHINHOS OFICIAIS (EscolaPWA.BICHINHOS).

   Faz três coisas:
   1) 📺 TELA SEMPRE ACESA — enquanto o app estiver na frente (em uso),
      o celular não apaga a tela nem bloqueia. Usa o "Wake Lock" do
      navegador; se o celular recusar ou não tiver, usa um modo reserva
      (um vídeo invisível e mudo, o mesmo truque dos players de vídeo).
      Um vigia confere a cada 15 segundos se continua valendo.
   2) ⛶ TELA CHEIA — a cada toque, se o app não estiver em tela cheia,
      volta para a tela cheia.
   3) 📲 CONVITE PARA INSTALAR — ao abrir pelo navegador, mostra uma
      janelinha oferecendo instalar o app na tela do celular. Aparece
      sempre que abrir pelo navegador, até o app ser instalado.

   Uso no app:  EscolaPWA.iniciar({ nome:'Curiosidades', icone:'icon-192.png',
                                    chaveTelaAcesa:'mundo_telaAcesa',
                                    aoEntrarTelaCheia: function(){...} });
   ===================================================================== */
(function(){
'use strict';

var VERSAO = '2';

/* OS 8 BICHINHOS OFICIAIS da Escola São Pedro — iguais em TODOS os apps,
   nesta ordem. A identidade da criança é NOME + BICHINHO (também na nuvem).
   Não acrescente, não tire e não troque a ordem. */
var BICHINHOS = [
  { e:'🦉', nome:'Coruja' },
  { e:'🦊', nome:'Raposa' },
  { e:'🐰', nome:'Coelho' },
  { e:'🐼', nome:'Panda' },
  { e:'🦋', nome:'Borboleta' },
  { e:'🐨', nome:'Coala' },
  { e:'🐯', nome:'Tigre' },
  { e:'🐴', nome:'Pônei' }
];
var VIDEO_MP4 = 'data:video/mp4;base64,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';
var VIDEO_WEBM = 'data:video/webm;base64,GkXfo59ChoEBQveBAULygQRC84EIQoKEd2VibUKHgQRChYECGFOAZwEAAAAAAAkfEU2bdLpNu4tTq4QVSalmU6yBoU27i1OrhBZUrmtTrIHYTbuMU6uEElTDZ1OsggGETbuMU6uEHFO7a1OsggkJ7AEAAAAAAABZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVSalmsirXsYMPQkBNgI1MYXZmNjAuMTYuMTAwV0GNTGF2ZjYwLjE2LjEwMESJiECfYAAAAAAAFlSua0CmrgEAAAAAAAA414EBc8WI+8rJiCU6uiicgQAitZyDdW5kiIEAhoVWX1ZQOIOBASPjg4QF9eEA4ImwgRC6gRCagQKuAQAAAAAAAFzXgQJzxYirgYM0NEicy5yBACK1nIN1bmSIgQCGhkFfT1BVU1aqg2MuoFa7hATEtACDgQLhkZ+BAbWIQL9AAAAAAABiZIEQY6KTT3B1c0hlYWQBATgBQB8AAAAAABJUw2dA1nNzoGPAgGfImkWjh0VOQ09ERVJEh41MYXZmNjAuMTYuMTAwc3PWY8CLY8WI+8rJiCU6uihnyKFFo4dFTkNPREVSRIeUTGF2YzYwLjMxLjEwMiBsaWJ2cHhnyKFFo4hEVVJBVElPTkSHkzAwOjAwOjAyLjAwMDAwMDAwMABzc9djwItjxYirgYM0NEicy2fIokWjh0VOQ09ERVJEh5VMYXZjNjAuMzEuMTAyIGxpYm9wdXNnyKFFo4hEVVJBVElPTkSHkzAwOjAwOjAyLjAwODAwMDAwMAAfQ7Z1RqPngQCji4IAAIAIC+Y7I6tgo6OBAACAEAIAnQEqEAAQAABHCIWFiIWEiAICAAwNYAD+/6tQgKOKggAVgAgIrLMOxqOKggApgAgIrLMOxqOKggA9gAgIrLMOxqOKggBRgAgIrLMOxqOKggBlgAgIrLMOxqOVgQBkALEBAAEQEAAYABhYL/QACAAAo4qCAHmACAissw7Go4qCAI2ACAissw7Go4qCAKGACAissw7Go4qCALWACAissw7Go4qCAMmACAissw7Go5WBAMgAsQEAARAQABgAGFgv9AAIAACjioIA3YAICKyzDsajioIA8YAICKyzDsajioIBBYAICKyzDsajioIBGYAICKyzDsajioIBLYAICKyzDsajlYEBLACxAQABEBAAGAAYWC/0AAgAAKOKggFBgAgIrLMOxqOKggFVgAgIrLMOxqOKggFpgAgIrLMOxqOKggF9gAgIrLMOxqOKggGRgAgIrLMOxqOVgQGQALEBAAEQEAAYABhYL/QACAAAo4qCAaWACAissw7Go4qCAbmACAissw7Go4qCAc2ACAissw7Go4qCAeGACAissw7Go4qCAfWACAissw7Go5WBAfQAsQEAARAQABgAGFgv9AAIAACjioICCYAICKyzDsajioICHYAICKyzDsajioICMYAICKyzDsajioICRYAICKyzDsajioICWYAICKyzDsajlYECWACxAQABEBAAGAAYWC/0AAgAAKOKggJtgAgIrLMOxqOKggKBgAgIrLMOxqOKggKVgAgIrLMOxqOKggKpgAgIrLMOxqOKggK9gAgIrLMOxqOVgQK8ALEBAAEQEBRgAGFgv9AAIAAAo4qCAtGACAissw7Go4qCAuWACAissw7Go4qCAvmACAissw7Go4qCAw2ACAissw7Go4qCAyGACAissw7Go5WBAyAAsQEAARAQABgAGFgv9AAIAACjioIDNYAICKyzDsajioIDSYAICKyzDsajioIDXYAICKyzDsajioIDcYAICKyzDsajioIDhYAICKyzDsajlYEDhACxAQABEBAAGAAYWC/0AAgAAKOKggOZgAgIrLMOxqOKggOtgAgIrLMOxqOKggPBgAgIrLMOxqOKggPVgAgIrLMOxqOKggPpgAgIrLMOxqOVgQPoALEBAAEQEAAYABhYL/QACAAAo4qCA/2ACAissw7Go4qCBBGACAissw7Go4qCBCWACAissw7Go4qCBDmACAissw7Go4qCBE2ACAissw7Go5WBBEwAsQEAARAQABgAGFgv9AAIAACjioIEYYAICKyzDsajioIEdYAICKyzDsajioIEiYAICKyzDsajioIEnYAICKyzDsajioIEsYAICKyzDsajlYEEsACxAQABEBAAGAAYWC/0AAgAAKOKggTFgAgIrLMOxqOKggTZgAgIrLMOxqOKggTtgAgIrLMOxqOKggUBgAgIrLMOxqOKggUVgAgIrLMOxqOVgQUUALEBAAEQEAAYABhYL/QACAAAo4qCBSmACAissw7Go4qCBT2ACAissw7Go4qCBVGACAissw7Go4qCBWWACAissw7Go4qCBXmACAissw7Go5WBBXgAsQEAARAQABgAGFgv9AAIAACjioIFjYAICKyzDsajioIFoYAICKyzDsajioIFtYAICKyzDsajioIFyYAICKyzDsajioIF3YAICKyzDsajlYEF3ACxAQABEBAAGAAYWC/0AAgAAKOKggXxgAgIrLMOxqOKggYFgAgIrLMOxqOKggYZgAgIrLMOxqOKggYtgAgIrLMOxqOKggZBgAgIrLMOxqOVgQZAALEBAAEQEAAYABhYL/QACAAAo4qCBlWACAissw7Go4qCBmmACAissw7Go4qCBn2ACAissw7Go4qCBpGACAissw7Go4qCBqWACAissw7Go5WBBqQAsQEAARAQABgAGFgv9AAIAACjioIGuYAICKyzDsajioIGzYAICKyzDsajioIG4YAICKyzDsajioIG9YAICKyzDsajioIHCYAICKyzDsajlYEHCACxAQABEBAUYABhYL/QACAAAKOKggcdgAgIrLMOxqOKggcxgAgIrLMOxqOKggdFgAgIrLMOxqOKggdZgAgIrLMOxqOKggdtgAgIrLMOxqOVgQdsALEBAAEQEAAYABhYL/QACAAAo4qCB4GACAissw7Go4qCB5WACAissw7Go4qCB6mACAissw7Go4qCB72ACAissw7GoJOhioIH0QAICKyzDsZ1ooQAzf5gHFO7a5G7j7OBALeK94EB8YICYPCBEA==';

var OPT = { nome:'', icone:'icon-192.png', chaveTelaAcesa:'escola_telaAcesa',
            telaCheia:true, convite:true, conviteDepoisMs:2500, aoEntrarTelaCheia:null };
var iniciado = false;
var ouvintes = [];

function ler(k){ try{ return window.localStorage.getItem(k); }catch(e){ return null; } }
function grava(k,v){ try{ window.localStorage.setItem(k,v); }catch(e){} }
function avisa(){ var e = estado(); ouvintes.forEach(function(f){ try{ f(e); }catch(er){} }); }
function visivel(){ return document.visibilityState === 'visible'; }

/* ----- como o app está aberto: navegador ou instalado ----- */
function modoApp(){
  var modos = ['fullscreen','standalone','minimal-ui'];
  for(var i=0;i<modos.length;i++){
    try{ if(window.matchMedia('(display-mode: '+modos[i]+')').matches) return modos[i]; }catch(e){}
  }
  if(window.navigator.standalone === true) return 'standalone';
  return 'browser';
}
function instaladoAberto(){ return modoApp() !== 'browser'; }

/* =====================================================================
   1) TELA SEMPRE ACESA
   ===================================================================== */
var T = { ligada:true, lock:null, pedindo:false, video:null, videoTocando:false, erro:'' };

function suportaNativo(){ return ('wakeLock' in navigator) && window.isSecureContext !== false; }
function ativaNativo(){ return !!(T.lock && !T.lock.released); }

function pedirTelaAcesa(){
  if(!T.ligada || !visivel()) return;
  if(ativaNativo()){ pararVideo(); return; }
  if(suportaNativo()){
    if(T.pedindo) return;
    T.pedindo = true;
    var p;
    try{ p = navigator.wakeLock.request('screen'); }catch(e){ p = Promise.reject(e); }
    Promise.resolve(p).then(function(lock){
      T.lock = lock; T.erro = '';
      pararVideo();
      try{
        lock.addEventListener('release', function(){
          if(T.lock === lock) T.lock = null;
          avisa();
          if(T.ligada && visivel()) setTimeout(pedirTelaAcesa, 700);
        });
      }catch(e){}
    }, function(e){
      T.erro = (e && e.name) || 'erro';
      iniciarVideo();                       /* modo reserva */
    }).then(function(){ T.pedindo = false; avisa(); });
  } else {
    iniciarVideo();                         /* navegador sem Wake Lock */
  }
}
function soltarTelaAcesa(){
  var l = T.lock; T.lock = null;
  try{ if(l) l.release(); }catch(e){}
  pararVideo();
  avisa();
}
function iniciarVideo(){
  if(!T.ligada || !document.body) return;
  if(!T.video){
    var v = document.createElement('video');
    v.setAttribute('playsinline',''); v.setAttribute('webkit-playsinline','');
    v.setAttribute('muted',''); v.muted = true; v.loop = true;
    v.setAttribute('aria-hidden','true'); v.setAttribute('title','');
    v.disablePictureInPicture = true;
    v.style.cssText = 'position:fixed;left:0;bottom:0;width:2px;height:2px;opacity:.01;pointer-events:none;z-index:1';
    var s1 = document.createElement('source'); s1.src = VIDEO_MP4; s1.type = 'video/mp4';
    var s2 = document.createElement('source'); s2.src = VIDEO_WEBM; s2.type = 'video/webm';
    v.appendChild(s1); v.appendChild(s2);
    v.addEventListener('pause', function(){ T.videoTocando = false; avisa(); });
    v.addEventListener('playing', function(){ T.videoTocando = true; avisa(); });
    document.body.appendChild(v);
    T.video = v;
  }
  if(!T.video.paused) return;
  try{
    var p = T.video.play();
    if(p && p.then) p.then(function(){ T.videoTocando = true; avisa(); }, function(){ T.videoTocando = false; avisa(); });
  }catch(e){}
}
function pararVideo(){
  if(T.video && !T.video.paused){ try{ T.video.pause(); }catch(e){} }
  T.videoTocando = false;
}
function estadoTela(){
  var modo = ativaNativo() ? 'nativo' : (T.videoTocando ? 'reserva' : 'nenhum');
  return { ligada:T.ligada, ativa: modo !== 'nenhum', modo:modo, suportaNativo:suportaNativo(), erro:T.erro };
}
function alternarTelaAcesa(forcar){
  T.ligada = (typeof forcar === 'boolean') ? forcar : !T.ligada;
  grava(OPT.chaveTelaAcesa, T.ligada ? '1' : '0');
  if(T.ligada) pedirTelaAcesa(); else soltarTelaAcesa();
  avisa();
  return T.ligada;
}

/* =====================================================================
   2) TELA CHEIA
   ===================================================================== */
function emTelaCheiaDoNavegador(){ return !!(document.fullscreenElement || document.webkitFullscreenElement); }
function pedirTelaCheia(){
  if(!OPT.telaCheia || emTelaCheiaDoNavegador()) return;
  var el = document.documentElement;
  var fn = el.requestFullscreen || el.webkitRequestFullscreen;
  if(!fn) return;
  try{
    var p = fn.call(el, { navigationUI:'hide' });
    if(p && p.then) p.then(function(){ if(OPT.aoEntrarTelaCheia) try{ OPT.aoEntrarTelaCheia(); }catch(e){} }, function(){});
    else if(OPT.aoEntrarTelaCheia) try{ OPT.aoEntrarTelaCheia(); }catch(e){}
  }catch(e){}
}
/* roda DEPOIS do botão tocado (fase de "borbulha"), para não atrapalhar
   botões que abrem o seletor de arquivo, a instalação etc. */
function aoTocar(ev){
  pedirTelaAcesa();
  var alvo = ev && ev.target;
  if(alvo && alvo.closest){
    if(alvo.closest('input,textarea,select,[contenteditable="true"],#escolaConvite')) return;
  }
  pedirTelaCheia();
}

/* =====================================================================
   3) CONVITE PARA INSTALAR
   ===================================================================== */
var I = { evento:null, aberto:false, css:false };
var CHAVE_INST = 'escola_instalado';

function cssConvite(){
  if(I.css) return; I.css = true;
  var st = document.createElement('style');
  st.textContent =
  '#escolaConvite{position:fixed;inset:0;z-index:2147483000;background:#0b1633b3;display:flex;align-items:center;justify-content:center;padding:10px;font-family:system-ui,"Segoe UI",Roboto,Arial,sans-serif}'+
  '#escolaConvite .ecCard{background:#fffdf7;border-radius:22px;max-width:520px;width:100%;max-height:94vh;overflow:auto;padding:clamp(12px,3vh,22px) clamp(14px,3vw,24px);box-shadow:0 12px 40px #0008;text-align:center;color:#123a63}'+
  '#escolaConvite .ecTopo{display:flex;align-items:center;justify-content:center;gap:12px}'+
  '#escolaConvite img{width:clamp(44px,12vh,68px);height:clamp(44px,12vh,68px);border-radius:16px;box-shadow:0 3px 10px #0003}'+
  '#escolaConvite .ecT{font-size:clamp(17px,4vh,23px);font-weight:900;line-height:1.2;text-align:left}'+
  '#escolaConvite .ecD{font-size:clamp(12.5px,2.6vh,15px);font-weight:700;color:#4a6a86;margin:clamp(6px,1.6vh,12px) 0;line-height:1.4}'+
  '#escolaConvite .ecPassos{text-align:left;background:#eef4ff;border-radius:14px;padding:8px 12px;margin:6px 0 4px;font-size:clamp(12.5px,2.5vh,15px);font-weight:700;line-height:1.5}'+
  '#escolaConvite .ecPassos b{color:#1e3a8a}'+
  '#escolaConvite .ecBts{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:clamp(8px,2vh,14px)}'+
  '#escolaConvite button{border:0;border-radius:18px;font-weight:900;font-size:clamp(14px,2.9vh,18px);padding:clamp(9px,2vh,13px) clamp(16px,4vw,26px);cursor:pointer;font-family:inherit;box-shadow:0 4px 12px #0003}'+
  '#escolaConvite .ecSim{background:#f0a030;color:#fff}'+
  '#escolaConvite .ecNao{background:#e6ecf5;color:#123a63}'+
  '#escolaConvite button:active{transform:translateY(2px)}';
  document.head.appendChild(st);
}
function nomeApp(){
  if(OPT.nome) return OPT.nome;
  var m = document.querySelector('meta[name="apple-mobile-web-app-title"]');
  return (m && m.content) || document.title || 'aplicativo';
}
function ehIOS(){ return /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform==='MacIntel' && navigator.maxTouchPoints>1); }
function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

function montarConvite(){
  cssConvite();
  var ov = document.getElementById('escolaConvite');
  if(!ov){ ov = document.createElement('div'); ov.id = 'escolaConvite'; document.body.appendChild(ov); }
  var nome = esc(nomeApp());
  var html = '<div class="ecCard" role="dialog" aria-modal="true">'+
    '<div class="ecTopo"><img alt="" src="'+esc(OPT.icone)+'"><div class="ecT">📲 Instalar o app<br>“'+nome+'”</div></div>'+
    '<div class="ecD">Assim ele fica na tela do celular como um aplicativo, abre em <b>tela cheia</b> e funciona <b>mesmo sem internet</b>.</div>';
  if(I.evento){
    html += '<div class="ecBts"><button class="ecSim" id="ecInstalar">📲 Instalar agora</button><button class="ecNao" id="ecAgoraNao">Agora não</button></div>';
  } else if(ehIOS()){
    html += '<div class="ecPassos">1. Toque no botão <b>Compartilhar</b> (quadradinho com seta ⬆️).<br>2. Toque em <b>Adicionar à Tela de Início</b>.<br>3. Toque em <b>Adicionar</b>.</div>'+
            '<div class="ecBts"><button class="ecNao" id="ecAgoraNao">Entendi</button></div>';
  } else {
    html += '<div class="ecPassos">1. Toque nos <b>três pontinhos ⋮</b> no canto de cima do Chrome.<br>'+
            '2. Toque em <b>Instalar app</b> (ou <b>Adicionar à tela inicial</b>).<br>3. Confirme em <b>Instalar</b>.</div>'+
            '<div class="ecBts"><button class="ecNao" id="ecAgoraNao">Entendi</button></div>';
  }
  html += '</div>';
  ov.innerHTML = html;
  var bi = document.getElementById('ecInstalar');
  if(bi) bi.onclick = instalarAgora;
  document.getElementById('ecAgoraNao').onclick = fecharConvite;
  ov.onclick = function(e){ if(e.target === ov) fecharConvite(); };
  I.aberto = true;
}
function instalarAgora(){
  var ev = I.evento;
  if(!ev){ montarConvite(); return; }
  I.evento = null;
  try{
    var p = ev.prompt();
    Promise.resolve(p).then(function(){ return ev.userChoice; }).then(function(r){
      if(r && r.outcome === 'accepted') grava(CHAVE_INST,'1');
      fecharConvite();
    }, function(){ fecharConvite(); });
  }catch(e){ fecharConvite(); }
}
function fecharConvite(){
  var ov = document.getElementById('escolaConvite');
  if(ov && ov.parentNode) ov.parentNode.removeChild(ov);
  I.aberto = false;
  grava('escola_conviteVisto', String(Date.now()));
}
/* depois de "Agora não", só oferece de novo quando abrir o app outra vez
   (passados 10 minutos) — para não atrapalhar quem está usando agora */
function vistoAgoraHaPouco(){
  var t = +(ler('escola_conviteVisto')||0);
  return t && (Date.now() - t) < 10*60*1000;
}
function deveConvidar(){
  if(!OPT.convite || instaladoAberto()) return false;
  if(I.evento) return true;                         /* o Chrome confirmou: ainda NÃO está instalado */
  if(ler(CHAVE_INST) === '1') return false;         /* já foi instalado neste celular */
  return true;
}
function mostrarConvite(forcar){
  if(!document.body) return;
  if(!forcar && (I.aberto || vistoAgoraHaPouco() || !deveConvidar())) return;
  if(forcar && instaladoAberto()) return;
  montarConvite();
}

window.addEventListener('beforeinstallprompt', function(e){
  e.preventDefault();                  /* nós mostramos o nosso convite, em português */
  I.evento = e;
  try{ window.localStorage.removeItem(CHAVE_INST); }catch(er){}
  if(I.aberto) montarConvite();        /* troca as instruções pelo botão "Instalar agora" */
  else if(iniciado) mostrarConvite(false);
});
window.addEventListener('appinstalled', function(){
  grava(CHAVE_INST,'1'); I.evento = null; fecharConvite();
});

/* =====================================================================
   INÍCIO
   ===================================================================== */
function estado(){
  var t = estadoTela();
  return { telaAcesa:t, modoApp:modoApp(), instalado: instaladoAberto() || ler(CHAVE_INST)==='1',
           podeInstalar: !!I.evento, telaCheia: emTelaCheiaDoNavegador() || modoApp()==='fullscreen' };
}

window.EscolaPWA = {
  versao: VERSAO,
  BICHINHOS: BICHINHOS.map(function(b){ return { e:b.e, nome:b.nome }; }),
  iniciar: function(opt){
    if(iniciado) return;
    opt = opt || {};
    for(var k in opt) if(opt[k] !== undefined) OPT[k] = opt[k];
    iniciado = true;
    T.ligada = ler(OPT.chaveTelaAcesa) !== '0';
    if(instaladoAberto()) grava(CHAVE_INST,'1');

    document.addEventListener('visibilitychange', function(){
      if(visivel()) pedirTelaAcesa(); else pararVideo();
    });
    window.addEventListener('pageshow', pedirTelaAcesa);
    window.addEventListener('focus', pedirTelaAcesa);
    document.addEventListener('fullscreenchange', pedirTelaAcesa);
    document.addEventListener('pointerdown', function(){ pedirTelaAcesa(); }, { capture:true, passive:true });
    window.addEventListener('click', aoTocar);                  /* borbulha: depois do botão */
    window.addEventListener('touchend', function(ev){ pedirTelaAcesa(); }, { passive:true });
    setInterval(function(){ if(T.ligada && visivel()) pedirTelaAcesa(); }, 15000);   /* vigia */

    var comecar = function(){
      pedirTelaAcesa();
      setTimeout(function(){ mostrarConvite(false); }, OPT.conviteDepoisMs);
    };
    if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', comecar);
    else comecar();
  },
  aoMudar: function(f){ ouvintes.push(f); },
  estado: estado,
  telaAcesa: { pedir: pedirTelaAcesa, alternar: alternarTelaAcesa, estado: estadoTela },
  telaCheia: pedirTelaCheia,
  mostrarConvite: function(){ mostrarConvite(true); },
  fecharConvite: fecharConvite
};
})();
