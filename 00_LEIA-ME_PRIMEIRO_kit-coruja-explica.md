# 📦 Kit para o 🦉 Coruja Explica receber o novo cadastro da família

Montado em 15/10/2026 na conversa do 🌍 Curiosidades (que já recebeu o cadastro novo: a v2.2 está publicada e aprovada; a v2.3, entregue em 15/10/2026, só acrescenta ajustes de leitura e **não muda a ligação do cadastro**).

## O que anexar na conversa do Coruja Explica
1. **`kit-cadastro-coruja-explica.zip`** (este kit), com:
   - `GUIA_IMPLANTAR_CADASTRO_NOVO_APP.md` — **ler primeiro**: o passo a passo, a ordem da ligação, os defeitos que apareceram no Curiosidades e como evitar, os testes que valem a pena, e os pontos específicos do Coruja Explica.
   - `PLANO_CADASTRO_FAMILIA.md` — o plano aprovado (versão 3, decisões D1–D18).
   - `MODELO_LIGACAO_CURIOSIDADES_v2.2.js` — os trechos do Curiosidades que ligam o cadastro (trava "sem criança", adaptador, juntar com a nuvem, backup que junta, ligação). Só para ler e adaptar.
   - `compartilhados/` — as **cópias mestras** (`escola-familia.js` 1.2, `nuvem-sync.js` 4.1, `escola-pwa.js` 2), o `LEIA-ME_COMPARTILHADOS.md` com os md5, o **seu `nuvem-config.js` verdadeiro** (md5 `1d5f060a5ae8339921d3d58498807971`) e `modelos/sw_alfabetizacao_v123.js` (modelo de `sw.js`).
   - `testes_modelo_curiosidades/` — os testes de navegador do Curiosidades com o Firebase de mentira (modelo do **que** testar; os do Coruja são em JavaScript).
   - `HISTORICO_E_PLANO_curiosidades.md` — capítulos 15 e 16 contam a implantação no Curiosidades com todos os detalhes (o 18 conta a v2.3).
2. **`curiosidades-completo-v2.3.zip`** — o app modelo inteiro (código, testes, documentos). Se já tiver anexado o `curiosidades-completo-v2.2.zip`, **ele também serve**: a ligação do cadastro é a mesma nas duas.
3. **`alfabetizacao-completo-v123.zip`** — o 1º app que recebeu o cadastro (refeito a partir da pasta que você me mandou em 08/10/2026, sem mudança).
4. **Do próprio Coruja Explica** (você tem aí): o zip completo mais novo **com a pasta de testes** (só o zip do Netlify `coruja-explica-netlify_v3_1.zip` não basta — a conversa nova precisa dos testes) e o prompt de continuação (`claude/coruja-explica-prompt-continuacao.md`, no Projeto).
5. **Um backup exportado do Coruja Explica de agora** (⚙️ › 💾 Backup › Exportar), de cada celular que as meninas usam.

## Texto para colar na conversa do Coruja Explica
> Olá! Vamos colocar o **novo cadastro da família** no **🦉 Coruja Explica**, seguindo o `PLANO_CADASTRO_FAMILIA.md` (v3) e os modelos do **Curiosidades v2.3** (o zip da v2.2 também serve: a ligação do cadastro é a mesma) e do **Alfabetização v123**. Anexei: o kit (`kit-cadastro-coruja-explica.zip`, comece pelo `GUIA_IMPLANTAR_CADASTRO_NOVO_APP.md`), os dois zips completos de modelo, o zip completo do Coruja Explica com os testes, o prompt de continuação dele e um backup exportado de hoje. **Antes de começar, leia tudo; se faltar algum arquivo, me peça e não comece.** Regras de sempre: nunca perder progresso; meu `nuvem-config.js` sem nenhuma alteração; não mexer no Firebase sem eu pedir; os compartilhados não se editam dentro de um app só; edições cirúrgicas; plano e autorização antes de coisa grande; testes de verdade com Firebase de mentira; checagem em 3 etapas; site de teste primeiro (família `pmrtestes`); zip completo; explicar as causas em palavras simples; terminar com checklist ✅/⬜.
> Decisões para você me perguntar: nome do site de teste (sugestão `escolasaopedrocorujaexplicatestes`), nome do cache (sugestão `coruja-explica-v4-0`) e se a abertura passa a ser sempre "Quem vai estudar hoje?" (decisão D2).
