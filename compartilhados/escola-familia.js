/* =====================================================================
   escola-familia.js — Escola São Pedro · versão 1.2 (07/10/2026)
   O CADASTRO DA FAMÍLIA E DAS CRIANÇAS, IGUAL NOS 7 APPS
   (PLANO_CADASTRO_FAMILIA.md, aprovado em 06/10/2026)

   É o MESMO arquivo para todos os aplicativos, como o nuvem-sync.js e o
   escola-pwa.js. Não edite aqui dentro de um app só: quem mudar sobe a
   versão e leva a cópia nova para os outros apps.

   O que este arquivo faz:
   • as telas T1 a T8 (boas-vindas, código da família, criar código,
     "Quem vai estudar hoje?", nova criança, buscar na nuvem, arrumar,
     famílias neste celular) e as cópias de cada dia;
   • o chip da criança na barra de cima e a bolinha 🟢🟡🔴 na ⚙️;
   • a seção "☁️ Família e nuvem" no fim das Configurações;
   • a migração (só ACRESCENTA a chave escola_familia; nada antigo é
     apagado ou renomeado) e as regras de segurança (tirar uma criança só
     com tudo guardado na nuvem ou com uma cópia na lixeira do celular);
   • a trava do adulto (segurar o botão por 3 segundos).

   Cada app "liga" este arquivo ao seu jeito de guardar o progresso com
   EscolaFamilia.iniciar({ app, criancas:{ listar, atual, criar, mudar,
   exportar, importar, tirar, completoNaNuvem, entrar, resumo,
   chavesDaCrianca }, ... }) — veja a parte 5.2 do plano.
   Opcionais (1.2): abrirConfig(aoFechar) — abre as Configurações do app
   (o módulo mostra uma ⚙️ na "Quem vai estudar hoje?" e fica escondido
   até o app chamar aoFechar()); fecharConfig() — fecha as Configurações
   quando o adulto toca, lá dentro, numa opção que abre tela do módulo.

   Precisa do nuvem-sync.js v4 ou mais nova (4.1 desde 07/10/2026);
   funciona sem ele, só que sem nuvem.
   Nunca usa alert/confirm/prompt do navegador nem sessionStorage.
   ===================================================================== */
(function(){
'use strict';

var VERSAO = '1.2';   /* 1.2 (07/10/2026): ⚙️ na "Quem vai estudar hoje?" e bolinha 🟡 com criança guardada só na lixeira deste celular */
/* 1.1 (07/10/2026): só desenho — respiro e largura deitado (pedido do Pedro após o teste da v122) */
var LSo = window.localStorage;
/* funções originais do navegador: as chaves escola_* nunca passam pelo
   prefixo de criança do app nem pela vigia da nuvem */
var _get = Storage.prototype.getItem, _set = Storage.prototype.setItem, _rem = Storage.prototype.removeItem;
function lget(k){ try{ return _get.call(LSo,k); }catch(e){ return null; } }
function lset(k,v){ _set.call(LSo, k, String(v)); }          /* pode dar erro (memória cheia): quem chama trata */
function lrem(k){ try{ _rem.call(LSo,k); }catch(e){} }
function J(s,d){ try{ var v=JSON.parse(s); return (v===null||v===undefined)?d:v; }catch(e){ return d; } }

var DIA = 86400000;
var BLOQUEIO_DIAS = 14;          /* 2 semanas: 2ª família e tirar a última criança */
var MAX_FAMILIAS = 4;
var HOLD_MS = 3000;              /* trava do adulto (D15) */
var CHAVE = 'escola_familia';

var ICONES_APPS = { alfabetizacao:'📚', matematica:'🔢', fluencia:'📖', corujaexplica:'🦉',
                    provinha:'📝', historinhas:'📕', curiosidades:'🌍' };
var BICHINHOS_RESERVA = [
  {e:'🦉',nome:'Coruja'},{e:'🦊',nome:'Raposa'},{e:'🐰',nome:'Coelho'},{e:'🐼',nome:'Panda'},
  {e:'🦋',nome:'Borboleta'},{e:'🐨',nome:'Coala'},{e:'🐯',nome:'Tigre'},{e:'🐴',nome:'Pônei'}];
function bichinhos(){
  var b = window.EscolaPWA && window.EscolaPWA.BICHINHOS;
  return (b && b.length===8) ? b : BICHINHOS_RESERVA;
}
function nomeBicho(e){ var b = bichinhos().filter(function(x){ return x.e===e; })[0]; return b ? b.nome : ''; }
function oficial(e){ return bichinhos().some(function(x){ return x.e===e; }); }

/* ===================== TEXTOS (tabela 3-A do plano) =====================
   Todos os textos das telas moram aqui. A tela mostra em CAIXA ALTA pelo
   CSS (o que a criança digita é guardado como foi digitado). */
var T = {
  t1Titulo:'🦉 OLÁ! VAMOS COMEÇAR?',
  t1Ja:'🔑 JÁ TENHO CADASTRO', t1JaSub:'tenho o código da família',
  t1Novo:'🌱 SOU NOVO POR AQUI', t1NovoSub:'criar o código da família',
  t1AgoraNao:'AGORA NÃO ›',
  t1JaTem:'ESTE CELULAR JÁ TEM: {lista} — ELAS NÃO VÃO SUMIR.',
  t2Titulo:'🔑 CÓDIGO DA FAMÍLIA',
  t2Texto:'É O MESMO CÓDIGO EM TODOS OS APPS E EM TODOS OS CELULARES DA FAMÍLIA.',
  t2Exemplo:'ex.: panda-4827',
  t2Botao:'🔑 PROCURAR A FAMÍLIA',
  t2CasoB:'AS CRIANÇAS QUE JÁ ESTÃO NESTE CELULAR ({lista}) VÃO FICAR NESTA FAMÍLIA.',
  t2Procurando:'⏳ PROCURANDO A FAMÍLIA…',
  t2Achei:'🎉 ACHEI A SUA FAMÍLIA!',
  t2TrazerTodas:'TRAZER TODAS', t2Escolher:'ESCOLHER', t2OutroCodigo:'← OUTRO CÓDIGO', abrir:'ABRIR ▶',
  t2NaoAchei:'🤔 NÃO ACHEI NENHUMA CRIANÇA COM ESSE CÓDIGO.',
  t2NaoAcheiDica:'Confira letra por letra (o tracinho conta). Se é a primeira vez da família, toque em 🌱 Sou novo por aqui.',
  t2QuisDizer:'VOCÊ QUIS DIZER {c}?',
  t2JaNoCelular:'ESSA FAMÍLIA JÁ ESTÁ NESTE CELULAR.',
  semInternet:'📴 SEM INTERNET AGORA.',
  guardarDepois:'GUARDAR E CONFERIR DEPOIS', tentarDeNovo:'TENTAR DE NOVO',
  codigoCurto:'O CÓDIGO PRECISA TER PELO MENOS 6 LETRAS OU NÚMEROS 🙂',
  codigoTeste:'NO SITE DE TESTE, USE SÓ UM CÓDIGO QUE TENHA A PALAVRA "TESTE" (EX.: TESTE-PEDRO-2026).',
  t3Titulo:'🌱 CRIAR O CÓDIGO DA FAMÍLIA',
  t3Texto:'O app sugeriu um código. Pode usar ou escrever outro (6 letras ou números ou mais).',
  t3Botao:'✅ CRIAR A FAMÍLIA',
  t3JaExiste:'ESSE CÓDIGO JÁ TEM CRIANÇAS. SE É DA SUA FAMÍLIA, USE 🔑 JÁ TENHO CADASTRO. SE NÃO É, ESCOLHA OUTRO.',
  t3Anote:'📝 ANOTE NUM PAPEL', t3AnoteTexto:'É com ele que os outros celulares e os outros apps encontram as crianças.',
  t3JaAnotei:'✅ JÁ ANOTEI',
  cancelar:'✕ CANCELAR', voltar:'← VOLTAR',
  t4Titulo:'🦉 QUEM VAI ESTUDAR HOJE?',
  t4Nova:'➕ NOVA CRIANÇA', t4Buscar:'☁️ BUSCAR NA NUVEM', t4Atualizar:'🔄 ATUALIZAR AGORA', t4Arrumar:'✏️ ARRUMAR',
  t4Trazer:'TOQUE PARA TRAZER',
  t4Familia:'🔑 FAMÍLIA {c}', t4SemFamilia:'🔑 SEM CÓDIGO DA FAMÍLIA — TOQUE AQUI',
  t4Atualizando:'⏳ ATUALIZANDO…', t4Trazendo:'☁️ TRAZENDO {nome}…',
  t4TudoCerto:'🔑 FAMÍLIA {c} — TUDO CERTO ✅',
  t5Titulo:'🌟 QUAL É O SEU NOME?', t5Campo:'DIGITE O SEU NOME', t5Escolha:'ESCOLHA O SEU BICHINHO:',
  t5Escolheu:'VOCÊ ESCOLHEU: {e} {nome}', t5Pronto:'PRONTO! ✅',
  t5Mudar:'✏️ MUDAR NOME OU BICHINHO',
  t5BichoAntigo:'O BICHINHO {e} MUDOU: ESCOLHA UM DOS 8 NOVOS 🙂',
  t5SemNome:'ESCREVA O SEU NOME PRIMEIRO 🙂', t5SemBicho:'ESCOLHA O SEU BICHINHO 🙂', t5EnterSemBicho:'AGORA ESCOLHA O SEU BICHINHO 🙂',
  t5JaAqui:'{e} {nome} JÁ ESTÁ NESTE CELULAR — ABRINDO!',
  t5JaExisteAqui:'{e} {nome} JÁ EXISTE NESTE CELULAR. ESCOLHA OUTRO NOME OU BICHINHO.',
  t5Maximo:'JÁ SÃO {n} CRIANÇAS NESTA FAMÍLIA — O MÁXIMO.',
  t5EVoce:'JÁ EXISTE {e} {nome} NA FAMÍLIA. É VOCÊ?', t5SouEu:'{e} SOU EU!', t5Outra:'NÃO, SOU OUTRA CRIANÇA',
  t5Agora:'{e} AGORA É {nome} ({bicho})',
  t5JaNaNuvem:'JÁ EXISTE {e} {nome} NA NUVEM DESTA FAMÍLIA. JUNTAR AS DUAS?',
  t5JaNaNuvemTexto:'SE FOR A MESMA CRIANÇA, O PROGRESSO DAS DUAS FICA JUNTO. SE FOR OUTRA CRIANÇA, ESCOLHA OUTRO NOME OU BICHINHO.',
  t5AcheiNuvem:'☁️ {e} ACHEI O PROGRESSO DE {nome} NA NUVEM!',
  t6Titulo:'☁️ BUSCAR NA NUVEM',
  t6JaAqui:'JÁ ESTÁ AQUI — TOQUE PARA JUNTAR', t6Trazer:'TOQUE PARA TRAZER',
  t6Procurar:'🔄 PROCURAR DE NOVO', t6Procurando:'⏳ PROCURANDO AS CRIANÇAS DA FAMÍLIA…',
  t6Nenhuma:'AINDA NÃO TEM NENHUMA CRIANÇA DESTA FAMÍLIA NA NUVEM.',
  t6Explica:'Toque na criança para trazer o progresso dela para este celular. Nada que já está aqui é apagado.',
  t6Lixeira:'🗑️ TIRADAS DESTE CELULAR', t6TrazerDeVolta:'↩️ TRAZER DE VOLTA',
  t6Antigos:'📦 NOMES ANTIGOS', t6AntigoPara:'MUDOU PARA {e} {nome} — TOQUE PARA JUNTAR',
  t6SemFamilia:'PRIMEIRO ENTRE NA FAMÍLIA (🔑 JÁ TENHO CADASTRO).',
  juntando:'☁️ JUNTANDO O PROGRESSO DE {nome}…', juntado:'✅ {e} PROGRESSO DE {nome} JUNTADO!',
  nadaNovo:'{e} {nome}: NADA NOVO NA NUVEM',
  recuperado:'✅ {e} {nome} VOLTOU COM TODO O PROGRESSO!', semLeituras:'{e} {nome} PRONTO! (AINDA SEM PROGRESSO NESTE APP)',
  devolvido:'↩️ {e} {nome} VOLTOU PARA ESTE CELULAR!',
  t7Titulo:'✏️ ARRUMANDO', t7Sub:'toque em ✏️ para mudar, 🗑️ para tirar deste celular',
  t7Terminei:'✅ TERMINEI DE ARRUMAR', t7Tirar:'🗑️ TIRAR DESTE CELULAR',
  t7Pergunta:'TIRAR {e} {nome} DESTE CELULAR?',
  t7PerguntaTexto:'O PROGRESSO DELA CONTINUA GUARDADO NA NUVEM E PODE VOLTAR EM ☁️ BUSCAR NA NUVEM.',
  t7PerguntaSemNuvem:'O PROGRESSO VAI PARA A LIXEIRA DESTE CELULAR E PODE VOLTAR EM ☁️ BUSCAR NA NUVEM › 🗑️ TIRADAS DESTE CELULAR.',
  t7BotaoTirar:'🗑️ TIRAR',
  t7Guardando:'⏳ GUARDANDO NA NUVEM ANTES DE TIRAR…',
  t7NaoGarante:'⚠️ AINDA NÃO DÁ PARA GARANTIR',
  t7NaoGaranteTexto:'O PROGRESSO DE {nome} AINDA NÃO FOI GUARDADO NA NUVEM. CONECTE NA INTERNET E ESPERE A BOLINHA FICAR 🟢.',
  t7Incompleto:'UMA PARTE DO PROGRESSO DE {nome} NÃO CABE NA NUVEM. SÓ DÁ PARA TIRAR GUARDANDO UMA CÓPIA NESTE CELULAR.',
  t7SemNuvem:'ESTE APP ESTÁ SEM NUVEM. SÓ DÁ PARA TIRAR GUARDANDO UMA CÓPIA NESTE CELULAR.',
  t7Copia:'GUARDAR UMA CÓPIA NESTE CELULAR E TIRAR',
  t7Saiu:'🗑️ {e} {nome} SAIU DESTE CELULAR.',
  t7NaoCoube:'❌ A CÓPIA NÃO COUBE NA MEMÓRIA DO CELULAR. NADA FOI TIRADO.',
  t7Ultima:'⏳ AINDA NÃO DÁ PARA TIRAR A ÚLTIMA CRIANÇA',
  t7UltimaTexto:'NAS 2 PRIMEIRAS SEMANAS DESTA VERSÃO (ATÉ {data}), DEIXE PELO MENOS UMA CRIANÇA NESTE CELULAR.',
  t7UltimaDica:'SE PRECISAR, CADASTRE OUTRA CRIANÇA ANTES E DEPOIS TIRE ESTA.',
  avisoVersaoAntiga:'DEPOIS DISSO, VOLTAR À VERSÃO ANTERIOR DO APP NÃO É MAIS SEGURO.',
  liberar:'LIBERAR MESMO ASSIM',
  t7Repetida:'HÁ DUAS {e} {nome}: JUNTAR?', repetidaEspera:'⏳ HÁ DUAS {e} {nome}: JUNTE EM ✏️ ARRUMAR', t7Juntar:'JUNTAR',
  t7Mudou:'{e1} {n1} MUDOU PARA {e2} {n2} EM OUTRO APP. MUDAR AQUI TAMBÉM?', t7MudarSim:'MUDAR', t7AgoraNao:'AGORA NÃO',
  trocar:'👥 TROCAR DE CRIANÇA',
  t8Titulo:'👨‍👩‍👧 FAMÍLIAS NESTE CELULAR',
  t8Mostrar:'👁 MOSTRAR', t8Entrar:'➕ ENTRAR EM OUTRA FAMÍLIA', t8Criar:'🌱 CRIAR OUTRA FAMÍLIA', t8Tirar:'🚪 TIRAR UMA FAMÍLIA',
  t8Esperando:'{n} ESPERANDO', t8AConferir:'A CONFERIR', t8Maximo:'JÁ SÃO {n} FAMÍLIAS NESTE CELULAR — O MÁXIMO.',
  t8TirarQual:'🚪 QUAL FAMÍLIA SAI DESTE CELULAR?', t8TirarPergunta:'TIRAR A FAMÍLIA {c} DESTE CELULAR?',
  t8TirarTexto:'AS CRIANÇAS DELA SAEM DESTE CELULAR. NA NUVEM FICA TUDO GUARDADO.',
  t8TirarNao:'⚠️ NÃO DEU PARA GARANTIR TUDO DE {lista}. NADA FOI TIRADO. CONECTE NA INTERNET E TENTE DE NOVO.',
  t8SoUma:'SÓ DÁ PARA TIRAR UMA FAMÍLIA QUANDO HÁ MAIS DE UMA NESTE CELULAR.',
  t8Bloqueio:'⏳ NAS 2 PRIMEIRAS SEMANAS DESTA VERSÃO (ATÉ {data}) É MELHOR TER SÓ UMA FAMÍLIA NESTE CELULAR.',
  verde:'TUDO GUARDADO NA NUVEM (ÀS {h})', verdeSemHora:'TUDO GUARDADO NA NUVEM',
  guardando:'GUARDANDO…',
  semInternetFila:'📴 SEM INTERNET: {n} {criancas} ESPERANDO. NÃO LIMPE OS DADOS DO NAVEGADOR.',
  faltaCodigo:'FALTA O CÓDIGO DA FAMÍLIA',
  aConferir:'⏳ FAMÍLIA {c} A CONFERIR (PRECISA DE INTERNET)',
  confiraCodigo:'❓ CONFIRA O CÓDIGO DA FAMÍLIA {c}',
  erro:'A NUVEM DEU ERRO: {m}',
  desligada:'NUVEM DESLIGADA (FALTA O ARQUIVO NUVEM-CONFIG.JS)',
  nuvem:'☁️ NUVEM',
  cfgSecao:'☁️ FAMÍLIA E NUVEM', cfgNuvem:'NUVEM: {frase}',
  cfgCriancas:'👧 CRIANÇAS DESTE CELULAR: {lista}', cfgBuscar:'☁️ BUSCAR CRIANÇAS NA NUVEM',
  copias:'🕘 CÓPIAS DE CADA DIA', copiasDe:'🕘 CÓPIAS DE CADA DIA (DE {e} {nome})',
  cfgFamilia:'🔑 FAMÍLIA: {c}', cfgFamilias:'👨‍👩‍👧 FAMÍLIAS ▶',
  copiasProcurando:'⏳ PROCURANDO AS CÓPIAS DE {nome}…',
  copiasExplica:'Uma cópia por dia. Tocar numa cópia JUNTA ela com o progresso de hoje — nada é apagado.',
  copiasNenhuma:'AINDA NÃO TEM CÓPIAS DE {nome} (A PRIMEIRA APARECE DEPOIS DO PRIMEIRO ENVIO).',
  copiasPergunta:'🕘 JUNTAR A CÓPIA DE {data}?', copiasPerguntaTexto:'NADA É APAGADO: SÓ VOLTA O QUE ESTIVER FALTANDO.',
  copiasJuntada:'✅ CÓPIA DE {data} JUNTADA!', copiasNaoAchei:'NÃO ENCONTREI ESSA CÓPIA',
  semCrianca:'PRIMEIRO ESCOLHA UMA CRIANÇA.',
  atualizado:'✅ TUDO GUARDADO NA NUVEM!', atualizadoOffline:'📴 SEM INTERNET — FICA GUARDADO NO CELULAR',
  adulto:'👨 PEÇA PARA UM ADULTO', adultoDica:'👨 PEÇA PARA UM ADULTO SEGURAR O BOTÃO POR 3 SEGUNDOS',
  pergNaoExiste:'NÃO ACHEI A FAMÍLIA {c}. CONFERIR O CÓDIGO OU CRIAR UMA FAMÍLIA NOVA COM ELE?',
  pergConferir:'🔑 CONFERIR O CÓDIGO', pergCriarCom:'🌱 CRIAR COM ELE',
  pergJaExiste:'O CÓDIGO {c} JÁ TEM CRIANÇAS. É DA SUA FAMÍLIA?', pergEMinha:'✅ É DA MINHA FAMÍLIA', pergOutro:'🔑 ESCOLHER OUTRO CÓDIGO',
  erroTxt:'❌ {m}', naoDeu:'NÃO DEU CERTO',
  sim:'SIM', ok:'ENTENDI', juntar:'JUNTAR', telaCheia:'TELA CHEIA', configuracoes:'CONFIGURAÇÕES',
  lixeiraSoAqui:'🗑️ {n} {criancas} TIRADA(S) GUARDADA(S) SÓ NESTE CELULAR: TRAGA DE VOLTA EM ☁️ BUSCAR NA NUVEM',
  siteTeste:'🧪 SITE DE TESTE — USE SÓ O CÓDIGO DE TESTE'
};
function fmt(s, o){ return String(s).replace(/\{(\w+)\}/g, function(_, k){ return (o && o[k]!=null) ? o[k] : ''; }); }

/* ===================== estado ===================== */
var C = null;            /* configuração do app */
var A = null;            /* adaptador do app (criancas) */
var st = null;           /* escola_familia */
var S = { trazendo:{}, nuvemCache:{}, arrumando:false, hist:false, ignorarPop:false, chips:[], pontos:[], secoes:[],
          avisoMigracao:'', recusouMudanca:{}, iniciado:false };
var raiz = null, toastEl = null, toastT = null;
var pilha = [];

function NS(){ return window.NuvemSync || null; }
function nuvemLigada(){ var n = NS(); return !!(n && n.configurada && n.configurada()); }
function nuvemV4(){ var n = NS(); return !!(n && n.existeFamilia && n.garantirGuardado); }
function online(){ return navigator.onLine !== false; }
function norm(c){
  var n = NS(); if(n && n.normalizaFamilia) return n.normalizaFamilia(c);
  return String(c||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().trim().replace(/\s+/g,'-').replace(/[^a-z0-9-]/g,'').slice(0,40);
}
function chaveDe(nome, av){
  var n = NS(); if(n && n.chaveUsuario) return n.chaveUsuario(nome, av);
  var a = String(nome||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'') || 'leitor';
  var e = Array.from(av||'').map(function(c){ return c.codePointAt(0).toString(16); }).filter(function(h){ return h!=='fe0f' && h!=='200d'; }).join('-') || 'x';
  return a+'_'+e;
}
function mascara(c){ return c ? (c.slice(0,3)+'••••') : ''; }
function siteDeTeste(){ return /teste/i.test(location.hostname||''); }   /* ex.: escolasaopedrotestes.netlify.app */
function dataTxt(t){ var d = new Date(t); return String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0'); }

function estadoVazio(){
  return { v:1, familias:[], criancas:{}, atual:'', ultimoNuvemFamilia:'', primeiraAberturaEm:0,
           liberouSegundaFamilia:false, mudancasPendentes:[], recusas:{} };
}
function carregar(){
  var s = J(lget(CHAVE), null);
  if(!s || typeof s!=='object' || s.v!==1) s = estadoVazio();
  var v = estadoVazio();
  for(var k in v) if(!(k in s)) s[k] = v[k];
  if(!Array.isArray(s.familias)) s.familias = [];
  if(!s.criancas || typeof s.criancas!=='object') s.criancas = {};
  if(!Array.isArray(s.mudancasPendentes)) s.mudancasPendentes = [];
  st = s;
}
function salvar(){
  /* nuvem_familia (lido pelo app antigo, se for preciso voltar) só recebe
     família JÁ CONFERIDA: um código não conferido nunca vai para lá */
  var fa = st.atual ? fam(st.atual) : null;
  if(fa && fa.conferida){
    var n = NS();
    if(n && n.definirFamiliaAtual) n.definirFamiliaAtual(st.atual); else { try{ lset('nuvem_familia', st.atual); }catch(e){} }
    st.ultimoNuvemFamilia = st.atual;
  } else {
    st.ultimoNuvemFamilia = norm(lget('nuvem_familia') || '');
  }
  try{ lset(CHAVE, JSON.stringify(st)); }catch(e){}
}
function fam(c){ for(var i=0;i<st.familias.length;i++) if(st.familias[i].c===c) return st.familias[i]; return null; }
function addFamilia(c, conferida, origem){
  var f = fam(c);
  if(!f){ f = { c:c, desde:Date.now(), conferida:!!conferida, origem:origem||'' }; st.familias.push(f); }
  else if(conferida){ f.conferida = true; delete f.problema; }
  if(!st.atual) st.atual = c;
  return f;
}
function familiaDe(id){ return (st && st.criancas[id]) || ''; }
function lista(){ try{ return (A.listar() || []).slice(); }catch(e){ return []; } }
function listaOuNull(){ try{ var l = A.listar(); return Array.isArray(l) ? l.slice() : null; }catch(e){ return null; } }
function local(id){ return lista().filter(function(u){ return u.id===id; })[0] || null; }
function daFamilia(c){ return lista().filter(function(u){ return familiaDe(u.id)===c; }); }
function atualId(){ try{ return A.atual(); }catch(e){ return null; } }
function dentroDoBloqueio(){ return Date.now() < (st.primeiraAberturaEm||0) + BLOQUEIO_DIAS*DIA; }
function fimDoBloqueio(){ return dataTxt((st.primeiraAberturaEm||Date.now()) + BLOQUEIO_DIAS*DIA); }
function max(){ return (C && C.maxPorFamilia) || 6; }

/* ===================== migração (parte 6) =====================
   Roda em TODA abertura e pode rodar quantas vezes for preciso: só
   acrescenta. Nunca apaga lista antiga nem chave de progresso. */
function migrar(){
  carregar();
  if(!st.primeiraAberturaEm) st.primeiraAberturaEm = Date.now();
  var cfgFam = norm((window.NUVEM_CONFIG && window.NUVEM_CONFIG.familia) || '');
  var nf = norm(lget('nuvem_familia') || '') || cfgFam;
  var lOk = listaOuNull();
  var ids = (lOk || []).map(function(u){ return u.id; });
  /* H) o código foi trocado no app antigo (zip anterior): ele vence */
  if(nf.length>=6 && st.ultimoNuvemFamilia && nf!==st.ultimoNuvemFamilia){
    var antiga = st.ultimoNuvemFamilia;
    addFamilia(nf, true, 'app-antigo');
    ids.forEach(function(id){ if(st.criancas[id]===antiga) st.criancas[id] = nf; });
    st.atual = nf;
    /* a família antiga ficou sem ninguém neste celular: sai da lista (só do celular) */
    if(!ids.some(function(id){ return st.criancas[id]===antiga; })) st.familias = st.familias.filter(function(f){ return f.c!==antiga; });
  }
  /* A) e G) já tinha o código da família neste app */
  if(nf.length>=6 && !st.familias.length){
    addFamilia(nf, true, 'migracao'); st.atual = nf;
    S.avisoMigracao = fmt(T.t4TudoCerto, {c:mascara(nf)});
  }
  /* criança sem família (criada no app antigo) ganha a família do celular */
  var padrao = (nf.length>=6 && fam(nf)) ? nf : st.atual;
  ids.forEach(function(id){ if(!st.criancas[id] && padrao) st.criancas[id] = padrao; });
  /* crianças que não existem mais neste app: só tira a ligação (nunca se a lista deu erro) */
  if(lOk) Object.keys(st.criancas).forEach(function(id){ if(ids.indexOf(id)<0) delete st.criancas[id]; });
  if(st.atual && !fam(st.atual)) st.atual = st.familias.length ? st.familias[0].c : '';
  salvar();
}

/* lista que vai para o nuvem-sync.js: cada criança com a família dela.
   "segurar" = espera na fila e não sobe (família a conferir, criança
   sendo trazida, nome + bichinho repetido na mesma família). */
function paraNuvem(l){
  var vistos = {};
  return (l || lista()).map(function(u){
    var f = familiaDe(u.id), fi = fam(f);
    var o = { id:u.id, nome:u.nome, av:u.av, fam:f };
    if(fi && !fi.conferida) o.segurar = 'familia-a-conferir';
    if(S.trazendo[u.id]) o.segurar = 'trazendo';
    var k = f+'/'+chaveDe(u.nome, u.av);
    if(vistos[k]) o.segurar = 'repetida'; else vistos[k] = u.id;
    return o;
  });
}
function repetidas(){
  var vistos = {}, r = [];
  lista().forEach(function(u){
    var k = familiaDe(u.id)+'/'+chaveDe(u.nome,u.av);
    if(vistos[k]) r.push({ primeira:vistos[k], segunda:u }); else vistos[k] = u;
  });
  return r;
}

/* ===================== a bolinha (4.11) ===================== */
function situacao(){
  var n = NS();
  if(!n || !nuvemLigada()) return { cor:'vermelho', txt:T.desligada };
  var s = n.status();
  var us = lista();
  var semFam = !st.familias.length || us.some(function(u){ return !familiaDe(u.id); });
  if(semFam) return { cor:'vermelho', txt:T.faltaCodigo };
  var prob = st.familias.filter(function(f){ return f.problema; })[0];
  if(prob) return { cor:'vermelho', txt:fmt(T.confiraCodigo, {c:mascara(prob.c)}) };
  if(s.estado==='erro') return { cor:'vermelho', txt:fmt(T.erro, {m:s.detalhe||''}) };
  var aConf = st.familias.filter(function(f){ return !f.conferida; })[0];
  var rep = repetidas()[0];
  if(rep) return { cor:'amarelo', txt:fmt(T.repetidaEspera, {e:rep.segunda.av, nome:rep.segunda.nome}) };
  if(s.pendentes>0){
    if(s.estado==='offline' || !online())
      return { cor:'amarelo', txt:fmt(T.semInternetFila, {n:s.pendentes, criancas:s.pendentes===1?'CRIANÇA':'CRIANÇAS'}) };
    if(aConf) return { cor:'amarelo', txt:fmt(T.aConferir, {c:mascara(aConf.c)}) };
    return { cor:'amarelo', txt:T.guardando };
  }
  if(aConf) return { cor:'amarelo', txt:fmt(T.aConferir, {c:mascara(aConf.c)}) };
  /* 1.2 (C2): criança tirada com "guardar uma cópia neste celular": o progresso dela pode
     estar SÓ aqui. A bolinha não fica verde até ela voltar (☁️ Buscar na nuvem › Tiradas deste celular). */
  var soAqui = lerLixeira().filter(function(x){ return x && x.soAqui===true; }).length;   /* só cópias feitas a partir da 1.2 (as antigas, do site de teste, não contam) */
  if(soAqui) return { cor:'amarelo', txt:fmt(T.lixeiraSoAqui, {n:soAqui, criancas:soAqui===1?'CRIANÇA':'CRIANÇAS'}) };
  if(s.estado==='ok' || s.estado==='offline'){
    if(s.ultimoOk){ var h = new Date(s.ultimoOk); return { cor:'verde', txt:fmt(T.verde, {h:String(h.getHours()).padStart(2,'0')+':'+String(h.getMinutes()).padStart(2,'0')}) }; }
    return { cor:'verde', txt:T.verdeSemHora };
  }
  return { cor:'amarelo', txt:T.guardando };
}

/* ===================== desenho (DOM) ===================== */
function h(tag, at, filhos){
  var el = document.createElement(tag);
  if(at) for(var k in at){
    if(at[k]==null) continue;
    if(k==='class') el.className = at[k];
    else if(k==='text') el.textContent = at[k];
    else if(k.indexOf('on')===0) el.addEventListener(k.slice(2), at[k]);
    else el.setAttribute(k, at[k]);
  }
  (filhos||[]).forEach(function(f){ if(f==null) return; el.appendChild(typeof f==='string' ? document.createTextNode(f) : f); });
  return el;
}
function btn(texto, onclick, cls, at){
  var o = { type:'button', class:'ef-btn'+(cls?' '+cls:''), text:texto, onclick:onclick };
  if(at) for(var k in at) o[k] = at[k];
  return h('button', o);
}
var CSS_COMPACTO =
  '{X} .ef-so-compacto{display:inline-flex}'+
  '{X} .ef-t5 .ef-titulo,{X} .ef-t5 .ef-sub,{X} .ef-t5 .ef-escolhido,{X} .ef-t5 .ef-botoes-t5{display:none}'+
  '{X} .ef-t5{justify-content:center;padding:4px 6px}'+
  '{X} .ef-t5 .ef-miolo{gap:6px;margin:auto;padding:4px 6px}'+
  '{X} .ef-bicho{--t:clamp(30px,min(10.4vw,22vh),62px)}'+
  '{X} .ef-t2 .ef-card>.ef-titulo,{X} .ef-t3 .ef-card>.ef-titulo,{X} .ef-t2 .ef-texto,{X} .ef-t3 .ef-texto,{X} .ef-botoes-cod{display:none}'+
  '{X} .ef-t2,{X} .ef-t3{align-items:center;justify-content:center;padding:6px}'+
  '{X} .ef-t2 .ef-card,{X} .ef-t3 .ef-card{padding:8px 10px;border-radius:16px;max-height:100%;gap:6px;width:min(640px,96vw)}'+
  '{X} .ef-erro:empty,{X} .ef-res:empty{display:none}';
function css(){
  if(document.getElementById('efCss')) return;
  var s =
  '#efRaiz{position:fixed;inset:0;z-index:2147482000;pointer-events:none}'+
  '#efRaiz.ef-ativo{pointer-events:auto}'+
  '.ef,.ef *{box-sizing:border-box}'+
  '.ef{font-family:var(--ef-fonte,"Arial Rounded MT Bold","Baloo 2",Nunito,"Segoe UI Rounded",system-ui,Arial,sans-serif);color:#123a63;text-transform:uppercase;-webkit-tap-highlight-color:transparent;font-size:16px}'+
  '.ef .ef-normal{text-transform:none}'+
  '.ef-tela{position:fixed;left:0;right:0;top:0;bottom:0;background:linear-gradient(180deg,#e6f5ff 0%,#fff8e8 100%);display:flex;flex-direction:column;overflow:auto;-webkit-overflow-scrolling:touch;padding:10px 14px}'+
  '.ef-pop{position:fixed;left:0;right:0;top:0;bottom:0;background:#0b1633b0;display:flex;align-items:center;justify-content:center;padding:12px;overflow:auto}'+
  '.ef-card{background:#fffdf7;border-radius:22px;box-shadow:0 14px 44px #0006;padding:clamp(10px,3vh,20px) clamp(12px,3vw,22px);max-width:96vw;width:560px;max-height:96%;overflow:auto;text-align:center;display:flex;flex-direction:column;gap:clamp(8px,2.4vh,16px)}'+
  '.ef-titulo{font-weight:900;font-size:clamp(18px,min(5vw,4.6vh),30px);line-height:1.15;margin:0}'+
  '.ef-titulo-grande{font-weight:900;font-size:clamp(22px,min(6vw,6vh),36px);letter-spacing:.04em;color:#123a63;background:#fff3c4;border-radius:14px;padding:8px 10px;word-break:break-all}'+
  '.ef-texto{font-weight:700;font-size:clamp(14px,2.6vh,16px);color:#3d5878;line-height:1.4}'+
  '.ef-erro{color:#c0392b;font-weight:900;font-size:14px;min-height:1.2em}'+
  '.ef-res:empty{display:none}'+
  '.ef-btn{min-height:48px;border:0;border-radius:16px;padding:8px 16px;font:inherit;font-weight:900;font-size:clamp(14px,2.8vh,18px);cursor:pointer;box-shadow:0 4px 10px #0002;background:#fff;color:#123a63;text-transform:uppercase;line-height:1.15}'+
  '.ef-btn:active{transform:translateY(2px)}'+
  '.ef-btn.ef-verde{background:#2fb35a;color:#fff}'+
  '.ef-btn.ef-perigo{background:#e23b3b;color:#fff}'+
  '.ef-btn.ef-amarelo{background:#ffe9a8;color:#4a3b12}'+
  '.ef-btn.ef-leve{background:#eef3f8;box-shadow:none}'+
  '.ef-btn[disabled]{opacity:.5}'+
  '.ef-linha{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;align-items:center}'+
  '.ef-pergunta .ef-card{width:640px}'+
  '.ef-pergunta .ef-linha{margin-top:4px}'+
  '.ef-campo{font:inherit;font-weight:900;font-size:clamp(16px,3.6vh,24px);text-align:center;padding:6px 12px;border-radius:16px;border:4px solid #f0b429;background:#fff;color:#123a63;outline:none;width:min(380px,100%);min-height:48px;-webkit-user-select:text;user-select:text;text-transform:uppercase}'+
  '.ef-campo:focus{border-color:#2fb35a}'+
  '.ef-campo::placeholder{color:#9aa9b8;text-transform:uppercase}'+
  '.ef-fechar{position:absolute;right:6px;top:6px;min-width:48px;padding:6px 10px}'+
  /* T1 */
  '.ef-t1{align-items:center;justify-content:center;gap:clamp(10px,3vh,22px);text-align:center}'+
  '.ef-t1-botoes{display:flex;gap:clamp(10px,3vw,26px);justify-content:center;width:100%;max-width:900px}'+
  '.ef-t1-botoes .ef-btn{flex:1 1 0;min-height:64px;padding:clamp(12px,3vh,24px) 14px;font-size:clamp(17px,min(4.4vw,4.4vh),26px);display:flex;flex-direction:column;align-items:center;gap:6px;border-radius:22px}'+
  '.ef-t1-botoes .ef-btn small{font-size:clamp(14px,2.4vh,16px);font-weight:700;text-transform:none;opacity:.85}'+
  '@media (orientation:portrait){.ef-t1-botoes{flex-direction:column;align-items:stretch;max-width:420px}}'+
  /* T4 */
  '.ef-topo{display:flex;align-items:center;gap:10px;flex:0 0 auto;min-height:52px}'+
  '.ef-topo .ef-titulo{flex:1;text-align:left}'+
  '.ef-icone{min-width:48px;width:48px;height:48px;border-radius:50%;padding:0;font-size:22px;position:relative;display:inline-flex;align-items:center;justify-content:center}'+
  '.ef-grupo-tit{font-weight:900;font-size:15px;margin:10px 2px 6px;color:#4a6585}'+
  '.ef-grade{display:grid;grid-template-columns:repeat(auto-fit,clamp(136px,17vw,230px));justify-content:center;gap:clamp(10px,2vw,18px);padding:6px 4px}'+
  '@media (orientation:portrait){.ef-grade{grid-template-columns:repeat(2,minmax(0,1fr))}}'+
  '.ef-crianca{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:4px;border:0;border-radius:18px;padding:10px 8px;background:#fff;box-shadow:0 3px 9px #0002;cursor:pointer;min-height:clamp(118px,30vh,160px);font:inherit;color:#123a63;text-transform:uppercase}'+
  '.ef-crianca.ef-atual{outline:3px solid #2fb35a}'+
  '.ef-crianca .ef-av{font-size:clamp(40px,min(11vw,10vh),62px);line-height:1}'+
  '.ef-crianca .ef-nome{font-weight:900;font-size:clamp(15px,2.8vh,18px);max-width:100%;overflow:hidden;line-height:1.15;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow-wrap:break-word}'+
  '.ef-crianca .ef-prog{font-size:14px;font-weight:700;color:#5d7390;text-transform:none}'+
  '.ef-barra{width:90%;height:8px;border-radius:6px;background:#00000014;overflow:hidden}'+
  '.ef-barra i{display:block;height:100%;background:linear-gradient(90deg,#ffd54f,#ffab00)}'+
  '.ef-crianca.ef-nuvemcard{background:#f4f9ff;border:3px dashed #8fb3d9;box-shadow:none}'+
  '.ef-crianca.ef-novo{background:#f2fff5;border:3px dashed #7cc993;box-shadow:none}'+
  '.ef-crianca.ef-novo .ef-av{font-size:clamp(34px,8vh,48px)}'+
  '.ef-acoes-card{display:flex;gap:8px;justify-content:center;margin-top:4px}'+
  '.ef-acoes-card .ef-btn{min-height:48px;min-width:52px;padding:4px 8px;font-size:20px;border-radius:14px}'+
  '.ef-acoes-card .ef-tirar{background:#ffe3e3}'+
  '.ef-arrumando .ef-crianca .ef-prog,.ef-arrumando .ef-crianca .ef-barra{display:none}'+
  '.ef-arrumando .ef-crianca{gap:2px;padding:6px}'+
  '.ef-barra-botoes{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;padding:10px 0 6px;flex:0 0 auto}'+
  '.ef-rodape{display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap;padding:8px 12px;margin-top:4px;flex:0 0 auto;background:#ffffff8c;border-radius:16px}'+
  '.ef-status{display:flex;align-items:center;gap:8px;font-weight:800;font-size:14px;min-height:48px;min-width:0;flex:1 1 260px;line-height:1.3}'+
  '.ef-rodape .ef-familia-link{flex:0 0 auto}'+
  '.ef-aviso{background:#fff3c4;border-radius:14px;padding:8px 12px;font-weight:800;font-size:14px;display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap;margin:4px 0}'+
  '.ef-meio{flex:1 0 auto}'+
  '.ef-t4{overflow:auto}'+
  '.ef-t4 .ef-meio{flex:1 1 auto;min-height:130px;overflow:auto;-webkit-overflow-scrolling:touch;display:flex;flex-direction:column}'+
  '.ef-t4 .ef-meio>:first-child{margin-top:auto}.ef-t4 .ef-meio>:last-child{margin-bottom:auto}'+
  /* T5 */
  '.ef-t5{align-items:stretch;justify-content:center;padding:0}'+
  '.ef-miolo{display:flex;flex-direction:column;align-items:center;gap:clamp(4px,1.6vh,11px);text-align:center;margin:auto;padding:clamp(6px,2vh,16px) 8px clamp(8px,3vh,20px);width:100%}'+
  '.ef-sub{font-size:clamp(14px,min(3.6vw,2.6vh),16px);font-weight:800;color:#5d7390}'+
  '.ef-bichos{display:flex;flex-wrap:nowrap;justify-content:center;align-items:center;gap:clamp(3px,1.2vw,9px);max-width:98vw}'+
  '.ef-bicho{--t:clamp(30px,min(10.4vw,15vh),62px);width:var(--t);height:var(--t);font-size:calc(var(--t)*.58);line-height:1;background:#fff;border:3px solid transparent;border-radius:14px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px #00000018;cursor:pointer;flex:0 0 auto;padding:0}'+
  '.ef-bicho:active{transform:scale(.9)}'+
  '.ef-bicho.ef-on{border-color:#2fb35a;background:#eaffef;transform:scale(1.08);box-shadow:0 0 0 3px #f0a03055}'+
  '.ef-escolhido{font-size:clamp(14px,min(3.4vw,2.4vh),16px);font-weight:900;min-height:1.2em}'+
  /* a linha do campo: o campo NUNCA muda de lugar (mudar de lugar fecha o teclado);
     com o teclado aberto só aparecem os botões pequenos ao lado dele */
  '.ef-linha-campo{display:flex;gap:6px;align-items:center;justify-content:center;width:100%}'+
  '.ef-linha-campo .ef-campo{flex:0 1 380px;min-width:0}'+
  '.ef-linha-campo .ef-btn{flex:0 0 auto;padding:6px 10px}'+
  '.ef-linha-campo b{font-size:16px;flex:0 0 auto}'+
  '.ef-so-compacto{display:none}'+
  '.ef-linha-campo .ef-btn{align-items:center;justify-content:center;text-align:center}'+
  '.ef-linha-campo .ef-btn.ef-so-compacto{max-width:170px;white-space:normal;line-height:1.1;font-size:14px}'+
  '.ef-linha-campo .ef-campo{min-width:110px}'+
  '@media (max-width:520px){.ef-linha-campo .ef-btn.ef-so-compacto{max-width:122px}}'+
  '@media (max-width:420px){.ef-linha-campo b{display:none!important}}'+
  CSS_COMPACTO.replace(/\{X\}/g,'.ef-teclado')+
  '@media (max-height:300px){'+CSS_COMPACTO.replace(/\{X\} /g,'')+'}'+
  /* "achei a sua família" (T2 depois de procurar): largo, cartões em grade com espaço, botões embaixo */
  '.ef-card.ef-achou{width:960px;max-height:94%;overflow:hidden;gap:12px}'+
  '.ef-achou>.ef-titulo,.ef-achou>.ef-texto,.ef-achou>.ef-casob,.ef-achou>.ef-linha-campo,.ef-achou>.ef-erro,.ef-achou>.ef-botoes-cod{display:none}'+
  '.ef-achou .ef-res{display:flex;flex-direction:column;gap:clamp(10px,2.6vh,18px);min-height:0;flex:1 1 auto}'+
  '.ef-achou .ef-achei{font-weight:900;font-size:clamp(18px,min(4.6vw,5vh),28px);margin:0 auto;padding:0 54px;color:#1d7a3e}'+
  '.ef-achou .ef-codigo-achado{font-weight:800;font-size:15px;color:#5d7390;margin-top:-6px}'+
  '.ef-achou .ef-cartoes{--cw:180px;grid-auto-rows:max-content;grid-template-columns:repeat(auto-fit,var(--cw));justify-content:center;width:100%;max-width:calc(var(--cols,5) * (var(--cw) + 14px) + 8px);margin:0 auto;gap:14px;overflow:auto;min-height:0;flex:0 1 auto;padding:6px 4px 10px}'+
  '.ef-achou .ef-mini{padding:14px 8px;gap:6px;cursor:default}'+
  '.ef-achou .ef-mini .ef-av{font-size:clamp(34px,8vh,46px)}'+
  '.ef-achou .ef-mini{min-width:0}.ef-achou .ef-mini .ef-nome{font-size:17px;min-width:0;max-width:100%;white-space:normal;overflow-wrap:break-word;line-height:1.15}'+
  '@media (max-height:440px){.ef-achou .ef-cartoes{--cw:200px}.ef-achou .ef-mini .ef-nome{font-size:16px}.ef-achou .ef-mini{display:grid;grid-template-columns:auto minmax(0,1fr);grid-template-rows:auto auto;align-items:center;justify-items:start;text-align:left;padding:8px 12px;column-gap:10px;row-gap:0}.ef-achou .ef-mini .ef-av{font-size:34px;grid-row:1/3}.ef-achou .ef-mini .ef-prog{font-size:14px;line-height:1.1}}'+
  '@media (orientation:portrait){.ef-achou .ef-cartoes{grid-template-columns:repeat(2,minmax(0,1fr));max-width:none}}'+
  '.ef-card.ef-achou{position:relative}.ef-achou .ef-x-achei{position:absolute;right:10px;top:10px;min-width:48px;padding:6px 10px}.ef-x-achei{display:none}.ef-achou .ef-x-achei{display:inline-flex;align-items:center;justify-content:center}'+
  '.ef-botoes-achei{flex:0 0 auto;padding-top:4px;border-top:1px solid #00000010;gap:16px}'+
  '.ef-botoes-achei .ef-btn{min-width:150px;min-height:52px}'+
  /* listas */
  '.ef-cartoes{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px;text-align:center}'+
  '.ef-mini{display:flex;flex-direction:column;align-items:center;gap:4px;border:0;border-radius:16px;padding:12px 8px;background:#fff;box-shadow:0 3px 8px #0002;font:inherit;color:#123a63;text-transform:uppercase;cursor:pointer;min-height:48px}'+
  '.ef-mini .ef-av{font-size:34px;line-height:1}'+
  '.ef-mini .ef-nome{font-weight:900;font-size:15px}'+
  '.ef-mini .ef-prog{font-size:14px;font-weight:700;color:#5d7390;text-transform:none}'+
  '.ef-mini.ef-ja{outline:3px solid #2fb35a;background:#eafff0}'+
  '.ef-secao-tit{font-weight:900;font-size:15px;margin:14px 2px 6px;color:#4a6585;text-align:left}'+
  '.ef-msg{font-weight:800;font-size:clamp(14px,2.4vh,16px);text-align:center;margin:6px auto 10px;max-width:62ch;line-height:1.4}'+
  '.ef-corpo{max-width:980px;width:100%;margin:0 auto;flex:1 0 auto}'+
  '.ef-fam-linha{display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#fff;border-radius:16px;box-shadow:0 3px 8px #0002;padding:12px 16px;margin:10px 0;font-weight:800;font-size:15px}'+
  '.ef-fam-linha .ef-cod{font-size:17px;font-weight:900;letter-spacing:.03em}'+
  '.ef-fam-linha .ef-quem{flex:1;min-width:120px}'+
  '.ef-fam-linha .ef-status{flex:0 0 auto;min-height:0}'+
  '.ef-t8 .ef-barra-botoes{gap:16px;padding-top:14px}'+
  '.ef-dica-adulto{font-size:14px;margin-top:6px;text-align:center}'+
  /* bolinha e chip */
  '.ef-ponto{position:absolute;right:1px;top:1px;width:14px;height:14px;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px #0005;pointer-events:none;background:#b9c3cf;display:block}'+
  '.ef-ponto.ef-p-verde{background:#2fb35a}.ef-ponto.ef-p-amarelo{background:#f0a030}.ef-ponto.ef-p-vermelho{background:#e23b3b}'+
  '.ef-ponto-solto{position:relative;display:inline-block;flex:0 0 auto;right:auto;top:auto}'+
  '.ef-chip{display:inline-flex;align-items:center;gap:6px;height:48px;min-width:48px;max-width:150px;padding:0 12px 0 4px;border:0;border-radius:24px;background:#ffffffdd;box-shadow:0 2px 6px #0002;font-family:var(--ef-fonte,inherit);font-weight:900;font-size:14px;color:#123a63;text-transform:uppercase;cursor:pointer;flex:0 0 auto}'+
  '.ef-chip .ef-chip-av{width:38px;height:38px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 2px #2fb35a55;display:flex;align-items:center;justify-content:center;font-size:24px;line-height:1;flex:0 0 auto}'+
  '.ef-chip .ef-chip-nome{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:88px}'+
  '@media (max-width:560px){.ef-chip{padding:0 4px}.ef-chip .ef-chip-nome{display:none}}'+
  /* trava do adulto */
  '.ef-adulto{display:inline-flex;flex-direction:column;align-items:center;gap:2px;-webkit-user-select:none;user-select:none;touch-action:none}'+
  '.ef-adulto .ef-adulto-l{display:flex;align-items:center;gap:8px}'+
  '.ef-adulto .ef-anel{width:26px;height:26px;border-radius:50%;flex:0 0 auto;background:conic-gradient(#2fb35a calc(var(--p,0)*360deg),#00000022 0);box-shadow:inset 0 0 0 4px #fff}'+
  '.ef-adulto small{font-size:14px;font-weight:800;opacity:.85}'+
  '.ef-adulto.ef-segurando{background:#eaffef}'+
  '.ef-adulto.ef-adulto-curto{flex-direction:row;padding:6px 16px 6px 10px}'+
  /* seção das Configurações */
  '.ef-cfg{display:flex;flex-direction:column;gap:12px;text-transform:uppercase;grid-column:1/-1}'+
  '.ef-cfg-tit{font-size:14px;font-weight:900;color:#a08030;letter-spacing:.04em;margin:8px 2px 0;padding-top:10px;border-top:1px solid #00000014}'+
  '.ef-cfg-linha{display:flex;align-items:center;gap:12px 16px;flex-wrap:wrap;background:#fff;border-radius:16px;box-shadow:0 2px 6px #0002;padding:12px 16px;min-height:68px;font-weight:800;font-size:15px;color:#123a63;font-family:var(--ef-fonte,inherit)}'+
  '.ef-cfg-linha .ef-cfg-txt{flex:1 1 220px;min-width:0;line-height:1.35}'+
  '.ef-cfg-acoes{display:flex;gap:12px;align-items:center;justify-content:flex-end;flex:0 1 auto;max-width:100%;flex-wrap:wrap;margin-left:auto}'+
  '.ef-cfg-linha .ef-btn{font-size:15px;padding:8px 16px;min-height:48px;white-space:nowrap}'+
  '.ef-cfg-linha .ef-cfg-ir{font-size:18px;padding:0 6px;flex:0 0 auto}'+
  '.ef-cfg-linha.ef-toca{cursor:pointer}'+
  /* aviso rápido */
  '.ef-toast{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:2147482500;background:#123a63;color:#fff;padding:12px 18px;border-radius:16px;font-weight:900;font-size:15px;max-width:92vw;text-align:center;box-shadow:0 6px 20px #0005;opacity:0;transition:opacity .2s;pointer-events:none;text-transform:uppercase;font-family:var(--ef-fonte,"Arial Rounded MT Bold",Nunito,system-ui,sans-serif)}'+
  '.ef-toast.ef-on{opacity:1}'+
  '#efRaiz.ef-sob-config{visibility:hidden!important;pointer-events:none!important}'+
  'body:has(#efRaiz.ef-sob-config) .ef-teste{display:none}'+
  '.ef-topo .ef-t4-config{margin-right:4px}'+
  '.ef-topo .ef-voltar{white-space:nowrap;flex:0 0 auto}'+
  'body:has(#efRaiz .ef-teclado) .ef-teste{display:none}@media (max-height:300px){.ef-teste{display:none}}'+
  'body:not(:has(#efRaiz.ef-ativo)) .ef-teste{display:none}'+
  '.ef-no-site-teste .ef-tela{padding-top:30px}.ef-no-site-teste .ef-pop{padding-top:30px}'+
  '.ef-no-site-teste .ef-teclado.ef-tela,.ef-no-site-teste .ef-teclado.ef-pop{padding-top:6px}'+
  '.ef-teste{position:fixed;left:0;right:0;top:0;z-index:2147482400;background:#7b2cbf;color:#fff;font:900 14px system-ui,sans-serif;text-align:center;padding:3px;pointer-events:none;opacity:.92}';
  var el = document.createElement('style'); el.id = 'efCss'; el.textContent = s;
  (document.head || document.documentElement).appendChild(el);
}
function fonte(){
  try{ var f = C && C.fonte; return typeof f==='function' ? f() : (f||''); }catch(e){ return ''; }
}
function aplicarFonte(){
  var f = fonte();
  if(f) document.documentElement.style.setProperty('--ef-fonte', f);
}
function toast(msg, ms){
  if(!toastEl){ toastEl = h('div', {class:'ef-toast', id:'efToast', role:'status'}); document.body.appendChild(toastEl); }
  toastEl.textContent = msg; toastEl.classList.add('ef-on');
  clearTimeout(toastT); toastT = setTimeout(function(){ toastEl.classList.remove('ef-on'); }, ms||2600);
}

/* ---------- pilha de telas (e o botão voltar do Android) ---------- */
function garantirRaiz(){
  if(raiz && raiz.parentNode) return raiz;
  raiz = h('div', {id:'efRaiz', class:'ef'});
  document.body.appendChild(raiz);
  raiz.addEventListener('focusin', function(){ setTimeout(ajustarTeclado, 30); });
  raiz.addEventListener('focusout', function(){ setTimeout(ajustarTeclado, 60); });
  return raiz;
}
/* ⚙️ da "Quem vai estudar hoje?": as Configurações do app abrem por cima e o módulo
   fica escondido (sem sair do lugar) até elas fecharem */
function abrirConfigDoApp(){
  if(!C || typeof C.abrirConfig!=='function' || !raiz) return;
  S.sobConfig = true; raiz.classList.add('ef-sob-config');
  try{ C.abrirConfig(function(){ mostrarRaiz(false); }); }catch(e){ mostrarRaiz(false); }
}
function mostrarRaiz(fecharConfig){
  if(!S.sobConfig) return;
  S.sobConfig = false;
  if(raiz) raiz.classList.remove('ef-sob-config');
  if(fecharConfig && C && typeof C.fecharConfig==='function'){ try{ C.fecharConfig(); }catch(e){} }
  atualizar(true);
}
function empilhar(el, fechar, nome){
  garantirRaiz(); aplicarFonte();
  if(S.sobConfig) mostrarRaiz(true);      /* uma tela do módulo pedida de dentro das Configurações */
  raiz.appendChild(el);
  var it = { el:el, fechar:fechar||null, nome:nome||'' };
  pilha.push(it);
  raiz.classList.add('ef-ativo');
  if(pilha.length===1){
    try{ if(C && C.aoAbrirTelas) C.aoAbrirTelas(); }catch(e){}
    historicoEntrar();
  }
  ajustarTeclado();
  return it;
}
function desempilhar(it){
  var i = pilha.indexOf(it); if(i<0) return;
  pilha.splice(i,1);
  if(it.el.parentNode) it.el.parentNode.removeChild(it.el);
  if(!pilha.length){
    raiz.classList.remove('ef-ativo');
    try{ if(C && C.aoFecharTelas) C.aoFecharTelas(); }catch(e){}
    historicoSair();
  }
}
function fecharTudo(){
  while(pilha.length){ var it = pilha.pop(); if(it.el.parentNode) it.el.parentNode.removeChild(it.el); }
  if(raiz) raiz.classList.remove('ef-ativo');
  try{ if(C && C.aoFecharTelas) C.aoFecharTelas(); }catch(e){}
  historicoSair();
}
function topo(){ return pilha[pilha.length-1] || null; }
function aberta(nome){ for(var i=0;i<pilha.length;i++) if(pilha[i].nome===nome) return pilha[i]; return null; }
function fecharTopo(){
  var t = topo(); if(!t) return false;
  if(t.fechar){ t.fechar(); return true; }
  return false;
}
function historicoEntrar(){
  clearTimeout(S.histT);
  if(S.hist) return;                       /* já tem a "página" do módulo no histórico */
  try{ history.pushState({escolaFamilia:1}, ''); S.hist = true; }catch(e){}
}
/* só volta no histórico se o módulo continuar fechado (fechar uma tela e
   abrir outra logo em seguida não mexe no histórico) */
function historicoSair(){
  clearTimeout(S.histT);
  S.histT = setTimeout(function(){
    if(pilha.length) return;
    if(S.hist){ S.hist = false; S.ignorarPop = true; try{ history.back(); }catch(e){ S.ignorarPop = false; correrDepois(); } }
    else correrDepois();
  }, 0);
}
function correrDepois(){ var f = S.depoisDoPop; S.depoisDoPop = null; if(f) f(); }
window.addEventListener('popstate', function(){
  if(S.ignorarPop){ S.ignorarPop = false; correrDepois(); return; }
  if(!pilha.length) return;
  if(S.sobConfig){ S.hist = false; mostrarRaiz(true); historicoEntrar(); return; }   /* voltar fecha as Configurações */
  S.hist = false;
  fecharTopo();
  if(pilha.length) historicoEntrar();
});

/* ---------- teclado: o cartão gruda em cima do que sobra da tela ---------- */
function ajustarTeclado(){
  if(!raiz) return;
  var vv = window.visualViewport;
  var alt = vv ? vv.height : window.innerHeight;
  var cima = vv ? vv.offsetTop : 0;
  var foco = document.activeElement;
  var digitando = !!(foco && foco.tagName==='INPUT' && raiz.contains(foco));
  var compacto = digitando && alt <= 300;
  pilha.forEach(function(it){
    it.el.classList.toggle('ef-teclado', compacto);
    if(digitando && vv && (alt < window.innerHeight - 40 || cima > 0)){
      it.el.style.top = cima+'px'; it.el.style.height = alt+'px'; it.el.style.bottom = 'auto';
    } else { it.el.style.top = ''; it.el.style.height = ''; it.el.style.bottom = ''; }
  });
  if(digitando) setTimeout(function(){ try{ foco.scrollIntoView({block:'nearest'}); }catch(e){} }, 60);
}
if(window.visualViewport){
  window.visualViewport.addEventListener('resize', function(){ if(pilha.length) ajustarTeclado(); });
  window.visualViewport.addEventListener('scroll', function(){ if(pilha.length) ajustarTeclado(); });
}
window.addEventListener('resize', function(){ if(pilha.length) ajustarTeclado(); });

/* ---------- trava do adulto (D15): segurar 3 segundos ---------- */
function botaoAdulto(texto, aoLiberar, cls, curto){
  /* curto = uma linha só ("◯ 👨 MOSTRAR"): o toque rápido explica que é para um adulto segurar */
  var b = h('button', {type:'button', class:'ef-btn ef-adulto'+(curto?' ef-adulto-curto':'')+(cls?' '+cls:'')}, [
    h('span', {class:'ef-adulto-l'}, [ h('span', {class:'ef-anel'}), h('span', {text: curto ? '👨 '+texto : texto}) ]),
    curto ? null : h('small', {text:T.adulto})
  ]);
  var t = null, ini = 0, raf = 0;
  /* enquanto o adulto segura, nada redesenha a tela (senão o botão sumiria da mão dele) */
  function parar(){
    if(t){ clearTimeout(t); t = null; }
    if(b._seg){ b._seg = false; S.segurando = Math.max(0,(S.segurando||0)-1); if(!S.segurando && S.adiado){ var tudo = S.adiado==='tudo'; S.adiado = ''; setTimeout(function(){ atualizar(tudo); }, 0); } }
    b.classList.remove('ef-segurando'); b.style.setProperty('--p','0'); try{ cancelAnimationFrame(raf); }catch(e){}
  }
  function anima(){ if(!t) return; b.style.setProperty('--p', String(Math.min(1,(Date.now()-ini)/HOLD_MS))); raf = requestAnimationFrame(anima); }
  b.addEventListener('pointerdown', function(ev){
    if(ev.button>0) return;
    try{ ev.preventDefault(); }catch(e){}
    parar(); ini = Date.now(); b.classList.add('ef-segurando'); b._seg = true; S.segurando = (S.segurando||0)+1;
    t = setTimeout(function(){ t = null; parar(); b.dataset.liberado = '1'; try{ aoLiberar(); }catch(e){} }, HOLD_MS);
    anima();
  });
  ['pointerup','pointerleave','pointercancel'].forEach(function(n){ b.addEventListener(n, parar); });
  b.addEventListener('click', function(ev){ ev.preventDefault(); if(b.dataset.liberado==='1'){ b.dataset.liberado=''; return; } toast(T.adultoDica); });
  b.addEventListener('contextmenu', function(ev){ ev.preventDefault(); });
  return b;
}

/* ---------- pergunta no estilo do módulo (nunca o confirm do navegador) ---------- */
function perguntar(o){
  return new Promise(function(resolve){
    var it = null;
    var fim = function(v){ if(it){ desempilhar(it); it = null; } resolve(v); };
    var linhas = (o.linhas||[]).map(function(l){ return h('div', {class:'ef-texto', text:l}); });
    var botoes = [];
    if(o.nao !== false) botoes.push(btn(o.nao || T.cancelar, function(){ fim(false); }, 'ef-leve ef-nao'));
    if(o.sim===null){ /* só os botões extras */ }
    else if(o.adulto) botoes.push(botaoAdulto(o.sim || T.sim, function(){ fim(true); }, o.perigo?'ef-perigo ef-sim':'ef-verde ef-sim'));
    else botoes.push(btn(o.sim || T.ok, function(){ fim(true); }, o.perigo?'ef-perigo ef-sim':'ef-verde ef-sim'));
    (o.extras||[]).forEach(function(x){ botoes.push(btn(x.texto, function(){ fim(x.valor); }, x.cls||'')); });
    var card = h('div', {class:'ef-card', role:'dialog', 'aria-modal':'true'},
      [h('div', {class:'ef-titulo', text:o.titulo||''})].concat(linhas).concat([h('div', {class:'ef-linha'}, botoes)]));
    var pop = h('div', {class:'ef-pop ef-pergunta'}, [card]);
    it = empilhar(pop, function(){ fim(o.nao===false ? true : false); }, 'pergunta');
  });
}

/* ===================== ações ===================== */
function escolher(id, naAbertura){
  /* fechar as telas faz um history.back(); entrar (que pode recarregar a
     página) só depois dele, senão o Chrome cancela o recarregamento */
  var feito = false;
  var ir = function(){ if(feito) return; feito = true; try{ A.entrar(id, {naAbertura:!!naAbertura}); }catch(e){} };
  S.depoisDoPop = ir;
  fecharTudo();
  setTimeout(ir, 700);                     /* reserva, se o "voltar" não avisar */
}
function marcarTodasPendentes(c){
  var n = NS(); if(!n) return;
  daFamilia(c).forEach(function(u){ try{ n.marcarPendente(u.id); }catch(e){} });
}
/* acrescenta (ou corrige) a família e liga as crianças certas a ela */
function entrarNaFamilia(c, conferida, origem, modo, cAntigo){
  if(modo==='corrigir' && cAntigo){
    var fa = fam(cAntigo);
    if(fa){
      if(fam(c) && c!==cAntigo){ st.familias = st.familias.filter(function(f){ return f.c!==cAntigo; }); }
      else { fa.c = c; }
      Object.keys(st.criancas).forEach(function(id){ if(st.criancas[id]===cAntigo) st.criancas[id] = c; });
      if(st.atual===cAntigo) st.atual = c;
    }
    var f2 = addFamilia(c, conferida, origem); if(!conferida){ f2.conferida = false; f2.origem = origem; delete f2.problema; }
  } else {
    var nova = !fam(c);
    var f = addFamilia(c, conferida, origem);
    if(nova){ f.conferida = !!conferida; f.origem = origem; }
    if(modo!=='outra'){
      lista().forEach(function(u){ if(!st.criancas[u.id]) st.criancas[u.id] = c; });
      st.atual = c;
    }
  }
  salvar();
  marcarTodasPendentes(c);
  var n = NS(); if(n && nuvemLigada()) try{ n.sincronizar(); }catch(e){}
  atualizar(true);
}
/* confere na nuvem as famílias guardadas sem internet (T2/T3 offline) */
var conferindo = false;
function conferirFamilias(){
  if(conferindo || !nuvemV4() || !nuvemLigada() || !online()) return Promise.resolve();
  var falta = st.familias.filter(function(f){ return !f.conferida && !f.problema; });
  if(!falta.length) return Promise.resolve();
  conferindo = true;
  var cadeia = Promise.resolve();
  falta.forEach(function(f){
    cadeia = cadeia.then(function(){
      return NS().existeFamilia(f.c).then(function(r){
        var g = fam(f.c); if(!g) return;
        if(g.origem==='t3'){ if(!r.existe) g.conferida = true; else g.problema = 'ja-existe'; }
        else { if(r.existe) g.conferida = true; else g.problema = 'nao-existe'; }
        salvar();
        if(g.conferida){ marcarTodasPendentes(g.c); try{ NS().sincronizar(); }catch(e){} }
      }, function(){});
    });
  });
  return cadeia.then(function(){ conferindo = false; atualizar(true); }, function(){ conferindo = false; });
}
/* mudanças de nome/bichinho que ainda vão marcar o movidoPara (5.3 item 6) */
var processando = false;
function processarMudancas(){
  if(processando || !nuvemV4() || !nuvemLigada() || !online() || !st.mudancasPendentes.length) return Promise.resolve();
  processando = true;
  var n = NS();
  var cadeia = Promise.resolve();
  st.mudancasPendentes.slice().forEach(function(m){
    cadeia = cadeia.then(function(){
      var u = local(m.id);
      var tira = function(){ st.mudancasPendentes = st.mudancasPendentes.filter(function(x){ return x!==m && !(x.id===m.id && x.chaveAntiga===m.chaveAntiga); }); salvar(); };
      if(!u){ tira(); return; }
      var fi = fam(m.fam); if(!fi || !fi.conferida) return;
      /* 1) junta a ficha antiga na criança; 2) a nuvem confirma a ficha nova; 3) só então marca */
      return n.recuperar(m.id, m.nomeAntigo, m.avAntigo, false, m.fam).then(function(){
        return n.garantirGuardado(m.id);
      }).then(function(ok){
        if(!ok) return;
        var u2 = local(m.id); if(!u2) return tira();
        return n.marcarMovido(m.fam, m.chaveAntiga, chaveDe(u2.nome, u2.av)).then(function(feito){ if(feito){ tira(); delete S.nuvemCache[m.fam]; } });
      }).catch(function(){});
    });
  });
  return cadeia.then(function(){ processando = false; }, function(){ processando = false; });
}
function mudarCrianca(id, nome, av){
  var u = local(id); if(!u) return;
  var f = familiaDe(id);
  var antes = chaveDe(u.nome, u.av), depois = chaveDe(nome, av);
  try{ A.mudar(id, nome, av); }catch(e){}
  if(antes!==depois && f){
    st.mudancasPendentes.push({ id:id, fam:f, chaveAntiga:antes, chaveNova:depois, nomeAntigo:u.nome, avAntigo:u.av, quando:Date.now() });
    salvar();
    var n = NS(); if(n) try{ n.marcarPendente(id); }catch(e){}
    processarMudancas();
  }
  atualizar(true);
}

/* lista da nuvem (com cache curto por família) */
function listaNuvem(c, forcar){
  var cc = S.nuvemCache[c];
  if(!forcar && cc && Date.now()-cc.quando < 60000) return Promise.resolve(cc.lista);
  if(!nuvemLigada() || !online() || !NS().listarUsuarios) return Promise.reject(new Error(T.semInternet));
  return NS().listarUsuarios(c).then(function(l){ S.nuvemCache[c] = { quando:Date.now(), lista:l }; return l; });
}
function fimDaCadeia(lista_, chave){
  var mapa = {}; lista_.forEach(function(x){ mapa[x.chave] = x; });
  var vis = {}, at = mapa[chave];
  while(at && at.movidoPara && !vis[at.chave] && mapa[at.movidoPara]){ vis[at.chave] = 1; at = mapa[at.movidoPara]; }
  return at || null;
}
function cobreApps(nova, antiga){
  var a = antiga.apps || {}, b = (nova && nova.apps) || {};
  return Object.keys(a).every(function(k){ return !!b[k]; });
}
/* uma ficha "mudou para" outra? (movidoPara na nuvem, ou mudança feita
   neste celular que ainda vai ser marcada na nuvem) */
function movida(l, x, c){
  if(x.movidoPara){ var fim = fimDaCadeia(l, x.chave); if(fim && fim.chave!==x.chave) return fim; }
  var m = st.mudancasPendentes.filter(function(m){ return m.fam===c && m.chaveAntiga===x.chave; })[0];
  if(m){ var u = local(m.id); if(u) return { chave:chaveDe(u.nome,u.av), nome:u.nome, av:u.av, apps:{} }; }
  return null;
}
/* o que aparece como "criança da família na nuvem": fichas antigas de quem
   mudou de nome NUNCA aparecem como criança (elas ficam em "📦 Nomes antigos") */
function fichasVisiveis(l, c){
  return l.filter(function(x){ return !x.oculta && !movida(l, x, c); });
}
function localDaFicha(c, chave){
  return daFamilia(c).filter(function(u){ return chaveDe(u.nome,u.av)===chave; })[0] || null;
}
/* junta na criança as fichas antigas (que mudaram para esta) deste app */
function juntarAntigas(id, chave, c, l){
  var n = NS(); var app = C.app;
  return (l ? Promise.resolve(l) : listaNuvem(c).catch(function(){ return []; })).then(function(lst){
    var cadeia = Promise.resolve();
    lst.forEach(function(x){
      if(x.chave===chave || !x.movidoPara || !(x.apps||{})[app]) return;
      var fim = fimDaCadeia(lst, x.chave);
      if(fim && fim.chave===chave) cadeia = cadeia.then(function(){ return n.recuperar(id, x.nome, x.av, false, c).catch(function(){}); });
    });
    return cadeia;
  });
}
/* traz uma criança da nuvem para este celular (nunca deixa criança vazia
   que depois sobe por cima da ficha: se o download falhar, ela sai) */
function trazer(ficha, c, l){
  var fimC = l ? movida(l, ficha, c) : null;
  if(fimC && fimC.chave){ var alvo = l.filter(function(x){ return x.chave===fimC.chave; })[0] || fimC; if(alvo.chave!==ficha.chave) ficha = alvo; }
  var ja = localDaFicha(c, ficha.chave);
  if(ja) return juntar(ja.id, ficha, c).then(function(){ return ja.id; });
  if(daFamilia(c).length >= max()){ toast(fmt(T.t5Maximo, {n:max()})); return Promise.resolve(null); }
  var id;
  try{ id = A.criar(ficha.nome, ficha.av, 'nuvem'); }catch(e){ toast(fmt(T.erroTxt,{m:T.naoDeu})); return Promise.resolve(null); }
  st.criancas[id] = c; S.trazendo[id] = true; salvar();
  toast(fmt(T.t4Trazendo, {nome:ficha.nome}));
  var n = NS();
  return n.recuperar(id, ficha.nome, ficha.av, true, c).then(function(achou){
    return juntarAntigas(id, ficha.chave, c, l).then(function(){ return achou; });
  }).then(function(achou){
    delete S.trazendo[id];
    juntarLixeira(id, c);
    try{ n.marcarPendente(id); }catch(e){}
    toast(fmt(achou ? T.recuperado : T.semLeituras, {e:ficha.av, nome:ficha.nome}));
    atualizar(true);
    return id;
  }, function(e){
    delete S.trazendo[id];
    descartarNova(id);
    toast(fmt(T.erroTxt, {m:(e && e.message) || T.naoDeu}), 4000);
    atualizar(true);
    return null;
  });
}
/* criança que acabou de ser criada e não recebeu nada (o download falhou) */
function descartarNova(id){
  var n = NS();
  var f = function(){ try{ A.tirar(id); }catch(e){} };
  if(n && n.semVigiar) n.semVigiar(f); else f();
  if(n && n.limparPendencia) n.limparPendencia(id);
  delete st.criancas[id]; salvar();
}
function juntar(id, ficha, c){
  var n = NS();
  toast(fmt(T.juntando, {nome:ficha.nome}));
  return n.recuperar(id, ficha.nome, ficha.av, false, c).then(function(achou){
    toast(fmt(achou ? T.juntado : T.nadaNovo, {e:ficha.av, nome:ficha.nome}));
    atualizar(true);
    return achou;
  }, function(e){ toast(fmt(T.erroTxt, {m:(e&&e.message)||T.naoDeu}), 4000); return false; });
}

/* ---------- tirar deste celular (T7) ---------- */
function lixeiraChave(){ return 'escola_lixeira_'+C.app; }
function lerLixeira(){ return J(lget(lixeiraChave()), []); }
function pedirTirar(id){
  var u = local(id); if(!u) return Promise.resolve(false);
  var ultima = lista().length<=1;
  var passo0 = Promise.resolve(true);
  /* nas 2 primeiras semanas, a última criança fica: se o app voltar à
     versão anterior com a lista vazia, ela cria a "Hana 👧" fantasma */
  if(ultima && dentroDoBloqueio()){
    return perguntar({ titulo:T.t7Ultima, linhas:[fmt(T.t7UltimaTexto,{data:fimDoBloqueio()}), T.t7UltimaDica], nao:false, sim:T.ok })
      .then(function(){ return false; });
  }
  return passo0.then(function(ok){
    if(!ok) return false;
    var semNuvem = !nuvemLigada();
    return perguntar({ titulo:fmt(T.t7Pergunta,{e:u.av,nome:u.nome}), linhas:[semNuvem ? T.t7PerguntaSemNuvem : T.t7PerguntaTexto],
                       sim:T.t7BotaoTirar, perigo:true });
  }).then(function(ok){
    if(!ok) return false;
    var n = NS(); var f = fam(familiaDe(id));
    if(!nuvemLigada()) return semGarantia(id, T.t7SemNuvem);
    if(!nuvemV4() || !f || !f.conferida || !online()) return semGarantia(id, fmt(T.t7NaoGaranteTexto,{nome:u.nome}));
    toast(T.t7Guardando, 6000);
    return n.garantirGuardado(id).then(function(guardado){
      var completo = true; try{ completo = A.completoNaNuvem ? A.completoNaNuvem(id)!==false : true; }catch(e){ completo = false; }
      if(guardado && completo) return efetivarTirar(id, false);
      if(guardado) return semGarantia(id, fmt(T.t7Incompleto,{nome:u.nome}));
      return semGarantia(id, fmt(T.t7NaoGaranteTexto,{nome:u.nome}));
    }, function(){ return semGarantia(id, fmt(T.t7NaoGaranteTexto,{nome:u.nome})); });
  });
}
function semGarantia(id, texto){
  return perguntar({ titulo:T.t7NaoGarante, linhas:[texto], sim:T.t7Copia, adulto:true, perigo:true }).then(function(ok){
    return ok ? efetivarTirar(id, true) : false;
  });
}
function efetivarTirar(id, comCopia, soAqui){
  var u = local(id); if(!u) return false;
  var c = familiaDe(id);
  if(comCopia){
    var dados;
    try{ dados = A.exportar(id); }catch(e){ toast(fmt(T.erroTxt,{m:T.naoDeu})); return false; }
    var lix = lerLixeira();
    /* soAqui: a nuvem não garantiu esta criança (a cópia pode ser o único lugar do progresso) */
    lix.push({ id:id, nome:u.nome, av:u.av, fam:c, quando:Date.now(), dados:dados, soAqui: soAqui!==false });
    try{ lset(lixeiraChave(), JSON.stringify(lix)); }catch(e){ toast(T.t7NaoCoube, 4500); return false; }
  }
  var eraAtual = atualId()===id;
  var r = null, n = NS();
  var f = function(){ r = A.tirar(id); };
  try{ if(n && n.semVigiar) n.semVigiar(f); else f(); }catch(e){ toast(fmt(T.erroTxt,{m:T.naoDeu})); return false; }
  if(n && n.limparPendencia) n.limparPendencia(id);
  delete st.criancas[id];
  st.mudancasPendentes = st.mudancasPendentes.filter(function(m){ return m.id!==id; });
  salvar();
  toast(fmt(T.t7Saiu, {e:u.av, nome:u.nome}));
  if(eraAtual || (r && r.recarregar)){ setTimeout(function(){ try{ location.reload(); }catch(e){} }, 900); return true; }
  if(!lista().length) S.arrumando = false;
  atualizar(true);
  return true;
}
/* a mesma criança (família + nome + bichinho) voltou por outro caminho:
   o que estava na lixeira do celular é juntado nela sozinho */
function juntarLixeira(id, c){
  var u = local(id); if(!u) return 0;
  var ch = chaveDe(u.nome, u.av), lix = lerLixeira(), resta = [], n = 0;
  lix.forEach(function(item){
    var mesma = chaveDe(item.nome, item.av)===ch && ((item.fam||'')===(c||'') || !item.fam);
    if(mesma){ try{ A.importar(id, item.dados || {}); n++; return; }catch(e){} }
    resta.push(item);
  });
  if(n){
    try{ lset(lixeiraChave(), JSON.stringify(resta)); }catch(e){}
    try{ NS() && NS().marcarPendente(id); }catch(e){}
  }
  return n;
}
/* devolve uma criança da lixeira do celular (junta, nunca substitui) */
function trazerDaLixeira(item){
  var c = item.fam && fam(item.fam) ? item.fam : st.atual;
  var ja = localDaFicha(c, chaveDe(item.nome, item.av));
  var id = ja ? ja.id : null;
  if(!id){
    if(daFamilia(c).length >= max()){ toast(fmt(T.t5Maximo,{n:max()})); return; }
    try{ id = A.criar(item.nome, item.av, 'lixeira'); }catch(e){ toast(fmt(T.erroTxt,{m:T.naoDeu})); return; }
    st.criancas[id] = c; salvar();
  }
  try{ A.importar(id, item.dados || {}); }catch(e){ toast(fmt(T.erroTxt,{m:T.naoDeu})); return; }
  var n = NS(); if(n) try{ n.marcarPendente(id); }catch(e){}
  var lix = lerLixeira().filter(function(x){ return !(x.id===item.id && x.quando===item.quando); });
  try{ lset(lixeiraChave(), JSON.stringify(lix)); }catch(e){}
  toast(fmt(T.devolvido, {e:item.av, nome:item.nome}));
  atualizar(true);
}

/* ===================== TELAS ===================== */
function tela(cls){ return h('div', {class:'ef-tela '+(cls||'')}); }
function pop(cls){ return h('div', {class:'ef-pop '+(cls||'')}); }

/* ---------- [T1] boas-vindas ---------- */
function abrirT1(){
  if(aberta('t1')) return;
  var el = tela('ef-t1');
  var us = lista();
  var lst = us.map(function(u){ return u.av+' '+u.nome; }).join(' · ');
  var it;
  el.appendChild(h('h1', {class:'ef-titulo', text:T.t1Titulo}));
  el.appendChild(h('div', {class:'ef-t1-botoes'}, [
    h('button', {type:'button', class:'ef-btn ef-t1-ja', onclick:function(){ abrirT2({modo:'entrar', depois:function(){ desempilhar(it); abrirT4({naAbertura:true}); }}); }},
      [h('span',{text:T.t1Ja}), h('small',{text:T.t1JaSub})]),
    h('button', {type:'button', class:'ef-btn ef-verde ef-t1-novo', onclick:function(){ abrirT3({modo:'criar', depois:function(semCriancas){ desempilhar(it); abrirT4({naAbertura:true}); if(semCriancas) abrirT5({modo:'nova', fam:st.atual}); }}); }},
      [h('span',{text:T.t1Novo}), h('small',{text:T.t1NovoSub})])
  ]));
  if(us.length){
    el.appendChild(h('div', {class:'ef-texto ef-t1-jatem', text:fmt(T.t1JaTem, {lista:lst})}));
    el.appendChild(btn(T.t1AgoraNao, function(){ desempilhar(it); abrirT4({naAbertura:true}); }, 'ef-leve ef-t1-agoranao'));
  }
  it = empilhar(el, null, 't1');
}

/* ---------- [T2] código da família ("já tenho cadastro") ---------- */
function validarCodigo(c, erroEl, o){
  if(c.length<6){ erroEl.textContent = T.codigoCurto; return false; }
  if(siteDeTeste() && c.indexOf('teste')<0){ erroEl.textContent = T.codigoTeste; return false; }
  if(o.modo==='outra' && fam(c)){ erroEl.textContent = T.t2JaNoCelular; return false; }
  return true;
}
function abrirT2(o){
  o = o || {};
  var el = pop('ef-t2'), it;
  var campo = h('input', {class:'ef-campo ef-codigo', type:'text', maxlength:'40', autocomplete:'off', autocorrect:'off',
                          autocapitalize:'none', spellcheck:'false', enterkeyhint:'search', placeholder:T.t2Exemplo, 'aria-label':T.t2Titulo});
  var erro = h('div', {class:'ef-erro'});
  var res = h('div', {class:'ef-res'});
  var fechar = function(){ desempilhar(it); };
  var procurarBt = btn(T.t2Botao, function(){ procurar(); }, 'ef-verde ef-procurar');
  var procurarMini = btn(T.t2Botao, function(){ procurar(); }, 'ef-verde ef-procurar-mini ef-so-compacto');
  var casoB = (o.modo==='entrar' && lista().some(function(u){ return !familiaDe(u.id); }))
    ? h('div', {class:'ef-texto ef-normal ef-casob', text:fmt(T.t2CasoB, {lista:lista().filter(function(u){ return !familiaDe(u.id); }).map(function(u){ return u.av+' '+u.nome; }).join(' · ')})}) : null;
  var card = h('div', {class:'ef-card', role:'dialog', 'aria-modal':'true'}, [
    h('div', {class:'ef-titulo', text:T.t2Titulo}),
    h('div', {class:'ef-texto', text:T.t2Texto}),
    casoB,
    h('div', {class:'ef-linha-campo'}, [h('b',{class:'ef-so-compacto',text:'🔑'}), campo, procurarMini, btn('✕', fechar, 'ef-leve ef-x-mini ef-so-compacto', {'aria-label':T.cancelar})]),
    erro, res,
    h('div', {class:'ef-linha ef-botoes-cod'}, [btn(T.cancelar, fechar, 'ef-leve ef-cancelar'), procurarBt]),
    btn('✕', fechar, 'ef-leve ef-x-achei', {'aria-label':T.cancelar, title:T.cancelar})
  ]);
  el.appendChild(card);
  campo.addEventListener('keydown', function(e){ if(e.key==='Enter'){ e.preventDefault(); procurar(); } });
  campo.addEventListener('input', function(){ erro.textContent = ''; });
  if(o.valor) campo.value = o.valor;
  it = empilhar(el, fechar, 't2');
  setTimeout(function(){ try{ campo.focus(); }catch(e){} }, 150);

  function limpar(){ res.innerHTML = ''; card.classList.remove('ef-achou'); }
  function botoesDepois(c){
    return h('div', {class:'ef-linha'}, [
      btn(T.guardarDepois, function(){ concluir(c, false); }, 'ef-amarelo ef-guardar-depois'),
      btn(T.tentarDeNovo, function(){ procurar(); }, 'ef-tentar')
    ]);
  }
  function concluir(c, conferida, depoisFn){
    entrarNaFamilia(c, conferida, 't2', o.modo, o.cAntigo);
    fechar();
    if(depoisFn) depoisFn(); else if(o.depois) o.depois(); else abrirT4({});
  }
  function procurar(){
    var c = norm(campo.value);
    erro.textContent = ''; limpar();
    if(!validarCodigo(c, erro, o)){ try{ campo.focus(); }catch(e){} return; }
    try{ campo.blur(); }catch(e){}
    if(!nuvemLigada()){ concluir(c, false); return; }
    if(!online()){ res.appendChild(h('div', {class:'ef-msg', text:T.semInternet})); res.appendChild(botoesDepois(c)); return; }
    res.appendChild(h('div', {class:'ef-msg', text:T.t2Procurando}));
    NS().existeFamilia(c).then(function(r){
      limpar();
      if(r.existe){
        var vis = fichasVisiveis(r.criancas, c);
        /* o pop-up fica largo e mostra só: título, código, crianças e os botões (embaixo, sempre à vista) */
        card.classList.add('ef-achou');
        try{ campo.blur(); }catch(e){}            /* fecha o teclado (a lupa do teclado pode deixar o foco no campo) */
        res.appendChild(h('div', {class:'ef-msg ef-achei', text:T.t2Achei}));
        res.appendChild(h('div', {class:'ef-codigo-achado', text:'🔑 '+c.toUpperCase()}));
        var botoesAchei = h('div', {class:'ef-linha ef-botoes-achei'}, [
          btn(T.t2OutroCodigo, function(){ limpar(); setTimeout(function(){ try{ campo.focus(); campo.select(); }catch(e){} }, 50); }, 'ef-leve ef-outro-codigo')]);
        var g = h('div', {class:'ef-cartoes'});
        g.style.setProperty('--cols', String(vis.length > 4 ? Math.ceil(vis.length/2) : Math.max(1, vis.length)));
        vis.forEach(function(x){
          var apps = Object.keys(x.apps||{}).map(function(a){ return ICONES_APPS[a]||''; }).join('');
          g.appendChild(h('div', {class:'ef-mini'}, [h('span',{class:'ef-av',text:x.av}), h('span',{class:'ef-nome',text:x.nome}), h('span',{class:'ef-prog',text:apps})]));
        });
        res.appendChild(g);
        res.appendChild(botoesAchei);
        if(o.modo==='corrigir'){
          botoesAchei.appendChild(btn(T.ok, function(){ concluir(c, true); }, 'ef-verde ef-escolher'));
          return;
        }
        [
          btn(T.t2Escolher, function(){ S.nuvemCache[c] = {quando:Date.now(), lista:r.criancas}; concluir(c, true); }, 'ef-escolher'),
          btn(T.t2TrazerTodas, function(){
            concluir(c, true, function(){
              var cadeia = Promise.resolve();
              vis.forEach(function(x){ cadeia = cadeia.then(function(){ return localDaFicha(c, x.chave) ? null : trazer(x, c, r.criancas); }); });
              cadeia.then(function(){ if(o.depois) o.depois(); else abrirT4({}); });
            });
          }, 'ef-verde ef-trazer-todas')
        ].forEach(function(b){ botoesAchei.appendChild(b); });
      } else {
        res.appendChild(h('div', {class:'ef-msg ef-naoachei', text:T.t2NaoAchei}));
        res.appendChild(h('div', {class:'ef-texto ef-normal', text:T.t2NaoAcheiDica}));
        if(c.indexOf('-')>=0){
          var c2 = c.replace(/-/g,'');
          if(c2.length>=6) NS().existeFamilia(c2).then(function(r2){
            if(r2.existe && res.isConnected) res.appendChild(btn(fmt(T.t2QuisDizer,{c:c2}), function(){ campo.value = c2; procurar(); }, 'ef-amarelo ef-quisdizer'));
          }, function(){});
        }
      }
    }, function(e){
      limpar();
      res.appendChild(h('div', {class:'ef-msg', text: e && e.offline ? T.semInternet : fmt(T.erro,{m:(e&&e.message)||''})}));
      res.appendChild(botoesDepois(c));
    });
  }
  return it;
}

/* ---------- [T3] criar o código ("sou novo por aqui") ---------- */
var BICHOS_COD = ['tigre','panda','coruja','raposa','coelho','coala','ponei','leao','girafa','golfinho','tucano','arara'];
function sugerirCodigo(){
  var b = BICHOS_COD[Math.floor(Math.random()*BICHOS_COD.length)];
  var n = String(1000+Math.floor(Math.random()*9000));
  return (siteDeTeste() ? 'teste-' : '')+b+'-'+n;
}
function abrirT3(o){
  o = o || {};
  var el = pop('ef-t3'), it;
  var campo = h('input', {class:'ef-campo ef-codigo', type:'text', maxlength:'40', autocomplete:'off', autocorrect:'off',
                          autocapitalize:'none', spellcheck:'false', enterkeyhint:'done', 'aria-label':T.t3Titulo});
  campo.value = sugerirCodigo();
  var erro = h('div', {class:'ef-erro'});
  var fechar = function(){ desempilhar(it); };
  var criarBt = btn(T.t3Botao, function(){ criar(); }, 'ef-verde ef-criar');
  var criarMini = btn(T.t3Botao, function(){ criar(); }, 'ef-verde ef-criar-mini ef-so-compacto');
  var card = h('div', {class:'ef-card', role:'dialog', 'aria-modal':'true'}, [
    h('div', {class:'ef-titulo', text:T.t3Titulo}),
    h('div', {class:'ef-texto ef-normal', text:T.t3Texto}),
    h('div', {class:'ef-linha-campo'}, [h('b',{class:'ef-so-compacto',text:'🌱'}), campo, criarMini, btn('✕', fechar, 'ef-leve ef-so-compacto', {'aria-label':T.cancelar})]),
    erro,
    h('div', {class:'ef-linha ef-botoes-cod'}, [btn(T.cancelar, fechar, 'ef-leve ef-cancelar'), criarBt])
  ]);
  el.appendChild(card);
  campo.addEventListener('keydown', function(e){ if(e.key==='Enter'){ e.preventDefault(); criar(); } });
  campo.addEventListener('input', function(){ erro.textContent=''; });
  it = empilhar(el, fechar, 't3');

  function anotar(c){
    card.innerHTML = '';
    card.appendChild(h('div', {class:'ef-titulo', text:T.t3Anote}));
    card.appendChild(h('div', {class:'ef-titulo-grande ef-codigo-anotar', text:c}));
    card.appendChild(h('div', {class:'ef-texto ef-normal', text:T.t3AnoteTexto}));
    card.appendChild(h('div', {class:'ef-linha'}, [btn(T.t3JaAnotei, function(){
      fechar();
      var sem = !daFamilia(c).length;
      if(o.depois) o.depois(sem); else { abrirT4({}); if(sem) abrirT5({modo:'nova', fam:c}); }
    }, 'ef-verde ef-ja-anotei')]));
  }
  function feito(c, conferida){ entrarNaFamilia(c, conferida, 't3', o.modo==='corrigir'?'corrigir':(o.modo==='outra'?'outra':'criar'), o.cAntigo); anotar(c); }
  function criar(){
    var c = norm(campo.value);
    erro.textContent = '';
    if(!validarCodigo(c, erro, {modo:o.modo==='corrigir'?'outra':o.modo})) return;
    try{ campo.blur(); }catch(e){}
    if(!nuvemLigada() || !nuvemV4() || !online()){ feito(c, false); return; }
    criarBt.disabled = true;
    NS().existeFamilia(c).then(function(r){
      criarBt.disabled = false;
      if(r.existe){ erro.textContent = T.t3JaExiste; return; }
      feito(c, true);
    }, function(){ criarBt.disabled = false; feito(c, false); });
  }
  return it;
}

/* ---------- [T4] 🦉 Quem vai estudar hoje? (e [T7] arrumar) ---------- */
function abrirT4(o){
  o = o || {};
  var ja = aberta('t4');
  if(ja){ if(S.sobConfig) mostrarRaiz(true); if(o.naAbertura) ja.naAbertura = true; ja.render(); return ja; }
  var el = tela('ef-t4');
  var it = empilhar(el, null, 't4');
  it.naAbertura = !!o.naAbertura;
  it.fechar = function(){
    if(S.arrumando){ S.arrumando = false; it.render(); return; }
    if(it.naAbertura || !lista().length) return;     /* precisa escolher uma criança */
    S.arrumando = false; desempilhar(it);
  };
  it.render = function(){ renderT4(it); };
  S.arrumando = false;
  if(S.avisoMigracao){ toast(S.avisoMigracao, 3500); S.avisoMigracao = ''; }
  it.render();
  buscarNuvemT4(it);
  conferirFamilias(); processarMudancas();
  return it;
}
function buscarNuvemT4(it){
  if(!nuvemLigada() || !online() || !NS().listarUsuarios) return;
  st.familias.filter(function(f){ return f.conferida; }).forEach(function(f){
    listaNuvem(f.c, true).then(function(){ if(aberta('t4')===it) it.render(); }, function(){});
  });
}
function cardCrianca(u, it){
  var r = {}; try{ r = A.resumo(u.id) || {}; }catch(e){}
  var b = h('div', {class:'ef-crianca'+(u.id===atualId()?' ef-atual':''), role:'button', tabindex:'0', 'data-id':u.id}, [
    h('span', {class:'ef-av', text:u.av}), h('span', {class:'ef-nome', text:u.nome}),
    r.linha ? h('span', {class:'ef-prog', text:r.linha}) : null,
    (r.barra!=null) ? h('span', {class:'ef-barra'}, [h('i', {style:'width:'+Math.round(Math.max(0,Math.min(1,r.barra))*100)+'%'})]) : null
  ]);
  if(S.arrumando){
    b.appendChild(h('span', {class:'ef-acoes-card'}, [
      btn('✏️', function(ev){ ev.stopPropagation(); abrirT5({modo:'mudar', id:u.id}); }, 'ef-mudar', {'aria-label':T.t5Mudar}),
      btn('🗑️', function(ev){ ev.stopPropagation(); pedirTirar(u.id); }, 'ef-tirar', {'aria-label':T.t7Tirar})
    ]));
  } else {
    b.addEventListener('click', function(){ var t = aberta('t4'); escolher(u.id, !!(t && t.naAbertura)); });
  }
  return b;
}
function renderT4(it){
  var el = it.el; el.innerHTML = '';
  el.classList.toggle('ef-arrumando', !!S.arrumando);
  var us = lista();
  var podeVoltar = !it.naAbertura && us.length;
  var top = h('div', {class:'ef-topo'}, [
    podeVoltar ? btn(T.voltar, function(){ it.fechar(); }, 'ef-leve ef-voltar') : null,
    h('h1', {class:'ef-titulo', text: S.arrumando ? T.t7Titulo : T.t4Titulo}),
    (C && typeof C.abrirConfig==='function') ? botaoConfigT4() : null,
    btn('⛶', function(){ telaCheia(); }, 'ef-icone ef-leve', {title:T.telaCheia, 'aria-label':T.telaCheia})
  ]);
  el.appendChild(top);
  if(S.arrumando) el.appendChild(h('div', {class:'ef-texto ef-normal', text:T.t7Sub}));
  var meio = h('div', {class:'ef-meio'});
  el.appendChild(meio);
  /* perguntas para o adulto: famílias a conferir, mudanças de nome em outro app, repetidas */
  st.familias.filter(function(f){ return f.problema; }).forEach(function(f){
    var av = h('div', {class:'ef-aviso ef-aviso-familia'});
    if(f.problema==='nao-existe'){
      av.appendChild(h('span', {text:fmt(T.pergNaoExiste, {c:f.c})}));
      av.appendChild(btn(T.pergConferir, function(){ abrirT2({modo:'corrigir', cAntigo:f.c, depois:function(){ it.render(); }}); }, 'ef-amarelo'));
      av.appendChild(btn(T.pergCriarCom, function(){ var g = fam(f.c); g.conferida = true; delete g.problema; salvar(); marcarTodasPendentes(f.c); try{ NS().sincronizar(); }catch(e){} atualizar(true); }, 'ef-verde'));
    } else {
      av.appendChild(h('span', {text:fmt(T.pergJaExiste, {c:f.c})}));
      av.appendChild(btn(T.pergEMinha, function(){ var g = fam(f.c); g.conferida = true; delete g.problema; salvar(); marcarTodasPendentes(f.c); try{ NS().sincronizar(); }catch(e){} atualizar(true); }, 'ef-verde'));
      av.appendChild(btn(T.pergOutro, function(){ abrirT3({modo:'corrigir', cAntigo:f.c, depois:function(){ it.render(); }}); }, 'ef-amarelo'));
    }
    meio.appendChild(av);
  });
  avisosMudanca(meio, it);
  if(S.arrumando) repetidas().forEach(function(p){
    var u1 = local(p.primeira.id) || p.primeira, u2 = p.segunda;
    meio.appendChild(h('div', {class:'ef-aviso'}, [h('span', {text:fmt(T.t7Repetida, {e:u2.av, nome:u2.nome})}),
      btn(T.t7Juntar, function(){ juntarRepetidas(u1.id, u2.id); }, 'ef-verde')]));
  });
  /* grupos por família (um título por família quando há 2 ou mais) */
  var grupos = [];
  st.familias.forEach(function(f){ grupos.push({ c:f.c, us:daFamilia(f.c) }); });
  var semFam = us.filter(function(u){ return !familiaDe(u.id) || !fam(familiaDe(u.id)); });
  if(semFam.length || !grupos.length) grupos.push({ c:'', us:semFam });
  var varios = grupos.length>1;
  grupos.forEach(function(g){
    if(varios) meio.appendChild(h('div', {class:'ef-grupo-tit', text: g.c ? ('👨‍👩‍👧 '+fmt(T.t4Familia,{c:mascara(g.c)}).replace('🔑 ','')) : T.t4SemFamilia}));
    var grade = h('div', {class:'ef-grade', 'data-familia':g.c});
    g.us.forEach(function(u){ grade.appendChild(cardCrianca(u, it)); });
    /* crianças da família que estão na nuvem e não neste celular (D6) */
    var fi = fam(g.c);
    var cc = g.c && S.nuvemCache[g.c];
    if(!S.arrumando && fi && fi.conferida && cc && online()){
      /* fichas para onde uma criança DESTE celular mudou em outro app: quem
         decide é o aviso "MUDOU PARA… MUDAR AQUI TAMBÉM?" (senão viram duas) */
      var alvos = {};
      g.us.forEach(function(u){ var mx = cc.lista.filter(function(x){ return x.chave===chaveDe(u.nome,u.av); })[0]; var fm = mx && movida(cc.lista, mx, g.c); if(fm) alvos[fm.chave] = 1; });
      fichasVisiveis(cc.lista, g.c).forEach(function(x){
        if(localDaFicha(g.c, x.chave) || alvos[x.chave]) return;
        var b = h('div', {class:'ef-crianca ef-nuvemcard', role:'button', tabindex:'0', 'data-chave':x.chave}, [
          h('span', {class:'ef-av', text:x.av}), h('span', {class:'ef-nome', text:x.nome+' ☁️'}), h('span', {class:'ef-prog', text:T.t4Trazer})]);
        b.addEventListener('click', function(){ trazer(x, g.c, cc.lista).then(function(id){ if(id) escolher(id); }); });
        grade.appendChild(b);
      });
    }
    if(!S.arrumando && (g.c || !st.familias.length) && g.us.length < max()){
      var nv = h('div', {class:'ef-crianca ef-novo', role:'button', tabindex:'0'}, [h('span',{class:'ef-av',text:'➕'}), h('span',{class:'ef-nome',text:T.t4Nova.replace('➕ ','')})]);
      nv.addEventListener('click', function(){ abrirT5({modo:'nova', fam:g.c}); });
      grade.appendChild(nv);
    }
    meio.appendChild(grade);
  });
  /* barra de botões */
  var barra = h('div', {class:'ef-barra-botoes'});
  if(S.arrumando){
    barra.appendChild(btn(T.t7Terminei, function(){ S.arrumando = false; it.render(); }, 'ef-verde ef-terminei'));
  } else {
    barra.appendChild(btn(T.t4Buscar, function(){ abrirT6(); }, 'ef-buscar'));
    if(nuvemLigada() && us.length) barra.appendChild(btn(T.t4Atualizar, function(){ atualizarAgora(); }, 'ef-atualizar'));
    if(us.length) barra.appendChild(btn(T.t4Arrumar, function(){ S.arrumando = true; it.render(); }, 'ef-arrumar'));
  }
  el.appendChild(barra);
  /* rodapé: bolinha + frase e a família */
  var s = situacao();
  var rod = h('div', {class:'ef-rodape'}, [
    h('div', {class:'ef-status ef-status-t4'}, [h('span', {class:'ef-ponto ef-ponto-solto ef-p-'+s.cor}), h('span', {class:'ef-status-txt', text:T.nuvem+' · '+s.txt})]),
    nuvemLigada() ? btn(st.familias.length ? fmt(T.t4Familia, {c:mascara(st.atual)}) : T.t4SemFamilia,
        function(){ if(st.familias.length) abrirT8(); else abrirT1Sobre(); }, 'ef-leve ef-familia-link') : null
  ]);
  el.appendChild(rod);
}
function botaoConfigT4(){
  var b = btn('⚙️', function(){ abrirConfigDoApp(); }, 'ef-icone ef-leve ef-t4-config', {title:T.configuracoes, 'aria-label':T.configuracoes});
  var p = h('span', {class:'ef-ponto'}); b.appendChild(p); S.pontos.push(p);
  var s = situacao(); p.className = 'ef-ponto ef-p-'+s.cor; p.setAttribute('data-cor', s.cor); p.title = T.nuvem+': '+s.txt;
  return b;
}
function abrirT1Sobre(){ abrirT2({modo:'entrar', depois:function(){ var t = aberta('t4'); if(t) t.render(); }}); }
function avisosMudanca(meio, it){
  st.familias.forEach(function(f){
    var cc = S.nuvemCache[f.c]; if(!cc) return;
    daFamilia(f.c).forEach(function(u){
      var ch = chaveDe(u.nome, u.av);
      var minha = cc.lista.filter(function(x){ return x.chave===ch; })[0];
      if(!minha || !minha.movidoPara || (Date.now() - (st.recusas[f.c+'/'+ch]||0)) < DIA) return;   /* "agora não" vale 1 dia */
      var fim = fimDaCadeia(cc.lista, ch);
      if(!fim || fim.chave===ch || localDaFicha(f.c, fim.chave)) return;
      meio.appendChild(h('div', {class:'ef-aviso ef-aviso-mudou'}, [
        h('span', {text:fmt(T.t7Mudou, {e1:u.av, n1:u.nome, e2:fim.av, n2:fim.nome})}),
        btn(T.t7MudarSim, function(){
          try{ A.mudar(u.id, fim.nome, fim.av); }catch(e){}
          NS().recuperar(u.id, fim.nome, fim.av, false, f.c).catch(function(){}).then(function(){
            try{ NS().marcarPendente(u.id); }catch(e){}
            toast(fmt(T.t5Agora, {e:fim.av, nome:fim.nome, bicho:nomeBicho(fim.av)})); atualizar(true);
          });
        }, 'ef-verde'),
        btn(T.t7AgoraNao, function(){ st.recusas[f.c+'/'+ch] = Date.now(); salvar(); it.render(); }, 'ef-leve')
      ]));
    });
  });
}
function juntarRepetidas(id1, id2){
  var u2 = local(id2); if(!u2) return;
  perguntar({ titulo:fmt(T.t7Repetida,{e:u2.av,nome:u2.nome}), linhas:[T.copiasPerguntaTexto], sim:T.t7Juntar }).then(function(ok){
    if(!ok) return;
    var dados; try{ dados = A.exportar(id2); }catch(e){ return; }
    try{ A.importar(id1, dados); }catch(e){ toast(fmt(T.erroTxt,{m:T.naoDeu})); return; }
    try{ NS() && NS().marcarPendente(id1); }catch(e){}
    efetivarTirar(id2, true, false);     /* o progresso já foi juntado na outra: a cópia é só reserva */
  });
}
function telaCheia(){
  try{
    if(window.EscolaPWA && window.EscolaPWA.telaCheia){ window.EscolaPWA.telaCheia(); return; }
    var d = document.documentElement; (d.requestFullscreen||d.webkitRequestFullscreen||function(){}).call(d);
  }catch(e){}
}
function atualizarAgora(){
  var n = NS();
  if(!nuvemLigada()){ toast(T.desligada); return; }
  if(!st.familias.length){ abrirT1Sobre(); return; }
  toast(T.t4Atualizando, 8000);
  S.nuvemCache = {};
  conferirFamilias().then(function(){ return processarMudancas(); }).then(function(){ return n.sincronizar(); }).then(function(ok){
    var s = n.status();
    toast(ok && !s.pendentes ? T.atualizado : (s.estado==='offline' || !online() ? T.atualizadoOffline : (s.estado==='erro' ? fmt(T.erro,{m:s.detalhe}) : situacao().txt)));
    var t = aberta('t4'); if(t) buscarNuvemT4(t);
    atualizar(true);
  });
}

/* ---------- [T5] 🌟 qual é o seu nome? ---------- */
function abrirT5(o){
  o = o || {};
  var u = o.modo==='mudar' ? local(o.id) : null;
  if(o.modo==='mudar' && !u) return;
  var c = o.modo==='mudar' ? familiaDe(o.id) : (o.fam!=null ? o.fam : st.atual);
  if(o.modo!=='mudar' && daFamilia(c).length >= max()){ toast(fmt(T.t5Maximo,{n:max()})); return; }
  var el = tela('ef-t5'), it;
  var escolhido = (u && oficial(u.av)) ? u.av : null;
  var campo = h('input', {class:'ef-campo ef-nome-campo', type:'text', maxlength:'14', placeholder:T.t5Campo, autocomplete:'off',
                          autocorrect:'off', autocapitalize:'words', spellcheck:'false', enterkeyhint:'done', 'aria-label':T.t5Campo});
  if(u) campo.value = u.nome;
  var bichos = h('div', {class:'ef-bichos', role:'radiogroup', 'aria-label':'Bichinhos'});
  var esc = h('div', {class:'ef-escolhido'});
  var fechar = function(){ desempilhar(it); };
  var voltarBt = btn(T.voltar, fechar, 'ef-leve ef-voltar');
  var prontoBt = btn(T.t5Pronto, function(){ pronto(); }, 'ef-verde ef-pronto');
  var voltarMini = btn('←', fechar, 'ef-leve ef-voltar-mini ef-so-compacto', {'aria-label':T.voltar});
  var prontoMini = btn(T.t5Pronto, function(){ pronto(); }, 'ef-verde ef-pronto-mini ef-so-compacto');
  function desenhar(){
    bichos.innerHTML = '';
    bichinhos().forEach(function(b){
      var x = h('button', {type:'button', class:'ef-bicho'+(b.e===escolhido?' ef-on':''), title:b.nome, 'aria-label':b.nome, role:'radio',
                            'aria-checked': b.e===escolhido ? 'true':'false', text:b.e});
      x.addEventListener('click', function(){ escolhido = b.e; desenhar(); });
      bichos.appendChild(x);
    });
    esc.textContent = escolhido ? fmt(T.t5Escolheu, {e:escolhido, nome:nomeBicho(escolhido)}) : (u && !oficial(u.av) ? fmt(T.t5BichoAntigo,{e:u.av}) : '');
  }
  desenhar();
  var miolo = h('div', {class:'ef-miolo'}, [
    h('h1', {class:'ef-titulo', text: o.modo==='mudar' ? T.t5Mudar : T.t5Titulo}),
    h('div', {class:'ef-linha-campo'}, [voltarMini, campo, prontoMini]),
    h('div', {class:'ef-sub', text:T.t5Escolha}),
    bichos, esc,
    h('div', {class:'ef-linha ef-botoes-t5'}, [voltarBt, prontoBt])
  ]);
  el.appendChild(miolo);
  campo.addEventListener('keydown', function(e){
    if(e.key!=='Enter') return;
    e.preventDefault();
    if(escolhido) pronto(); else { try{ campo.blur(); }catch(er){} toast(T.t5EnterSemBicho); }
  });
  it = empilhar(el, fechar, 't5');
  it.campo = campo;
  setTimeout(function(){ try{ campo.focus(); }catch(e){} }, 200);

  function pronto(){
    var nome = (campo.value||'').trim().replace(/\s+/g,' ').slice(0,14);
    if(!nome){ toast(T.t5SemNome); try{ campo.focus(); }catch(e){} return; }
    if(!escolhido || !oficial(escolhido)){ try{ campo.blur(); }catch(e){} toast(T.t5SemBicho); return; }
    var ch = chaveDe(nome, escolhido);
    var igual = localDaFicha(c, ch);
    if(o.modo==='mudar'){
      if(igual && igual.id!==o.id){ toast(fmt(T.t5JaExisteAqui, {e:escolhido, nome:nome})); return; }
      var feitoMudar = function(){ fechar(); mudarCrianca(o.id, nome, escolhido); toast(fmt(T.t5Agora, {e:escolhido, nome:nome, bicho:nomeBicho(escolhido)})); };
      var ccM = c && S.nuvemCache[c];
      var outraNuvem = (ccM && ch!==chaveDe(u.nome,u.av)) ? ccM.lista.filter(function(x){ return x.chave===ch && !x.movidoPara; })[0] : null;
      if(outraNuvem){
        perguntar({ titulo:fmt(T.t5JaNaNuvem,{e:escolhido,nome:nome}), linhas:[T.t5JaNaNuvemTexto], sim:T.t7Juntar }).then(function(ok){ if(ok) feitoMudar(); });
        return;
      }
      feitoMudar();
      return;
    }
    if(igual){ toast(fmt(T.t5JaAqui, {e:igual.av, nome:igual.nome})); fechar(); setTimeout(function(){ escolher(igual.id); }, 700); return; }
    if(daFamilia(c).length >= max()){ toast(fmt(T.t5Maximo,{n:max()})); return; }
    var cc = c && S.nuvemCache[c];
    var naNuvem = cc ? cc.lista.filter(function(x){ return x.chave===ch; })[0] : null;
    if(naNuvem){ fechar(); trazer(naNuvem, c, cc.lista).then(function(id){ if(id) escolher(id); }); return; }
    var nomeN = chaveDe(nome,'x').replace(/_x$/,'');
    var mesmoNome = daFamilia(c).filter(function(x){ return chaveDe(x.nome,'x').replace(/_x$/,'')===nomeN; })[0];
    var mesmoNomeNuvem = (!mesmoNome && cc) ? fichasVisiveis(cc.lista, c).filter(function(x){ return x.chave.replace(/_[^_]*$/,'')===nomeN; })[0] : null;
    var outro = mesmoNome || mesmoNomeNuvem;
    if(outro){
      perguntar({ titulo:fmt(T.t5EVoce, {e:outro.av, nome:outro.nome}), sim:fmt(T.t5SouEu,{e:outro.av}), nao:T.t5Outra }).then(function(souEu){
        if(souEu){
          fechar();
          if(mesmoNome) escolher(mesmoNome.id);
          else trazer(mesmoNomeNuvem, c, cc.lista).then(function(id){ if(id) escolher(id); });
        } else criarNova(nome, escolhido);
      });
      return;
    }
    criarNova(nome, escolhido);
  }
  function criarNova(nome, av){
    var id;
    try{ id = A.criar(nome, av, 'nova'); }catch(e){ toast(fmt(T.erroTxt,{m:T.naoDeu})); return; }
    st.criancas[id] = c; salvar();
    juntarLixeira(id, c);
    fechar();
    var fi = fam(c), n = NS();
    var rec = Promise.resolve(false);
    /* mesmo nome + bichinho que já existe na nuvem: o progresso volta sozinho */
    if(c && fi && fi.conferida && nuvemLigada() && online() && n){
      rec = Promise.race([
        n.recuperar(id, nome, av, true, c).then(function(achou){ if(achou) toast(fmt(T.t5AcheiNuvem,{e:av,nome:nome}), 2200); return achou; }, function(){ return false; }),
        new Promise(function(r){ setTimeout(function(){ r(false); }, 6000); })
      ]);
    }
    rec.then(function(){
      var extra = (C.passoExtra ? C.passoExtra(id) : null);
      return extra && extra.then ? extra : null;
    }).then(function(){ setTimeout(function(){ escolher(id); }, 400); }, function(){ escolher(id); });
  }
  return it;
}

/* ---------- [T6] ☁️ buscar na nuvem ---------- */
function abrirT6(){
  var ja = aberta('t6'); if(ja){ if(S.sobConfig) mostrarRaiz(true); ja.render(); return ja; }
  var el = tela('ef-t6'), it;
  it = empilhar(el, function(){ desempilhar(it); }, 't6');
  it.render = function(forcar){ renderT6(it, forcar); };
  it.render(true);
  return it;
}
function renderT6(it, forcar){
  var el = it.el; el.innerHTML = '';
  el.appendChild(h('div', {class:'ef-topo'}, [btn(T.voltar, function(){ it.fechar(); }, 'ef-leve ef-voltar'), h('h1', {class:'ef-titulo', text:T.t6Titulo})]));
  var corpo = h('div', {class:'ef-corpo'}); el.appendChild(corpo);
  var msg = h('div', {class:'ef-msg ef-t6-msg'}); corpo.appendChild(msg);
  var listas = h('div'); corpo.appendChild(listas);
  var fams = st.familias.filter(function(f){ return f.conferida; });
  if(!nuvemLigada()) msg.textContent = T.desligada;
  else if(!st.familias.length) msg.textContent = T.t6SemFamilia;
  else if(!online()) msg.textContent = T.semInternet;
  else if(!fams.length) msg.textContent = fmt(T.aConferir, {c:mascara(st.atual)});
  else {
    msg.textContent = T.t6Procurando;
    var feitas = 0, alguma = false;
    fams.forEach(function(f){
      listaNuvem(f.c, forcar).then(function(l){
        feitas++;
        if(l.length) alguma = true;
        if(fams.length>1) listas.appendChild(h('div', {class:'ef-secao-tit', text:fmt(T.t4Familia,{c:mascara(f.c)})}));
        var g = h('div', {class:'ef-cartoes', 'data-familia':f.c});
        var antigos = [];
        l.forEach(function(x){
          if(x.oculta) return;
          var fim = movida(l, x, f.c); if(fim){ antigos.push({x:x, fim:fim}); return; }
          var loc = localDaFicha(f.c, x.chave);
          var apps = Object.keys(x.apps||{}).map(function(a){ return ICONES_APPS[a]||''; }).join('');
          var b = h('button', {type:'button', class:'ef-mini'+(loc?' ef-ja':''), 'data-chave':x.chave}, [
            h('span',{class:'ef-av',text:x.av}), h('span',{class:'ef-nome',text:x.nome}),
            h('span',{class:'ef-prog',text:apps}), h('span',{class:'ef-prog ef-normal',text: loc ? T.t6JaAqui : T.t6Trazer})]);
          b.addEventListener('click', function(){
            if(loc) juntar(loc.id, x, f.c).then(function(){ it.render(); });
            else trazer(x, f.c, l).then(function(){ it.render(); });
          });
          g.appendChild(b);
        });
        listas.appendChild(g);
        if(antigos.length){
          listas.appendChild(h('div', {class:'ef-secao-tit', text:T.t6Antigos}));
          var ga = h('div', {class:'ef-cartoes'});
          antigos.forEach(function(a){
            var b = h('button', {type:'button', class:'ef-mini ef-antigo'}, [h('span',{class:'ef-av',text:a.x.av}), h('span',{class:'ef-nome',text:a.x.nome}),
              h('span',{class:'ef-prog', text:fmt(T.t6AntigoPara,{e:a.fim.av,nome:a.fim.nome})})]);
            b.addEventListener('click', function(){
              var alvo = localDaFicha(f.c, a.fim.chave);
              if(alvo){ juntar(alvo.id, a.x, f.c).then(function(){ it.render(); }); return; }
              /* a criança nova ainda não está aqui: traz ela (e a antiga é juntada junto) */
              var nova = l.filter(function(x){ return x.chave===a.fim.chave; })[0];
              if(nova) trazer(nova, f.c, l).then(function(){ it.render(); });
            });
            ga.appendChild(b);
          });
          listas.appendChild(ga);
        }
        if(feitas===fams.length) msg.textContent = alguma ? T.t6Explica : T.t6Nenhuma;
      }, function(e){ feitas++; msg.textContent = (e && e.offline) ? T.semInternet : fmt(T.erro,{m:(e&&e.message)||''}); });
    });
  }
  /* lixeira do celular */
  var lix = lerLixeira();
  if(lix.length){
    corpo.appendChild(h('div', {class:'ef-secao-tit', text:T.t6Lixeira}));
    var gl = h('div', {class:'ef-cartoes ef-lixeira'});
    lix.forEach(function(item){
      var b = h('button', {type:'button', class:'ef-mini'}, [h('span',{class:'ef-av',text:item.av}), h('span',{class:'ef-nome',text:item.nome}),
        h('span',{class:'ef-prog',text:new Date(item.quando).toLocaleDateString('pt-BR')}), h('span',{class:'ef-prog',text:T.t6TrazerDeVolta})]);
      b.addEventListener('click', function(){ trazerDaLixeira(item); it.render(); });
      gl.appendChild(b);
    });
    corpo.appendChild(gl);
  }
  corpo.appendChild(h('div', {class:'ef-barra-botoes'}, [nuvemLigada() ? btn(T.t6Procurar, function(){ it.render(true); }, 'ef-procurar-de-novo') : null]));
}

/* ---------- 🕘 cópias de cada dia (só adulto) ---------- */
function abrirCopias(){
  var id = atualId(), u = id ? local(id) : null;
  var el = tela('ef-copias'), it;
  it = empilhar(el, function(){ desempilhar(it); }, 'copias');
  el.appendChild(h('div', {class:'ef-topo'}, [btn(T.voltar, function(){ it.fechar(); }, 'ef-leve ef-voltar'), h('h1', {class:'ef-titulo', text:T.copias})]));
  var corpo = h('div', {class:'ef-corpo'}); el.appendChild(corpo);
  var msg = h('div', {class:'ef-msg'}); corpo.appendChild(msg);
  var g = h('div', {class:'ef-cartoes'}); corpo.appendChild(g);
  if(!u){ msg.textContent = T.semCrianca; return it; }
  var c = familiaDe(id);
  if(!nuvemLigada()){ msg.textContent = T.desligada; return it; }
  if(!c){ msg.textContent = T.faltaCodigo; return it; }
  if(!online()){ msg.textContent = T.semInternet; return it; }
  msg.textContent = fmt(T.copiasProcurando, {nome:u.nome});
  NS().listarVersoes(u.nome, u.av, c).then(function(l){
    if(!l.length){ msg.textContent = fmt(T.copiasNenhuma, {nome:u.nome}); return; }
    msg.textContent = T.copiasExplica; msg.classList.add('ef-normal');
    l.forEach(function(v){
      var p = v.dia.split('-'), data = p[2]+'/'+p[1]+'/'+p[0];
      var res = ''; try{ res = A.resumoDados ? A.resumoDados(v.dados||{}) : ''; }catch(e){}
      var b = h('button', {type:'button', class:'ef-mini', 'data-dia':v.dia}, [h('span',{class:'ef-av',text:'🗓️'}), h('span',{class:'ef-nome',text:data}), h('span',{class:'ef-prog',text:res})]);
      b.addEventListener('click', function(){
        perguntar({ titulo:fmt(T.copiasPergunta,{data:data}), linhas:[T.copiasPerguntaTexto], sim:T.juntar }).then(function(ok){
          if(!ok) return;
          NS().juntarVersao(u.id, u.nome, u.av, v.dia, c).then(function(r){
            toast(r ? fmt(T.copiasJuntada,{data:p[2]+'/'+p[1]}) : T.copiasNaoAchei); atualizar(true);
          }, function(e){ toast(fmt(T.erroTxt,{m:(e&&e.message)||T.naoDeu})); });
        });
      });
      g.appendChild(b);
    });
  }, function(e){ msg.textContent = (e && e.offline) ? T.semInternet : fmt(T.erro,{m:(e&&e.message)||''}); });
  return it;
}

/* ---------- [T8] 👨‍👩‍👧 famílias neste celular ---------- */
function abrirT8(){
  var ja = aberta('t8'); if(ja){ if(S.sobConfig) mostrarRaiz(true); ja.render(); return ja; }
  var el = tela('ef-t8'), it;
  it = empilhar(el, function(){ desempilhar(it); }, 't8');
  it.mostrar = {};
  it.render = function(){ renderT8(it); };
  it.render();
  return it;
}
function liberarOutraFamilia(){
  if(st.familias.length >= MAX_FAMILIAS){ toast(fmt(T.t8Maximo,{n:MAX_FAMILIAS})); return Promise.resolve(false); }
  if(dentroDoBloqueio() && !st.liberouSegundaFamilia){
    return perguntar({ titulo:fmt(T.t8Bloqueio,{data:fimDoBloqueio()}), linhas:[T.avisoVersaoAntiga], sim:T.liberar, adulto:true, perigo:true }).then(function(ok){
      if(ok){ st.liberouSegundaFamilia = true; salvar(); }
      return ok;
    });
  }
  return Promise.resolve(true);
}
function renderT8(it){
  var el = it.el; el.innerHTML = '';
  el.appendChild(h('div', {class:'ef-topo'}, [btn(T.voltar, function(){ it.fechar(); }, 'ef-leve ef-voltar'), h('h1', {class:'ef-titulo', text:T.t8Titulo})]));
  var corpo = h('div', {class:'ef-corpo'}); el.appendChild(corpo);
  var s = NS() && nuvemLigada() ? NS().status() : { porFamilia:{} };
  st.familias.forEach(function(f){
    var quem = daFamilia(f.c).map(function(u){ return u.av+' '+u.nome; }).join(' · ') || '—';
    var pend = (s.porFamilia||{})[f.c] || 0;
    var cor = f.problema ? 'vermelho' : (!f.conferida || pend ? 'amarelo' : 'verde');
    var estado = f.problema ? fmt(T.confiraCodigo,{c:''}).trim() : (!f.conferida ? T.t8AConferir : (pend ? fmt(T.t8Esperando,{n:pend}) : ''));
    var cod = h('span', {class:'ef-cod', text: it.mostrar[f.c] ? f.c : mascara(f.c)});
    corpo.appendChild(h('div', {class:'ef-fam-linha', 'data-familia':f.c}, [
      h('span', {text:'🔑'}), cod,
      it.mostrar[f.c] ? null : botaoAdulto(T.t8Mostrar, function(){ it.mostrar[f.c] = true; it.render(); }, 'ef-leve ef-mostrar', true),
      h('span', {class:'ef-quem', text:quem}),
      h('span', {class:'ef-status'}, [h('span', {class:'ef-ponto ef-ponto-solto ef-p-'+cor}), estado ? h('span',{text:estado}) : null])
    ]));
  });
  if(dentroDoBloqueio() && !st.liberouSegundaFamilia) corpo.appendChild(h('div', {class:'ef-texto', text:fmt(T.t8Bloqueio,{data:fimDoBloqueio()})}));
  corpo.appendChild(h('div', {class:'ef-texto ef-dica-adulto', text:T.adultoDica}));
  corpo.appendChild(h('div', {class:'ef-barra-botoes'}, [
    botaoAdulto(T.t8Entrar, function(){ liberarOutraFamilia().then(function(ok){ if(ok) abrirT2({modo:'outra', depois:function(){ it.render(); var t = aberta('t4'); if(t) t.render(); }}); }); }, 'ef-entrar-outra', true),
    botaoAdulto(T.t8Criar, function(){ liberarOutraFamilia().then(function(ok){ if(ok) abrirT3({modo:'outra', depois:function(){ it.render(); var t = aberta('t4'); if(t) t.render(); }}); }); }, 'ef-criar-outra', true),
    botaoAdulto(T.t8Tirar, function(){ escolherFamiliaParaTirar(it); }, 'ef-perigo ef-tirar-familia', true)
  ]));
}
function escolherFamiliaParaTirar(it){
  if(st.familias.length<2){ perguntar({titulo:T.t8Tirar, linhas:[T.t8SoUma], nao:false, sim:T.ok}); return; }
  perguntar({ titulo:T.t8TirarQual, linhas:[], sim:null, nao:T.cancelar,
              extras: st.familias.map(function(f){ return { texto:'🚪 '+mascara(f.c), valor:f.c, cls:'ef-perigo' }; }) }).then(function(c){
    if(!c || c===true) return;
    perguntar({ titulo:fmt(T.t8TirarPergunta,{c:mascara(c)}), linhas:[T.t8TirarTexto], sim:T.t7BotaoTirar, perigo:true }).then(function(ok){
      if(!ok) return;
      tirarFamilia(c).then(function(){ it.render(); });
    });
  });
}
function tirarFamilia(c){
  var us = daFamilia(c), n = NS();
  var falharam = [];
  var cadeia = Promise.resolve();
  us.forEach(function(u){
    cadeia = cadeia.then(function(){
      if(!nuvemV4() || !nuvemLigada() || !online() || !(fam(c)||{}).conferida){ falharam.push(u); return; }
      return n.garantirGuardado(u.id).then(function(ok){
        var comp = true; try{ comp = A.completoNaNuvem ? A.completoNaNuvem(u.id)!==false : true; }catch(e){ comp = false; }
        if(!ok || !comp) falharam.push(u);
      }, function(){ falharam.push(u); });
    });
  });
  return cadeia.then(function(){
    if(falharam.length){ perguntar({ titulo:T.t7NaoGarante, linhas:[fmt(T.t8TirarNao,{lista:falharam.map(function(u){ return u.av+' '+u.nome; }).join(' · ')})], nao:false, sim:T.ok }); return; }
    var recarregar = false;
    us.forEach(function(u){
      var eraAtual = atualId()===u.id, r = null;
      var f = function(){ r = A.tirar(u.id); };
      try{ if(n && n.semVigiar) n.semVigiar(f); else f(); }catch(e){ return; }
      if(n && n.limparPendencia) n.limparPendencia(u.id);
      delete st.criancas[u.id];
      if(eraAtual || (r && r.recarregar)) recarregar = true;
    });
    if(daFamilia(c).length){ salvar(); atualizar(true); return; }   /* alguma não saiu: a família fica */
    st.familias = st.familias.filter(function(f){ return f.c!==c; });
    st.mudancasPendentes = st.mudancasPendentes.filter(function(m){ return m.fam!==c; });
    if(st.atual===c) st.atual = st.familias.length ? st.familias[0].c : '';
    salvar();
    if(recarregar){ setTimeout(function(){ location.reload(); }, 900); return; }
    atualizar(true);
  });
}

/* ===================== chip, bolinha e seção das Configurações ===================== */
function atualizarChips(){
  var id = atualId(), u = id ? local(id) : null;
  S.chips = S.chips.filter(function(el){ return el.isConnected; });
  S.chips.forEach(function(el){
    var b = el.querySelector('.ef-chip');
    if(!b) return;
    b.style.display = u ? '' : 'none';
    if(u){ b.querySelector('.ef-chip-av').textContent = u.av; b.querySelector('.ef-chip-nome').textContent = String(u.nome).split(' ')[0]; b.title = T.trocar; }
  });
}
function atualizarPontos(){
  var s = situacao();
  S.pontos = S.pontos.filter(function(p){ return p.isConnected; });
  S.pontos.forEach(function(p){ p.className = 'ef-ponto ef-p-'+s.cor; p.title = T.nuvem+': '+s.txt; p.setAttribute('data-cor', s.cor); });
  var t = aberta('t4');
  if(t){ var tx = t.el.querySelector('.ef-status-txt'), pt = t.el.querySelector('.ef-status-t4 .ef-ponto');
    if(tx) tx.textContent = T.nuvem+' · '+s.txt; if(pt) pt.className = 'ef-ponto ef-ponto-solto ef-p-'+s.cor; }
}
function renderSecao(el){
  var s = situacao();
  var id = atualId(), u = id ? local(id) : null;
  var lst = lista().map(function(x){ return x.av+' '+x.nome; }).join(' · ') || '—';
  /* só redesenha se algo mudou (o "👁 mostrar" e um botão sendo segurado não se perdem à toa) */
  var mostrando = (el._efMostrarAte||0) > Date.now();    /* "👁 mostrar" vale por 1 minuto */
  var assinatura = JSON.stringify([s, lst, u && u.av, u && u.nome, st.atual, st.familias.length, nuvemLigada(), mostrando]);
  if(el._efSig===assinatura && el.firstChild) return;
  el._efSig = assinatura;
  el.innerHTML = '';
  el.classList.add('ef-cfg');
  el.appendChild(h('div', {class:'ef-cfg-tit', text:T.cfgSecao}));
  function acoes(l){ return h('span', {class:'ef-cfg-acoes'}, l); }
  el.appendChild(h('div', {class:'ef-cfg-linha ef-cfg-nuvem'}, [
    h('span', {class:'ef-ponto ef-ponto-solto ef-p-'+s.cor}),
    h('span', {class:'ef-cfg-txt', text:fmt(T.cfgNuvem,{frase:s.txt})}),
    nuvemLigada() ? acoes([btn(T.t4Atualizar, function(){ atualizarAgora(); }, 'ef-verde ef-cfg-atualizar')]) : null
  ]));
  el.appendChild(h('div', {class:'ef-cfg-linha ef-cfg-criancas'}, [
    h('span', {class:'ef-cfg-txt', text:fmt(T.cfgCriancas,{lista:lst})}),
    acoes([
      btn(T.trocar, function(){ abrirT4({}); }, 'ef-cfg-trocar'),
      btn(T.t4Arrumar, function(){ var t = abrirT4({}); S.arrumando = true; t.render(); }, 'ef-cfg-arrumar')
    ])
  ]));
  el.appendChild(h('div', {class:'ef-cfg-linha ef-toca ef-cfg-buscar', role:'button', tabindex:'0', onclick:function(){ abrirT6(); }}, [
    h('span', {class:'ef-cfg-txt', text:T.cfgBuscar}), h('span', {class:'ef-cfg-ir', text:'▶'})]));
  el.appendChild(h('div', {class:'ef-cfg-linha ef-cfg-copias'}, [
    h('span', {class:'ef-cfg-txt', text: u ? fmt(T.copiasDe,{e:u.av,nome:u.nome}) : T.copias}),
    acoes([botaoAdulto(T.abrir, function(){ abrirCopias(); }, 'ef-leve ef-cfg-copias-bt', true)])
  ]));
  var cod = h('span', {class:'ef-cfg-cod', text: st.atual ? (mostrando ? st.atual : mascara(st.atual)) : '—'});
  el.appendChild(h('div', {class:'ef-cfg-linha ef-cfg-familia'}, [
    h('span', {class:'ef-cfg-txt'}, [document.createTextNode(fmt(T.cfgFamilia,{c:''})), cod]),
    acoes([
      (st.atual && !mostrando) ? botaoAdulto(T.t8Mostrar, function(){ el._efMostrarAte = Date.now()+60000; cod.textContent = st.atual; setTimeout(function(){ if(el.isConnected) renderSecao(el); }, 60500); }, 'ef-leve ef-cfg-mostrar', true) : null,
      nuvemLigada() ? btn(st.familias.length ? T.cfgFamilias : T.t1Ja, function(){ if(st.familias.length) abrirT8(); else abrirT1Sobre(); }, 'ef-cfg-familias') : null
    ])
  ]));
}
var _atT = null;
function atualizar(tudo){
  if(!st) return;
  if(S.segurando){ S.adiado = (tudo || S.adiado==='tudo') ? 'tudo' : 'pouco'; return; }
  atualizarChips(); atualizarPontos();
  if(tudo){
    S.secoes = S.secoes.filter(function(e){ return e.isConnected; });
    S.secoes.forEach(renderSecao);
    var t = aberta('t4'); if(t) t.render();
    var t8 = aberta('t8'); if(t8) t8.render();
  }
}

/* ===================== API pública ===================== */
window.EscolaFamilia = {
  versao: VERSAO,
  TEXTOS: T,
  /* cfg = { app, nomeApp, iconeApp, maxPorFamilia, criancas:{…}, passoExtra, aoAbrirTelas, aoFecharTelas, fonte, abrirConfig, fecharConfig } */
  iniciar: function(cfg){
    C = cfg || {}; A = C.criancas || {};
    css();
    migrar();
    S.iniciado = true;
    if(siteDeTeste()){
      var mostra = function(){ document.documentElement.classList.add('ef-no-site-teste'); if(!document.querySelector('.ef-teste')) document.body.appendChild(h('div', {class:'ef-teste', text:T.siteTeste})); };
      if(document.body) mostra(); else document.addEventListener('DOMContentLoaded', mostra);
    }
    var n = NS();
    if(n && n.aoMudar) n.aoMudar(function(){ clearTimeout(_atT); _atT = setTimeout(function(){
      if(S.segurando){ if(!S.adiado) S.adiado = 'pouco'; return; }
      atualizar(false); S.secoes.forEach(function(e){ if(e.isConnected) renderSecao(e); }); }, 80); });
    window.addEventListener('online', function(){ setTimeout(function(){ conferirFamilias().then(processarMudancas); atualizar(true); }, 600); });
    window.addEventListener('offline', function(){ atualizar(false); });
    setTimeout(function(){ conferirFamilias().then(processarMudancas); }, 3500);
    setInterval(function(){ if(st.mudancasPendentes.length) processarMudancas(); }, 120000);
    return this;
  },
  /* lista para o NuvemSync.iniciar({usuarios}) com a família de cada criança */
  paraNuvem: function(l){ return st ? paraNuvem(l) : (l||[]); },
  familiaDe: function(id){ return familiaDe(id); },
  familiaAtual: function(){ return st ? st.atual : ''; },
  familias: function(){ return st ? JSON.parse(JSON.stringify(st.familias)) : []; },
  /* o que abrir quando o app abre: T1 (sem família) ou T4 (D2: sempre) */
  abrirInicio: function(){
    if(!st) return;
    if(nuvemLigada() && !st.familias.length) abrirT1();
    else abrirT4({naAbertura:true});
  },
  abrir: function(qual, arg){
    if(!st) return null;
    if(qual==='quem') return abrirT4({});
    if(qual==='inicio') return this.abrirInicio();
    if(qual==='nova') return abrirT5({modo:'nova', fam: arg!=null ? arg : st.atual});
    if(qual==='mudar') return abrirT5({modo:'mudar', id: arg || atualId()});
    if(qual==='nuvem') return abrirT6();
    if(qual==='familias') return abrirT8();
    if(qual==='copias') return abrirCopias();
    if(qual==='codigo') return abrirT2({modo:'entrar'});
    if(qual==='boasvindas') return abrirT1();
    return null;
  },
  montarChip: function(el){
    if(!el) return;
    el.innerHTML = '';
    el.appendChild(h('button', {type:'button', class:'ef-chip', 'aria-label':T.trocar, onclick:function(){ abrirT4({}); }},
      [h('span', {class:'ef-chip-av'}), h('span', {class:'ef-chip-nome'})]));
    if(S.chips.indexOf(el)<0) S.chips.push(el);
    atualizarChips();
  },
  montarPonto: function(botao){
    if(!botao) return;
    var p = botao.querySelector('.ef-ponto');
    if(!p){ p = h('span', {class:'ef-ponto'}); botao.appendChild(p); }
    try{ if(getComputedStyle(botao).position==='static') botao.style.position = 'relative'; }catch(e){}
    if(S.pontos.indexOf(p)<0) S.pontos.push(p);
    atualizarPontos();
  },
  montarSecaoConfig: function(el){
    if(!el) return;
    if(S.secoes.indexOf(el)<0) S.secoes.push(el);
    renderSecao(el);
  },
  atualizar: function(){ atualizar(true); },
  situacao: function(){ return st ? situacao() : { cor:'vermelho', txt:T.desligada }; },
  estaAberto: function(){ return pilha.length>0; },
  fecharTopo: function(){ return fecharTopo(); },
  fecharTudo: function(){ fecharTudo(); },
  toast: toast
};
})();
