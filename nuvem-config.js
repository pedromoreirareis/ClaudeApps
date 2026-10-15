/* =====================================================================
   nuvem-config.js — CONFIGURAÇÃO DA NUVEM (Firebase)
   Escola São Pedro — é o MESMO arquivo para todos os aplicativos.

   O QUE FAZER (veja o guia GUIA_FIREBASE_PASSO_A_PASSO.md, Etapa 7):
   1. Apague as 5 linhas de exemplo que estão entre as duas linhas de ===== abaixo.
   2. No lugar delas, cole o bloco que o Firebase mostrou, que começa com
         const firebaseConfig = {
      e termina com
         };
   3. Salve o arquivo. Não mexa em mais nada.

   Enquanto este arquivo estiver com os campos vazios, os aplicativos
   funcionam normalmente, só que SEM nuvem (tudo fica só no celular).
   ===================================================================== */

/* ======== COLE AQUI (apague daqui ...) ======== */
const firebaseConfig = {
	apiKey: "AIzaSyBjxYeUXIX6tmAtf5xWgUC6wcGO8VsxJqE",
	authDomain: "escola-sao-pedro-5ee62.firebaseapp.com",
	projectId: "escola-sao-pedro-5ee62",
	storageBucket: "escola-sao-pedro-5ee62.firebasestorage.app",
	messagingSenderId: "303759712495",
	appId: "1:303759712495:web:551f8b87c724b2d1fc7b1a"
};
/* ======== (... até aqui) ======== */


/* ---------------------------------------------------------------------
   CÓDIGO DA FAMÍLIA (opcional)
   Se deixar vazio (""), cada aplicativo pergunta o código UMA vez em
   cada celular (Configurações → ☁️ Nuvem → Código da família).
   Isso é o mais seguro, porque o código não fica visível na internet.
   Se preferir não digitar nada nunca, escreva o código aqui entre as
   aspas (ex.: "saopedro-renata-2026"). Mais prático, porém menos privado.
   --------------------------------------------------------------------- */
const codigoDaFamilia = "";


/* ----- não mexa daqui para baixo ----- */
window.NUVEM_CONFIG = {
  apiKey: (typeof firebaseConfig !== 'undefined' && firebaseConfig.apiKey) || '',
  projectId: (typeof firebaseConfig !== 'undefined' && firebaseConfig.projectId) || '',
  familia: codigoDaFamilia || ''
};
