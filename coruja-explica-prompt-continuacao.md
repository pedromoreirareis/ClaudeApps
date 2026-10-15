# 🦉 Prompt de continuação — Coruja Explica (v3.1)

**Passagem de 14/10/2026.** Use este arquivo para começar a **conversa nova** do Coruja Explica.

> Este arquivo **substitui** o documento antigo do Projeto `claude/coruja-explica-prompt-continuacao.md` (de 24/09). Use este.

## O que anexar na conversa nova (Pedro)

**Sempre:**
1. **`corujaexplica-completo-v3.1.zip`**: o zip completo desta passagem (app, documentos, testes, trabalho).
2. **`HISTORICO_E_PLANO_corujaexplica.md`**: o histórico e plano (também está dentro do zip, em `documentos/`).

**Quando for mexer no cadastro da família (próximo passo):**

3. **`PLANO_CADASTRO_FAMILIA.md`** (versão 3). Uma cópia está no zip, em `documentos/referencias/`; anexe a mais nova que você tiver.
4. **Os modelos já prontos:**
   - o zip completo do **📚 Alfabetização v123** (cadastro novo **publicado**);
   - o zip completo do **🌍 Curiosidades v2.x**: o cadastro novo está feito, mas em 14/10/2026 está **só no site de teste**; o site de verdade do Curiosidades ainda é a v1.8.
5. **As cópias mestras dos compartilhados:** `escola-familia.js` 1.2, `nuvem-sync.js` 4.1 e `escola-pwa.js` 2, com o `LEIA-ME_COMPARTILHADOS.md`. Uma cópia está no zip, em `trabalho/modelo-cadastro-novo/`.
6. **O seu `nuvem-config.js` verdadeiro** (md5 `1d5f060a5ae8339921d3d58498807971`). Também está no zip, em `pacote-netlify/`.
7. **Um backup exportado do Coruja Explica de agora**, de **cada criança** (⚙️ → 💾 Backup → ⬇️ Exportar), para testar a migração com os textos reais das meninas.

**Modelo indicado:** Sonnet 5.5, esforço alto.

`========== COPIE DAQUI ==========`

Olá! Vamos continuar o **🦉 Coruja Explica**, um dos 7 apps da **Escola São Pedro**. Esta é uma conversa nova. A conversa antiga foi fechada com uma passagem completa, e os arquivos dela estão anexados.

**Quem sou eu e para quem é o app**
- Sou o **Pedro**, de Mara Rosa (GO). **Não sou programador:** você escreve todo o código, e eu decido a parte pedagógica.
- Testo com as minhas filhas num **celular Android de verdade**, quase sempre **espelhado na TV**, com elas a uns 3 metros.
- **Hinata, 6 anos:** 1º ano, mas lê e faz matemática no nível do 3º ano. Está aprendendo interpretação de texto e os sinais da escrita.
- **Hana, 4 anos:** já lê com certa fluência e faz pequenas contas.
- A marca é **Coruja 🦉 / "Esforço Vence"**: o esforço vale mais que o talento.

**O que é o app**
- **Endereço:** https://escolasaopedrocorujaexplica.netlify.app
- **ID na nuvem:** `corujaexplica`
- **Versão:** **3.1**, cache **`coruja-explica-v3-1`**, publicada.
- **Testes:** **816 verificações, 0 falhas** (9 baterias, Node + Playwright, Firebase de mentira), rodadas em 14/10/2026.
- **Como funciona:** eu peço um texto a uma IA (o app copia o pedido pronto: "Leitura do dia", "Entender de verdade" e mais 3), colo a resposta, o app arruma (Formato Coruja) e guarda na **biblioteca de cada criança**. A leitura é imersiva e deitada, com:
  - marca-texto;
  - dicionário por toque;
  - tamanhos de 12 a 64 px;
  - margem Normal/Sílabas/Espaços e recuo;
  - quiz no fim;
  - "Textos lidos" com histórico.
- **Cadastro de hoje:** nome + 1 dos 8 bichinhos, até 6 crianças. Nuvem pelo `nuvem-sync.js` **v3**, com código da família **por celular**. Também usa o `escola-pwa.js` v2 (tela sempre acesa, tela cheia, convite para instalar).

**Antes de mexer em qualquer coisa:** leia o **`HISTORICO_E_PLANO_corujaexplica.md` inteiro**, principalmente:
- o **capítulo 6** (cadastro, família e nuvem como estão hoje);
- o **capítulo 7** (regras);
- o **capítulo 11** (defeitos conhecidos).

Se faltar algum arquivo de que você precise, **me peça e não comece**. **A fonte da verdade é o arquivo**, não a memória.

**Regras que não podem ser quebradas**
1. **Nunca perder** textos, leituras ou respostas do quiz de nenhuma criança. Isso vale para migração, nuvem e backup.
2. O meu **`nuvem-config.js` vai no zip exatamente como está** (md5 `1d5f060a5ae8339921d3d58498807971`). Não mexa no Firebase sem eu pedir.
3. **Os compartilhados não se editam dentro de um app só:** `nuvem-sync.js`, `escola-pwa.js` e `escola-familia.js`. Se precisar mudar, **pare e me pergunte**.
4. **Nada de `alert`/`confirm`/`prompt`** do navegador. **Todo botão avisa** se deu certo ou errado.
5. **Edições cirúrgicas.** Plano e **autorização antes de coisa grande**.
6. **Letras de 12 a 24 px** (maiores quando precisar). Nada visível abaixo de 12 px.
7. Leitura com maiúsculas e marca-texto de fábrica, voz desligada, sem seleção de texto e tela sempre acesa.

**Como entregar**
- **Zip para o Netlify** só com os arquivos de `pacote-netlify/`, na raiz:
  - `index.html`, `sw.js`, `manifest.webmanifest`, os 2 ícones;
  - `nuvem-sync.js`, `escola-pwa.js` (e `escola-familia.js` quando entrar o cadastro novo);
  - o meu `nuvem-config.js` sem alteração.
- **Suba o nome do cache** do `sw.js` (hoje `coruja-explica-v3-1`) e o rodapé "versão X" das Configurações.
- **Rode os testes** (`cd testes && sh rodar_todos.sh`) e acrescente testes para o que mudar. Só o `teste-v3.js` intercepta o Firebase; **nunca** rode os testes com um código da família escrito no `nuvem-config.js`. Diga claramente o que foi **rodado de verdade** e o que foi só **lido**.
- **Checagem em 3 etapas** antes de me entregar: autochecagem, 1 agente conferente independente e um revisor-chefe.
- Entregue também o zip completo atualizado (com documentos e testes) e o `HISTORICO_E_PLANO` atualizado.
- **Como falar comigo:**
  - português do Brasil;
  - explique **a causa de verdade** de cada problema, em palavras simples;
  - seja honesto sobre o que foi e o que não foi testado;
  - termine com um **checklist ✅/⬜** do que foi feito e do que eu preciso fazer.
- Às vezes eu falo por voz e o texto sai trocado (ex.: "Wolf screen" = "Full screen").

**O próximo passo combinado:** colocar o **cadastro novo da família e das crianças** (código da família + crianças com nome + bichinho, telas e palavras iguais nos 7 apps), seguindo o `PLANO_CADASTRO_FAMILIA.md` (v3) e copiando o jeito do Curiosidades/Alfabetização.
- Os cuidados próprios deste app estão no capítulo 12 do histórico:
  - `popstate` com degrau de segurança;
  - chip e ⚙️ nas outras telas;
  - `completoNaNuvem` = false quando um texto subiu cortado (limite de 850 KB);
  - apagar só com a nuvem confirmada ou com cópia na lixeira;
  - `nuvem-sync.js` v3 → 4.1;
  - testar a migração com o meu backup real, deitado **e em pé**.
- **Antes de começar, confirme comigo:**
  - o nome do **site de teste** (sugestão: `escolasaopedrocorujaexplicatestes`);
  - o **nome do cache** (sugestão: `coruja-explica-v4-0`);
  - se a abertura passa a ser sempre "Quem vai estudar hoje?" (decisão D2 do plano).

**O que eu quero agora:** (escreva aqui)

`========== ATÉ AQUI ==========`
