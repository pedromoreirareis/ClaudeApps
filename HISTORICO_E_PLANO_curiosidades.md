# 🌍 HISTÓRICO E PLANO — Curiosidades do Mundo (`curiosidades`)

Passagem feita em **08/10/2026**, no fim da conversa longa deste app.
**Leia este documento inteiro antes de mexer em qualquer coisa.**

> **🆕 Atualização de 08/10/2026 (tarde) — v2.0, o novo cadastro da família.** Numa conversa nova, o novo cadastro (`PLANO_CADASTRO_FAMILIA.md` v3) foi implantado em cima da v1.8: é a **v2.0** (cache `curiosidades-mundo-v2-0`), entregue **para o SITE DE TESTE** (`escolasaopedrocuriosidadestestes.netlify.app`). O site de verdade **continua na v1.8** até o Pedro aprovar. Tudo o que mudou está no **capítulo 15** (no fim). Os capítulos 1 a 14 continuam descrevendo a **v1.8** (a publicada); onde a v2.0 muda alguma coisa, o capítulo 15 vale.

> **🆕 Atualização de 14/10/2026 (noite) — v2.3, versão final desta rodada.** A v2.2 (220 curiosidades novas) foi publicada e aprovada pelo Pedro. A v2.3 traz o Ler Mais com margem por sílabas/espaços e recuo (como no Coruja Explica), tira o "destacar por sílabas", cria o destaque duplo da palavra e corrige conteúdos (capítulo **18**). O que ainda não foi feito: `documentos/ALTERACOES_FUTURAS_curiosidades.md`. **Estado publicado: v2.2** (até o Pedro publicar a v2.3).

> **🆕 Atualização de 14/10/2026 — v2.1.** As 10 novidades da v1.9 foram levadas para cima da v2.0b (cache `curiosidades-mundo-v2-1`), menos o código de backup da v1.9 (a v2.0 já faz melhor). Capítulo **16**. Passo a passo: `documentos/INSTRUCOES_PUBLICAR_v2.1.md`.

> **🆕 Atualização de 08/10/2026 (noite) — v2.0b, aprovada para publicar.** O Pedro testou a v2.0 no site de teste (família `pmrtestes`): cadastro, gravação e recuperação "excelentes". Achou um defeito ("destacar por sílaba" só valia depois de fechar e abrir o app), que era **antigo** (já existia na v1.8) e foi corrigido: é a **v2.0b** (cache `curiosidades-mundo-v2-0b`), **aprovada por ele para o site de verdade** (capítulo 15.8; passo a passo em `documentos/INSTRUCOES_PUBLICAR_v2.0b.md`). Depois dela: a v1.9 (15.9) e mais curiosidades (15.10).

**Como ler as marcas deste documento:**
- 📄 **certeza** — está no arquivo (código, zip, teste rodado de verdade em 08/10/2026).
- 💭 **lembrança** — vem da conversa ou dos documentos antigos desta conversa (ex.: o `PROMPT_CONTINUACAO.md` da v1.7). Pode estar incompleta.
- ❓ **não sei** — não tenho como saber daqui.

Os números de linha citados (ex.: "linha 1535") são do `pacote-netlify/index.html` da v1.8.

---

## 1. Identificação

| Item | Valor |
|---|---|
| Nome do app | **Curiosidades do Mundo** (nome curto no celular: "Curiosidades") 📄 |
| Endereço no Netlify | https://escolasaopedrocuriosidades.netlify.app/ 📄 |
| ID na nuvem (`APP_NUVEM`) | `curiosidades` 📄 (linha 2846) |
| Versão atual (publicada) | **v1.8** 📄 |
| Nome do cache do `sw.js` | `curiosidades-mundo-v1-8` 📄 |
| Data da última entrega | **24/09/2026** (v1.8) 📄 — 💭 por volta das 07h20 no relógio do ambiente da conversa |
| Conferência do que está publicado | Em **08/10/2026** baixei os arquivos do site e comparei pelo md5: `index.html`, `sw.js`, `manifest.webmanifest`, `nuvem-sync.js`, `escola-pwa.js` e `nuvem-config.js` publicados são **idênticos** aos do pacote abaixo 📄 (os ícones não foram baixados) |
| Versão pendente | **v1.9** — feita em **outra conversa**, ainda **não publicada**. 💭 Ela nunca existiu nesta conversa (aqui a última foi a v1.8; a transcrição desta conversa não tem nenhuma v1.9) e não veio no primeiro pedido de passagem; o Pedro **anexou em seguida (08/10/2026)** o `index.html` e o `sw.js` dela (cache `curiosidades-mundo-v1-9`) 📄. Está em `trabalho/v1.9-pendente/`, com o `O_QUE_MUDA_NA_V1.9.md` |

**Arquivos do pacote (`pacote-netlify/`)** 📄

| Arquivo | Tamanho (bytes) | md5 | O que é |
|---|---|---|---|
| `index.html` | 2.931.198 | `70190499ea6d33962b7ed7d609dc3be0` | O app inteiro (HTML + CSS + JS + dados + 5 fontes embutidas) |
| `sw.js` | 1.600 | `54724597b0ed5f95669262fffd034fdf` | Service worker, cache `curiosidades-mundo-v1-8` |
| `manifest.webmanifest` | 747 | `7bc096a1d6e3805c61e27519ab8c6d63` | Manifesto do PWA |
| `icon-192.png` | 3.252 | `3b076500c5db8aa861f11b7fb661ad2e` | Ícone (lupa dourada) |
| `icon-512.png` | 7.968 | `6b75981813f0d7cb0d041f2744f04b3a` | Ícone grande (também "maskable") |
| `nuvem-sync.js` | 20.277 | `f6736f30a4eb5c2e29af1866e79eafe8` | Nuvem, **versão 3** (compartilhado) |
| `escola-pwa.js` | 21.976 | `ec31bf4a195ccf6a28f70e4fe3748c5f` | Tela acesa, tela cheia, convite, 8 bichinhos — **versão 2** (compartilhado) |
| `nuvem-config.js` | 2.043 | `1d5f060a5ae8339921d3d58498807971` | **O do Pedro**, com as chaves do Firebase (byte a byte igual ao que ele mandou) |

---

## 2. Para quem e para quê

- 📄/💭 App de leitura **offline** (PWA) em que a criança explora **curiosidades do mundo** lendo frases curtas em **CAIXA ALTA**: países, Brasil, cidades, história, religiões, espaço, dinossauros, animais, mar, corpo humano, clima, fazenda, ciências, cientistas, transportes, matemática, Língua Portuguesa, convívio, artes, esportes, experimentos, química e física, alimentação.
- 💭 **Para quem:** as filhas do Pedro. Os documentos antigos desta conversa (v1.4–v1.7) dizem "app de leitura **da Renata**". O pedido de passagem de **08/10/2026 (o mais novo)** diz que as meninas são **Hinata (6 anos**, 1º ano, lê e faz matemática no nível do 3º ano) e **Hana (4 anos**, já lê com certa fluência e faz pequenas contas). A memória diz que o Curiosidades foi feito para a **filha mais nova**. ❓ Não sei quem é "Renata" (pode ter sido um nome de exemplo: ele aparece nos testes, `Renata 🦋`, e no exemplo do `nuvem-config.js`, "saopedro-renata-2026"). **Vale o mais novo: Hinata e Hana.**
- 💭 **Como usam:** no celular Android do Pedro, quase sempre **espelhado na TV**, com as meninas a uns 3 metros. Por isso: letra grande, **tela deitada (paisagem)**, tela que **não pode apagar**, botões grandes.
- 💭 **Filosofia:** marca Escola São Pedro / Coruja 🦉 / **"Esforço Vence"** — o esforço vale mais que o talento. A coruja incentivadora festeja marcos de leitura (10, 25, 50, 100… curiosidades) com frases como "Isso é muito esforço!" 📄 (linhas 1975–1997).
- 💭 Marcar como lida é **sempre um toque de propósito** da criança no botão "LIDA" — "passar os olhos" não conta como "ler".

---

## 3. Linha do tempo, versão por versão

> As versões **v1.0 a v1.3** foram feitas em **conversas anteriores** a esta. Não tenho a conversa delas; o que sei vem do `PROMPT_CONTINUACAO.md` da v1.7 (está em `documentos/antigos/`) e da memória 💭. ❓ Não sei a data de cada uma nem em qual delas entrou cada recurso, exceto onde está escrito.

### v1.0 a v1.3 — o app de leitura (💭)
- **O que existe desde essa época:** cartões (subcategorias) agrupados em seções; tela inicial em 2 níveis (seções → cartões); leitura com sílabas, destaque ao tocar e voz (TTS); "Ler Mais" (texto longo); popups da bandeira/emoji; temas de cor; 9 tipos de letra (os mesmos do Esforço Vence); Favoritas; Curiosidades de Hoje (3 por dia); 🎲 Surpresa; Dicionário de palavras difíceis; 🏅 Minhas Conquistas; 🎯 Desafio Rápido; 🕒 Últimas Lidas; destaque por linha (marca-texto); vários perfis (crianças) no mesmo celular; backup (exportar/importar arquivo .json).
- **Marcação de lida:** botão "LIDA" manual. **Foi tentado** mover as lidas para o fim da fila → causou bugs sérios de navegação → **desfeito a pedido do Pedro**.
- **Gravação (a parte mais delicada):** (1) bug de avisos falsos de "já leu tudo" → removida a reordenação; (2) foram colocados "ouvintes de segurança" (`blur`/`pagehide`/`visibilitychange` gravando tudo) → **pioraram** (uma aba velha apagava dados novos) → **desfeito**; (3) a gravação acontecia **depois** do festejo de marcos e, se ele desse erro, a marcação se perdia ("só às vezes") → **corrigido: grava primeiro**; (4) solução final: relê do disco antes de marcar, grava na hora, só lê ao voltar ao app, e ao sair regrava só a curiosidade atual. 📄 (linhas 1088–1155)
- **Tamanho da letra:** um botão único que "dava a volta" foi **rejeitado** (não dava para diminuir) → **dois botões A− / A+**, padrão 16. Bug do `Math.min(2,…)` que travava o tamanho em 2 → corrigido.
- **Largura do texto:** `text-wrap:balance` foi **tentado e rejeitado** (empurrava o texto para o meio) → **removido**; o ganho veio de reduzir margens. O recuo grande da direita é de propósito (botões 🔊 e ❤️ ficam por cima).
- **Língua Portuguesa:** 4 subcategorias (LP1 pontuação na ordem da BNCC, LP2 acentos, LP3 sinais gráficos, LP4 símbolos tipográficos); texto "Ler Mais" em 5 blocos + exemplos; o ícone da categoria **some** e o símbolo ensinado fica gigante em vermelho (um "selo pequeno" intermediário também foi **rejeitado**).
- **Busca 🔍:** v1.2 = lista corrida (limite 60); **v1.3 = sanfona por assunto** (limite 50 por assunto, vários abertos ao mesmo tempo; com 1 assunto, abre sozinho). Não busca dentro do "Ler Mais" (decisão do Pedro).
- Contagem na v1.3: 4.034 curiosidades, 278 cartões (igual hoje 📄).

### v1.4 — 23/09/2026 — Tela sempre acesa + nuvem (Firebase) 💭/📄
- **Pedido:** o celular do Pedro bloqueia a cada 1 minuto sem toque; com o app na frente, nunca pode bloquear. E guardar o progresso na internet (Firebase), "de extrema importância", sem perder nada sem internet.
- **Feito:** tela sempre acesa (código próprio no app); `nuvem-config.js` + `nuvem-sync.js` **v1** (só REST, login anônimo, fila offline, recuperar pelo nome + bichinho); tela "Recuperar"; pontinho da nuvem na ⚙️; `sw.js` que nunca guarda pedidos do Firebase e busca o `nuvem-config.js` na internet primeiro. Documentos: guia do Firebase, como pedir nos outros apps, pedido para nova conversa, referência de integração. Testes `teste_nuvem.py` 52/52.
- **Desfeito depois:** o código próprio da tela acesa foi para o `escola-pwa.js` na v1.5; o "conferir antes só no 1º envio" da nuvem v1 foi trocado pelo envio seguro da v2.
- 📄 O pacote da v1.4 está em `trabalho/pacotes-antigos/` (`curiosidades-netlify_v1.4.zip`).

### v1.5 — 23/09/2026 — Tela acesa reforçada, convite para instalar, tela cheia, nuvem v2 💭/📄
- **Pedido:** a tela ainda apagava; ao abrir pelo navegador, oferecer instalar (sempre, até instalar); tela cheia sempre; histórico no Firebase. Para os 7 apps.
- **Feito:** `escola-pwa.js` novo e compartilhado (Wake Lock + **modo reserva** com vídeo mudo de 2×2 px; vigia a cada 15 s; tela cheia a cada toque; convite próprio "📲 Instalar agora"); `nuvem-sync.js` **v2** (antes de gravar, lê a nuvem e junta; grava com trava de versão; repete até 3 vezes). Testes 75/75 + `sw_test.py` + `regressao.py` 10/10.

### v1.6 — 23/09/2026 — Histórico de versões na nuvem 💭/📄
- **Pedido:** garantir histórico de versões no Firebase e que limpar o navegador não perca dados.
- **Feito:** `nuvem-sync.js` **v3** (a cada envio, uma cópia do dia em `.../apps/curiosidades/versoes/AAAA-MM-DD`; envio 1,5 s depois da mudança; pede armazenamento persistente); botão **🕘 Versões guardadas** na tela da nuvem. Testes 86/86.
- 💭 Resposta honesta dada ao Pedro: limpar histórico/cache não perde nada; limpar "dados de sites" apaga o celular, mas o que já subiu volta; o único risco que não dá para eliminar é limpar **sem internet** com alteração ainda não enviada.
- ❓ Não existe `patch16.py`; não sei se a v1.6 foi feita por script ou por edição direta.

### v1.7 — 23/09/2026 — Cadastro padrão: nome + 8 bichinhos numa linha 💭/📄
- **Pedido** (texto completo em `documentos/referencias/PEDIDO_v1.7_padronizar_bichinhos.txt`): os mesmos 8 bichinhos em todos os apps, **numa linha só** (o teclado deitado escondia as linhas de baixo); mesmo jeito de cadastrar, acessar e recuperar; testar em pé, deitado e com teclado; documentos para Claude ou ChatGPT; tripla conferência.
- **Feito:** 🦉 Coruja · 🦊 Raposa · 🐰 Coelho · 🐼 Panda · 🦋 Borboleta · 🐨 Coala · 🐯 Tigre · 🐴 Pônei (lista no `escola-pwa.js` v2, com cópia de reserva no app); cadastro sem rotação forçada; `interactive-widget=resizes-content`; nome + bichinho já existentes não criam repetido; trocar nome/bichinho leva a ficha antiga da nuvem; bichinho antigo (🦄 etc.) continua funcionando. Documento `PADRAO_CADASTRO_NOME_BICHINHO.md`. Testes `teste_cadastro.py` 41/41, `teste_nuvem.py` 94/94, `regressao.py` 10/10, `sw_test.py` ok.

### v1.8 — 24/09/2026 — Pop-up próprio do código da família 📄/💭
- **Pedido** 💭: o Pedro mandou prints (estão em `documentos/referencias/v1.8_prints/`): (a) a caixinha **do navegador** ("escolasaopedrocuriosidades.netlify.app diz…") que o app usava (`prompt()`); (b) com o celular deitado e o teclado aberto, o Android abria um **editor de tela cheia** feio por cima de tudo; (c) o pop-up do **Esforço Vence** (Alfabetização) como modelo: "🔑 CÓDIGO DA FAMÍLIA", texto, campo com "ex.: saopedro2026", botões "Cancelar" e "🔑 Guardar código" (verde). Pediu: "deixar o pop-up do código da família bonito como no Esforço Vence, **sem mexer em mais nada**".
- **Feito** 📄: `prompt()` e os 2 `alert()` do código da família trocados por um pop-up próprio `#codigoOv` no estilo dos outros pop-ups do app (cartão creme arredondado, 🔑 grande, campo com borda dourada, botões "Cancelar" / "Confirmar ✅", erro escrito em vermelho dentro do cartão, Enter confirma, tocar fora fecha). Quando o código vem do arquivo `nuvem-config.js`, o mesmo cartão só explica e mostra "Entendi 👍". Cache `v1-8`. Testado com navegador sem tela (em pé, 390×844): abre, erro com código curto, confirma, fecha, nenhuma caixinha do navegador.
- **Diferenças em relação ao Esforço Vence** 📄 (o Pedro aprovou assim: "Ok. Perfeito." — e publicou): título "Código da família" (não em CAIXA ALTA e sem "🔑" no título; o 🔑 fica grande em cima), botão **"Confirmar ✅"** (não "🔑 Guardar código"), placeholder **"Digite aqui..."** (não "ex.: saopedro2026"), botão dourado (não verde).
- 💭 Nessa conversa apareceu um texto estranho colado numa mensagem, pedindo para responder só com texto e não usar ferramentas; foi tratado como injeção de comando e ignorado.
- **Desfeito depois:** nada.

### Depois da v1.8
- 💭 **v1.9**: feita em outra conversa, **não publicada**. 📄 Os arquivos (anexados pelo Pedro em 08/10/2026) estão em `trabalho/v1.9-pendente/`. Pela comparação linha a linha com a v1.8: ▶️ "Continuar de onde parei"; "ler ao tocar" lembrado (chave nova `sayTap`); dias seguidos só com leitura de verdade; karaokê sincronizado com a voz; marcos até 4.034; Desafio com placar; backup conferido antes de importar; arrastar o dedo/setas/Esc; busca mais leve; Últimas Lidas mais segura. Detalhes e conflitos com o novo cadastro: `trabalho/v1.9-pendente/O_QUE_MUDA_NA_V1.9.md`. ❓ O pedido, as decisões e o que foi rejeitado na conversa da v1.9 não são conhecidos aqui (o link compartilhado não pôde ser lido).

---

## 4. Decisões de design e de pedagogia

**Aceitas (valem hoje)** 📄/💭
1. Marcar como lida é **manual** (botão "LIDA" no canto de cima à esquerda do cartão). Lida fica cinza/escurecida (`#card.jaLida`), **no mesmo lugar**.
2. **Primeira entrada** num cartão nunca visitado abre na **1ª curiosidade**; depois, **volta onde parou** (`posPais`). Ver de passagem pelas Favoritas ou pelas Curiosidades de Hoje **não** muda o "onde parou".
3. Letra padrão **16** (`fsizeIdx=3`), com **A−** e **A+** separados, que param nos limites.
4. Texto ocupa a largura toda; recuo direito grande reservado aos botões 🔊 e ❤️.
5. Cartões de Língua Portuguesa: só o símbolo ensinado, gigante, vermelho, fundo branco.
6. Busca só em nome da seção + nome do cartão + frase curta (não no "Ler Mais"); resultados em sanfona.
7. "Ajuda sonora" e "Destaque por linha" andam juntos: ligar um desliga o outro (a criança sempre tem um jeito de saber onde está lendo). Com a voz muda (🔇), todo toque marca a linha inteira.
8. Gravação **instantânea, sem travar botões** (o Pedro não quer botão travado enquanto salva).
9. **Celular é o dono dos dados** (localStorage); a nuvem é cópia de segurança. Juntar dados **nunca apaga** uma lida (regra "OU" caractere por caractere). ⚠️ Mas o **envio do mesmo celular substitui** a ficha da nuvem, sem juntar (ver 6.6 e 6.9 item 11).
10. Identidade da criança = **Nome + um dos 8 bichinhos oficiais** (numa linha só), igual nos 7 apps.
11. Código da família **digitado no celular**, não escrito no `nuvem-config.js` (privacidade); `codigoDaFamilia` fica `""`.
12. App sempre **deitado** (paisagem) na leitura; o **cadastro funciona em pé e deitado** (não é girado à força).
13. Tela sempre acesa, tela cheia a cada toque, convite para instalar até instalar.

**Rejeitadas (não voltar a fazer)** 💭
- Reordenar as lidas para o fim da fila.
- "Ouvintes de segurança" que gravam o estado inteiro ao sair.
- `text-wrap:balance`.
- Um botão único de tamanho de letra que dá a volta.
- Mostrar o ícone da categoria ao lado do símbolo ensinado (nem como selo pequeno).
- Buscar dentro do "Ler Mais".
- Travar botões enquanto salva.
- Caixinhas do navegador (`prompt()`) para o código da família (trocada na v1.8).

---

## 5. Como o app é por dentro (v1.8)

### 5.1 Estrutura do arquivo 📄
Um único `index.html` (3.149 linhas, 2,9 MB):
- `<head>`: um `<script>` pequeno (linha 14, `window.__nuvemCfgArq='carregando'`) e depois carrega **nesta ordem** `nuvem-config.js` (marca `window.__nuvemCfgArq` = 'ok'/'falta'), `nuvem-sync.js`, `escola-pwa.js`; depois o `<style>`, com **5 fontes embutidas em base64** nas linhas 19–23 (HanaSassoon, HanaBeaba, HanaMamae, HanaPlaywrite, HanaNarrow).
- `<body>`: telas (linhas 617–942), depois o `<script>` principal (944–3147).
- Dados no começo do script, cada um numa linha só, muito grande: `DATA` (linha 946, 2,4 MB), `PAIS_DESC` (947), `EMOJI_DESC` (948), `GLOSSARIO` (950); `TOPICO` (951).
- 161 funções de primeiro nível.

### 5.2 Telas (os `id`s) 📄
`mostrarTela(id)` (linha 1353) alterna: `home`, `reader`, `users`, `novoUser`, `palavras`, `conquistas`, `desafio`, `ultimasLidasTela`, `buscaTela`, `nuvemTela`.

| id | O que é |
|---|---|
| `#home` | Tela inicial. Nível 1: cartões especiais (🌟 Curiosidades de Hoje, ❤️ Favoritas, 📖 Dicionário, 🏅 Minhas Conquistas, 🎯 Desafio Rápido, 🕒 Últimas Lidas) em "✨ Seus Cantinhos Especiais ✨" + 23 seções com barra de progresso. Nível 2: os cartões da seção. Barra de cima: 🏠 (voltar às seções), 🦉, título, **chip da criança** `#userChip`, 🔍, 🎲, ⛶, ⚙️ `#cfgGearHome` com a bolinha `#nuvemPonto` |
| `#reader` | Leitura: 🏠, `#meta` (cartão n/total · seção · cartão), 🔎 (só nas Curiosidades de Hoje), gaveta `#ajustes` (🎨 ✒️ Aa A− A+ ⛶), 🔇/🔊 `#mute`, ⚙️ `#gear` (abre/fecha a gaveta, **não** as Configurações); barra de progresso; cartão com "LER MAIS", "LIDA", bandeira, emoji, texto; 🔊 `#say` e ❤️ `#fav` flutuantes; ◀ ▶ e "SÍLABAS" + 🔊 `#sayWord` (ler ao tocar) |
| `#users` | "Quem vai estudar hoje?" |
| `#novoUser` | Cadastro / trocar nome ou bichinho |
| `#nuvemTela` | "Recuperar cadastro" (nuvem e versões guardadas) |
| `#palavras`, `#conquistas`, `#desafio`, `#ultimasLidasTela`, `#buscaTela` | Dicionário, conquistas, desafio, últimas lidas, busca |
| Pop-ups (`.ov`) | `#infoOv` (bandeira/emoji/palavra), `#cfgOv` (⚙️ Configurações), `#detOv` (Ler Mais), `#transOv` (fim de cartão / próximo), **`#codigoOv` (código da família, v1.8)** |
| `#toast` | Avisos curtos (1,9 s) |

### 5.3 Funções principais 📄
- Crianças: `carregarUsers`, `salvarUsers`, `userAtual`, `K(n)`, `abrirUsers`, `trocarUser`, `abrirNovoUser`, `editarUser`, `focarNome`, `montarEmojisUser`, `confirmarUser`, `apagarUser`, `chaveLeitor`, `nomeDoBichinho`, `atualizaChipUser`.
- Progresso: `carregarDados`, `saveState`, `toggleLida`, `resincronizarDoDisco`, `reforcarGravacaoAoSair`, `registrarUltimaLida`, `atualizarSequencia` (dias seguidos), `checarMarco`.
- Leitura: `buildHome`, `openReader`, `render`, `go`, `iniciarTransicaoCartao`/`avancarTransicaoCartao`, `handleTap`, `tapRead`, `speak`/`speakText`/`karaoke`, `fitText`, `silabas`.
- Outras: `abrirBusca`/`procuraCuriosidades`/`renderBusca`, `abrirDetalhes`, `abrirDesafio`, `abrirConquistas`, `abrirPalavras`, `abrirDoDia`, `abrirSurpresa`, `openFavs`, `exportarBackup`/`importarBackup`, `openCfg`/`syncCfgUI`/`cfgToggle`.
- Tela acesa / instalar: `pedirTelaAcesa`, `alternaTelaAcesa`, `atualizaTelaAcesaUI`, `instalarApp` (chamam o `EscolaPWA`).
- Nuvem: ver capítulo 6.

### 5.4 Conteúdo (contado em 08/10/2026) 📄
- **278 cartões**, **4.034 curiosidades**, **23 seções**; `PAIS_DESC` 40, `EMOJI_DESC` 808, `GLOSSARIO` 113 palavras; maior cartão: 100 curiosidades.
- Língua Portuguesa: LP1 13, LP2 5, LP3 6, LP4 10 (todos `simbolo:true`).
- Seções (cartões / curiosidades): Países do Mundo 36/852 · Brasil: Estados 27/311 · Brasil: Cidades 14/198 · História do Mundo 18/361 · Religiões Do Mundo 16/167 · Espaço 14/230 · Dinossauros E Pré-História 7/89 · Reino Animal 9/180 · Vida No Mar 7/105 · Corpo Humano 13/196 · Clima E Natureza 6/91 · Campo E Fazenda 4/61 · Ciências Da Escola 5/75 · Cientistas E Inventores 11/165 · Transportes E Invenções 3/45 · Matemática Divertida 9/135 · Convívio E Cidadania 5/73 · Artes E Música 3/45 · Esportes Do Mundo 3/31 · Experimentos Em Casa 45/334 · Química E Física 14/196 · Alimentação Saudável 5/60 · Língua Portuguesa 4/34.
- ⚠️ **1 frase repetida** (contra a regra "nenhuma frase repetida"): "O CERRADO É CHAMADO DE CAIXA-D'ÁGUA DO BRASIL PORQUE NELE NASCEM MUITOS RIOS." em `W3`, 2ª curiosidade (índice 1; Clima E Natureza / Nossa Terra) e `F4`, 3ª curiosidade (índice 2; Campo E Fazenda / Nosso Cerrado). Lembrete: `lidas`, `favs` e `posPais` contam a posição a partir de **0**. Não foi corrigida (capítulo 11).
- Formato de cada curiosidade: `{e: emoji, c: "FRASE EM CAIXA ALTA", t: tópico, d: "texto do Ler Mais"}`; cartão: `{code, name, flag, sec, items[], simbolo?}`.
- ⚠️ **Nunca inserir curiosidades no meio de um cartão**: `lidas` guarda a posição (índice) de cada curiosidade. Acrescentar só no fim do cartão. 📄 (formato de `lidas`, capítulo 5.7)

### 5.5 Orientação da tela 📄
- `@media (max-aspect-ratio:1/1)` (celular em pé) **gira** só `#home`, `#reader` e `#users` 90° (paisagem forçada, linhas 37–44). **Não giram** (ficam como o celular estiver): o cadastro `#novoUser`, a `#nuvemTela`, `#palavras`, `#conquistas`, `#desafio`, `#ultimasLidasTela`, `#buscaTela` e os pop-ups.
- `screen.orientation.lock('landscape')` ao abrir, ao voltar ao app e ao entrar em tela cheia (só funciona instalado/tela cheia).
- `manifest`: `"orientation": "landscape"`, `"display": "fullscreen"`.
- Meta viewport com `interactive-widget=resizes-content` (o teclado encolhe a página).

### 5.6 Service worker e manifest 📄
- `sw.js`: cache `curiosidades-mundo-v1-8` com `./`, `index.html`, `manifest.webmanifest`, os 2 ícones, `nuvem-sync.js`, `escola-pwa.js` (+ tenta `nuvem-config.js`). Pedidos de outro endereço (Firebase) nunca são guardados. `nuvem-config.js` é **buscado na internet primeiro** (se o Pedro trocar a configuração, os celulares pegam a nova). O resto: cache primeiro. Ao ativar, apaga os caches antigos.
- Registro do SW só em `https:` ou em `localhost` (linha 3143). **Atenção:** em `127.0.0.1` o SW **não** registra (já confundiu um teste).
- `manifest`: nome "Curiosidades do Mundo", curto "Curiosidades", `id/start_url/scope` "./", cores `#0e1226`, ícones 192/512 (512 também maskable).

### 5.7 TODAS as chaves do `localStorage` 📄
(Conferido lendo o código e abrindo o app num navegador sem tela em 08/10/2026.)

**Lista de crianças**
| Chave | Guarda |
|---|---|
| `mundo_usuarios` | `{"us":[{"id":"p1791441401492","nome":"Bia","av":"🐰"}],"atual":"p1791441401492"}`. Com 0 crianças, já é gravada na **primeira abertura** como `{"us":[],"atual":null}` (`carregarUsers`, linha 1033) |

**Progresso de cada criança** — prefixo `mundo_<id>_`, com `<id>` = `p` + número (`'p'+Date.now()`). A lista `CHAVES_DADOS` (linha 1002) tem 20 chaves; mais 2 da sequência de dias:

| Chave (`mundo_<id>_…`) | Guarda | Formato |
|---|---|---|
| `lidas` | curiosidades lidas | `{"<code do cartão>":"0101…"}` — um caractere por curiosidade, na ordem do cartão ('1' = lida) |
| `favs` | favoritas | `{"<code>:<índice>":1}` |
| `posPais` | onde parou em cada cartão | `{"<code>":índice}` |
| `ultimasLidas` | últimas 10 marcadas | `[{"code":…,"idx":…}]` (mais nova primeiro) |
| `palavrasAprendidas` | dicionário | `{"palavra":{"def","sec","sub","ico"}}` |
| `marcos` | festejos já mostrados | `{"10":1,"25":1,…}` |
| `theme` | tema de cor | número 0–7 |
| `font` | tipo de letra | número 0–8 (padrão 2) |
| `caps` | CAIXA ALTA | '1'/'0' |
| `fsize` | tamanho da letra | número 0–6 (padrão 3 = 16) |
| `cfgHi` | destacar ao tocar | '1'/'0' |
| `cfgSyl` | destacar por sílabas | '1'/'0' |
| `cfgAudio` | ajuda sonora | '1'/'0' |
| `modoLinha` | destaque por linha | '1'/'0' |
| `voz` | voz ligada (🔊/🔇) | '1'/'0' |
| `ajustes` | gaveta de ajustes aberta | '1'/'0' |
| `pais` | último cartão (índice no `DATA`) | número |
| `secAtual` | seção aberta na tela inicial | nome da seção (apagada ao voltar ao menu) |
| `ultPais` | último cartão visto | code |
| `ultCur` | última curiosidade vista | número |
| `ultimoDia` | último dia de uso | "AAAA-M-D" (sem zero à esquerda, ex.: "2026-10-8") |
| `seqDias` | dias seguidos | número |

**Chaves "fantasmas" `mundo_p0_…`** 📄: com **0 crianças**, `K()` usa `p0`, e `atualizarSequencia()` grava `mundo_p0_ultimoDia` e `mundo_p0_seqDias` logo ao abrir. Não fazem mal (a nuvem ignora `p0`), mas ficam para sempre.

**Chave antiga (antes dos perfis)**: se existir `mundo_lidas`, na primeira abertura o app cria a criança **"Leitor 1" 🦊** e copia as chaves `mundo_<chave>` para ela (linhas 1021–1029). As antigas não são apagadas.

**Chaves globais**
| Chave | Quem grava | Guarda |
|---|---|---|
| `mundo_telaAcesa` | `escola-pwa.js` | '0' = tela acesa desligada (padrão: ligada) |
| `escola_instalado` | `escola-pwa.js` | '1' = já instalado neste celular |
| `escola_conviteVisto` | `escola-pwa.js` | data/hora do último "Agora não/Entendi" (não insiste por 10 min) |
| `nuvem_familia` | `nuvem-sync.js` v3 | código da família normalizado (ex.: `familia-teste-2026`) |
| `nuvem_dispositivo` | `nuvem-sync.js` | id deste celular (`d…`) |
| `nuvem_auth` | `nuvem-sync.js` | `{idToken, refreshToken, exp}` do login anônimo |
| `nuvem_curiosidades_pendentes` | `nuvem-sync.js` | fila: `{"<id>":data/hora}` — é criada **mesmo sem nuvem configurada** |
| `nuvem_curiosidades_meta` | `nuvem-sync.js` | por criança: `{enviadoEm, chave, vistoUpdate, conferido}` |

**Fora do `localStorage`:** nenhum `sessionStorage`, nenhum IndexedDB 📄. O SW usa a Cache Storage (`curiosidades-mundo-v1-8`). **`sayTapOn`** (botão 🔊 "ler ao tocar", ao lado de SÍLABAS) fica **só na memória**: volta a "ligado" toda vez que o app abre (não é gravado em lugar nenhum) 📄 (linha 2702).

---

## 6. Cadastro, família e nuvem: como está HOJE (v1.8)

### 6.1 Lista de crianças e criança atual 📄
- Variável `U = {us:[{id,nome,av}], atual:<id>}` ← `mundo_usuarios`.
- **Tipo de id:** `'p' + Date.now()` (ex.: `p1791441401492`). Não usa nome sem acento nem `1`. Exceção antiga: a migração "Leitor 1" também usa `'p'+Date.now()`.
- Máximo **6 crianças** (`MAX_USERS`).
- `userAtual()` devolve a atual; sem criança devolve `{id:null, nome:'Leitor', av:'🦉'}`.

### 6.2 Como o progresso é separado 📄
- Toda chave de criança é `mundo_<id>_<nome>` (função `K(n)` usa `U.atual`).
- Lista de isolamento: `CHAVES_DADOS` (20 chaves, capítulo 5.7). A nuvem usa `CHAVES_NUVEM` = `CHAVES_DADOS` + `ultimoDia` + `seqDias` (22).
- Trocar de criança: `saveState()` da que estava → muda `U.atual` → `carregarDados()` (começa dos valores padrão e lê os da nova) → aplica tema, letra etc.
- Criança nova **nunca herda** nada (testado nas versões anteriores e no `teste_cadastro.py`).

### 6.3 Telas e textos exatos 📄

**Primeira abertura (0 crianças)** → vai direto ao cadastro `#novoUser`; o botão "← Voltar" fica escondido.

**Cadastro `#novoUser`** (linhas 657–671)
- Título `#nuTitulo`: **"🌟 Qual é o seu nome?"**
- Campo `#nuNome`: placeholder **"Digite o seu nome..."**, máx. 14, `enterkeyhint="done"`.
- **"Escolha o seu bichinho:"** + os 8 bichinhos numa linha (`#nuEmojis`), nenhum pré-escolhido.
- `#nuEscolhido`: **"Você escolheu: 🦋 Borboleta"**.
- Botões: **"← Voltar"** (vai para "Quem vai estudar hoje?"), **"Pronto! ✅"**, **"☁️ Já tenho cadastro"** (só aparece com a nuvem configurada; abre a tela de recuperar).
- Avisos (toast): "Escreva o seu nome primeiro 🙂" · "Escolha o seu bichinho 🙂" · Enter sem bichinho: "Agora escolha o seu bichinho 🙂" · já existe no celular: "🐰 Bia já está neste celular — abrindo!" (abre a dela, não cria outra) · sucesso: "🐰 Bem-vindo, Bia!" · máximo: "Já são 6 crianças — o máximo."
- Nome: `trim`, espaços juntados, até 14 letras. A comparação "mesma criança" usa `chaveLeitor(nome, bichinho)` (= `NuvemSync.chaveUsuario`): sem acento, minúsculo → "Bia"+🐰 = `bia_1f430`.

**Escolher a criança `#users`** (linhas 637–654)
- Título: **"Quem vai estudar hoje?"** (com 🦉 e ⛶ na barra; **sem ⚙️ e sem chip**).
- Aviso: "Cada criança tem o próprio progresso. Toque no seu nome e no seu bichinho para começar."
- Um cartão por criança: bichinho, nome, "N de 4034", e "lendo agora" na atual.
- Cartão final (com ➕): **"+ NOVO USUÁRIO"** e, embaixo, "cadastrar outro leitor". Abre o cadastro.
- Botões: **"✏️ Trocar nome ou bichinho"**, **"🗑️ Apagar este usuário"**, **"☁️ Recuperar da nuvem"** (só com nuvem).
- Ao tocar numa criança: "🐰 Agora é a vez de Bia!". Tocar na criança que já é a atual ("lendo agora") abre direto a tela inicial, **sem** esse aviso.

**Mudar nome ou bichinho** (mesma tela `#novoUser`)
- Vale para a criança **atual** ("lendo agora"), não para um cartão escolhido.
- Título: **"✏️ Trocar nome ou bichinho"**; nome já preenchido; bichinho atual marcado.
- Bichinho antigo (fora dos 8): nenhum marcado e aparece **"O bichinho 🦄 mudou: escolha um dos 8 novos 🙂"**.
- Se o novo nome + bichinho é de **outra** criança: "🐰 Bia já existe neste celular. Escolha outro nome ou bichinho."
- Sucesso: "🐨 Agora é Bia (Coala)". Se a chave mudou, `nuvemLevarFichaAntiga()` junta a ficha antiga da nuvem na nova (a antiga continua na nuvem).

**Apagar** (`apagarUser`, linha 1532)
- Apaga a criança **atual** (não a do cartão tocado).
- Com 1 criança só: "É preciso ter ao menos um usuário." (**não dá para apagar a última**).
- Pergunta com caixinha do navegador `confirm`: **"Apagar Bia e todo o progresso dele? Isso não tem volta."**
- Apaga do celular as 20 chaves de `CHAVES_DADOS`. **Não apaga** `ultimoDia`/`seqDias` (ficam órfãs), nem a ficha na nuvem, nem a entrada dela em `nuvem_curiosidades_meta`. O id apagado fica em `nuvem_curiosidades_pendentes` até o próximo envio (sem nuvem configurada, fica para sempre; sem internet, entra na contagem "N leitor(es)… esperando para subir").
- Depois: a primeira criança da lista vira a atual; toast "Usuário apagado."
- **O que se perde:** o que ainda **não subiu** para a nuvem (sem internet, ou nuvem sem código) **some para sempre**. O que já estava na nuvem pode voltar por "Recuperar".

**Recuperar da nuvem `#nuvemTela`** (linhas 725–741, funções 3008–3109)
- Título: **"Recuperar cadastro"** (☁️), botão 🏠.
- Botões: **"🔑 Código da família"**, **"🔄 Procurar de novo"**, **"🕘 Versões guardadas"**.
- Mensagens (`#nuvemMsg`): "A nuvem ainda não foi configurada neste aplicativo (veja o guia do Firebase)." · "Primeiro digite o código da família (botão 🔑 abaixo)." · "📴 Sem internet agora. Conecte no Wi-Fi e toque em "Procurar de novo"." · "⏳ Procurando os leitores guardados na nuvem..." · "Ainda não tem nenhum leitor guardado na nuvem com este código da família." · "Toque no leitor para trazer o progresso dele para este celular. Nada que já está aqui é apagado."
- Cartões: bichinho, **"Bia · Coelho"**, e "já está neste celular — toque para juntar" / "tem progresso neste app" / "veio de outro app".
- Tocar: se já existe no celular → ela **vira a criança atual** (linha 3084) e junta (`recuperar(…, restaurando=false)`); se não → cria criança nova e traz (`restaurando=true`: cores e letra vêm da nuvem). Toasts: "☁️ Buscando o progresso de Bia..." → "✅ 🐰 Progresso de Bia recuperado!" ou "🐰 Bia pronto! (ainda sem leituras neste app)"; erro: "❌ <mensagem>" ou "❌ Não deu certo". Máximo: "Já são 6 usuários — o máximo."
- Erro ao listar: "❌ <mensagem>" ou "❌ Não foi possível falar com a nuvem."
- 🏠 volta: 0 crianças → cadastro; 1 → tela inicial; 2+ → "Quem vai estudar hoje?".

**Versões guardadas** (mesma tela, `montarVersoesTela`)
- Mensagens: "Primeiro escolha ou recupere um leitor." · "A nuvem ainda não está pronta (configuração ou código da família)." · "📴 Sem internet agora." · "❌ <mensagem>" ou "❌ Não foi possível falar com a nuvem." · "⏳ Procurando as versões guardadas de Bia..." · "Ainda não tem versões guardadas de Bia (a primeira aparece depois do primeiro envio)." · "🕘 Versões de 🐰 Bia (uma por dia). Tocar numa versão JUNTA ela com o progresso atual — nada é apagado."
- Cartões "🗓️ 23/09/2026 — N curiosidade(s) lida(s)". Tocar → `confirm` **"Juntar a versão de 23/09/2026 com o progresso atual de Bia?\n\nNada é apagado: só volta o que estiver faltando."** → "✅ Versão de 23/09 juntada!" ou "Não encontrei essa versão"; erro: "❌ <mensagem>" ou "❌ Não deu certo".

**Pop-up do código da família `#codigoOv`** (v1.8, linhas 927–940 e 2968–3005)
- Abre por: ⚙️ → Nuvem → **"🔑 Digitar"**; tela Recuperar → **"🔑 Código da família"**; e por "🔄 Enviar agora" quando falta o código.
- Normal: 🔑 grande, título **"Código da família"**, texto **"É o mesmo código em todos os aplicativos e em todos os celulares (pelo menos 6 letras ou números, sem espaço)."**, campo com placeholder **"Digite aqui..."** (máx. 40), botões **"Cancelar"** e **"Confirmar ✅"**. Enter confirma; tocar fora fecha.
- Código curto (menos de 6 depois de normalizar): **"O código precisa ter pelo menos 6 letras ou números."** (vermelho, dentro do cartão).
- Sucesso: fecha, toast **"🔑 Código guardado!"**; se veio da tela Recuperar, já procura de novo.
- Código escrito no arquivo `nuvem-config.js`: mostra **"O código da família já está escrito no arquivo nuvem-config.js. Para trocar, edite aquele arquivo."** e só o botão **"Entendi 👍"**.
- Nuvem não configurada: não abre; toast "☁️ A nuvem ainda não foi configurada".
- O código é normalizado pelo `nuvem-sync.js` (sem acento, minúsculo, espaço → hífen, só a-z 0-9 -, até 40). Ex.: "Familia Teste 2026" → `familia-teste-2026`. Trocar o código **muda a família de todas as crianças do celular** e marca todas para subir.

### 6.4 Ao abrir o app 📄 (linhas 3138–3140)
- **0 crianças** → cadastro.
- **1 criança** → `goHome()`: tela inicial dela, **já dentro da seção do último cartão** (ou de "🌍 Países do Mundo", se nunca leu). Não mostra "Quem vai estudar hoje?".
- **2 ou mais** → "Quem vai estudar hoje?" (sempre, para não marcar no perfil errado).

### 6.5 Onde ficam os botões 📄
- **Chip da criança** (`#userChip`, bichinho + nome, abre "Quem vai estudar hoje?"): **só na barra de cima da tela inicial** `#home`. Não aparece na leitura nem nas outras telas.
- **⚙️ Configurações** (`#cfgGearHome`): **só na tela inicial**. Na leitura, o ⚙️ `#gear` só abre/fecha a gaveta de ajustes.
- **Bolinha da nuvem** (`#nuvemPonto`, no canto da ⚙️ da tela inicial): escondida sem nuvem configurada; **verde** = tudo guardado (também sem internet, se não há nada esperando); **laranja** = enviando, preparando, ou alterações na fila (com ou sem internet); **vermelha** = erro ou falta o código.
- Seção **"☁️ Nuvem (guarda o progresso na internet)"** nas Configurações: "Situação" + **"🔄 Enviar agora"**; "Código da família" ("Em uso: fam•••", "(vem do arquivo)", "Ainda não digitado") + **"🔑 Digitar"**; "Recuperar leitores" + **"☁️ Recuperar"**. Textos da situação nas linhas 2935–2951 (ex.: "✅ Tudo guardado na nuvem (às 19:32)", "📴 Sem internet. N leitor(es) com progresso guardado só no celular, esperando para subir. ⚠️ Não limpe os dados do navegador até conectar na internet.").

### 6.6 Ligação com o `nuvem-sync.js` (v3) 📄 (linhas 2841–3120)
```js
NuvemSync.iniciar({ app:'curiosidades',
  usuarios: ()=>U.us.map(u=>({id:u.id,nome:u.nome,av:u.av})),
  idDaChave: nuvemIdDaChave, exportar: nuvemExportar, mesclar: nuvemMesclar });
```
- `APP_NUVEM = 'curiosidades'`.
- `idDaChave(k)`: reconhece `mundo_(p\d+)_<chave>` só se `<chave>` está em `CHAVES_NUVEM` **e** a criança existe. Toda gravação dessas vira pendência (o `nuvem-sync.js` "vigia" o `setItem/removeItem`).
- `exportar(id)`: as 22 chaves de `CHAVES_NUVEM` que existirem, como texto.
- `mesclar(id, dn, restaurando)` — regra campo por campo:
  - `lidas`: **OU caractere por caractere** (lida em qualquer lado = lida). Desmarcar num celular pode "voltar" se o outro tinha marcado (aceito).
  - `favs`, `palavrasAprendidas`, `marcos`: **união** (o do celular vence em caso de chave igual).
  - `posPais`: união; o celular manda, a não ser `restaurando` (aí a nuvem manda).
  - `ultimasLidas`: junta sem repetir, só as que continuam lidas, máx. 10.
  - simples (`theme, font, caps, fsize, cfgHi, cfgSyl, cfgAudio, voz, pais, secAtual, ultPais, ultCur, ajustes, modoLinha, ultimoDia, seqDias`): o celular manda; a nuvem só entra se `restaurando` ou se a chave não existe no celular.
  - Criança **sem nenhuma lida neste celular** é tratada como `restaurando` (adota as preferências da nuvem).
  - Se for a criança atual: recarrega a tela.
- `nuvemTentarRecuperarNovo(id,nome,av)`: ao cadastrar alguém com nome + bichinho que já existe na nuvem, traz o progresso sozinho ("☁️ 🐰 Achei o progresso de Bia na nuvem!").
- `nuvemLevarFichaAntiga(id,nomeAntigo,avAntigo)`: ao trocar nome/bichinho, junta a ficha antiga na nova. **Sem internet (ou sem código), só marca para subir e nunca tenta de novo**: o que estiver só na ficha antiga (ex.: vindo de outro celular) **não se perde** (fica na nuvem, na ficha antiga), mas **fica fora da ficha nova**.
- `nuvemRecuperarLeitor(item, local)`: botão da tela Recuperar.
- ⚠️ **Como o `nuvem-sync.js` v3 ENVIA** 📄 (no `nuvem-sync.js` do pacote: linha 289, em `enviarComSeguranca`, e linha 313, em `checarNuvem`): antes de gravar, baixa a ficha da nuvem, mas **só junta se a ficha foi gravada por OUTRO celular** (`doc.dispositivo !== dispositivo()`). Se o último a gravar foi **este mesmo celular**, ele **grava por cima** o campo `dados` com o que está no celular agora (e a cópia do dia também). A frase "juntar nunca apaga" vale para a **junção**; o **envio do mesmo celular substitui**. Ver riscos 11 e 12 do capítulo 6.9. (A versão 4.1 do `nuvem-sync.js` corrige **só em parte**: ela junta também quando este celular **não conhece** a ficha — o que resolve o caso da criança **recriada**, que ganha id novo e não tem registro em `nuvem_curiosidades_meta`. Mas **não resolve** o caso do **backup antigo importado no mesmo celular**: os ids são os mesmos, o registro de envio continua lá, a 4.1 acha que "conhece" a ficha e grava por cima do mesmo jeito.)
- Caminhos no Firestore: `familias/{codigo}/usuarios/{nome_hexdobichinho}` (perfil: nome, av, apps.curiosidades) e `.../apps/curiosidades` (dados = JSON das chaves, atualizadoEm, dispositivo, versao) e `.../apps/curiosidades/versoes/AAAA-MM-DD`.

### 6.7 Passos próprios do cadastro deste app 📄
Nenhum: só nome + bichinho. Não pergunta turma, idade nem ano.

### 6.8 Caixinhas do navegador que ainda existem 📄
- `confirm`: apagar criança (linha 1535); importar backup (2637); juntar versão guardada (3038).
- `alert`: erro ao exportar backup (2611); arquivo inválido (2630); arquivo de outro app (2634); backup importado (2651); erro ao importar (2654); erro ao ler o arquivo (2657).
- `prompt`: **nenhum** (o do código da família saiu na v1.8).

### 6.9 Riscos e defeitos conhecidos nesta parte 📄
1. **Apagar é imediato e sem rede de segurança**: o que não subiu para a nuvem se perde. Não confere se está tudo guardado antes.
2. **"Apagar este usuário" e "Trocar nome ou bichinho" agem na criança atual**, não na que a pessoa olha na lista. Fácil apagar a errada.
3. Ao apagar, `ultimoDia`/`seqDias` e a entrada em `nuvem_curiosidades_meta` ficam órfãs no celular.
4. **Importar backup substitui tudo** (apaga as crianças atuais do celular) e o backup **não leva** `ultimoDia`/`seqDias`.
5. Pop-up do código, **com o teclado aberto e o celular deitado** (medido em 740×170, 640×150, 568×140): o campo fica visível, mas **"Cancelar" e "Confirmar" ficam abaixo do teclado** (dá para rolar o cartão; o ✓/Enter do teclado confirma). Em pé com teclado (360×420, 320×300) o "Confirmar" também fica abaixo. ❓ Não testado no celular de verdade.
6. Textos diferentes do Esforço Vence e dos outros apps: "Código da família" × "🔑 CÓDIGO DA FAMÍLIA"; "Confirmar ✅" × "🔑 Guardar código"; "Digite aqui..." × "ex.: saopedro2026". Na mesma tela o app mistura "criança", "usuário" e "leitor" ("+ NOVO USUÁRIO", "Já são 6 crianças", "Já são 6 usuários", "Recuperar leitores").
7. Chaves fantasmas `mundo_p0_ultimoDia`/`mundo_p0_seqDias` com 0 crianças. (A v1.9 não publicada para de criá-las.)
8. `nuvem_curiosidades_pendentes` é criada mesmo sem nuvem configurada (inofensivo).
9. Trocar o código da família no pop-up muda a família de **todas** as crianças deste celular.
10. `sayTapOn` não é gravado (volta a ligado a cada abertura) — não é cadastro, mas é preferência da criança que se perde. (Resolvido na v1.9 não publicada: chave `sayTap`.)
11. ⚠️ **Risco alto — envio do mesmo celular substitui a nuvem** (capítulo 6.6). Exemplos de perda: (a) **importar um backup antigo** neste celular (com os mesmos ids) → os `removeItem`/`setItem` da importação já passam pela vigia e deixam essas crianças **na fila**; uns 2,5 s depois de o app recarregar, a ficha da nuvem e a cópia de hoje viram o backup antigo, **sem precisar de nenhuma outra alteração** (só as cópias dos **dias anteriores** guardam o que havia); (b) **apagar uma criança e cadastrar de novo** o mesmo nome + bichinho neste celular **sem internet** → quando a internet volta, o `checarNuvem` não junta (a ficha é "deste celular") e a criança quase vazia sobe por cima. Com internet, o `nuvemTentarRecuperarNovo` costuma trazer a ficha antes do envio (1,5 s), mas não há garantia. Recuperação possível pelas "🕘 Versões guardadas" dos dias anteriores.
12. ⚠️ **Risco alto — aviso falso ao importar backup** (linhas 2640–2654): o app **primeiro apaga** as 20 chaves de cada criança atual e só depois grava as do backup. Se der erro no meio (ex.: memória cheia), aparece **"Ocorreu um erro ao importar o backup. Nada foi alterado."** — mas o progresso já pode ter sido apagado.
13. O texto da situação da nuvem pode se contradizer: "✅ Tudo guardado na nuvem (às 19:32) — 1 alteração(ões) na fila" (linhas 2946–2947).

---

## 7. Regras que não podem ser quebradas

1. **Nunca perder progresso.** Nenhuma mudança pode apagar ou sobrescrever `lidas`, `favs`, `palavrasAprendidas` de ninguém. Na publicação, o progresso que já está nos celulares tem que continuar.
2. **Não mudar o `nuvem-config.js` do Pedro**: vai no pacote byte a byte igual (md5 `1d5f060a5ae8339921d3d58498807971`). Nunca usar o `testes/nuvem-config.js` (falso) no pacote.
3. **Não mexer no Firebase** (regras, projeto) sem o Pedro pedir. 💭 (memória: "não quer nenhuma alteração no Firebase")
4. **Os arquivos compartilhados** (`nuvem-sync.js`, `escola-pwa.js`, e o futuro `escola-familia.js`) **não são editados dentro de um app só**. Mudança sobe a versão e vale para os 7 apps — **pare e pergunte ao Pedro**.
5. **Subir o nome do cache** do `sw.js` a cada entrega.
6. `DATA`/`EMOJI_DESC`/`PAIS_DESC`/`GLOSSARIO`: editar só com **parser de colchetes balanceados** (nunca troca de texto direta no HTML); curiosidade nova **só no fim** do cartão.
7. `node --check` no JavaScript e testes de verdade (Playwright) antes de entregar.
8. Não reintroduzir nada da lista "Rejeitadas" (capítulo 4).
9. `toggleLida()` grava **antes** de qualquer enfeite; voltar ao app **só lê**; sair só reforça a curiosidade atual.
10. Os 8 bichinhos oficiais, nesta ordem, numa linha só. Identidade = nome + bichinho.
11. Edições **cirúrgicas**; pedir autorização antes de coisas grandes.
12. O ID na nuvem é `curiosidades` — mudar faz o app não achar o que já está guardado.

---

## 8. Aprendizados difíceis

| Problema | Causa de verdade | Solução |
|---|---|---|
| Marcação de lida sumia "às vezes" 💭 | A gravação vinha depois do festejo de marcos; se ele desse erro, não gravava | Gravar primeiro, enfeites depois, cada um no seu `try` |
| Dados novos apagados ao fechar 💭 | Ouvintes "de segurança" gravavam o estado inteiro de uma aba velha | Remover; ao voltar só ler; ao sair regravar só a curiosidade atual |
| Cartão abria no meio sem nunca ter sido escolhido 💭 | Ver de passagem (Favoritas/Hoje) atualizava `posPais` | Só gravar `posPais` na navegação direta |
| Texto "flutuando no meio" 💭 | `text-wrap:balance` | Removido; margens menores |
| Tamanho 16/18 sumia ao reabrir 💭 | `Math.min(2,…)` ao carregar | `Math.min(FSIZES.length-1,…)` |
| Tela apagava no celular do Pedro 💭 | Wake Lock recusado (economia de bateria) | Modo reserva com vídeo mudo + vigia 15 s (`escola-pwa.js`) |
| Dois celulares gravando juntos 💭 | Sem trava de versão | Ler → juntar → gravar com `currentDocument.updateTime` (até 3 tentativas) |
| Teclado deitado escondia os bichinhos 💭 | Bichinhos em várias linhas e cadastro girado à força | Uma linha só, cadastro sem rotação, `interactive-widget=resizes-content` |
| Teste do SW "não registrava" 📄 | O app só registra o SW em `localhost`/https; o teste usava `127.0.0.1` | Usar `http://localhost:PORTA` |
| Terminal "morreu" no meio de um teste 📄 | `pkill -f "texto"` com um texto que aparecia no próprio comando | Nunca usar `pkill -f` assim; matar pelo número do processo |
| `teste_nuvem.py` quebra na v1.8 📄 | Ele respondia ao `prompt()` do navegador; a v1.8 trocou por pop-up próprio | Preencher `#codigoInput` e tocar `#codigoOkBtn` (cópia ajustada `teste_nuvem_v18.py`) |
| Erro de sintaxe em script de teste 💭 | Aspas triplas `"""` dentro de `"""` no Python | Alternar `'''` e `"""` |

---

## 9. Testes automáticos

### 9.1 O que existe (`testes/`) 📄
| Arquivo | Verifica | Pasta que usa |
|---|---|---|
| `regressao.py` | 10: 1ª visita abre na 1ª, reabre onde parou, LIDA grava na hora e persiste, busca sanfona, fonte, símbolo LP, sem erros | `/home/claude/z` |
| `sw_test.py` | SW real: nome do cache, arquivos guardados, abre **sem internet** | `/home/claude/t/site` (em `localhost`) |
| `teste_cadastro.py` | 41: cadastro nome + bichinho, 8 numa linha em 12 tamanhos de tela (deitado, em pé, com teclado), clicáveis, sem rotação | `/home/claude/z` |
| `teste_nuvem.py` | 94 (grupos A 11, B 17, C 9, D 4, E 4, F 5, G 2, H 4, P 19, V 11, K 8): nuvem com **Firebase de mentira** (rotas `identitytoolkit`/`securetoken`/`firestore` interceptadas), fila offline, recuperar, juntar, trava de versão, convite, tela acesa, versões, troca de bichinho | `/home/claude/t/site` (nuvem configurada falsa) e `/home/claude/z` (sem configurar) |
| `teste_nuvem_v18.py` | **O mesmo** `teste_nuvem.py` com **2 linhas** trocadas (153 e 192) para preencher o pop-up da v1.8 em vez de responder ao `prompt()` | idem |
| `nuvem-config.js` | **FALSO** (`AIzaFAKE`, `proj-teste`) — só para `/home/claude/t/site` | — |
| `nuvem-config-vazio.js` | o modelo vazio — para `/home/claude/z` | — |
| `preparar_pastas.sh` | monta `/home/claude/z` e `/home/claude/t/site` a partir de `pacote-netlify/` | — |
| `extras_v1.8/` | os testes avulsos usados na v1.8 e nesta passagem (pop-up, SW v1-8, medidas do pop-up com teclado, chaves do localStorage) | — |

### 9.2 Como rodar 📄
Precisa de Python 3 + Playwright com Chromium (no ambiente do Claude já existe).
```bash
cd <pasta onde o zip foi aberto>/curiosidades-completo-v1.8
bash testes/preparar_pastas.sh        # cria /home/claude/z e /home/claude/t/site
cd testes
python3 regressao.py
python3 sw_test.py
python3 teste_cadastro.py
python3 teste_nuvem_v18.py            # use este na v1.8 (o original quebra no B6)
```
Os testes gravam prints em `/home/claude/t/` (pasta é criada pelo `preparar_pastas.sh`).

### 9.3 Última vez que rodaram — **08/10/2026**, sobre a v1.8 📄 (rodado de verdade)
| Teste | Resultado |
|---|---|
| `regressao.py` | **10/10** ✅ |
| `sw_test.py` | ✅ cache `curiosidades-mundo-v1-8` com 8 arquivos; abre sem internet: `True True []` |
| `teste_cadastro.py` | **41/41** ✅ |
| `teste_nuvem.py` (original) | ❌ **18 ✅, depois falha B6–B10 e para com erro no B13** — porque responde a um `prompt()` que não existe mais (v1.8). Não é defeito do app. |
| `teste_nuvem_v18.py` (2 linhas ajustadas) | **94/94** ✅ |

Os mesmos testes também foram rodados sobre a **v1.9 não publicada** (resultados e o teste próprio `teste_v19_novidades.py` em `trabalho/v1.9-pendente/`, ver o `O_QUE_MUDA_NA_V1.9.md`): 10/10, SW ok, 41/41, nuvem **93/94** (K4), novidades 20/20.

Antes (23/09/2026, v1.7): `teste_nuvem.py` 94/94, `teste_cadastro.py` 41/41, `regressao.py` 10/10, `sw_test.py` ok 💭/📄 (saída guardada em `trabalho/saida_testes_v1.7.txt`).

### 9.4 O que os testes **não** cobrem
- O **Firebase de verdade** do Pedro e as regras reais (só o falso).
- O **celular de verdade**: teclado do Android, Wake Lock real, espelhamento na TV, convite nativo do Chrome, vozes do TTS.
- O pop-up do código **com o teclado aberto** (só medido em 08/10, sem teste automático com resultado ✅/❌).
- Barulho conhecido (não é erro): no Chromium sem tela aparecem avisos "Failed to execute 'requestFullscreen' on 'Element': API can only be initiated by a user gesture." (o app tenta a tela cheia ao abrir).
- Renderizar os 278 cartões, os 34 itens de LP um por um, colisão do texto com os botões flutuantes, desafio, conquistas, dicionário, backup.
- **PERDIDOS** (existiam em conversas anteriores, como `/home/claude/test_*.py`; 💭 lembrança, **não reescritos**): `valida.py` (validação dos dados: frases repetidas, formato do "Ler Mais", `EMOJI_DESC`, `SECTION_ORDER`, `PAIS_DESC` dos cartões LP); a **suíte funcional completa** (278 cartões, 34 itens LP, persistência com funções sabotadas, navegação, marca-texto, colisão texto × botões); a **suíte da busca em sanfona** ("Egito" com 3 assuntos etc.).

---

## 10. Como empacotar e publicar

1. Trabalhe numa cópia do `pacote-netlify/`.
2. Mexa só no necessário. Se mexer no `DATA`, use o parser de colchetes.
3. **Suba o nome do cache** no `sw.js` (linha 2: `const C='curiosidades-mundo-vX-Y'`) e o comentário da linha 1. Se entrar arquivo novo (ex.: `escola-familia.js`), coloque-o na lista `FILES`.
   - ⚠️ **Próximo número:** **não use `v1-9`**: já existe uma v1.9 não publicada (feita em outra conversa). Sugestão: a versão do novo cadastro ser **v2.0** → `curiosidades-mundo-v2-0`. **O Pedro decide.**
4. Copie o `nuvem-config.js` **do Pedro** (o do `pacote-netlify/`, md5 `1d5f060a…`) — nunca o de `testes/`.
5. `node --check` em cada `.js` e no `<script>` extraído do `index.html`.
6. Rode os testes (capítulo 9) e mostre os resultados.
7. Zip com os arquivos **soltos na raiz** (sem pasta dentro), confira a lista dentro do zip e o md5 do `nuvem-config.js`.
8. O Pedro arrasta no Netlify (Deploys → arrastar a pasta/zip). No celular: abrir o app; se não atualizar, fechar e abrir de novo (o cache novo apaga o antigo).
9. Terminar com o checklist ✅/⬜.

Para o **zip completo** de uma passagem (como este): o `LEIA-ME.txt` com tamanhos e md5 é gerado por `python3 trabalho/gerar_leiame.py <pasta>` (deixa de fora o próprio LEIA-ME e o relatório da conferência).

---

## 11. Estado atual

> **v2.1 (14/10/2026):** v2.0b + as novidades da v1.9 (capítulo 16). A v1.9 guardada já foi aplicada; não há mais versão pendente.
>
> **v2.0b (08/10/2026, noite):** testada pelo Pedro no site de teste e **aprovada para o site de verdade** (capítulo 15.8). Próximos: v1.9 (15.9), mais curiosidades (15.10), ideias (15.11).
>
> **v2.0 (08/10/2026):** o novo cadastro está **pronto para o site de teste** (capítulo 15). Os itens abaixo descrevem a v1.8; os riscos 2, 2b, 2c, 2d, 3 (D2: agora sempre abre na "Quem vai estudar hoje?") e a troca do `nuvem-sync.js` para a 4.1 foram resolvidos na v2.0 (capítulo 15.4). Continuam: a frase repetida do Cerrado, o `sayTapOn` (vem com a v1.9) e a v1.9 guardada.

**Pronto** 📄
- v1.8 publicada e idêntica ao pacote (conferido em 08/10/2026).
- Cadastro nome + 8 bichinhos, nuvem v3 com histórico, tela acesa, convite, tela cheia, pop-up próprio do código.
- `escola-pwa.js`: igual ao das cópias mestras de 08/10/2026 (versão 2, md5 `ec31bf4a…`) — nada a fazer.

**Pendente**
- ✅ ~~**v1.9**~~ — **aplicada na v2.1 (capítulo 16)**. Texto antigo: (outra conversa, não publicada, cache `curiosidades-mundo-v1-9`): arquivos em `trabalho/v1.9-pendente/` + `O_QUE_MUDA_NA_V1.9.md` (10 mudanças; chave nova `mundo_<id>_sayTap`; testes de hoje sobre a v1.9: regressão 10/10, SW ok, cadastro 41/41, nuvem 93/94 — falha o K4 porque a primeira troca do dia para uma criança não dispara mais o envio dela; novidades 20/20). **Aplicar só depois do novo cadastro publicado e conferido.**
- ⬜ **`nuvem-sync.js`**: o Curiosidades usa a **versão 3** (md5 `f6736f30…`). O Pedro anexou a **4.1** do Alfabetização (md5 `f151bb17…`). **Não troquei** (regra da passagem). A 4.1 é compatível com a v3 no documento da nuvem, mas foi feita para trabalhar com o `escola-familia.js`; a troca entra junto com o novo cadastro.
- ⬜ Documentos antigos (em `documentos/antigos/`, da v1.7) estão **desatualizados** em um ponto: a `REFERENCIA_INTEGRACAO_CURIOSIDADES.md` ainda mostra o `prompt()` do código da família (linha 530 dela) e o `GUIA_FIREBASE` fala em "digite o código → OK". Os pedidos para os outros apps também foram superados pelo `PLANO_CADASTRO_FAMILIA.md` (v3).
- ⬜ `teste_nuvem.py` original quebra na v1.8 (usar `teste_nuvem_v18.py`).

**Defeitos conhecidos** 📄 (nenhum foi corrigido; o código não mudou)
1. Frase repetida W3 item 2 / F4 item 3 (Cerrado "caixa-d'água").
2. Riscos do capítulo 6.9 (apagar sem garantia, apagar/editar agem na criança atual, órfãs, backup substitui tudo e não leva a sequência de dias, botões do pop-up abaixo do teclado, textos misturados, chaves `p0`).
2b. ⚠️ **Risco alto — envio do mesmo celular substitui a ficha da nuvem** (6.6 e 6.9 item 11). Trocar para o `nuvem-sync.js` 4.1 **resolve o caso (b)** (criança recriada, sem registro de envio) e **NÃO resolve o caso (a)** (backup antigo importado no mesmo celular, com os mesmos ids). O importar backup precisa ser tratado à parte (capítulo 12, ponto 4).
2c. ⚠️ **Risco alto — importar backup**: apaga antes de gravar e, se der erro, diz "Nada foi alterado" (6.9 item 12).
2d. Texto da situação da nuvem contraditório ("Tudo guardado… — 1 alteração(ões) na fila").
3. Com 1 criança, o app abre dentro da seção do último cartão (e numa criança nova, dentro de "🌍 Países do Mundo") em vez do menu de seções. ❓ Não sei se é de propósito.
4. `sayTapOn` (🔊 ler ao tocar) não é gravado. (A v1.9 não publicada resolve.)

**Pedidos do Pedro que ficaram para depois** 💭
- Padronizar o cadastro da família e das crianças nos 7 apps (já planejado: `PLANO_CADASTRO_FAMILIA.md` v3, D1–D18).
- Aplicar a v1.9.
- ❓ Não sei de outros pedidos em aberto deste app.

**Ideias futuras** 💭 (não pedidas formalmente)
- Recriar `valida.py` e a suíte funcional (perdidos).
- Pop-up do código igual ao do Esforço Vence (vai vir naturalmente com o `escola-familia.js`, que tem a tela T2 "🔑 CÓDIGO DA FAMÍLIA").

---

## 12. Plano de desenvolvimento (em ordem)

### 1º — Padronizar o cadastro da família e das crianças (código da família + nome + bichinho, telas e palavras iguais nos 7 apps)
> **✅ Implantado na v2.0 / v2.0b (capítulo 15)** — testado e aprovado pelo Pedro no site de teste; zip do site de verdade entregue (`curiosidades-netlify_v2.0b_SITE_DE_VERDADE.zip`). Falta só ele publicar e conferir. O texto abaixo é o planejamento original (antes da implantação).

Base: **v1.8** + `PLANO_CADASTRO_FAMILIA.md` (v3, anexar na conversa nova) + **o `index.html` do Alfabetização v123** (o modelo de ligação: o `LEIA-ME_COMPARTILHADOS.md` manda copiar o `ADAPTADOR_CRIANCAS` e o bloco "liga o cadastro da família, a nuvem e o escola-pwa.js" do fim dele — ⚠️ **ele não está neste zip**, precisa ser anexado) + cópias mestras de **08/10/2026** (`escola-familia.js` 1.2, `nuvem-sync.js` 4.1, `escola-pwa.js` 2 — guardadas em `trabalho/compartilhados-para-o-novo-cadastro/`, conferir md5 com o `LEIA-ME_COMPARTILHADOS.md`). Ordem dos apps (D10): **Curiosidades é o próximo** depois do Alfabetização.

O que o `escola-familia.js` 1.2 espera do app (lido no arquivo 📄): `EscolaFamilia.iniciar({ app:'curiosidades', nomeApp, iconeApp, maxPorFamilia, criancas:{ listar, atual, criar(nome,av,origem)→id, mudar(id,nome,av), exportar(id), importar(id,dados), tirar(id), completoNaNuvem(id), entrar(id,{naAbertura}), resumo(id)→{linha,barra}, resumoDados(dados) }, passoExtra, aoAbrirTelas, aoFecharTelas, fonte, abrirConfig(aoFechar), fecharConfig })` e `NuvemSync.iniciar({usuarios: ()=>EscolaFamilia.paraNuvem(lista)})`. Ele cria as telas T1–T8, o chip, a bolinha 🟢🟡🔴 e a seção "☁️ FAMÍLIA E NUVEM"; guarda `escola_familia` e `escola_lixeira_curiosidades`; **nunca** usa `alert/confirm/prompt`; migração só **acrescenta**.

Como o Curiosidades se encaixa (sugestão para a conversa nova, a conferir com o plano):
- `listar` → `U.us`; `atual` → `U.atual`; ids `p…` continuam.
- `criar` → a parte de `confirmarUser`/`nuvemRecuperarLeitor` que cria `{id:'p'+Date.now(), nome, av}` (sem abrir tela).
- `mudar` → a parte de edição (o módulo já cuida da ficha antiga com `movidoPara`).
- `exportar` → `nuvemExportar` (22 chaves); `importar` → `nuvemMesclar(id, dados, false)` (junta, não substitui).
- `tirar` → apagar as **22** chaves (não só as 20) + tirar de `U.us` (sem `confirm`).
- `entrar` → `trocarUser` + `irParaEstante`.
- `resumo` → "N de 4034" e barra `N/4034`.

**Pontos de atenção** (conflitos com o que existe hoje):
1. As telas atuais `#users`, `#novoUser`, `#nuvemTela`, `#codigoOv`, a seção "☁️ Nuvem" das Configurações, o chip e o `#nuvemPonto` passam a ser do módulo — decidir o que sai do `index.html` sem quebrar `abrirUsers()`/`abrirNovoUser()`, que são chamados em vários lugares (abertura, 🏠 da nuvem, cadastro).
2. **Abertura:** hoje 1 criança vai direto à tela inicial; o plano (D2) diz abrir sempre T4 "QUEM VAI ESTUDAR HOJE?". Confirmar com o Pedro.
3. **Apagar:** hoje apaga direto (com `confirm`) e não deixa apagar a última; o módulo só tira com tudo guardado na nuvem ou com cópia na lixeira, e bloqueia tirar a última nas 2 primeiras semanas.
4. **Backup** (importar substitui tudo, e o envio do mesmo celular substitui a nuvem — 6.9 itens 11 e 12; **a 4.1 não resolve este caso**): o importar precisa **juntar em vez de substituir** (ex.: usar a mesma regra do `mesclar`), ou então **limpar o registro de envio** (`nuvem_curiosidades_meta`) dessas crianças para a 4.1 juntar com a nuvem antes de enviar — decidir com o Pedro. Além disso, depois do módulo, importar pode criar crianças sem família em `escola_familia` — a migração do módulo dá a família do celular a elas, mas é preciso testar.
5. **Textos**: o módulo usa CAIXA ALTA e "CRIANÇA" ("🦉 QUEM VAI ESTUDAR HOJE?", "➕ NOVA CRIANÇA", "🌟 QUAL É O SEU NOME?", "PRONTO! ✅"). Os textos atuais (capítulo 6.3) mudam.
6. `nuvem-sync.js` 4.1 junto (a v3 não tem `existeFamilia`, `garantirGuardado`, `marcarMovido`…); `sw.js` com `./escola-familia.js` na lista e cache novo.
7. As chaves fantasmas `mundo_p0_*` e a migração "Leitor 1 🦊" continuam no código; não atrapalham, mas o `listar` não pode devolver `p0`.
8. Paisagem: o módulo tem telas próprias (`#efRaiz`, `position:fixed`); o app gira `#home/#reader/#users` em pé — conferir que as telas do módulo não ficam giradas nem escondidas.
9. Testes: `teste_cadastro.py` e `teste_nuvem_v18.py` vão quebrar (procuram `#nuNome`, `.nuPronto`, `#nuvemGrid`…). Precisam ser adaptados, com o Firebase de mentira.
10. Prioridade máxima: **nenhuma criança e nenhum progresso podem sumir na publicação.**

### 2º — Aplicar as novidades da v1.9 depois que o novo cadastro estiver publicado e conferido
Usar o `trabalho/v1.9-pendente/O_QUE_MUDA_NA_V1.9.md` (feito em 08/10/2026) e o `diferencas_v1.8_para_v1.9.diff`. Levar as 10 mudanças **uma a uma para cima do novo cadastro** (não copiar o index da v1.9 por cima). Pontos de atenção: `sayTap` na lista de chaves do adaptador; a primeira troca do dia para uma criança não dispara mais o envio dela (K4); regra `/^p\d+$/` do backup; Esc e setas com as telas do `escola-familia.js`. A v1.9 também resolve, de quebra, dois defeitos do capítulo 11: `sayTapOn` não gravado e chaves `mundo_p0_*`; e corrige o texto falso "Nada foi alterado" do backup (o risco de apagar antes de gravar continua).

### 3º — Arrumar os pequenos defeitos (com autorização)
Frase repetida do Cerrado; levar `ultimoDia/seqDias` no backup; importar backup sem apagar antes de gravar. (`sayTapOn` gravado e chaves `p0` já vêm resolvidos na v1.9.)

### 4º — Recriar os testes perdidos (`valida.py`, suíte funcional, busca)

---

## 13. Sobre o Pedro e as meninas, e como trabalhar com ele

**Quem é** 💭
- **Pedro**, de **Mara Rosa (GO)**. **Não é programador**: decide a parte pedagógica e testa; o Claude escreve todo o código. Sonha em criar bons aplicativos para a aprendizagem das filhas.
- **Hinata, 6 anos**: 1º ano do ensino fundamental, lê e faz matemática no nível do 3º ano.
- **Hana, 4 anos** (jardim): já lê com certa fluência; faz pequenas contas de adição e subtração (matemática nível 1º ano).
- (Versão antiga dos documentos: "app da Renata" — ver capítulo 2. Vale a mais nova.)
- Testa num **Android de verdade**, quase sempre **espelhado na TV** (meninas a ~3 m). O celular dele **bloqueia em 1 minuto** sem toque.
- Escola São Pedro: 7 apps (Alfabetização/"Esforço Vence", Matemática, Fluência, Coruja Explica, Provinha, Historinhas, Curiosidades), cada um em `escolasaopedro<nome>.netlify.app`, quase todos usados **deitados**.
- Usou o Firebase pela primeira vez neste projeto (precisou de guia passo a passo).

**Como trabalhar** 💭
- Português do Brasil, simples.
- **Edições cirúrgicas**; nunca quebrar o que funciona; **pedir autorização antes de coisas grandes**.
- Explicar a **causa** de cada problema em palavras simples, junto com a correção.
- **Honestidade**: dizer o que foi testado de verdade e o que não foi; diagnóstico honesto vale mais que tranquilizar.
- **Terminar sempre com checklist ✅/⬜** (feito / falta).
- Pede "checagem tripla" em mudanças sensíveis: rodar testes e mostrar os resultados.
- É **muito detalhista**: nota coisas sutis; manda **prints** e sensações ("parece que travou"); prints são a melhor pista.
- Às vezes **fala por voz** e o texto sai trocado (ex.: "Wolf screen" = "Full screen"; "eu te disse os que for necessário" = "me diga os que forem necessários").
- Quer: não perder **nenhum** dado ou progresso; testar tudo antes de publicar; inclusão e exclusão de crianças funcionando; **nenhuma alteração no Firebase**; cadastro que funcione deitado com o teclado aberto; na primeira abertura, opção de cadastrar e de recuperar.
- Prefere soluções sem fricção para a criança (ex.: não travar botões enquanto salva).
- Referência de teclado deitado: o **Esforço Vence** (o teclado não tampa o campo de nome/código).
- Os pedidos para outros apps devem servir para **Claude ou ChatGPT**.

---

## 14. Glossário

| Palavra | Quer dizer |
|---|---|
| Curiosidade | Uma frase curta em CAIXA ALTA (`c`), com emoji (`e`), tópico (`t`) e texto longo (`d`) |
| Cartão | Uma subcategoria (`DATA[i]`, ex.: "Alemanha", "Sinais De Pontuação"), com `code` |
| Seção | Grupo de cartões na tela inicial (`sec`, ex.: "🌍 Países do Mundo") |
| Ler Mais | O texto longo da curiosidade (`d`), no pop-up `#detOv` |
| LIDA | Botão que marca/desmarca a curiosidade como lida |
| Curiosidades de Hoje | 3 curiosidades sorteadas pelo dia (`diaMode`) |
| Surpresa | 🎲 uma curiosidade ao acaso |
| Dicionário / Palavras Aprendidas | Palavras difíceis (`GLOSSARIO`) que a criança tocou |
| Marcos | Festejos da coruja em 10, 25, 50, 100, 200, 300, 500, 800, 1000 lidas |
| Destaque por linha / marca-texto | Tocar marca a linha inteira (`modoLinha`) |
| Ajuda sonora | Botões de ouvir (🔊) e ler ao tocar |
| Gaveta de ajustes | 🎨 ✒️ Aa A− A+ ⛶ na leitura (⚙️ da leitura) |
| Leitor / usuário / criança | A mesma coisa: um perfil com nome + bichinho |
| Bichinho | Um dos 8 emojis oficiais (`av` no código) |
| Chave do leitor | `nome-sem-acento_hexdoemoji` (ex.: `bia_1f430`) — identidade na nuvem |
| Código da família | Texto (≥ 6 letras/números) que junta as crianças da família na nuvem |
| Nuvem | Firebase (Firestore) via `nuvem-sync.js` |
| Ficha | O documento da criança na nuvem |
| Pendência / fila | Alteração guardada no celular esperando subir |
| Juntar / mesclar | Misturar o que veio da nuvem com o do celular sem apagar nada |
| Versões guardadas | Cópia de cada dia na nuvem (`versoes/AAAA-MM-DD`) |
| Bolinha / pontinho | `#nuvemPonto`: verde, laranja ou vermelho |
| Modo reserva | Vídeo mudo invisível que mantém a tela acesa quando o Wake Lock é recusado |
| Convite | Pop-up "📲 Instalar o app" do `escola-pwa.js` |
| Pacote | Os 8 arquivos que vão para o Netlify |
| Cópias mestras | Versões oficiais dos arquivos compartilhados (08/10/2026) |
| T1–T8 | Telas do `escola-familia.js` (boas-vindas, código, criar código, quem vai estudar, nova criança, buscar na nuvem, arrumar, famílias) |

---

## 15. v2.0 — novo cadastro da família (08/10/2026) 📄

**Estado (atualizado à noite):** a **v2.0b** (15.8) foi **aprovada pelo Pedro** para o site de verdade. O texto abaixo (15.1–15.7) conta a v2.0 como foi entregue para o site de teste.

**Estado da v2.0 (tarde):** entregue para o **SITE DE TESTE** (`curiosidades-netlify_v2.0_SITE_DE_TESTE.zip`, roteiro em `documentos/INSTRUCOES_SITE_DE_TESTE_v2.0.md`). O site de verdade continua na **v1.8** até o Pedro aprovar. Cache do `sw.js`: **`curiosidades-mundo-v2-0`** (o `v1-9` continua reservado para a v1.9 guardada). A v1.9 **não** foi aplicada (vem numa entrega separada, depois do cadastro publicado e conferido).

### 15.1 O pedido e as respostas do Pedro
- Pedido: implantar o `PLANO_CADASTRO_FAMILIA.md` (v3, D1–D18) em cima da v1.8 publicada, seguindo o Alfabetização v123 como modelo; não começar se faltasse arquivo.
- Faltava o zip completo do Alfabetização v123 (com os testes): o Pedro anexou. Também anexou o **backup real** do app (`curiosidades-do-mundo-backup-2026-10-08.json`: 1 criança, 🦋 Hinata, 33 curiosidades lidas), guardado em `testes/dados/`.
- Decisões dele nesta conversa: cache **`curiosidades-mundo-v2-0`**; **site de teste novo** (`escolasaopedrocuriosidadestestes`) e apagar o antigo; **chip e bolinha também na barra da leitura** (opção A: chip à esquerda da ⚙️ da gaveta de ajustes, bolinha nessa ⚙️, que continua abrindo a gaveta).

### 15.2 O que mudou (só o `index.html` e o `sw.js` do app; os compartilhados são as cópias mestras sem mudança)
Feito por `trabalho/patch20.py` (trocas exatas a partir da v1.8 publicada, que confere o md5 da base e que as 4 linhas de dados ficaram idênticas).
- **Arquivos:** entra o `escola-familia.js` **1.2**; o `nuvem-sync.js` passa da v3 para a **4.1** (cópias mestras, md5 conferido); `escola-pwa.js` v2 e o `nuvem-config.js` do Pedro iguais. `sw.js`: cache `curiosidades-mundo-v2-0` e `./escola-familia.js` na lista.
- **Saíram** (agora são do módulo): as telas `#users`, `#novoUser`, `#nuvemTela` e o pop-up `#codigoOv`, o chip antigo `#userChip`, a bolinha `#nuvemPonto`, a seção "☁️ Nuvem" das Configurações e as funções deles. Ficaram como atalhos: `abrirUsers()` → T4 e `abrirNovoUser()` → T5.
- **Adaptador** `ADAPTADOR_CRIANCAS` (parte 5.2 do plano): `listar` (= `U.us`), `atual` (= `U.atual`), `criar(nome, av)` (id `p…` novo e nunca repetido, `novoIdCrianca`; não troca a criança aberta), `mudar`, `exportar` (as **22** chaves de `CHAVES_NUVEM`, com `ultimoDia`/`seqDias`), `importar` (= `nuvemMesclar(…, false)`: junta), `tirar` (1º sai da lista; se era a aberta, `U.atual=null`; depois apaga as 22 chaves; recarrega), `completoNaNuvem` (sempre true), `entrar` (= `trocarUser`; a mesma criança escolhida pelo chip no meio do uso volta para onde estava), `resumo` ("🌍 N de 4034" + barra), `resumoDados`, `chavesDaCrianca` (as 22).
- **Ligação** (no lugar da antiga ligação da nuvem): `EscolaFamilia.iniciar({app:'curiosidades', maxPorFamilia:6, criancas:ADAPTADOR_CRIANCAS, abrirConfig, fecharConfig, aoAbrirTelas (cala a voz), aoFecharTelas})` → `NuvemSync.iniciar({usuarios: EscolaFamilia.paraNuvem(…)})` → trava "sem criança" por cima da vigia → `montarChip` (tela inicial e leitura), `montarPonto` (⚙️ da tela inicial e ⚙️ da leitura), `montarSecaoConfig(#cfgFamilia)`.
- **Abertura (D2):** sempre T4 "🦉 QUEM VAI ESTUDAR HOJE?" (ou T1 sem família); atrás dela a estante; ao tocar na criança, vai para a estante dela. Acabou o "1 criança entra direto".
- **Barra de cima:** chip colado à esquerda da ⚙️ (tela inicial e leitura). Se não couber: 1º o chip fica só com o bichinho; 2º só os espaços entre os botões diminuem (`ajustarBarrasDeCima`, chamado ao abrir a estante, a leitura, a gaveta e ao girar). Os botões nunca encolhem (mesmas medidas da v1.8, conferidas no teste).
- **Configurações:** deitado, o pop-up usa a largura (até 980 px; 2 colunas a partir de 700 px); a última seção é "☁️ FAMÍLIA E NUVEM". Fica um aviso próprio do app, acima dela, só quando as cópias de cada dia não gravam (Regras antigas) — era o que a v1.8 mostrava na "Situação".
- **Backup (D13):** importar **junta** (antes apagava tudo e gravava por cima): cada criança do arquivo é achada pelo nome + bichinho na família atual; se não existe, entra como nova (primeiro entra na lista, depois junta); confere o arquivo antes; pergunta no estilo do app (`#perguntaOv`), sem `alert`/`confirm`. Exportar leva também `ultimoDia`/`seqDias`. Backups da v1.8 continuam sendo aceitos.
- **`nuvemMesclar` blindado** (plano 5.3, itens 14, 16 e 17): não grava em criança que não está na lista; cada parte num `try` (um dado estragado não para a junção no meio); só aceita listas onde espera lista e texto onde espera texto.
- **"Leitor 1" fantasma corrigido:** com `mundo_usuarios` existente e **vazio** (todas as crianças saíram), `carregarUsers` não recria o "Leitor 1 🦊" a partir da chave antiga `mundo_lidas`.
- **Trava "sem criança":** sem criança escolhida, nenhuma chave `mundo_p0_*` é gravada (ligada antes de carregar os dados e de novo por cima da vigia da nuvem). Acaba a criação das chaves fantasmas da v1.8 (capítulo 6.9, item 7).
- **Nada de caixinha do navegador:** sumiram todos os `alert`/`confirm` (apagar, juntar versão, backup).

### 15.3 Novas chaves no celular (só acrescenta; nada antigo é apagado ou renomeado)
- `escola_familia` (do módulo: famílias, criança → família, família atual, 1ª abertura da versão nova, mudanças pendentes).
- `escola_lixeira_curiosidades` (crianças tiradas com "guardar uma cópia neste celular").
- `nuvem_familia` continua sendo gravado (= família atual) para a v1.8 funcionar se for preciso voltar.
- Migração testada com o **backup real do Pedro**: abrindo a v1.8 e a v2.0 sobre o mesmo retrato, todas as chaves antigas ficam **idênticas byte a byte**; a única chave nova é `escola_familia` (teste_familia 7-A).

### 15.4 Riscos do capítulo 6.9 → v2.0
1 (apagar sem garantia) → só tira com a nuvem confirmando ou com cópia na lixeira (trava do adulto); 2 (age na criança atual) → ✏️/🗑️ no cartão de cada criança; 3 (órfãs) → `tirar` apaga as 22 chaves e o módulo limpa a fila e o meta; 4 (backup substitui) → junta; 5 (botões abaixo do teclado) → telas do módulo (cartão no meio); 6 (textos misturados) → tabela 3-A; 7 (`p0`) → trava; 9 (trocar o código move todas) → código novo acrescenta família; 10 (`sayTapOn`) → continua (vem com a v1.9); 11 (envio do mesmo celular substitui) → (a) backup junta e (b) `nuvem-sync` 4.1 junta quando não conhece a ficha — os dois testados; 12 (aviso falso do backup) → nada é apagado antes; 13 (texto contraditório) → bolinha do módulo. **Continua:** 8 (fila criada sem nuvem, inofensivo) e a frase repetida do Cerrado (fora do cadastro).

### 15.5 Testes (pasta `testes/`; rodar com `bash testes/rodar_todos.sh`, uma suíte de cada vez)
- Antigos adaptados às telas novas (o que cada conferência prova continua igual): `regressao.py` 10, `sw_test.py`, `teste_cadastro.py` 41, `teste_nuvem_v20.py` 94 (o mesmo `teste_nuvem_v18.py`, entrando pelas telas novas). Os originais ficaram em `testes/antigos_v1.8/`.
- Novos (`testes/navegador/`, adaptados do Alfabetização v123: `base.py`, `fakefb.py` — Firebase de mentira —, `ef.py`): `teste_familia.py` (parte 9 do plano + migração com o backup real + backup que junta + juntar com dados estragados + ⚙️ na T4), `teste_desenho.py` (tamanhos 984×432, 937×411, 740×360, 640×360, 568×320, tablet e em pé; seção 8 = barras de cima comparadas com a v1.8), `teste_v20.py` (⚙️ na T4, C1, C2, abertura) e `prova_testes_pegam.py` (cada correção desfeita → o teste falha; e a v1.8 publicada falha).
- `testes/versao_anterior_v1.8/` = o pacote publicado (com o `nuvem-config.js` FALSO dos testes), usado na migração e no "voltar ao zip anterior".
- Resultados: `trabalho/saida_testes/` e o `RELATORIO_CHECAGEM_curiosidades_v2.0.md`.

### 15.6 Aprendizados desta implantação
| O que aconteceu | Causa | Como evitar |
|---|---|---|
| A trava "sem criança" ligada só no fim do script deixaria a abertura gravar `mundo_p0_ultimoDia` | `carregarDados()` roda no começo do script (antes da nuvem) | ligar a trava antes de carregar os dados e de novo depois do `NuvemSync.iniciar` (a vigia troca o `setItem`) |
| Leitura em 568×320 com a gaveta aberta: a ⚙️ saía da tela | o chip ocupa 48–115 px numa barra que já estava cheia | compactar em 2 passos (chip só bichinho; depois só os espaços); teste compara com a v1.8 |
| Configurações a 740 px: a linha "Crianças deste celular" quebrava | o cartão ficava em 92% da largura | 96% deitado e um pouco menos de margem interna |
| Testes: `inner_text` devolve o texto em CAIXA ALTA (o CSS transforma) | `text-transform` | comparar com `text_content` |
| Roteiro do Pedro: tirar a Hinata quando ela é a única | regra das 2 semanas (não tira a última) | testar "tirar" com uma criança de teste |

### 15.7 Checagem (parte 9-A) — resultado
Autochecagem (matriz em `documentos/RELATORIO_CHECAGEM_curiosidades_v2.0.md`: regressão 10/10, SW ok, cadastro 41/41, nuvem 94/94, família 167/167, desenho 151/151, v20 36/36, prova 7/7) → **conferente independente** (rodada 1: 0 🔴 · 0 🟠 · 4 🟡; A1 título das Configurações e A2 botões de 48 px corrigidos; rodada 2: ✅) → **revisor-chefe: ✅ Pode publicar no site de teste** (0 🔴 · 0 🟠; 4 🟡: Y1 e Y2 arrumados nos documentos, Y3 e Y4 registrados como pendências). Pendências 🟡 para o Pedro decidir: A3/A4 (botões antigos do app com 40 px e ajudas de 13 px, iguais à v1.8), Y3 ("Leitor 1" só se tirar todas, passarem as 2 semanas, voltar à v1.8 e o celular tiver a chave muito antiga `mundo_lidas`), Y4 (backup trazendo criança nova leva também o tema/letra). **Regra daqui em diante:** qualquer mudança em `pacote-netlify/` sobe o cache (`v2-0b`, …).

### 15.8 v2.0b — o teste do Pedro e a correção (08/10/2026, noite) 📄
**O teste do Pedro** no site de teste (`escolasaopedrocuriosidadestestes`, família `pmrtestes`, criança nova, marcou lidas): cadastro, gravação e recuperação **"excelentes"**. Duas observações:
1. **"Destacar por sílaba" só valeu depois de fechar e abrir o app** → defeito de verdade, **antigo** (a v1.8 também tinha), corrigido.
2. Achou que a ⚙️ da barra de leitura devia sair (pensou que eram as Configurações e "não abriam"). Depois ele mesmo corrigiu: **"Não alterar nada. É para continuar da forma que está."** A ⚙️ da leitura continua abrindo a gaveta de ajustes (opção A da 15.1).

**Causa do defeito (palavras simples):** quando uma criança **ainda não tem nenhuma curiosidade lida neste celular**, o `nuvemMesclar` achava que o celular estava "vazio, acabando de chegar" (`restaurando=true`) e então deixava as **preferências da nuvem** (tema, sílabas, letra…) passarem por cima das daqui. Na criança nova do Pedro: ele ligou "sílabas"; logo depois chegou da nuvem uma cópia mais velha (a gravada ao criar a criança, ou de outro aparelho) com "sílabas desligado" → o app voltou a desligar, sem mostrar. Ao fechar e abrir, o valor certo acabou ficando (💭 provavelmente porque a nuvem já tinha recebido a mudança dele). Com a criança **com lidas** (a Hinata de verdade) isso não acontecia.

**Correção** (`trabalho/patch20.py`, dentro do `nuvemMesclar`): "celular vazio" agora só quando **não há lidas E não há nenhuma preferência guardada aqui** (`PREFS_LOCAIS = theme, font, caps, fsize, cfgHi, cfgSyl, cfgAudio, voz, modoLinha, ajustes` — as que o `saveState` grava). Os caminhos de **trazer a criança da nuvem** (T4/T6 num celular novo, voltar da lixeira) já mandam `restaurando=true` direto, então continuam adotando as preferências da nuvem. `sw.js`: cache **`curiosidades-mundo-v2-0b`**. `index.html` md5 `6052fb7fd374f56225e370fd8eb3133b`. Compartilhados e `nuvem-config.js` sem mudança.

**Efeito colateral aceito (🟡 do conferente, rodada 3):** uma criança com 0 lidas que **já gravou as preferências padrão** (só abriu o app) não adota mais as preferências da nuvem numa junção automática em segundo plano (o progresso continua juntando). Só aparece se a criança for criada sem internet com o mesmo nome + bichinho de uma que já está na nuvem. É o preço de "o que a criança mudou aqui vale".

**Outra coisa que pode confundir (não é defeito):** com **"Destaque por linha"** ligado (ou com a voz em 🔇), todo toque marca a **linha inteira**, então "por sílaba" e "por palavra" ficam iguais de ver. É a regra 7 do capítulo 4 (ajuda sonora e destaque por linha andam juntos).

**Testes (rodados de verdade, no pacote final; rodados de novo em 14/10/2026 — ver o relatório de checagem):** regressão 10/10 · SW ok · cadastro 41/41 · nuvem 94/94 · família 167/167 · desenho 151/151 · v20 **40/40** (nova seção 6: preferência mudada fica depois da junção, continua depois de recarregar, e criança trazida da nuvem ainda adota o tema/sílabas de lá) · prova **8/8** (novo item "preferência fica": a v1.8 falha nele).

**Checagem 9-A:** autochecagem acima + **conferente, rodada 3** (`documentos/revisao_independente/RELATORIO_CONFERENTE_v2.0b_rodada3.md`): 0 🔴, 1 🟡 (o efeito colateral acima), reproduziu o defeito na v2.0 e confirmou a correção; atualização do celular v2.0 → v2.0b apaga o cache velho sem tocar nos dados. **Revisor-chefe (14/10/2026): ✅ pode publicar no site de verdade** (`RELATORIO_REVISOR_CHEFE_v2.0b.md`); os 2 🟠 (texto "o Pedro testou a v2.0b" — ele testou a v2.0 — e um print antigo com um código digitado) foram corrigidos; a conferência 14 do `teste_familia` dependia da data e foi corrigida (só o teste).

**📝 Para os outros apps:** o `nuvemMesclar` do **Alfabetização** tem a mesma regra automática de "celular vazio" (olhando o `hana_done`). **Não foi mudado** (cada app tem o seu `nuvemMesclar`; não é arquivo compartilhado). Vale levar esta correção quando o Alfabetização for mexido de novo, com o OK do Pedro.

### 15.9 Quando entra a v1.9 💭 (proposta; o Pedro confirma)
Logo **depois que a v2.0b estiver publicada no site de verdade e conferida** (bolinha 🟢, Hinata com o progresso certo nos 2 celulares, um ou dois dias de uso). Entrega separada, levando as 10 mudanças do `trabalho/v1.9-pendente/O_QUE_MUDA_NA_V1.9.md` **uma a uma para cima da v2.0b** (nunca copiar o `index.html` da v1.9). Cache sugerido: `curiosidades-mundo-v2-1` (o `v1-9` fica sem uso). Atenção: `sayTap` entra no `CHAVES_NUVEM`/`PREFS_LOCAIS`; K4 (primeira troca do dia); Esc/setas com as telas do `escola-familia.js`; o backup da v1.9 apagava antes de gravar — **manter o "junta" da v2.0**.

### 15.10 Mais curiosidades (pedido do Pedro, 08/10/2026) 💭
O Pedro quer **mais curiosidades**: "sobre cientistas, matemáticos, filósofos como Platão e Sócrates, físicos, químicos de todas as áreas" — a Hinata acha muito interessante a história de **Marie Curie** (e está lendo **Leonardo da Vinci**); "mas não limitando a estas": ela também adorou um texto feito com o Claude (no Coruja Explica) sobre **asteroides, cometas e outros corpos celestes**.
O que já existe 📄: Cientistas E Inventores (C1 Einstein, **C2 Marie Curie**, C3 Santos Dumont, C4 Grandes Inventores, C5 Exploradores, C6 Newton, **C7 Leonardo Da Vinci**, C8 Darwin, C9 Ada Lovelace, C10 Cientistas Do Brasil, C11 Astronautas); Matemática Divertida X9 Matemáticos Famosos; Espaço (… COM Cometas E Asteroides, GIG Gigantes Do Espaço, CONST Constelações); História: HGR Gregos Antigos. Sócrates/Platão/Pitágoras/Hipátia aparecem só de passagem; **não têm cartão próprio**: Sócrates, Platão, Aristóteles, Galileu, Pasteur, Lavoisier, Mendeleiev, Faraday, Kepler, Copérnico, Hawking, planetas anões (Plutão), meteoros/meteoritos, estrelas, galáxias, buracos negros, telescópios e sondas.
Proposta (o Pedro escolhe a lista final): cartões novos **no fim** das seções (códigos novos, nunca reaproveitar), ~15 curiosidades cada, mesmo formato (frase curta + "Ler Mais"), CAIXA ALTA; e curiosidades novas **no fim** dos cartões C2 (Marie Curie) e C7 (Leonardo), se ele quiser. Regras: parser de colchetes balanceados; curiosidade nova só no fim do cartão; conferir que nenhuma lida existente muda de lugar; contagens novas (4.034 → …) nos textos que mostram o total.

### 15.11 Ideias para a educação da Hinata 💭 (sugestões, nada feito; o Pedro decide)
1. **Perguntas de compreensão por cartão** — ao terminar um cartão, 3 perguntas sobre o que ela leu (uma "o que o texto diz", uma "por quê", uma "o que você acha"). O 🎯 Desafio Rápido de hoje só liga a frase ao emoji (reconhecer, não compreender). A Hinata gostou do quiz do Coruja Explica.
2. **"Conte para alguém"** — no fim do cartão, a coruja convida: "Conte para o papai uma coisa que você aprendeu!", com um botão "Contei! ✅". Reconto oral é dos melhores exercícios de compreensão e custa quase nada.
3. **Linha do tempo dos cientistas e pensadores** — Sócrates → Platão → Aristóteles → … → Leonardo → Newton → Marie Curie → Einstein; tocar abre o cartão. Dá noção de tempo histórico ("antes de Cristo", séculos).
4. **"Leia também"** no fim do cartão (Marie Curie → Química e Física; Platão → Gregos Antigos; Cometas → Constelações). Transforma a curiosidade dela num caminho.
5. **Revisar o Dicionário** — mini-jogo palavra ↔ significado com as palavras que ela já tocou. Vocabulário é o que mais pesa na compreensão.
6. **Resumo para o pai** na ⚙️: o que ela leu na semana (seções, cartões, palavras novas) — assunto para a conversa no jantar.
7. **"Minha curiosidade"** — ela dita ou escreve uma curiosidade dela mesma (produção de texto); fica num cantinho dela.

**Escolhas do Pedro (14/10/2026), depois de ver a explicação de cada ideia:** gostou de **Revisar o Dicionário**, **Linha do Tempo**, **Conte para o papai**, **Resumo da semana** e **Leia também**. Sugestões a mais apresentadas (ele ainda não decidiu): **Perguntas de compreensão** (a mais recomendada), **Mapa do mundo** (países lidos coloridos) e **Eu leio primeiro** (ela lê em voz alta e depois confere com o 🔊). Atenção para o Resumo da semana: hoje o app não guarda a DATA de cada leitura; o resumo só conta a partir da versão que trouxer essa chave nova.
Ordem proposta: **v2.1** = v1.9 → **v2.2** = curiosidades novas (15.10) → **v2.3 em diante** = as ideias, uma ou duas por vez (começar por Conte para o papai e Revisar o Dicionário). Sempre com plano e autorização antes.

---

## 16. v2.1 — as novidades da v1.9 em cima do novo cadastro (14/10/2026) 📄

**Pedido:** "Ok v2.1 (as mudanças da v1.9, com o cache curiosidades-mundo-v2-1)." Cache: **`curiosidades-mundo-v2-1`** (o `v1-9` nunca foi usado no site).

### 16.1 Como foi feito
`trabalho/patch21.py` (rodar: `python3 trabalho/patch21.py testes/versao_anterior_v1.8/index.html trabalho/v1.9-pendente/index.html trabalho/base_v2.0b/index.html pacote-netlify/index.html`). Ele pega a diferença **v1.8 → v1.9** em grupos com 3 linhas de contexto, confere que cada trecho antigo existe **uma vez** na v2.0b e troca pelo trecho novo da v1.9 (25 grupos). Se a v2.0 tivesse mexido naquele trecho, o script para (assert) em vez de estragar. O bloco do arrastar/setas/Esc entra antes de `/* ===== INIT ===== */` (na v2.0b o que vem antes é a ligação do cadastro). A base da v2.0b fica guardada em `trabalho/base_v2.0b/`.

### 16.2 As 10 mudanças da v1.9 na v2.1
1. ▶️ **Continuar de onde parei** — faixa na tela inicial (usa `ultPais`/`ultCur`, que já existiam).
2. 🔊 **"Ler ao tocar" lembrado** — chave nova `mundo_<id>_sayTap` (padrão ligado). Entra no backup e na nuvem: `CHAVES_DADOS` 21, `CHAVES_NUVEM` **23** (o adaptador do cadastro exporta, tira e lista as 23), `CHAVES_SIMPLES_NUVEM` e `PREFS_LOCAIS`.
3. 🔥 **Dias seguidos só com leitura** — `atualizarSequencia` só lê; `registrarDiaDeLeitura` grava ao marcar LIDA. Abrir o app não grava mais o dia.
4. 🎤 **Karaokê no ritmo da voz** (evento `boundary`; sem ele, o ritmo antigo).
5. 🏅 **Marcos até 4.034** + medalhas 🚀 Astronauta do Saber, 🦉 Coruja Sábia, 🌈 Arco-Íris do Saber, 🌍 Leu o Mundo Inteiro.
6. 🎯 **Desafio com placar**, dica e "💪 Boa tentativa!".
7. 🛡️ **Backup conferido** — **NÃO entrou o código da v1.9**: ele usava `alert()` e continuava apagando antes de gravar. A v2.0 já confere o arquivo campo a campo e **junta** (nunca apaga), sem caixinha do navegador.
8. 👉 **Arrastar o dedo, setas ← → e Esc.**
9. 🔍 **Busca mais leve** (índice preparado uma vez).
10. 🕒 **Últimas Lidas com `textContent`.**

### 16.3 Ajustes próprios da v2.1 (encontros da v1.9 com o cadastro novo)
- **Esc**: sem `fecharCodigoFamilia()` (o pop-up antigo do código saiu na v2.0); com a pergunta do app (`#perguntaOv`) aberta, o Esc não fecha nada por baixo dela (a pergunta ficaria sem resposta).
- **Setas e arrastar**: não agem com uma tela do cadastro aberta por cima (`#efRaiz.ef-ativo`: T4, T5, T6, Arrumar…).
- **`sayTap` em `PREFS_LOCAIS`** (a lista da correção da v2.0b).
- **Entrar numa criança confere a nuvem** (🟠 achado pelo conferente, rodada 4). **Causa, em palavras simples:** na v1.8/v2.0b, a primeira troca do dia para uma criança gravava o "dia" dela, e essa gravação, de carona, disparava um envio para a nuvem — e o envio trazia junto o que ela tinha lido no outro celular. Com a v1.9 o dia só é gravado ao ler, então essa carona sumiu: escolher a Bia no celular B (aberto o dia todo) não trazia as leituras dela do celular A até alguma outra coisa sincronizar. **Correção:** `ADAPTADOR_CRIANCAS.entrar` chama `NuvemSync.sincronizar()` quando troca de criança (ou na abertura). Teste dos 2 celulares: na v2.1 sem a correção, nada chega em 16 s; com a correção, chega em menos de 1 s.

### 16.4 Testes
- Novo `testes/navegador/teste_v21.py` (adaptado do `teste_v19_novidades.py`, que usava as telas antigas): continuar, setas/Esc com as telas do cadastro, arrastar (com toque simulado), dias seguidos, marcos/medalhas, `sayTap` no celular/nuvem/backup/criança trazida da nuvem, desafio, karaokê com a "voz" de mentira avisando a palavra, busca igual à de antes, Últimas Lidas, e **2 celulares** (o achado do conferente).
- `prova_testes_pegam.py`: itens novos da v2.1 (seta com a T4 por cima; "ler ao tocar" lembrado e "abrir não conta o dia" contra a v2.0b; escolher a criança traz o outro celular). O item "sem chaves p0" foi reforçado: com a v1.9, abrir já não grava o dia, então a conferência também troca as cores sem criança escolhida.
- `teste_familia.py` 7-A: aceita que a v2.x **não** grave `ultimoDia`/`seqDias` ao abrir (a v1.8 gravava); todas as outras chaves continuam idênticas byte a byte. FAM 13 espera o cache `v2-1`.
- Resultados: `documentos/RELATORIO_CHECAGEM_curiosidades_v2.1.md`.

### 16.5 Limitações conhecidas (🟡, iguais ou melhores que antes)
- Um celular na v2.0b (ou v1.8) que envia a ficha da criança tira o `sayTap` dela na nuvem; o celular na v2.1 mantém o seu e devolve na próxima sincronização. Só a preferência; nenhuma leitura se perde.
- Dias seguidos: o celular que lê hoje manda na sequência (chave simples); um celular parado pode baixar a sequência do outro na nuvem (5 → 1). Já acontecia na v2.0b (até ao só abrir o app); na v2.1 acontece menos.
- "Continuar de onde parei" pode apontar para um cartão visto de passagem pelas Favoritas ou pelas Curiosidades de Hoje (é onde ela esteve por último).
- Não testável no computador: karaokê com a voz de verdade, arrastar com o dedo de verdade, celular real, Firebase real.

---

## 17. v2.2 — curiosidades novas (14/10/2026) 📄

**Pedido:** "Perfeito. Implementar." (a lista de 16 cartões proposta) + "Se possível aumentar 'Mulheres na Ciência: Hipátia'." Cache: **`curiosidades-mundo-v2-2`**.

### 17.1 O que entrou (220 curiosidades novas; 4.034 → **4.254**; 278 → **295** cartões)
- **🔬 Cientistas E Inventores** (no fim da seção): C12 🤔 Sócrates (12) · C13 📜 Platão (12) · C14 🦉 Aristóteles (12) · **C17 📐 Hipátia De Alexandria (15 — cartão próprio, como o Pedro pediu)** · C15 🌕 Galileu Galilei (12) · C16 🦠 Louis Pasteur (12) · **C18 👩‍🔬 Mulheres Na Ciência (15)** (Merian, Marie-Anne Lavoisier, Mary Anning, Lise Meitner, Barbara McClintock, Chien-Shiung Wu, Tu Youyou, Valentina Tereshkova, Mae Jemison, Grace Hopper, Jane Goodall, Katherine Johnson, Bertha Lutz, Nise da Silveira…) · C19 🧪 Químicos Famosos (12) · C20 ⚡ Físicos Famosos (12) · C21 🌟 Astrônomos (12).
- **🚀 Espaço** (no fim da seção): MET 🌠 Meteoros E Meteoritos · PLAN 🟣 Planetas Anões · EST ⭐ Estrelas · GALX 🌀 Galáxias · BN ⚫ Buracos Negros · TEL 🔭 Telescópios · SON 🛰️ Sondas Espaciais (12 cada).
- **+5 no fim de C2 Marie Curie** (Manya; universidade secreta; lua de mel de bicicleta; o rádio brilhando à noite; cadernos ainda radioativos) e **+5 no fim de C7 Leonardo** (passarinhos; cavaleiro robô; a ponte na Noruega; "descrever a língua do pica-pau"; estudos da água).
- **Frase do símbolo grande** (`PAIS_DESC`) para os 17 cartões novos (ao tocar no símbolo, diz quem/o que é). **1 emoji novo** com descrição: 📀 (Disco de Ouro).

### 17.2 Como foi feito
1. Guia de escrita (`trabalho/v22/GUIA_DE_ESCRITA.md`), referência dos emojis/códigos/curiosidades existentes e um conferidor de formato (`confere_formato.py`).
2. **5 agentes escritores** em paralelo (A filósofos + Hipátia; B Galileu, Pasteur, Mulheres + extras C2; C químicos, físicos, astrônomos + extras C7; D e E espaço), com pesquisa na web para os pontos duvidosos (`trabalho/v22/escrita/`).
3. **4 agentes conferentes de fatos independentes** (`trabalho/v22/checagem/`): 189 itens OK; **30 correções aplicadas** (ex.: sólidos de Platão explicados direito; "densímetro" no lugar de "hidrômetro"; Pasteur e a cólera das galinhas sem contradição; Faraday "apresentou" (não criou) as Palestras de Natal; radiação Hawking como previsão; a foto do M87 sem o telescópio da Antártida; os arpões do Philae falharam por defeito; Makemake com ~60% da largura de Plutão; DART 33 minutos; Betelgeuse supergigante; dois itens repetidos trocados por fatos novos). Lista completa em `CARTOES_V22_FINAL.json` → `correcoes_aplicadas`.
4. A coordenação ainda trocou TEL #2 (repetia Galileu e a Lua do cartão C15) por "o telescópio é um balde de luz".
5. `trabalho/patch22.py` (rodar: `python3 trabalho/patch22.py trabalho/base_v2.1/index.html trabalho/v22/CARTOES_V22_FINAL.json pacote-netlify/index.html`): **parser de colchetes balanceados**; cartões novos no fim do `DATA`, extras no fim de C2 e C7, frases no `PAIS_DESC`, emoji no `EMOJI_DESC`. Confere que cada cartão antigo ficou igual item por item e que **nenhuma linha de código mudou** (só as 3 linhas de dados).

### 17.3 O que NÃO muda
O código do app (idêntico à v2.1), as lidas de todas as crianças (guardadas por posição: nada antigo mudou de lugar), a nuvem, o cadastro. A última medalha ("🌍 Leu o Mundo Inteiro") e a última festa passam a valer 4.254 (o `TOTAL_CUR` é calculado).

### 17.4 Achados para depois (não mexidos — precisam do OK do Pedro)
- **Cartão de Netuno:** o "Ler Mais" diz que o sinal da Voyager 2 "demora mais de um dia" para chegar; isso vale para a Voyager 1 (a Voyager 2 leva cerca de 19–20 horas).
- **Cartão de Júpiter:** "A NAVE JUNO ESTUDA JÚPITER AGORA" pode estar desatualizado (a missão estendida terminou em 30/09/2025).
- **Defeito antigo do símbolo grande:** nos cartões que não são países e não têm frase própria (ex.: Albert Einstein, Sol, Dinossauros…), tocar no símbolo mostra "O … é um país do mundo." (o app usa essa frase de reserva). Os 17 cartões novos já têm frase própria. Correção sugerida: escrever a frase dos ~238 cartões antigos (só dados) ou trocar a frase de reserva.
- A frase repetida do Cerrado (W3/F4) continua.

### 17.5 Testes
Novo `testes/navegador/teste_v22.py` (dados: cartões antigos iguais item por item, novos no fim, emojis e frases do símbolo, caixa alta, sem frase repetida, código idêntico à v2.1; navegador com o retrato do celular do Pedro: 33 lidas iguais e no mesmo lugar, "33 de 4254", seções com os cartões novos no fim, abrir Hipátia, tocar no símbolo e no emoji, Ler Mais, marcar LIDA, a 16ª de Marie Curie depois das 15 antigas sem mexer nas lidas antigas, busca, marcos) + item novo na prova (curiosidade antiga alterada → o teste pega). Resultados: `documentos/RELATORIO_CHECAGEM_curiosidades_v2.2.md`.

### 17.6 Próximas ideias — estimativa de tempo (pedida pelo Pedro, 14/10/2026) 💭
Tempo = trabalho da IA na conversa (fazer + testar + checagem em 3 etapas), **sem** contar o teste do Pedro no celular. Referência: a v2.1 levou cerca de 3h30 e a v2.2 cerca de 3h. São estimativas.

| Ideia | O que é | Tamanho | Tempo |
|---|---|---|---|
| 🗣️ Conte para o papai | No fim do cartão (ou a cada 5 lidas no dia) a coruja convida a contar; botão "Contei! ✅" soma nas Conquistas | pequena | ~1h30 |
| 📖 Revisar o Dicionário | Jogo palavra ↔ significado com as palavras que ela já tocou; as que erra voltam mais vezes | média | ~2h30 |
| 🔗 Leia também | 2–3 cartões ligados no fim de cada cartão (lista escrita à mão para os 295 cartões) | média (conteúdo) | ~3h |
| 📊 Resumo da semana | Na ⚙️: leituras por dia, seções preferidas, palavras novas, acertos, "contou para o papai". Precisa de uma chave nova com a data de cada leitura (só conta a partir dessa versão) | média | ~2h30 |
| 🕰️ Linha do Tempo | Faixa que rola com 40–60 pessoas/fatos (Sócrates → Lua 1969), toque abre o cartão, lidos acesos | grande | ~3h30 |
| 🗺️ Mapa do mundo | Mapa desenhado dentro do app (sem internet), países lidos coloridos, toque abre o cartão; o arquivo cresce ~100–300 KB | grande | ~4h |
| 🧠 Perguntas de compreensão | 3 perguntas por cartão. Para os 295 cartões são ~885 perguntas (várias rodadas de conteúdo). 1ª rodada: a tela + 30 cartões favoritos | muito grande | ~4h a 1ª rodada (+~3h por leva de 30–40 cartões) |

**Tudo numa rodada só:** ~20–24 h de trabalho. **Não recomendado:** a conversa pode acabar no meio, fica difícil testar tudo de uma vez no celular e, se algo der errado, difícil achar a causa.
**Recomendado (3 rodadas)** *(numeração de 14/10; como a v2.3 virou a margem/recuo, passou a ser v2.4 → v2.5 → v2.6 — ver `ALTERACOES_FUTURAS_curiosidades.md`)*: **v2.3** Conte para o papai + Revisar o Dicionário + Leia também (~7h) → **v2.4** Linha do Tempo + Resumo da semana (~6h) → **v2.5** Mapa do mundo + Perguntas de compreensão, 1ª leva (~8h). Os tempos são o mínimo: cada rodada ainda costuma ter uma rodadinha de acertos depois do seu teste no celular (~1–2h). Antes de cada rodada: plano detalhado e autorização.

### 17.7 Pergunta do Pedro (14/10/2026, tarde): margem direita e recuo de parágrafo como no Coruja Explica 💭
O Pedro mandou o Coruja Explica v3.1 e 4 prints do "⚙️ Ajustes da leitura" dele: **Margem direita do texto** em 3 modos (☰ Normal · ✂️ Sílabas, que corta a palavra na sílaba com tracinho "VE-ZES" e deixa a margem quase reta · ↔️ Espaços, que não corta e só alarga um pouco os espaços) e **Recuo no começo do parágrafo** (liga/desliga, com amostra). Pediu só a avaliação (não implementar ainda).
- **Dá para fazer:** o "Ler Mais" do Curiosidades é o "pai" da tela de leitura do Coruja Explica (mesmo jeito de montar as palavras: `.w` e `.wsp`, parágrafos `<p>`, exemplos com "•"), então o código do Coruja (`hifenizarTexto`, `ajustaMargemDireita`, o teto de 75% do modo Espaços, o recuo `text-indent`) se encaixa quase direto.
- **Onde:** no **"Ler Mais"** (é onde há parágrafos). A frase curta do cartão é centralizada e curta, então margem e recuo não fazem diferença nela.
- **Como:** um **⚙️ novo no alto do "Ler Mais"** (ao lado do ❌) abrindo "⚙️ Ajustes da leitura" com Margem (3 modos) e Recuo, iguais aos do Coruja; o "Tipo de letra" do Coruja não entra (o Curiosidades já tem 9 letras nas Configurações). Padrão: Margem **Normal** (sílabas desligado, como o Pedro pediu) e Recuo **ligado** (como no Coruja) — a confirmar.
- **Cada criança com o seu ajuste**, guardado e levado para a nuvem e para o backup (2 chaves novas: `margem` e `recuo` → listas de chaves, preferências locais e o adaptador do cadastro passam de 23 para 25).
- **Tempo:** ~3h a 3h30 (código ~1h30; testes com textos reais em 6–7 tamanhos, celular deitado e em pé/girado, letras diferentes, A+/A−, caixa alta/baixa, e nuvem/backup ~1h; checagem em 3 etapas ~1h) + acertos depois do teste no celular. Pode ir sozinho numa v2.3 ou junto com "Conte para o papai" (rodada de ~5h).
- Cuidados: para cortar no fim da linha, usar o separador do Coruja (`hifenizarTexto`, com a regra de nunca deixar 1 letra sozinha na ponta da linha e sem cortar siglas/palavras estrangeiras); o texto do "Ler Mais" é todo em CAIXA ALTA (a regra das siglas do Coruja já trata isso).

---

## 18. v2.3 — versão final desta rodada (14–15/10/2026) 📄

**Situação de partida:** o Pedro publicou a **v2.2** e testou — "para mim tudo ok". Prints: tela inicial com "Continuar de onde parei", Configurações da 🐰 Hina, seção Cientistas com os cartões novos, "Quem vai estudar hoje?" no site de teste com "de 4254".
**Pedido:** (1) no "Ler Mais", **margem com sílabas** (justificar cortando na sílaba, como no Coruja Explica) **e o recuo**, ligados nas configurações como no Coruja; (2) "Destacar por sílabas não está fazendo mais sentido" → depois de uma pergunta: **tirar completamente as sílabas** e, se possível, fazer o **destaque duplo** — com o destaque por linha, uma **pressão prolongada** numa palavra dá a ela um segundo destaque (cor da letra ou outro marca-texto); (3) "se houver correções, pode realizar"; (4) entregar tudo para publicação, os documentos para futuras alterações, o **kit do Coruja Explica** e um documento só com as **alterações futuras**. Cache: **`curiosidades-mundo-v2-3`**.

### 18.1 O que mudou
- **Ler Mais — "⚙️ Ajustes da leitura"** (⚙️ novo no alto do Ler Mais, ao lado do ❌, e "📖 Ler Mais › ⚙️ Ajustar" nas Configurações): **Margem direita do texto** — ☰ Normal (padrão) · ✂️ Sílabas (corta a palavra na sílaba com tracinho "VE-ZES"; a sobra da linha é dividida entre os espaços, com teto de 0,20 da letra) · ↔️ Espaços (não corta; cada espaço cresce no máximo 75% do normal) — e **Recuo no começo do parágrafo** (ligado de fábrica, com amostra). O separador de sílabas (`silabasDe`/`hifenizarTexto`, o mesmo do Esforço Vence) e o ajuste da margem (`mapaLocal`, `ajustaMargemDireita`) foram **copiados do Coruja Explica v3.1 sem mudar a lógica** (arquivos em `trabalho/v23_*_coruja.js`). O dicionário e a voz usam a palavra sem o hífen invisível. Cada criança tem o seu ajuste (chaves `margem` e `recuo`, no backup e na nuvem).
- **Sílabas fora:** "Destacar por sílabas" sumiu das Configurações e a chavinha "SÍLABAS" sumiu da barra de baixo (o 🔊 "ler ao tocar" ficou). O valor antigo guardado é ignorado (a chave continua existindo, para não quebrar nada). **Efeito bom:** com "sílabas" ligado, a frase do cartão não marcava as palavras do Dicionário — agora marca (por isso o Dicionário da Hina estava "Nenhuma ainda").
- **Destaque duplo (nova opção "Destacar palavra (segurar o dedo)", ligada de fábrica):** **só com o destaque por linha** (ou a voz em 🔇), **segurar o dedo ~meio segundo** numa palavra marca a linha e dá à palavra um segundo destaque (as cores invertidas: fundo na cor da letra e letra na cor do cartão — aparece bem em todos os temas, inclusive Noite). Sem o destaque por linha, segurar o dedo é um toque normal (a palavra fala). Um toque normal em outra palavra tira. Vale na frase do cartão e no Ler Mais. Segurar não abre o menu do navegador. Chave `palavra`.
- **Marca-texto da linha:** passou a ser a `destacarLinha` do Coruja Explica (mede cada pedaço da palavra), porque com "✂️ Sílabas" uma palavra pode começar numa linha e terminar na de baixo.
- **Nomes de outras línguas não são cortados** com "✂️ Sílabas" (lista `NAO_CORTAR`: EINSTEIN, PASTEUR, CURIE, LOUIS, LAVOISIER, HERSCHEL, BEETHOVEN, BRAILLE… — as regras do português cortariam EINS-TE-IN, PAS-TE-UR).
- **Correções de conteúdo:** Júpiter #11 (a Juno "estuda agora" → "chegou em 2016 e passou anos estudando"); Netuno #8 (o sinal da Voyager 2 leva **quase 20 horas**, não "mais de um dia"); Nosso Cerrado #3 (repetia a frase da "caixa-d'água" de Nossa Terra #2 → "o Cerrado é o segundo maior bioma do Brasil"); **frase do símbolo grande nos 238 cartões que não tinham** (antes aparecia "O Albert Einstein é um país do mundo."). As lidas não mudam (as posições são as mesmas).
- **Correções do revisor-chefe (15/10/2026):** segurar a palavra por **mais de ~3 s** fazia o segundo destaque sumir ao soltar (a janela que "engole" o clique do soltar contava de quando o destaque aparecia; agora conta de quando o dedo **sobe**, e dura 1 s); Nosso Cerrado #3 com o emoji 🗺️ (o 💧 era da frase antiga); 3 hífens invisíveis escondidos no dado desde versões antigas, em 2 curiosidades (Brasil Colônia #5 "MIS-CIGENAÇÃO"; Idade Média #17 "OREL-HAS", 2 vezes — divisão errada), retirados, e na mesma curiosidade "NUM ARMAÇÃO" → "NUMA ARMAÇÃO"; frase do símbolo do cartão "Leite e Derivados" (AL5): "Juntos, eles formam a turma dos laticínios" (o leite não é derivado dele mesmo).
- Ajuste de desenho: o ✨ do título do Ler Mais saiu de cima da ⚙️ nova.
- Chaves por criança: `CHAVES_DADOS` 24, `CHAVES_NUVEM` **26** (o adaptador do cadastro exporta, tira e lista as 26); `PREFS_LOCAIS` com `margem`, `recuo`, `palavra`.

### 18.2 Como foi feito
`trabalho/patch23.py` (rodar, de dentro de `trabalho/`: `python3 patch23.py base_v2.2/index.html v23_frases_simbolo.json v23_silabador_coruja.js v23_mapalocal_coruja.js v23_margem_coruja.js v23_destacarlinha_coruja.js ../pacote-netlify/index.html`): trocas exatas; dados por JSON (o DATA/PAIS_DESC voltam idênticos ao serem lidos e escritos — conferido); confere que só as 5 curiosidades autorizadas mudaram (JUP #11, NET #8, F4 #3 e, só tirando hífens invisíveis, HBR #5 e HID #17), que todo cartão tem a frase do símbolo e que as fontes e o EMOJI_DESC não mudaram. As 238 frases do símbolo foram escritas por um agente (`trabalho/v23_frases_simbolo.json`), com 4 ajustes da coordenação (Tiradentes sem a Maria Fumaça; Paraíba "o lugar mais a leste do continente"; Índia "os números que usamos nasceram lá"; zero "precisou ser inventado").

### 18.3 Testes
Novo `testes/navegador/teste_v23.py` (dados; sílabas fora e o dicionário de volta; Ler Mais nos 3 modos com medições — pontos de corte, linhas rentes, teto de 75% nos espaços, recuo —; ajustes por criança no celular, nuvem e backup; ⚙️ do Ler Mais e das Configurações; Esc; tamanhos 984×432, 740×360, 568×320 e 360×740; destaque duplo no cartão e no Ler Mais, toque rápido não marca, menu do navegador não abre, desligar a opção). Ajustados: `teste_v20` seção 6 e a prova "preferência fica" usam o "destaque por linha" (as sílabas saíram); `teste_v21` 26 chaves; `teste_v22` confere a entrega da v2.2 guardada em `trabalho/base_v2.2/`; prova com 4 itens novos (destaque duplo; Ler Mais com sílabas; e, contra a v2.3 de antes da rodada 7 guardada em `trabalho/v23_rodada7_antes/`: marca-texto de uma linha só com Sílabas; segurar o dedo sem o destaque por linha faz a palavra falar). `teste_v23` seção 5 = correções da rodada 7; seção 6 = correções do revisor-chefe (segurar 3,5 s e 6 s mantém o destaque; um toque de propósito depois não é engolido; emoji, hífens, laticínios). Prova contra a v2.3 aprovada na rodada 8 (guardada em `trabalho/v23_rodada8_antes/`): segurar 3,5 s. Resultados: `documentos/RELATORIO_CHECAGEM_curiosidades_v2.3.md`.

### 18.4 Documentos novos desta rodada
- `documentos/ALTERACOES_FUTURAS_curiosidades.md` — **tudo o que ainda não foi feito**, com tempo estimado.
- `documentos/INSTRUCOES_PUBLICAR_v2.3.md` — passo a passo da publicação final.
- `kit-cadastro-coruja-explica.zip` (entregue à parte em 15/10/2026; cópia em `trabalho/kit-cadastro-coruja-explica/`) — o que anexar na conversa do Coruja Explica: `00_LEIA-ME_PRIMEIRO.md` (lista e texto pronto para colar), `GUIA_IMPLANTAR_CADASTRO_NOVO_APP.md`, plano, modelo da ligação, cópias mestras com o `nuvem-config.js`, testes de modelo e o histórico. Junto: `curiosidades-completo-v2.2.zip` e `alfabetizacao-completo-v123.zip` (modelos). Depois do revisor-chefe o kit foi corrigido (nomes de arquivos que não existiam, passo do `sw.js` no guia, modelo de `sw.js`, histórico atualizado) e **entregue de novo** junto com a v2.3; o modelo indicado passou a ser o `curiosidades-completo-v2.3.zip` (o da v2.2 também serve: a ligação do cadastro é a mesma).

### 18.5 Checagem (parte 9-A)
- **Conferente, rodada 7:** ❌ 2 🟠 — (1) com "✂️ Sílabas" e destaque por linha, o marca-texto saía com o dobro da altura e o Ler Mais rolava de lado (a `destacarLinha` antiga juntava os dois pedaços de uma palavra cortada); (2) segurar o dedo ~meio segundo no modo normal deixava a palavra **muda** e escura (o toque longo armava mesmo sem o destaque por linha). E 🟡: segundo destaque quase invisível no tema Noite; nomes estrangeiros cortados errado. **Todos corrigidos** (18.1).
- **Conferente, rodada 8:** ✅ 0 🔴 · 0 🟠 · 0 🟡 · 6 🟢 (pequenos, em `ALTERACOES_FUTURAS_curiosidades.md`).
- **Revisor-chefe:** ✅ "pode publicar" — 0 🔴 · 0 🟠 no app; 🟠 só no kit/documentos (corrigidos); 🟡 no app (segurar >3 s, emoji, hífens, laticínios) **corrigidos** e testados de novo (suíte inteira). Detalhes em `RELATORIO_CHECAGEM_curiosidades_v2.3.md`.
