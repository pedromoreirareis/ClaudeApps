/* =====================================================================
   nuvem-sync.js — Escola São Pedro
   Guarda o progresso das crianças no Firebase (Firestore), sem depender
   de internet para funcionar:

   • O celular continua sendo o "dono" dos dados (localStorage). Tudo é
     gravado primeiro no aparelho, na hora, como sempre foi.
   • Cada alteração vira uma "pendência" guardada no próprio aparelho.
     Quando tem internet, as pendências são enviadas sozinhas para a nuvem.
     Sem internet, elas esperam (pré-sincronização) e vão depois.
   • Se os dados do navegador forem apagados, o progresso pode ser
     recuperado da nuvem pelo NOME + BICHINHO da criança.

   É o MESMO arquivo para todos os aplicativos da Escola São Pedro.
   Não precisa editar nada aqui — a configuração fica em nuvem-config.js.

   Versão 2 — usa só a API REST do Firebase (não baixa biblioteca nenhuma).
   Cada envio é "conferido": antes de gravar, lê o que está na nuvem,
   junta o que veio de outro celular e grava com trava de versão
   (se alguém gravou no meio do caminho, junta de novo e tenta outra vez).
   Versão 3 — HISTÓRICO DE VERSÕES: a cada envio, guarda também uma cópia
   do dia em .../apps/{app}/versoes/{AAAA-MM-DD} (uma por dia, para sempre).
   Dá para listar e JUNTAR uma versão antiga (nunca apaga nada).
   Envio mais rápido (1,5 s depois da mudança) e pedido de armazenamento
   persistente ao navegador (o Android não apaga os dados sozinho).
   ===================================================================== */
(function(){
'use strict';

var VERSAO = '3';
var LS = window.localStorage;
var _setItem = Storage.prototype.setItem;
var _removeItem = Storage.prototype.removeItem;

var S = {
  cfg: null,          /* { apiKey, projectId, familia? } */
  opt: null,          /* o que o aplicativo informou em iniciar() */
  estado: 'desligada',/* desligada | sem-codigo | offline | pendente | enviando | ok | erro */
  detalhe: '',
  ultimoOk: 0,
  enviando: null,
  repetir: false,
  timer: null,
  ultimaChecagem: 0,
  suprimir: 0,
  ouvintes: []
};

/* ---------- utilidades ---------- */
function ler(k){ try{ return LS.getItem(k); }catch(e){ return null; } }
function gravaInterno(k,v){ try{ _setItem.call(LS,k,v); }catch(e){} }
function apagaInterno(k){ try{ _removeItem.call(LS,k); }catch(e){} }
function J(s,d){ try{ var v=JSON.parse(s); return (v===null||v===undefined)?d:v; }catch(e){ return d; } }
function enc(s){ return encodeURIComponent(s); }
function semAcento(s){
  return (s||'').toString().normalize('NFD').replace(/[̀-ͯ]/g,'');
}
function normalizaFamilia(s){
  return semAcento(s).toLowerCase().trim().replace(/\s+/g,'-').replace(/[^a-z0-9-]/g,'').slice(0,40);
}
/* nome + bichinho viram um "código de leitor" só com letras simples:
   "Renata" + 🦋  →  renata_1f98b                                        */
function chaveUsuario(nome, av){
  var n = semAcento(nome).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'') || 'leitor';
  var e = Array.from(av||'').map(function(c){ return c.codePointAt(0).toString(16); })
            .filter(function(h){ return h!=='fe0f' && h!=='200d'; }).join('-') || 'x';
  return n+'_'+e;
}
function dispositivo(){
  var d = ler('nuvem_dispositivo');
  if(!d){ d = 'd'+Date.now().toString(36)+Math.random().toString(36).slice(2,8); gravaInterno('nuvem_dispositivo',d); }
  return d;
}
function familia(){
  return normalizaFamilia((S.cfg && S.cfg.familia) || ler('nuvem_familia') || '');
}
function app(){ return S.opt.app; }
function kPend(){ return 'nuvem_'+app()+'_pendentes'; }
function kMeta(){ return 'nuvem_'+app()+'_meta'; }
function lerPend(){ return J(ler(kPend()),{}); }
function gravaPend(p){ gravaInterno(kPend(), JSON.stringify(p)); }
function lerMeta(){ return J(ler(kMeta()),{}); }
function gravaMeta(m){ gravaInterno(kMeta(), JSON.stringify(m)); }

function configurada(){ return !!(S.cfg && S.cfg.apiKey && S.cfg.projectId); }
function pronta(){ return configurada() && familia().length>=6 && !!S.opt; }

function setEstado(e, det){
  S.estado = e; S.detalhe = det||'';
  S.ouvintes.forEach(function(f){ try{ f(status()); }catch(er){} });
}
function status(){
  var pend = S.opt ? Object.keys(lerPend()).length : 0;
  return { estado:S.estado, detalhe:S.detalhe, pendentes:pend, ultimoOk:S.ultimoOk,
           avisoVersoes:S.avisoVersoes||'', persistente:S.persistente,
           configurada:configurada(), familia:familia(), temFamiliaNoArquivo:!!(S.cfg&&S.cfg.familia) };
}

/* traduz os erros do Firebase para português simples */
function traduz(e){
  var m = ((e && e.message)||'')+' '+((e && e.codigo)||'');
  if(/OPERATION_NOT_ALLOWED|ADMIN_ONLY_OPERATION/.test(m)) return 'O login "Anônimo" não está ativado no Firebase (Etapa 4 do guia).';
  if(/API key not valid|API_KEY_INVALID|INVALID_API_KEY/i.test(m)) return 'A chave (apiKey) do nuvem-config.js está errada.';
  if(/PERMISSION_DENIED|Missing or insufficient permissions/i.test(m)) return 'As Regras do Firestore estão bloqueando (Etapa 6 do guia).';
  if(e && e.status===404) return 'O banco Firestore não foi encontrado — confira o projectId e a Etapa 5 do guia.';
  if(/Failed to fetch|NetworkError|Load failed/i.test(m)) return 'Sem conexão com a internet.';
  return m || 'Erro desconhecido';
}

/* ---------- conversa com o Firebase (REST) ---------- */
function pedeJson(url, o){
  return fetch(url, o).then(function(r){
    return r.text().then(function(t){
      var j = null; try{ j = t ? JSON.parse(t) : null; }catch(er){}
      if(!r.ok){
        var err = new Error((j && j.error && (j.error.message || j.error.status)) || ('HTTP '+r.status));
        err.status = r.status; err.codigo = (j && j.error && j.error.status) || ''; throw err;
      }
      return j;
    });
  });
}
function salvaAuth(idToken, refreshToken, expira){
  gravaInterno('nuvem_auth', JSON.stringify({ idToken:idToken, refreshToken:refreshToken,
    exp: Date.now() + (+expira||3600)*1000 }));
}
function novoLogin(){
  return pedeJson('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key='+enc(S.cfg.apiKey), {
    method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({returnSecureToken:true})
  }).then(function(j){ salvaAuth(j.idToken, j.refreshToken, j.expiresIn); return j.idToken; });
}
function token(){
  var a = J(ler('nuvem_auth'), null);
  if(a && a.idToken && a.exp - Date.now() > 120000) return Promise.resolve(a.idToken);
  if(a && a.refreshToken){
    return pedeJson('https://securetoken.googleapis.com/v1/token?key='+enc(S.cfg.apiKey), {
      method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'},
      body:'grant_type=refresh_token&refresh_token='+enc(a.refreshToken)
    }).then(function(j){ salvaAuth(j.id_token, j.refresh_token, j.expires_in); return j.id_token; },
      function(e){ if(e.status===400||e.status===401||e.status===403){ apagaInterno('nuvem_auth'); return novoLogin(); } throw e; });
  }
  return novoLogin();
}
function base(){
  return 'https://firestore.googleapis.com/v1/projects/'+enc(S.cfg.projectId)+'/databases/(default)/documents/';
}
function pastaUsuarios(){ return 'familias/'+familia()+'/usuarios'; }
function docApp(uk){ return pastaUsuarios()+'/'+uk+'/apps/'+app(); }
function req(metodo, caminho, corpo, qs, keepalive){
  return token().then(function(tk){
    var o = { method:metodo, headers:{ 'Authorization':'Bearer '+tk } };
    if(corpo){ o.headers['Content-Type']='application/json'; o.body = JSON.stringify(corpo); }
    if(keepalive && o.body && o.body.length < 60000) o.keepalive = true;
    return pedeJson(base()+caminho+(qs||''), o);
  });
}
function txt(v){ return { stringValue: String(v==null?'':v) }; }
function num(v){ return { integerValue: String(Math.round(+v||0)) }; }
function lerCampo(f, nome){
  if(!f || !f[nome]) return undefined;
  var c = f[nome];
  if('stringValue' in c) return c.stringValue;
  if('integerValue' in c) return +c.integerValue;
  if('mapValue' in c){ var o={}, ff=(c.mapValue.fields||{}); for(var k in ff) o[k]=lerCampo(ff,k); return o; }
  return undefined;
}

/* ---------- pendências (pré-sincronização offline) ---------- */
function marcarPendente(id){
  if(!id) return;
  var p = lerPend(); p[id] = Date.now(); gravaPend(p);
  agendar(1500);
}
function agendar(ms){
  if(!pronta()) return;
  clearTimeout(S.timer);
  S.timer = setTimeout(function(){ sincronizar(); }, ms||1500);
}

/* toda gravação do aplicativo passa por aqui: se for dado de um leitor,
   vira pendência. Assim o aplicativo não precisa mudar o jeito de salvar. */
function vigiarGravacoes(){
  Storage.prototype.setItem = function(k, v){
    _setItem.call(this, k, v);
    if(this === LS && !S.suprimir && S.opt){ try{ var id = S.opt.idDaChave(k); if(id) marcarPendente(id); }catch(e){} }
  };
  Storage.prototype.removeItem = function(k){
    _removeItem.call(this, k);
    if(this === LS && !S.suprimir && S.opt){ try{ var id = S.opt.idDaChave(k); if(id) marcarPendente(id); }catch(e){} }
  };
}

/* ---------- enviar ---------- */
function hojeTxt(){
  var d = new Date();
  return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
}
function enviarUsuario(u, keepalive, condicao){
  var uk = chaveUsuario(u.nome, u.av);
  var agora = Date.now();
  var dados = S.opt.exportar(u.id) || {};
  var corpo = { fields: {
    nome: txt(u.nome), av: txt(u.av), app: txt(app()),
    dados: txt(JSON.stringify(dados)),
    atualizadoEm: num(agora), dispositivo: txt(dispositivo()), versao: txt(VERSAO)
  }};
  var gravado = '';
  var dia = hojeTxt();
  return req('PATCH', docApp(uk), corpo, condicao||'', keepalive).then(function(r){
    gravado = (r && r.updateTime) || '';
    var apps = { mapValue:{ fields:{} } }; apps.mapValue.fields[app()] = num(agora);
    return req('PATCH', pastaUsuarios()+'/'+uk,
      { fields:{ nome:txt(u.nome), av:txt(u.av), apps:apps } },
      '?updateMask.fieldPaths=nome&updateMask.fieldPaths=av&updateMask.fieldPaths=apps.'+app(), keepalive);
  }).then(function(){
    /* HISTÓRICO: cópia do dia (sobrescreve só a do mesmo dia). Se falhar
       (ex.: regras antigas sem "versoes"), o envio principal continua valendo. */
    return req('PATCH', docApp(uk)+'/versoes/'+dia, corpo, '', keepalive)
      .then(function(){ S.avisoVersoes = ''; },
            function(e){ S.avisoVersoes = 'Histórico de versões não gravou: '+traduz(e); });
  }).then(function(){
    var m = lerMeta(); m[u.id] = m[u.id]||{};
    m[u.id].enviadoEm = agora; m[u.id].chave = uk;
    if(gravado) m[u.id].vistoUpdate = gravado;      /* versão da nuvem que é nossa */
    gravaMeta(m);
  });
}

function sincronizar(opc){
  opc = opc||{};
  if(!configurada()){ setEstado('desligada'); return Promise.resolve(false); }
  if(familia().length<6){ setEstado('sem-codigo'); return Promise.resolve(false); }
  if(!S.opt) return Promise.resolve(false);
  if(navigator.onLine === false){ setEstado('offline'); return Promise.resolve(false); }
  /* já tem um envio andando: espera ele acabar e faz mais um, para que
     quem pediu receba a resposta já com a última alteração incluída */
  if(S.enviando){ S.repetir = true; return S.enviando.then(function(){ return sincronizar(opc); }); }

  var feito = (opc.checarNuvem || Date.now()-S.ultimaChecagem > 5*60*1000)
    ? checarNuvem() : Promise.resolve();

  S.enviando = feito.then(function(){
    var p = lerPend(); var ids = Object.keys(p);
    var us = S.opt.usuarios() || [];
    if(!ids.length){ S.ultimoOk = Date.now(); setEstado('ok'); return true; }
    setEstado('enviando');
    var cadeia = Promise.resolve();
    ids.forEach(function(id){
      cadeia = cadeia.then(function(){
        var marca = p[id];
        var u = us.filter(function(x){ return x.id===id; })[0];
        var tira = function(){ var p2 = lerPend(); if(p2[id]===marca){ delete p2[id]; gravaPend(p2); } };
        if(!u){ tira(); return; }            /* leitor apagado neste aparelho: nada a enviar */
        return enviarComSeguranca(u, opc.keepalive).then(tira);
      });
    });
    return cadeia.then(function(){ S.ultimoOk = Date.now(); setEstado('ok'); return true; });
  }).catch(function(e){
    var msg = traduz(e);
    if(navigator.onLine === false || /Sem conex/.test(msg)) setEstado('offline');
    else setEstado('erro', msg);
    clearTimeout(S.timer); S.timer = setTimeout(function(){ sincronizar(); }, 60000);
    return false;
  }).then(function(r){
    S.enviando = null;
    if(S.repetir){ S.repetir=false; agendar(1500); }
    return r;
  });
  return S.enviando;
}

/* ---------- receber (progresso feito em OUTRO aparelho) ---------- */
/* ENVIO SEGURO de um leitor:
   1) lê o que está na nuvem agora;
   2) se veio de OUTRO celular e é novidade, junta com o deste celular
      (nada lido se perde);
   3) grava com "trava de versão": se outro celular gravou entre o passo 1
      e o 3, a nuvem recusa, e começamos de novo (até 3 vezes).
   Assim um envio NUNCA apaga o que outro celular guardou. */
function conflito(e){
  return !!e && (e.status===409 || /FAILED_PRECONDITION|ALREADY_EXISTS|ABORTED/.test((e.codigo||'')+' '+(e.message||'')));
}
function enviarComSeguranca(u, keepalive, tentativa){
  tentativa = tentativa||0;
  var uk = chaveUsuario(u.nome, u.av);
  return baixarDoc(uk).then(function(doc){
    /* veio de outro celular? junta SEMPRE antes de gravar (juntar é
       seguro: só acrescenta). Não depende do relógio dos celulares. */
    if(doc && doc.dispositivo !== dispositivo()) aplicar(u.id, doc.dados, false);
    var m = lerMeta(); m[u.id] = m[u.id]||{};
    m[u.id].conferido = uk;
    if(doc && doc.updateTime) m[u.id].vistoUpdate = doc.updateTime;
    gravaMeta(m);
    var condicao = !doc ? '?currentDocument.exists=false'
                 : (doc.updateTime ? '?currentDocument.updateTime='+enc(doc.updateTime) : '');
    return enviarUsuario(u, keepalive, condicao);
  }).catch(function(e){
    if(tentativa < 3 && conflito(e)) return enviarComSeguranca(u, keepalive, tentativa+1);
    throw e;
  });
}
function checarNuvem(){
  S.ultimaChecagem = Date.now();
  var us = S.opt.usuarios() || [];
  var cadeia = Promise.resolve();
  us.forEach(function(u){
    cadeia = cadeia.then(function(){
      return baixarDoc(chaveUsuario(u.nome,u.av)).then(function(doc){
        var uk = chaveUsuario(u.nome,u.av);
        var m = lerMeta(); m[u.id] = m[u.id]||{};
        if(!doc){ marcarPendente(u.id); return; }       /* ainda não está na nuvem: sobe tudo */
        /* outro celular gravou algo que ainda não juntamos? */
        if(doc.dispositivo !== dispositivo() && (m[u.id].conferido !== uk || doc.updateTime !== m[u.id].vistoUpdate)){
          aplicar(u.id, doc.dados, false);
          m = lerMeta(); m[u.id] = m[u.id]||{};
          m[u.id].conferido = uk; m[u.id].vistoUpdate = doc.updateTime; gravaMeta(m);
          marcarPendente(u.id);             /* devolve à nuvem o resultado já juntado */
        }
      });
    });
  });
  return cadeia;
}
function baixarDoc(uk){
  return req('GET', docApp(uk)).then(function(d){
    if(!d || !d.fields) return null;
    return { dados: J(lerCampo(d.fields,'dados'), {}), atualizadoEm: lerCampo(d.fields,'atualizadoEm')||0,
             dispositivo: lerCampo(d.fields,'dispositivo')||'', updateTime: d.updateTime||'' };
  }, function(e){ if(e.status===404) return null; throw e; });
}
function aplicar(id, dados, restaurando){
  S.suprimir++;
  try{ S.opt.mesclar(id, dados||{}, !!restaurando); }catch(e){}
  finally{ S.suprimir--; }
}

/* ---------- API pública ---------- */
window.NuvemSync = {
  versao: VERSAO,
  chaveUsuario: chaveUsuario,

  /* opt = { app, usuarios(), idDaChave(k), exportar(id), mesclar(id,dados,restaurando) } */
  iniciar: function(opt){
    S.opt = opt;
    S.cfg = window.NUVEM_CONFIG || null;
    if(S.cfg && !S.cfg.apiKey) S.cfg = null;
    vigiarGravacoes();
    /* pede ao navegador para NÃO apagar os dados sozinho quando faltar espaço */
    try{
      if(navigator.storage && navigator.storage.persist){
        navigator.storage.persisted().then(function(ja){
          if(ja){ S.persistente = true; return; }
          return navigator.storage.persist().then(function(ok){ S.persistente = !!ok; });
        }).catch(function(){});
      }
    }catch(e){}
    window.addEventListener('online', function(){ sincronizar({checarNuvem:true}); });
    window.addEventListener('offline', function(){ if(configurada()) setEstado('offline'); });
    document.addEventListener('visibilitychange', function(){
      if(!pronta()) return;
      if(document.visibilityState==='hidden'){
        if(Object.keys(lerPend()).length) sincronizar({keepalive:true});
      } else {
        agendar(1500);
      }
    });
    setInterval(function(){ if(pronta() && Object.keys(lerPend()).length) sincronizar(); }, 60000);
    if(!configurada()) setEstado('desligada');
    else if(familia().length<6) setEstado('sem-codigo');
    else { setEstado(navigator.onLine===false?'offline':'pendente'); setTimeout(function(){ sincronizar({checarNuvem:true}); }, 2500); }
  },
  configurada: configurada,
  pronta: pronta,
  status: status,
  aoMudar: function(f){ S.ouvintes.push(f); },
  sincronizar: function(){ return sincronizar({checarNuvem:true}); },
  marcarPendente: marcarPendente,

  definirFamilia: function(codigo){
    var c = normalizaFamilia(codigo);
    if(c.length < 6) return false;
    gravaInterno('nuvem_familia', c);
    setEstado('pendente');
    /* tudo que já existe neste aparelho sobe para a nuvem */
    (S.opt.usuarios()||[]).forEach(function(u){ marcarPendente(u.id); });
    sincronizar({checarNuvem:true});
    return c;
  },

  /* lista os leitores que existem na nuvem desta família (de qualquer aplicativo) */
  listarUsuarios: function(){
    if(!pronta()) return Promise.reject(new Error(configurada()?'Falta o código da família.':'A nuvem não está configurada.'));
    return req('GET', pastaUsuarios(), null, '?pageSize=300').then(function(r){
      return ((r && r.documents) || []).map(function(d){
        var apps = lerCampo(d.fields,'apps') || {};
        return { chave: d.name.split('/').pop(), nome: lerCampo(d.fields,'nome')||'?', av: lerCampo(d.fields,'av')||'🙂',
                 temAqui: !!apps[app()], apps: apps };
      });
    }).catch(function(e){ throw new Error(traduz(e)); });
  },

  /* HISTÓRICO DE VERSÕES: lista as cópias diárias de um leitor neste app */
  listarVersoes: function(nome, av){
    if(!pronta()) return Promise.reject(new Error('A nuvem não está pronta.'));
    return req('GET', docApp(chaveUsuario(nome, av))+'/versoes', null, '?pageSize=1000').then(function(r){
      return ((r && r.documents) || []).map(function(d){
        var dados = J(lerCampo(d.fields,'dados'), {});
        return { dia: d.name.split('/').pop(), atualizadoEm: lerCampo(d.fields,'atualizadoEm')||0, dados: dados };
      }).sort(function(a,b){ return a.dia < b.dia ? 1 : -1; });
    }).catch(function(e){ throw new Error(traduz(e)); });
  },
  /* JUNTA uma versão antiga com o progresso atual (nunca apaga nada) */
  juntarVersao: function(id, nome, av, dia){
    if(!pronta()) return Promise.resolve(false);
    return req('GET', docApp(chaveUsuario(nome, av))+'/versoes/'+dia).then(function(d){
      if(!d || !d.fields) return false;
      aplicar(id, J(lerCampo(d.fields,'dados'), {}), false);
      marcarPendente(id);
      return true;
    }, function(e){ if(e.status===404) return false; throw new Error(traduz(e)); });
  },

  /* traz o progresso de um leitor da nuvem e mistura com o deste aparelho.
     restaurando=true: preferências (cores, letra, onde parou) vêm da nuvem. */
  recuperar: function(id, nome, av, restaurando){
    if(!pronta()) return Promise.resolve(false);
    return baixarDoc(chaveUsuario(nome, av)).then(function(doc){
      if(!doc) return false;
      aplicar(id, doc.dados, restaurando!==false);
      var m = lerMeta(); m[id] = m[id]||{}; m[id].vistoUpdate = doc.updateTime; m[id].conferido = chaveUsuario(nome, av); gravaMeta(m);
      marcarPendente(id);
      return true;
    }).catch(function(e){ throw new Error(traduz(e)); });
  }
};
})();
