# 🦉 Coruja Explica — Histórico e plano completo

**Passagem feita em 14/10/2026** (fechamento da conversa antiga, para continuar numa conversa nova).
**Regra desta passagem:** nada no aplicativo foi alterado. Este documento descreve **exatamente** o que existe na v3.1.

**Como ler as marcas deste documento:**
- **[certeza]**: está nos arquivos (código, zip, testes rodados). Foi conferido.
- **[lembrança]**: vem da conversa ou da memória, sem prova nos arquivos. Pode ter detalhe errado.
- **"não sei"**: não há como saber pelos arquivos nem pela conversa.

A conversa antiga foi resumida automaticamente algumas vezes. Por isso os pedidos das versões **v1.0 a v1.9** não estão mais na conversa. **O que mudou** nessas versões foi reconstruído comparando os zips entregues (arquivo `documentos/CHANGELOG_POR_VERSAO_v1.3-v3.1.md`). As versões v1.0 a v1.2 não existem mais em lugar nenhum.

---

## 1. Identificação

| Item | Valor |
|---|---|
| Nome | **Coruja Explica** 🦉 (Escola São Pedro) |
| Endereço | **https://escolasaopedrocorujaexplica.netlify.app** |
| ID na nuvem (`APP_NUVEM`) | **`corujaexplica`** |
| Versão atual | **3.1** (rodapé das Configurações: "Coruja Explica · versão 3.1") |
| Cache do `sw.js` | **`coruja-explica-v3-1`** |
| Última entrega | **24/09/2026, 17:36** (`coruja-explica-netlify_v3_1.zip`) |
| Publicado? | **Sim, a v3.1 está no ar** [certeza, conferido em 14/10/2026 baixando o site]: `sw.js`, `manifest`, ícones e os 3 compartilhados são idênticos byte a byte ao pacote. O `index.html` publicado é o do pacote **mais uma linha que o próprio Netlify acrescenta no fim** (`<script async src="/.netlify/scripts/hud?…">`, o "HUD" do Netlify). Não é do app; não faz parte do pacote. |

**Arquivos do pacote (`pacote-netlify/`)** [certeza]:

| Arquivo | Bytes | md5 | Observação |
|---|---|---|---|
| `index.html` | 447.863 | `24e3ad15cc7428934443673ea526c159` | o app inteiro |
| `sw.js` | 3.657 | `800cd3bee4f1dcd29c9753d68b9fc494` | service worker, cache `coruja-explica-v3-1` |
| `manifest.webmanifest` | 814 | `f44128db2ff08cfa94922657117daba9` | |
| `icon-192.png` | 7.715 | `987377708b29a789795d458c398b2e5d` | |
| `icon-512.png` | 26.212 | `5f29057e7e47967e9957e83e0ace467c` | |
| `nuvem-sync.js` | 20.277 | `f6736f30a4eb5c2e29af1866e79eafe8` | compartilhado, **versão 3** (`var VERSAO = '3'`) |
| `escola-pwa.js` | 21.976 | `ec31bf4a195ccf6a28f70e4fe3748c5f` | compartilhado, **versão 2** |
| `nuvem-config.js` | 2.043 | `1d5f060a5ae8339921d3d58498807971` | o do Pedro, byte a byte (Firebase `escola-sao-pedro-5ee62`, código da família vazio) |

**Os arquivos que o Pedro anexou nesta passagem** [certeza, md5 conferido]:
- `nuvem-config.js` anexado = **idêntico** ao do pacote (`1d5f060a…`).
- `escola-pwa.js` anexado = **idêntico** ao do pacote (`ec31bf4a…`, versão 2).
- `nuvem-sync.js` anexado = **diferente**: é a versão **4.1** (`f151bb17…`), a nova do cadastro da família. Hoje ela está **publicada só no Alfabetização**; o Curiosidades a usa só no site de teste (conferido em 14/10/2026). **O Coruja Explica ainda usa a versão 3** (`f6736f30…`). Seguindo a regra da passagem, **não foi trocado**; está registrado no capítulo 11. A 4.1 foi guardada só como modelo, em `trabalho/modelo-cadastro-novo/`.
- `escola-familia.js` 1.2 e `sw_alfabetizacao_v123.js`: **não são usados** pelo Coruja Explica hoje. Guardados em `trabalho/modelo-cadastro-novo/` para a próxima etapa.

---

## 2. Para quem e para quê

- **Para quem:** as filhas do Pedro (veja o capítulo 13). Na prática, quem usa mais é a **Hinata (6 anos)**, que já lê bem e está aprendendo **interpretação de texto** e os **sinais da escrita** (travessão, aspas, parênteses, reticências, dois-pontos, acentos, parágrafo) [lembrança, memória do Projeto].
- **O que é:** um app para **ler junto**. O pai pede a uma IA um texto sobre um assunto (o app copia o pedido pronto), cola a resposta, o app **arruma** o texto ("Formato Coruja") e guarda na **biblioteca da criança**. Depois pai e filha leem juntos numa **tela de leitura imersiva**, quase sempre com o celular **espelhado na TV**, as crianças a uns 3 metros.
- **Na leitura:** tocar numa palavra **pinta a linha** (marca-texto). Palavras difíceis vêm **sublinhadas com pontinhos** e abrem o **dicionário** (a explicação da IA). No fim há o **quiz de interpretação** (3 perguntas na "Leitura do dia"). O texto lido vai para **"Textos lidos"**, que guarda o histórico: quando leu, quantas vezes abriu e o melhor resultado do quiz.
- **Como a leitura é usada** [certeza: pedido escrito da v2.0]:
  1. a criança lê;
  2. relê partes, se precisar;
  3. explica com as próprias palavras;
  4. o objetivo é compreender e lembrar, não "terminar";
  5. nos dias seguintes, conversar de novo sobre o assunto.

  Tempo máximo ideal: **~20 minutos**.
- **Do que a criança gostou** [certeza: pedido escrito da v2.0]:
  - os **marcadores com palavras em destaque** (ex.: ACRUX, MIMOSA, GACRUX), "manter e, se possível, valorizar";
  - os **diálogos entre pai e filha**, que também servem para o pai explicar as regras de pontuação do diálogo;
  - as **perguntas de interpretação com a explicação da resposta**.

  [lembrança, outra conversa] A Hinata gostou do quiz.
- **A Hana também usa:** "Camila e o cavalo" era "[um texto] que minha filha menor [lê]" [certeza: pedido da v3.1]. Por isso o Formatar aprendeu a lidar com texto de cartilha (uma frase por linha).
- **Filosofia** [lembrança]: o esforço vale mais que o talento ("Esforço Vence"). Nada de pontuação que humilhe; o quiz explica com carinho ("Quase! Olha só 👀"). A prioridade da leitura é **compreensão → retenção → reconto → quantidade** (escrito no próprio pedido da "Leitura do dia" [certeza]). O texto deve ter **diálogo** e os **sinais gráficos** para o pai explicar cada sinal durante a leitura.

---

## 3. Linha do tempo, versão por versão

> O detalhe completo, versão por versão (funções, textos dos botões, tamanho dos pedidos à IA), está em **`documentos/CHANGELOG_POR_VERSAO_v1.3-v3.1.md`** [certeza: feito comparando os zips entregues]. Aqui fica o resumo, com o pedido do Pedro quando ele ainda é conhecido e o **porquê** de cada mudança: [certeza] quando está escrito no código ou num pedido guardado; [lembrança]; ou "não sei".
>
> **Pedidos escritos guardados** (em `documentos/historico/`): o texto de exemplo da IA de 18/09 (`ANEXO_18-09_texto-exemplo-com-PARA-O-PAI.txt`), o texto de teste do Cruzeiro do Sul de 21/09 (`ANEXO_21-09_texto-teste-cruzeiro.txt`), o **pedido da v2.0** (`PEDIDO_v2.0_23-09.txt`), o **pedido da v3.0** (`PEDIDO_v3.0_Prompt.txt`) e as **capturas de tela** que o Pedro mandou (`capturas-do-pedro/`). Os pedidos da v2.1 e da v3.1 foram escritos direto na conversa; o da v3.1 está copiado abaixo; o da v2.1 é lembrança.

### v1.0 a v1.2 (18/09/2026, antes das 20h)
- **Pedido:** não sei. **Feito:** não sei (os arquivos não existem mais). [lembrança, memória do Projeto] O app nasceu reaproveitando o pop-up "Ler Mais" do Curiosidades do Mundo, com 3 partes: Estúdio, Biblioteca e Leitura.
- **Por quê** [lembrança, memória do Projeto]: ler com a filha qualquer texto pesquisado ou gerado por IA, com os sinais gráficos da escrita para o pai explicar.

### v1.3 (18/09, 20:12): a primeira versão disponível
- **Pedido:** não sei.
- **Feito** [certeza]:
  - **Início:** PREPARAR / LER.
  - **Estúdio:** campo Título, Colar, Limpar, Formatar, ↩️ Desfazer, LER AGORA, SALVAR.
  - **Biblioteca:** backup, que **substituía** tudo.
  - **Leitura:** deitada, com A−/A+/Aa/voz, marca-texto e dicionário.
  - Formato Coruja e botão 🤖 PROMPT.
- **Por quê:** não sei.
- **Desfeito depois:**
  - o backup que substituía virou "juntar" na v3.0, porque com a nuvem o que fosse substituído voltaria [certeza, comentário do código];
  - o Desfazer saiu na v1.7 (por quê: não sei) e voltou dentro do Formatar na v3.1.

### v1.4 (18/09, 20:48)
- **Pedido:** não sei.
- **Feito:** recuo de 1ª linha; página "rede primeiro" no `sw.js`.
- **Por quê** [certeza, comentário do `sw.js`]: com "cache primeiro", uma atualização ficava "presa" mostrando a versão antiga.
- **Desfeito:** o espaço maior entre os cartões não funcionava. Foi corrigido na v1.6 [certeza, comentário do código].

### v1.5 (18/09, 21:07)
- **Pedido:** não sei.
- **Feito:** setinha ▾ com 4 pedidos (gerar, adaptar, continuar, consertar).
- **Por quê:** não sei. Os pedidos já existiam no código e não havia botão para usá-los [certeza].

### v1.6 (19/09, 00:49)
- **Pedido:** não sei. Provável [lembrança fraca]: o texto de exemplo da IA de 18/09, 23:03 (`ANEXO_18-09_…`), que tinha um bloco "PARA O PAI".
- **Feito:**
  - título lido do próprio texto (✏️ para trocar);
  - colar já formata sozinho;
  - avisos quando o navegador não deixa colar;
  - pedido à IA mais caprichado (gancho, comparações, dicionário de 5 a 10 palavras com explicação em 3 partes).
- **Por quê:**
  - [certeza, comentário do código] o emoji do título aparecia sem cor;
  - [certeza, comentário do código] o "colar sozinho" só funciona em https com permissão, daí o plano B de segurar o dedo;
  - o resto: não sei.

### v1.7 (19/09, 08:33)
- **Pedido:** não sei.
- **Feito:**
  - **quiz** no fim da leitura (PERGUNTAS:);
  - **busca** na biblioteca (TAGS:);
  - voltar do Android fecha uma camada por vez;
  - o tamanho do texto passa a ser decidido pelo assunto;
  - ↩️ Desfazer removido.
- **Por quê:**
  - [certeza, comentário do código] antes o voltar fechava a leitura e levava o quiz junto;
  - o resto: não sei.

### v1.8 (19/09, 08:51)
- **Pedido:** não sei.
- **Feito:** "conferência final" no fim de todos os pedidos à IA.
- **Por quê:** não sei.

### v1.9 (19/09, 09:16)
- **Pedido:** não sei.
- **Feito:** o pedido "gerar" virou dois: **📖 Leitura do dia** (650–950 palavras, no PROMPT) e **🧠 Entender de verdade** (sem limite).
- **Por quê:** não sei.
- **Desfeito:** 650–950 caiu para 300–500 na v2.0, porque não dava tempo de ler (ver v2.0).

### v2.0 (23/09, 08:37)
- **Pedido** [certeza: pedido escrito de 23/09, 06:52, `PEDIDO_v2.0_23-09.txt`]:
  - manter Bastão e Sassoon, **sem** fonte "redonda" nova;
  - perguntas sobre o silabador ("funciona com qualquer texto da IA?", chave "☐ Ativar separação silábica"), com "**não começar antes de responder**";
  - reduzir a Leitura do dia para "**aproximadamente 300 a 400 palavras**, podendo ficar um pouco abaixo ou acima";
  - prioridade compreensão → retenção → explicar com as próprias palavras → quantidade;
  - "Entender de verdade" mantém o tamanho, "que não seja cansativo";
  - **manter e valorizar** os marcadores (ACRUX, MIMOSA, GACRUX), os diálogos pai e filha e as perguntas com explicação;
  - **revisão tripla obrigatória** (leitura, compreensão e envolvimento, conhecimento);
  - parágrafos de até 4 linhas (5 no máximo).
- **Outros pedidos do mesmo dia** [lembrança]:
  - tamanhos maiores para a TV;
  - tela sempre acesa;
  - não selecionar texto ao tocar;
  - Início com LER grande no centro;
  - cartões com Ler largo e Editar/✅ Lido/Excluir;
  - tela "Textos lidos";
  - lista "• Nome: explicação";
  - correção do ":.".
- **Feito** [certeza]: tudo isso. Silabador desligado de fábrica, só no fim da linha. Leitura do dia com **300 a 500 palavras**.
- **Por quê:**
  - [certeza, comentário do código e pedido escrito] no teste real, um texto de ~830 palavras chegou só na metade (40–50%) em 20 minutos, e 20 minutos é o tempo máximo ideal;
  - **pedido 300–400, feito 300–500:** não sei o motivo exato [lembrança fraca: o próprio pedido diz "podendo ficar um pouco acima"]. Fica registrado para o Pedro decidir se quer apertar para 300–400;
  - [lembrança] as telas maiores e a tela acesa são porque o celular vai espelhado na TV e bloqueava em 1 minuto.
- **Desfeito:** os "níveis" de tamanho viraram px na v3.1, a pedido do Pedro, para ficar igual aos outros apps.

### v2.1 (23/09, 13:42)
- **Pedido** [lembrança, resumo da conversa]:
  - marca-texto dentro do dicionário;
  - margem direita mais reta com o silabador;
  - mais espaço entre Ler e os outros botões;
  - no pedido à IA: diálogo entre **personagens que combinem com o assunto** (pai e filha é só uma possibilidade);
  - parágrafos de 3–4 linhas (5 só se não tiver jeito).
- **Feito:** tudo isso [certeza]. A margem alinhada só funcionava com as sílabas ligadas (teto 0,20 da letra).
- **Por quê:**
  - [lembrança] o Pedro queria ler a explicação do dicionário com a filha, linha por linha;
  - [lembrança] o diálogo sempre "pai e filha" ficava forçado em alguns assuntos;
  - [certeza, comentário do código] sem sílabas, a sobra da linha é uma palavra inteira, e esticar deixaria os espaços desiguais.
- **Desfeito:** a chave "Alinhar" virou parte do modo "Sílabas" na v3.1 (3 modos pedidos pelo Pedro).

### v3.0 (24/09, 13:40)
- **Pedido** [certeza: `PEDIDO_v3.0_Prompt.txt` e os documentos de referência]:
  - padronizar com os outros apps: **um usuário por criança** com histórico completo;
  - nuvem;
  - tela acesa;
  - convite para instalar;
  - pop-up do código da família que **encolhe com o teclado** (sem `prompt()`);
  - análise de bugs;
  - zip com o `nuvem-config.js` dele sem alteração.
- **Feito** [certeza]:
  - cadastro Nome + Bichinho (até 6);
  - biblioteca e ajustes por criança;
  - passagem dos textos antigos para a 1ª criança;
  - nuvem (`nuvem-sync.js` v3) e `escola-pwa.js` v2;
  - Configurações, Recuperar cadastro e Versões guardadas;
  - histórico do quiz;
  - backup que **junta**.
  
  Correções de um revisor independente:
  - apagar no meio de um envio;
  - memória cheia;
  - lápide × leitura feita depois;
  - dois toques em Recuperar;
  - internet lenta;
  - degrau de segurança no voltar.
- **Por quê:**
  - [certeza, pedido e documentos] os 7 apps precisam do mesmo cadastro e nenhum histórico pode se perder;
  - [lembrança] o celular bloqueava a tela no meio da leitura na TV.

### v3.1 (24/09, 17:36)
- **Pedido** [certeza: o texto exato, com os erros de ditado, está em `documentos/historico/PEDIDO_v3.1_24-09.txt`; abaixo, trechos com o ditado corrigido]:
  - "Quando o silabador estiver desativado, gostaria que houvesse a opção em configurações para aumentar o espaçamento entre as palavras… calcule uma boa média máxima de distância entre as palavras… três configurações: Normal, Sílabador, Tentativa de justificar aumentando espaços";
  - "A configuração de tela sempre acesa deve vir marcada por padrão";
  - "O tamanho da fonte… ser por tamanho como tamanho 12 14 16 18 20 24 26 32… [igual o] padrão dos outros aplicativos";
  - "Colei o texto 'Camila e o cavalo', [um texto] que minha filha menor [lê]… cliquei em formatar e não foi feito nenhuma formatação e não foi retornado nenhuma mensagem";
  - "Todos os botões devem ter [toasts] informando sobre o sucesso [ou] fracasso";
  - checagem tripla, de bugs e de design.
  
  No meio do trabalho, ele pediu também:
  - o botão de **recuo de parágrafo**;
  - "em relação ao design, se coloque no lugar da criança e do pai".
- **Feito** [certeza]:
  - estudo com 9.291 linhas, teto de **75% do espaço normal**;
  - tamanhos em px;
  - tela acesa ligada também no modo simples;
  - Formatar reconhece título e frases de cartilha e vira **↩️ Desfazer**;
  - todo botão avisa;
  - recuo com chave e amostra;
  - ajustes em 2 colunas;
  - Colar com texto na caixa **pergunta e troca**.
- **Por quê:**
  - [certeza, diagnóstico registrado] o Formatar "não fazia nada" porque ficava **apagado** depois do formatar automático, e tocar num botão apagado não dá retorno;
  - o texto de cartilha (uma frase por linha) não era agrupado;
  - [certeza, revisor independente] colar duas vezes juntava duas histórias e dizia "sucesso".
- **Desfeito:** nada até hoje.

### Depois da v3.1
- [certeza] Nenhuma mudança no app até hoje (14/10/2026).
- Nesse meio tempo, em **outras conversas**, nasceram o `escola-familia.js` 1.2 e o `nuvem-sync.js` 4.1 (📚 Alfabetização v123, **publicado**).
- **🌍 Curiosidades, duas versões diferentes:**
  - **pelo pedido de passagem** (o `PROMPT_HANDOFF_APPS.md` diz "versão 3 · 07/10/2026"; foi anexado aqui em 14/10): "os outros continuam com o `nuvem-sync.js` de hoje", e o Curiosidades é v1.8 publicada + v1.9 guardada;
  - **pela lembrança da conversa do Curiosidades (até 14/10):** ele já recebeu o cadastro novo (v2.0b, v2.1, v2.2);
  - **conferido em 14/10/2026, a mais nova e certa:** o site **de verdade** do Curiosidades ainda é a **v1.8** (`nuvem-sync.js` **v3**, sem `escola-familia.js`). A versão com o cadastro novo (cache `curiosidades-mundo-v2-0`, `nuvem-sync.js` 4.1) está só no **site de teste** `escolasaopedrocuriosidadestestes.netlify.app`. Ou seja: o cadastro novo do Curiosidades foi feito, mas **ainda não foi publicado**.
- 📕 Historinhas: `nuvem-sync.js` v3 (conferido).
- O próximo da fila do cadastro novo é o **Coruja Explica** (capítulo 12).

---

## 4. Decisões de design e de pedagogia (inclusive as rejeitadas)

**Aceitas** [certeza no código; motivos de lembrança quando marcado]:
1. **Leitura sempre deitada.** O cartão de leitura trava em paisagem. Se o celular não deixar travar (navegador sem tela cheia), o cartão é **girado por CSS** quando a tela está em pé (`@media (max-aspect-ratio:1/1)`). Os pop-ups da leitura (dicionário, quiz, ajustes) giram junto.
2. **Preparar e as listas ficam em pé** (`lockRetrato`): com o teclado aberto é mais fácil editar em pé. O **cadastro não trava** a orientação (o teclado tem que funcionar nas duas).
3. **Letras em MAIÚSCULAS de fábrica** na leitura (Aa alterna). Tamanho padrão **22 px**.
4. **Bastão é a letra padrão.** A antiga "Redonda" caía na Bastão no Android. Sassoon (letra escolar) vem embutida. [Rejeitada: uma terceira letra "redonda" nova; o Pedro preferiu ficar com Bastão e Sassoon, lembrança.]
5. **Silabador desligado de fábrica**, e só no fim da linha (tracinho invisível que o navegador usa quando precisa), com o mesmo silabador do Esforço Vence.
6. **Margem direita em 3 modos** (v3.1): Normal (padrão), Sílabas, Espaços. No modo Espaços, cada espaço cresce **no máximo 75%** do espaço normal. Com 100%, ficariam retas 73% das linhas no celular, contra 64% com 75%: ganho pequeno para espaços já dobrados. A última linha do parágrafo nunca é esticada.
7. **Recuo de parágrafo ligado de fábrica** (v3.1), com chave e amostra nos ajustes.
8. **Marca-texto ligado e voz desligada de fábrica** (mesma regra do Curiosidades).
9. **Sem seleção de texto** ao tocar (some o "Copiar / Pesquisar" do Chrome). As caixas de digitar continuam selecionáveis.
10. **Tamanhos em px** (12 a 64), aviso "🔤 Tamanho 24", como nos outros apps. Os 3 maiores (48/56/64) são para a TV.
11. **Leitura do dia: 300 a 500 palavras** (antes 650–950: não dava tempo). Prioridade compreensão → retenção → reconto → quantidade. Revisão tripla obrigatória no pedido. Diálogo **sempre**, com personagens do assunto. Parágrafos de 3–4 linhas.
12. **Backup junta, nunca substitui** (v3.0): com a nuvem, o que fosse "substituído" voltaria na próxima sincronização.
13. **Nada de `alert`/`confirm`/`prompt` do navegador.** Tudo em pop-ups do app (`abrirConfirm`, `pedirCodigoModal`).
14. **Todo botão dá retorno** (v3.1): nenhum botão fica apagado sem explicação; cada ação mostra um aviso (toast).
15. **"Degrau de segurança" no voltar** (v3.0): a 1ª tela entra duas vezes no histórico; o voltar fecha primeiro um pop-up e, sem pop-up, avisa "Para sair do app, toque em voltar de novo" (a criança não sai sem querer).

**Rejeitadas ou desfeitas:**
- ↩️ Desfazer como botão separado (saiu na v1.7; voltou na v3.1 **dentro** do botão Formatar).
- Leitura do dia com 650–950 palavras (v1.9) → 300–500 (v2.0).
- Diálogo sempre "entre a filha e o pai" (v2.0) → personagens do assunto (v2.1).
- "Alinhar margem" como chave separada (v2.1) → modo "Sílabas" (v3.1).
- Tamanhos com nomes ("Média", "TV máxima", nível n de 10) → px (v3.1).
- Juntar dois textos ao colar com a caixa cheia → perguntar e trocar (v3.1).
- 9 letras na lista → 2 (v2.0). As outras 4 letras **continuam embutidas** no arquivo, sem uso (capítulo 11).
- Temas de cor: a lista de 8 temas existe desde a v1.3, mas **nunca teve tela de escolha**; sempre "Céu".

---

## 5. Como o app é por dentro

### 5.1 Estrutura do `index.html` (5.367 linhas, 447.863 bytes) [certeza]
- Linhas 1–18: `<head>`, meta, manifest, ícones e os 3 scripts compartilhados: `nuvem-config.js` (marca `window.__nuvemCfgArq` = `ok` ou `falta`), `nuvem-sync.js`, `escola-pwa.js`.
- Linhas ~20–724: CSS.
- **Linhas 725–729: 5 letras embutidas em base64** (HanaSassoon, HanaBeaba, HanaMamae, HanaPlaywrite, HanaNarrow; linhas de 13 mil a 105 mil caracteres). **Só a HanaSassoon é usada.**
- Linhas 732–1101: HTML das telas e pop-ups.
- Linha 1104: `GLOSSARIO` (dicionário embutido, **113 palavras**, igual desde a v1.3).
- Linhas ~1126–2800: **`CorujaLogic`** (lógica pura, testável no Node): limpeza, divisor de frases, parágrafos, Formato Coruja, avisos, silabador, **pedidos à IA (`montarPrompt`)**, juntar bibliotecas da nuvem, título e frases soltas.
- Linhas ~2801–5367: a parte da tela: estado, crianças e armazenamento, navegação, Estúdio, Biblioteca, backup, leitura, marca-texto, margem, quiz, ajustes, tela acesa, cadastro, Configurações, nuvem, início (`iniciarApp`).

### 5.2 Telas e pop-ups (ids) [certeza]

| id | O que é |
|---|---|
| `telaInicio` | Início: chip da criança (`userChip`), ⚙️ (`cfgGearHome`) com a bolinha da nuvem (`nuvemPonto`), coruja, "Coruja Explica", "Prepare um texto e leia junto.", botão grande **📖 LER** (`inicioContagem`: "nenhum texto para ler" / "N textos para ler"), **📝 Preparar texto** e **📦 Textos lidos** |
| `telaEstudio` | 📝 Preparar texto: `caixaTexto`, `contadorInfo`, `avisoInfo`, linha "Título:" (`linhaTitulo`, `tituloDetectado`, ✏️ → `linhaTituloManual`/`inpTitulo`/OK), **📋 Colar** (`btnColar`), **🧹 Limpar** (`btnLimpar`), **🪄 Formatar / ↩️ Desfazer** (`btnFormatar`), **📖 LER AGORA**, **💾 SALVAR / 💾 ATUALIZAR** (`btnSalvar`); topo **🤖 PROMPT** e **▾** |
| `telaBiblioteca` | "📚 Textos de <nome>" (`marcaBiblioteca`), **+ Novo**, busca (`buscaTexto`, aparece com textos), `listaBiblioteca`, link "📦 Textos lidos (N)" (`linkArquivo`), rodapé ⬇️ Exportar backup / ⬆️ Importar backup (`backupFileInput`) |
| `telaArquivo` | "📦 Textos lidos": busca (`buscaArquivo`), `listaArquivo` |
| `telaUsuarios` | "🦉 Quem vai estudar hoje?" |
| `telaCadastro` | cadastro / trocar nome ou bichinho |
| `telaNuvem` | "☁️ Recuperar cadastro" e "🕘 Versões guardadas" |
| `telaConfig` | "⚙️ Configurações" |
| `detOv` / `detCard` | leitura: `detEmoji`, `detTit`, **A−** (`btnFontMenos`), **A+** (`btnFontMais`), **Aa**, **⚙️** (`btnAjustes`), **🔇/🔊** (`btnMute`), **❌**; `detTexto`; aviso grande `detAviso` |
| `ajustesOv` | "⚙️ Ajustes da leitura": Margem direita (Normal/Sílabas/Espaços, `opcoesMargem`, `subMargem`), Recuo (`chaveRecuo`, `amostraRecuo`), Tipo de letra (`opcoesFonte`), **Pronto 👍** |
| `quizOv` | quiz: "Pergunta X de N", alternativas, "Isso mesmo! 🎉" / "Quase! Olha só 👀", explicação, "Próxima pergunta" / "Ver o resultado"; fim 🏆/🌟/📖 + **Fechar** |
| `glossOv` | dicionário: 📖, palavra, explicação, **Entendi! 👍** |
| `promptOv` | "Qual pedido você quer copiar?": 📖 Leitura do dia, 🧠 Entender de verdade, 🔄 Adaptar um texto pronto, ➡️ Continuar o mesmo assunto, 🛠️ Consertar formato; passo extra com campo, **📋 Copiar pedido**, **← Voltar às opções** |
| `codOv` | pop-up do código da família |
| `confirmOv` | confirmação do app (**Cancelar** / **Confirmar**, ou só **Entendi 👍**) |
| `toast` | aviso curto embaixo (2,2 a 6 segundos, conforme o tamanho) |

**Cartões da biblioteca:** título (toque abre), resumo, linha "✅ Lido em dd/mm/aaaa · aberto N vezes · 🎯 melhor: X de Y", **📖 Ler** (largo) e embaixo **✏️ Editar**, **✅ Lido**, **🗑️ Excluir**. Em "Textos lidos": **↩️ Ler de novo** e **🗑️ Excluir**. Texto antigo que subiu cortado (`semTexto`): "📦 Texto guardado só no backup…".

### 5.3 Funções principais [certeza]
- **Texto:** `limparBruto`, `removerEnfeitesIA`, `dividirSentencas`, `processarBloco`, `limparEDividirEmParagrafos`, `arrumarParaCaixa` (Formatar), `separarTituloSolto`, `juntarFrasesSoltas`, `parseFormatoCoruja`, `parsePerguntas`, `interpretarTexto`, `contarPalavras`.
- **Silabador:** `silabasDe`, `hifenizarPalavra`, `hifenizarTexto`.
- **Pedidos à IA:** `montarPrompt(tipo, dados)` com tipos `leitura`, `entender`, `adaptar`, `continuar`, `consertar`.
- **Estúdio:** `colarTexto`, `aplicarTextoColado`, `clicarFormatar`, `formatarNaCaixa`, `desfazerFormatacao`, `limparCaixa`, `lerAgora`, `salvarNaBiblioteca`, `salvarRascunho`.
- **Biblioteca:** `renderizaBiblioteca`, `renderizaArquivo`, `montaCard`, `arquivarTexto`, `devolverTexto`, `confirmarExclusao`, `registrarLeitura`, `registrarQuiz`, `exportarBackup`, `importarBackup`.
- **Leitura:** `abrirLeitura`, `renderizaConteudoLeitura`, `fecharDet`, `destacarLinha` (marca-texto), `mapaLocal` (geometria com o cartão girado), `ajustaMargemDireita`, `mudaFontSize`, `toggleCase`, `toggleVoz`, `abrirAjustes`, `escolherModoMargem`, `alternarRecuo`, `escolherFonte`, `abrirQuiz`, `quizAvancar`.
- **Crianças e nuvem:** capítulo 6.
- **Navegação:** `mostrarTela(nome, push)`, `popstate`, `iniciarApp`.

### 5.4 Conteúdo e dados [certeza]
- Dicionário embutido `GLOSSARIO`: **113 palavras**. As **PALAVRAS NOVAS** de cada texto têm preferência sobre ele.
- Pedidos à IA (palavras do texto copiado): Leitura do dia **2.753**, Entender de verdade **2.671**, Adaptar **1.006** (sem o texto colado), Continuar **604** (sem a pergunta), Consertar **212**. Idênticos desde a v2.1. Texto completo, gerado do código da v3.1, em `documentos/PROMPTS_IA_v3.1.md` (lá Adaptar e Continuar aparecem com um trecho de exemplo entre colchetes, por isso contam 1.015 e 612).
- Tamanhos de letra (`FSIZES`): **12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 36, 40, 48, 56, 64**; padrão 22 (`TAMANHO_PADRAO_IDX = 5`). Até a v3.0 era guardado como nível de `[16,19,22,26,30,34,40,48,56,64]` (`FSIZES_ANTIGOS`), convertido sozinho.
- Margem: `AJUSTE_MAX_EM = 0.20` (Sílabas), `ESPACO_MAX_FATOR = 0.75` (Espaços).
- Nuvem: `LIMITE_NUVEM_BYTES = 850000` por criança; até **6 crianças** (`MAX_USERS`); quiz guarda as **30 tentativas** mais novas.

### 5.5 Orientação da tela [certeza]
- Leitura: `lockPaisagem()` + cartão girado por CSS se a tela estiver em pé.
- Início, Preparar, Textos lidos, "Quem vai estudar hoje?": `lockRetrato()`.
- Cadastro: destrava (`screen.orientation.unlock`).
- Ao voltar para o app ou entrar em tela cheia, `travarOrientacaoDaTela()` trava de novo conforme a tela aberta.
- A trava só funciona em **tela cheia**; o `escola-pwa.js` pede tela cheia a cada toque (menos em campos de digitar).

### 5.6 Service worker e manifest [certeza]
- `sw.js`: guarda `./`, `./index.html`, manifest, 2 ícones, `nuvem-sync.js`, `escola-pwa.js` (e tenta `nuvem-config.js`). **Nunca** mexe em pedidos de outro endereço (Firebase). `nuvem-config.js` é **rede primeiro**, com espera de **2,5 s**. A página principal é **rede primeiro**, com espera de **4 s**; depois disso abre a cópia guardada e atualiza por trás. O resto é **cache primeiro**. Ao ativar, apaga os caches antigos.
- `manifest.webmanifest`: `name`/`short_name` "Coruja Explica", `id` e `start_url` "./", `display` fullscreen (+ `display_override` fullscreen → standalone → minimal-ui), `orientation` any, cores `#f6f1e6` / `#f0a030`, `lang` pt-BR, ícones 192 (any), 512 (any) e 512 (maskable).

### 5.7 TODAS as chaves do `localStorage` [certeza: procuradas no `index.html`, no `nuvem-sync.js` v3 e no `escola-pwa.js` v2]

| Chave | Quem grava | O que guarda |
|---|---|---|
| `explica_usuarios` | app | `{ us: [{id, nome, av}], atual: id }`: lista de crianças e a criança atual |
| `explica_<id>_textos` | app | biblioteca da criança (lista de textos, ver abaixo) |
| `explica_<id>_excluidos` | app | "lápides": `{ idDoTexto: dataISO }` dos textos apagados (para a nuvem não trazer de volta) |
| `explica_<id>_config` | app | `{ fsize (px), capsMode, fontIdx, modoMargem ('normal'/'silabas'/'espacos'), recuo }`. Lê também os formatos antigos `fsizeIdx` e `silabasOn`; o `alinharOn` antigo é **ignorado** (cap. 11, item 9) |
| `explica_rascunho` | app | rascunho do Preparar (do **aparelho**, não da criança): `{ titulo, texto, editando (id do texto em edição ou null), crianca }` |
| `explica_telaAcesa` | `escola-pwa.js` (e o modo simples do app) | `'1'` ligado / `'0'` desligado; sem a chave = ligado |
| `explica_textos` | versões até 2.1 | biblioteca antiga sem criança; **é lida** e passa para a 1ª criança (depois é apagada) |
| `explica_config` | versões até 2.1 | ajustes antigos; **é lida** e passa para a 1ª criança (depois é apagada) |
| `explica_textos_antes_v3` | app (migração) | cópia de segurança da biblioteca antiga. É apagada sozinha **só** se faltar espaço |
| `explica_config_antes_v3` | app (migração) | cópia de segurança dos ajustes antigos |
| `escola_instalado` | `escola-pwa.js` | `'1'` quando o app foi instalado |
| `escola_conviteVisto` | `escola-pwa.js` | hora do último "Agora não" do convite (não mostra de novo por 10 minutos) |
| `nuvem_familia` | `nuvem-sync.js` | código da família digitado (normalizado) |
| `nuvem_dispositivo` | `nuvem-sync.js` | identidade deste celular (`d…`) |
| `nuvem_auth` | `nuvem-sync.js` | login anônimo do Firebase (token) |
| `nuvem_corujaexplica_pendentes` | `nuvem-sync.js` | fila: `{ idDaCriança: hora }` esperando subir |
| `nuvem_corujaexplica_meta` | `nuvem-sync.js` | por criança: `enviadoEm`, `chave`, `conferido`, `vistoUpdate` |

**Cada texto** em `explica_<id>_textos`: `{ id: 't…', titulo, texto, criadoEm, alteradoEm, arquivado?, arquivadoEm?, estadoEm?, leituras?, ultimaLeitura?, quiz?: { tentativas:[{em, acertos, total}], melhor, total }, semTexto? }`.

**Outros lugares:** não usa IndexedDB, cookies nem sessionStorage. O service worker usa o **Cache Storage** (`coruja-explica-v3-1`). O backup é um **arquivo** `.json` baixado no celular.

---

## 6. Cadastro, família e nuvem: como está HOJE (v3.1)

> Este é o capítulo mais importante para o próximo passo (cadastro novo da família). Tudo aqui é [certeza], lido no código, salvo quando marcado.

### 6.1 Onde ficam as crianças
- **Lista e criança atual:** `explica_usuarios` = `{ us: [{ id, nome, av }], atual }`.
- **Tipo de id:** `'p' + Date.now() + Math.floor(Math.random()*1000)`: a letra `p`, a hora em milissegundos e um número de 0 a 999 **com 1 a 3 algarismos** (ex.: `p1790265835872200` ou `p17902658358725`). A nuvem reconhece qualquer `p` seguido de algarismos (`/^explica_(p\d+)_/`). **Não** é o nome. Não há id legado `1` (antes da v3.0 não existiam crianças).
- **Nome:** até 14 letras (`maxlength`), espaços limpos e juntados. **Bichinho (`av`):** um dos 8 oficiais (🦉 Coruja, 🦊 Raposa, 🐰 Coelho, 🐼 Panda, 🦋 Borboleta, 🐨 Coala, 🐯 Tigre, 🐴 Pônei), vindos de `EscolaPWA.BICHINHOS`, com cópia idêntica de reserva no app (`BICHINHOS_OFICIAIS`). Bichinho antigo fora da lista continua funcionando; ao editar, pede um dos 8.
- **Máximo:** 6 crianças (`MAX_USERS`).

### 6.2 Como o progresso de cada criança é separado
- **Prefixo:** `explica_<id>_`. São 3 chaves por criança: `textos`, `excluidos` e `config` (lista `DADOS_NUVEM`).
- **Não é por criança:** `explica_rascunho` (do aparelho), `explica_telaAcesa`, `escola_*`, `nuvem_*`.
- **Isolamento:** não há uma "lista de chaves da leitora" como no Alfabetização. Tudo passa por `chaveDe(id, dado)` e pelas funções `textosDe`, `salvarTextosDe`, `excluidosDe`, `carregarConfig`/`salvarConfig` (sempre da `U.atual`).
- **Migração da v2.x** (`migrarBibliotecaAntiga`): ao cadastrar a **primeira** criança (ou ao abrir com crianças e ainda existir `explica_textos`), a biblioteca e os ajustes antigos passam para ela (junta, não substitui). A cópia fica em `explica_*_antes_v3`. Se não couber na memória, **não mexe em nada** e tenta de novo depois.

### 6.3 O que acontece ao abrir
- **0 crianças:** tela de **cadastro** (sem "← Voltar").
- **1 criança:** **Início** direto, já nela.
- **2 ou mais:** **"Quem vai estudar hoje?"**.
- **Degrau de segurança:** a 1ª tela entra duas vezes no histórico do navegador. No voltar: fecha pop-up aberto; sem pop-up, avisa **"Para sair do app, toque em voltar de novo"**.

### 6.4 Telas, com os textos exatos

**Cadastro (`telaCadastro`)**, nesta ordem:
- título **"🌟 Qual é o seu nome?"** (`nuTitulo`);
- campo com placeholder **"Digite o seu nome..."** (`nuNome`);
- **"Escolha o seu bichinho:"**;
- 8 bichinhos numa linha (`nuEmojis`), **nenhum já escolhido**;
- **"Você escolheu: 🦋 Borboleta"** (`nuEscolhido`);
- botões **"← Voltar"** (`nuVoltar`, escondido se não há criança), **"Pronto! ✅"** (`nuPronto`), **"☁️ Já tenho cadastro"** (`nuNuvem`, só com a nuvem configurada).

Regras e avisos:
- sem nome: "Escreva o seu nome primeiro 🙂";
- sem bichinho: "Escolha o seu bichinho 🙂";
- Enter sem bichinho: "Agora escolha o seu bichinho 🙂";
- **mesmo nome + bichinho** já no celular (sem diferença de maiúscula ou acento): não cria repetida, abre a que existe ("🦋 Renata já está neste celular — abrindo!");
- **mesmo nome com outro bichinho** é outra criança;
- 7ª criança: "Já são 6 crianças — o máximo.";
- sucesso: "🦋 Bem-vindo, Ana!".

**Trocar nome ou bichinho** (mesma tela):
- título **"✏️ Trocar nome ou bichinho"**, com o nome já preenchido;
- bichinho antigo fora dos 8: "O bichinho X mudou: escolha um dos 8 novos 🙂";
- trocar para a identidade de **outra** criança do celular é bloqueado: "🐯 Ana já existe neste celular. Escolha outro nome ou bichinho.";
- sucesso: "🐰 Agora é Renatinha (Coelho)". **Os textos vão junto** (o id não muda).

**Quem vai estudar hoje? (`telaUsuarios`)**:
- título **"🦉 Quem vai estudar hoje?"**;
- aviso "Cada criança tem os próprios textos e o próprio histórico. Toque no seu nome e no seu bichinho para começar.";
- um cartão por criança (bichinho, nome, "N textos lidos · N para ler", marca **"lendo agora"** na atual);
- cartão **"➕ Novo usuário"** ("cadastrar outra criança"), que some com 6 crianças;
- botões **"✏️ Trocar nome ou bichinho"**, **"🗑️ Apagar este usuário"**, **"☁️ Recuperar da nuvem"** (só com a nuvem configurada). Os botões valem para a criança **atual** (a "lendo agora");
- tocar no cartão: "🦊 Agora é a vez de Ana!" e vai para o Início.

**Apagar (`apagarUser`)**:
- pop-up do app: **"Apagar 🦊 Ana deste celular, com todos os textos e o histórico? Não tem como desfazer aqui (o que já subiu para a nuvem continua lá)."** [Cancelar] [Confirmar];
- se é a **única** criança: "É preciso ter ao menos uma criança." (**não pode apagar a última**);
- depois: "Criança apagada deste celular." e volta para "Quem vai estudar hoje?".

**Recuperar da nuvem (`telaNuvem`)**:
- título **"☁️ Recuperar cadastro"**, botão 🏠 (volta: 0 crianças → cadastro; 1 → Início; 2+ → "Quem vai estudar hoje?");
- mensagens (`nuvemMsg`):
  - "A nuvem ainda não foi configurada neste aplicativo (veja o guia do Firebase).";
  - "Primeiro digite o código da família (botão 🔑 abaixo).";
  - "📴 Sem internet agora. Conecte no Wi-Fi e toque em "Procurar de novo".";
  - "⏳ Procurando as crianças guardadas na nuvem...";
  - "Ainda não tem nenhuma criança guardada na nuvem com este código da família.";
  - "Toque na criança para trazer os textos e o histórico dela para este celular. Nada que já está aqui é apagado.";
- cartões: "Ana · Raposa" com "já está neste celular — toque para juntar" / "tem textos neste app" / "veio de outro app";
- botões **"🔑 Código da família"**, **"🔄 Procurar de novo"**, **"🕘 Versões guardadas"**;
- ao tocar: "☁️ Buscando os textos de Ana...", e depois "✅ 🦊 Textos de Ana recuperados!" ou "🦊 Ana pronto! (ainda sem textos neste app)". Dois toques seguidos não criam criança repetida.
- tocar numa criança que **já está no celular** junta a nuvem nela **e a torna a criança atual** [certeza: `nuvemRecuperarLeitor`];
- num celular **sem nenhuma criança**, a primeira criança recuperada também recebe a biblioteca antiga da v2.x, se ainda existir (`migrarBibliotecaAntiga`) [certeza].

**Versões guardadas** (na mesma tela):
- o botão **"🕘 Versões guardadas"** some quando não há criança atual (celular sem crianças);
- mensagens: "Primeiro escolha ou recupere uma criança."; "A nuvem ainda não está pronta (configuração ou código da família)."; "📴 Sem internet agora."; "Ainda não tem versões guardadas de Ana (a primeira aparece depois do primeiro envio)."; erro: "❌ …" (ou "Não foi possível falar com a nuvem.");
- "⏳ Procurando as versões guardadas de Ana...";
- "🕘 Versões de 🦊 Ana (uma por dia). Tocar numa versão JUNTA ela com o que está aqui — nada é apagado.";
- cartões 🗓️ dd/mm/aaaa "N texto(s) · N lido(s)";
- pop-up "Juntar a versão de dd/mm/aaaa com os textos atuais de Ana? Nada é apagado: só volta o que estiver faltando." → "✅ Versão de dd/mm juntada!".

**Pop-up do código da família (`codOv`)**:
- título **"🔑 Código da família"**;
- texto "É o mesmo código em todos os aplicativos e em todos os celulares da família. Pelo menos 6 letras ou números, sem espaço.";
- campo com placeholder "ex.: saopedro2026";
- botões **"Cancelar"** e **"🔑 Guardar código"**;
- código curto: erro **dentro** do pop-up, "O código precisa ter pelo menos 6 letras ou números 🙂";
- sucesso: "🔑 Código guardado!";
- Enter guarda; o voltar do Android fecha só o pop-up;
- **com o teclado aberto** (tela baixa, `max-height:300px`), a explicação some e ficam o campo e os botões (`max-height:200px`: some também o título);
- se o código estiver escrito no `nuvem-config.js`: "🔑 O código da família já está escrito no arquivo nuvem-config.js. Para trocar, edite aquele arquivo." [Entendi 👍].

**Configurações (`telaConfig`)**, na ordem:
1. **👧 Quem está usando**: criança atual ("Cada criança tem os próprios textos, letra e histórico") e **🔄 Trocar**.
2. **📺 Tela**:
   - **Tela sempre acesa** (chave, ligada de fábrica; situação: "✅ Ligado: com o app aberto, a tela não apaga nem bloqueia (bom para a TV)", modo reserva, recusa etc.);
   - **Instalar o app** (**📲 Instalar**, só no navegador).
3. **☁️ Nuvem (guarda os textos e o histórico na internet)**:
   - **Situação** + **🔄 Enviar agora**;
   - **Código da família** ("Em uso: fam•••" / "Ainda não digitado") + **🔑 Digitar**;
   - **Recuperar crianças** + **☁️ Recuperar**.
4. **💾 Backup (arquivo no celular)**: **⬇️ Exportar** / **⬆️ Importar** (da criança atual).
5. Rodapé "Coruja Explica · versão 3.1".

### 6.5 Onde ficam o chip, a ⚙️ e a bolinha da nuvem
- **Só no Início** (`telaInicio`): o **chip** da criança no canto de cima à esquerda (`userChip`, toque → "Quem vai estudar hoje?") e a **⚙️** no canto direito (`cfgGearHome`), com a **bolinha** (`nuvemPonto`: verde = ok, amarela = esperando, vermelha = erro; sem bolinha = nuvem desligada).
- Nas outras telas (Preparar, Meus textos, Textos lidos, leitura) **não há chip nem ⚙️** (o PLANO pede para levar; capítulo 12).
- **Celular novo, sem código da família digitado:** com o `nuvem-config.js` do Pedro (nuvem configurada, código vazio), o estado é `sem-codigo` e a **bolinha fica vermelha** até alguém digitar o código (Situação: "Falta digitar o código da família (botão 🔑 abaixo)").
- A situação da nuvem aparece por escrito em Configurações → Situação. Sem internet e com coisas na fila: "⚠️ Não limpe os dados do navegador até conectar na internet."

### 6.6 Regras de apagar e o que pode se perder
- **Não pode apagar a última criança.**
- Apagar tira do celular as 3 chaves dela (`textos`, `excluidos`, `config`) e a tira da lista. **A ficha na nuvem não é apagada** (o `nuvem-sync.js` não apaga nada).
- **⚠️ Risco de perda:** o app **não confere** se tudo da criança já está na nuvem antes de apagar. Perde-se para sempre se:
  - **(a)** nunca foi digitado o código da família (nada subiu);
  - **(b)** havia mudanças na fila, sem internet;
  - **(c)** textos lidos antigos subiram **cortados** (só título e histórico) por causa do limite de 850 KB.
  
  O texto do pop-up diz "o que já subiu para a nuvem continua lá", o que é verdade, mas não avisa os casos (a), (b) e (c).
- Apagar **no meio de um envio** não esvazia a ficha da nuvem (correção da v3.0: `nuvemExportar` lança erro para criança que não existe mais).
- **Depois de apagar**, a criança atual passa a ser a **primeira da lista** [certeza: `apagarUser`].
- **Fila que sobra** [rodado pelo revisor-chefe em 14/10]: apagar uma criança deixa o id dela na fila `nuvem_corujaexplica_pendentes` (e em `nuvem_corujaexplica_meta`), porque o `removeItem` das chaves dela passa pela "vigia" do `nuvem-sync.js`. Com o código da família digitado, a próxima sincronização tira esse id da fila (criança que não existe mais). **Sem código da família, fica para sempre** e entra na contagem "N criança(s) …" da Situação. Não perde dados; é só contagem errada (cap. 11).

### 6.7 Ligação com o `nuvem-sync.js` (v3)
- `iniciarNuvem()` chama `NuvemSync.iniciar({ app: 'corujaexplica', usuarios, idDaChave, exportar, mesclar })`:
  - **`usuarios()`**: `U.us` como `{id, nome, av}`.
  - **`idDaChave(k)` = `nuvemIdDaChave`**: chave `explica_(p\d+)_(textos|excluidos|config)` de criança que existe → id; o resto → null. O `nuvem-sync.js` "vigia" todo `localStorage.setItem`/`removeItem` e põe na fila a criança daquela chave.
  - **`exportar(id)` = `nuvemExportar`**: monta `{ textos, excluidos, config }` (cada um em texto JSON) com `CorujaLogic.montarExportacao`. **Limite de 850.000 bytes:** se passar, os **textos já lidos mais antigos** sobem sem o conteúdo (`texto:''`, `semTexto:true`); o histórico sobe inteiro. **Lança erro, e não envia nada,** se a criança não existe mais (apagada no meio do envio) ou se uma junção anterior não coube na memória do celular (`nuvemJuntoNaoGravado`).
  - **`mesclar(id, dados, restaurando)` = `nuvemMesclar`**: junta a nuvem com o celular por `CorujaLogic.mesclarBibliotecas`. **Regra de ouro: nada se perde.** Campo por campo:
    - `alteradoEm`: vale a edição mais nova (título e texto);
    - `estadoEm`: vale quem marcou lido/devolvido por último;
    - `criadoEm`: o mais antigo;
    - `leituras`: o maior;
    - `ultimaLeitura`: a mais nova;
    - `quiz`: junta as tentativas sem repetir (30 mais novas); `melhor` e `total` = o maior;
    - texto que subiu cortado não apaga o texto do celular;
    - **lápides** (`excluidos`) se juntam com a data mais nova. O texto só some se a lápide for **mais nova que a última mexida** (editar, lido, abrir para ler, responder o quiz);
    - **ajustes (`config`):** adota os da nuvem só se `restaurando` ou se o celular não tem ajustes. Criança sem textos no celular conta como `restaurando`;
    - memória cheia: o resultado fica em memória (`nuvemJuntoNaoGravado`) e o envio daquela criança espera (a nuvem nunca recebe menos do que tinha).
- **Chave da criança na nuvem:** `NuvemSync.chaveUsuario(nome, av)` (nome minúsculo, sem acento, com hífen + código do bichinho, ex.: `ana_1f98a`). Caminho: `familias/<código>/usuarios/<chave>/apps/corujaexplica` + `…/versoes/AAAA-MM-DD` (uma cópia por dia).
- **Os 2 documentos que cada envio grava** [certeza: `nuvem-sync.js` v3, `enviarUsuario`]:
  - **ficha do app** `familias/<código>/usuarios/<chave>/apps/corujaexplica`: `nome`, `av`, `app` ("corujaexplica"), `dados` (texto JSON com `textos`, `excluidos` e `config`), `atualizadoEm` (milissegundos), `dispositivo` (id do celular, `nuvem_dispositivo`) e `versao` ("3"); a cópia do dia em `…/versoes/AAAA-MM-DD` tem os mesmos campos;
  - **ficha da criança** `familias/<código>/usuarios/<chave>`: `nome`, `av` e o mapa `apps` (`apps.corujaexplica` = hora do último envio). É ela que a tela "Recuperar" lista, para todos os apps da família.
- **`nuvemTentarRecuperarNovo(id, nome, av)`:** depois de cadastrar uma criança nova, se a nuvem já tem esse nome + bichinho, traz os textos sozinha ("☁️ 🦊 Achei os textos de Ana na nuvem!").
- **`nuvemLevarFichaAntiga(id, nomeAntigo, avAntigo)`:** ao trocar nome ou bichinho, junta a ficha antiga da nuvem na nova (a antiga continua lá; nada é marcado como "mudou para"). **Só acontece se, naquela hora, a nuvem estiver configurada, o código da família digitado e houver internet**; senão, não junta e **nunca tenta de novo** [certeza: lido no código]. Nada se perde no celular (os textos vão junto, o id não muda), mas a ficha antiga fica "órfã" na nuvem, com o nome antigo (cap. 11).
- **`nuvemRecuperarLeitor(item, local)`:** "Recuperar cadastro" (cria a criança no celular, se precisar, e chama `NuvemSync.recuperar`).
- **Código da família:** `NuvemSync.definirFamilia(codigo)` (vale para **todas** as crianças do celular, como na v3).
- **Firebase (o Pedro configura; o app não mexe)** [certeza: `documentos/referencias/PEDIDO_CONVERSA_EXISTENTE.md` e o `GUIA_FIREBASE_PASSO_A_PASSO.md`]:
  - login **Anônimo** ligado;
  - Regras do Firestore: `usuarios`, `apps` e `versoes` com `allow read, create, update: if request.auth != null;`, **sem delete**;
  - sem `versoes` nas regras, o principal continua subindo e o app avisa na Situação ("Histórico de versões não gravou…").
- **Situação na tela:** `atualizaNuvemUI()` (bolinha e textos), `nuvemSincronizarAgora()` ("☁️ Enviando..." → "✅ Tudo guardado na nuvem!" / "📴 Sem internet — fica guardado no celular" / "❌ …").

### 6.8 Passos próprios do cadastro deste app
- Não tem turma, idade nem ano. Só nome + bichinho.
- A **letra, o tamanho, a margem e o recuo** são de cada criança (`explica_<id>_config`). O **rascunho** do Preparar é do aparelho.

### 6.9 Pop-ups do navegador
- **Nenhum** `alert`, `confirm` ou `prompt` no app [certeza: procurado no código; há um teste para isso no `teste-v3.js`]. O único `prompt()` está no `escola-pwa.js` (`ev.prompt()`), que é o **convite oficial de instalação do Chrome**, não um pop-up de texto.

### 6.10 Riscos e defeitos conhecidos nesta parte
1. **Apagar sem conferir a nuvem** (6.6): risco real de perda.
2. **Chip e ⚙️ só no Início**: para trocar de criança no meio é preciso voltar ao Início.
3. **Textos diferentes dos outros apps / do plano novo:** "Novo usuário", "Apagar este usuário", "☁️ Recuperar da nuvem", "☁️ Já tenho cadastro" etc. O `PLANO_CADASTRO_FAMILIA.md` (parte 3-A) define os textos padronizados.
4. **Código da família por celular** (não por criança, como no `nuvem-sync.js` 4.1). Código digitado errado cria uma "família órfã" na nuvem sem aviso (problema geral, citado no plano).
5. **Trocar nome ou bichinho** confere repetição só no celular. Se o novo nome + bichinho já existir na nuvem (outra criança), as duas fichas se juntam. A ficha antiga não ganha "mudou para".
6. **Teclado:** o cadastro e o pop-up do código foram testados com teclado aberto em pé e deitado (12 tamanhos de tela, no Chromium) [certeza nos testes]. No celular de verdade: não sei.
7. **Limite de 850 KB:** textos lidos antigos podem existir na nuvem só com o título. Num celular novo, aparecem como "📦 Texto guardado só no backup…".
8. **Biblioteca gigante de textos NÃO lidos** (pouco provável): o `montarExportacao` só corta os **lidos**. Se mesmo assim passar do limite, a ficha é enviada assim mesmo, e acima de ~1 MB o Firestore recusa. Aí aquela criança **nunca sobe**, e o erro aparece em Configurações → Situação. [certeza: lido no código; não testado com o Firebase real]
9. **Fila que sobra depois de apagar** (6.6): sem código da família, o id da criança apagada fica para sempre na fila e na contagem da Situação.
10. **Trocar nome ou bichinho sem internet ou sem código** (6.7): a ficha antiga da nuvem não é juntada, e o app não tenta de novo; ela fica órfã com o nome antigo.

---

## 7. Regras que não podem ser quebradas
1. **Nunca perder** textos, leituras ou respostas do quiz de nenhuma criança (nem na migração, nem ao juntar com a nuvem, nem no backup).
2. **`nuvem-config.js` vai no zip exatamente como o Pedro mandou** (md5 `1d5f060a5ae8339921d3d58498807971`). Não mexer no Firebase sem ele pedir.
3. **`nuvem-sync.js`, `escola-pwa.js` (e, no futuro, `escola-familia.js`) são compartilhados:** não se editam dentro de um app só. Mudança vale para todos e sobe a versão.
4. **Nada de `alert`/`confirm`/`prompt`** do navegador.
5. **Todo botão dá retorno** (aviso de sucesso ou falha).
6. **Edições cirúrgicas.** Não reescrever o que funciona. Plano e autorização antes de coisa grande.
7. **Fontes de 12 a 24 px** (ou maiores quando necessário). Nada visível abaixo de 12 px (há teste).
8. **A cada entrega, subir o nome do cache** do `sw.js` (`coruja-explica-v3-1` → o próximo).
9. Testes de verdade (Playwright + **Firebase de mentira**), nunca contra o Firebase real.
10. Leitura: maiúsculas e marca-texto de fábrica, voz desligada, sem seleção de texto, tela sempre acesa.

---

## 8. Aprendizados difíceis
1. **Atualização "presa" no PWA:** o `sw.js` usava cache primeiro para a página e o celular continuava na versão velha. Solução (v1.4): página **rede primeiro**. Depois (v3.0), com espera de 4 s, porque em internet lenta a tela ficava branca.
2. **Tela branca em internet lenta (v3.0):** o `nuvem-config.js` é carregado com `<script>` no começo e o `sw.js` esperava a rede sem limite. Solução: espera de 2,5 s, depois a cópia guardada.
3. **Silabador e margem com o cartão girado:** as medidas da tela vinham "deitadas". Solução: `mapaLocal` (converte para a posição dentro do cartão).
4. **"são:." no fim de frases:** `garantirPontoFinal` punha ponto depois de dois-pontos. Corrigido (v2.0).
5. **Esc fechava a leitura mesmo fechada** (chamava `history.back()`). Corrigido (v3.0).
6. **Pop-ups da leitura apertados com o cartão girado:** o `flex` encolhia o cartão. Solução: `flex:0 0 auto` + regras compactas (v3.0).
7. **Nuvem, achados do revisor independente (v3.0):**
   - (a) apagar criança durante um envio subia biblioteca vazia → `exportar` lança erro;
   - (b) memória cheia ao juntar → subia menos do que a nuvem tinha → espera;
   - (c) lápide apagava texto lido depois em outro celular → "última mexida" inclui leitura e quiz;
   - (d) dois toques em Recuperar → criança repetida;
   - (e) backup não devolvia texto apagado (a lápide tirava de novo) → o texto importado ganha data nova.
8. **Formatar "não fazia nada" (v3.1):** o botão ficava **apagado** depois do formatar automático, e tocar num botão apagado não dá retorno. E texto de cartilha (uma frase por linha) não era agrupado. Solução: botão nunca apagado, aviso sempre, ↩️ Desfazer, título e frases soltas.
9. **Colar duas vezes juntava duas histórias** (título duplo, perguntas misturadas) e ainda dizia "sucesso" (v3.1). Solução: pergunta e troca.
10. **Título "roubando" a 1ª frase** (poema, PDF, cartilha em maiúsculas, recado de WhatsApp) (v3.1). Solução: o título precisa de linha em branco depois (exceto MAIÚSCULAS seguido de texto normal).
11. **Medir antes de decidir:** a 1ª medição do espaço entre palavras deu 0,23 da letra por erro de medição (tamanho aplicado sem esperar a tela). A certa é 0,28 (Bastão) / 0,31 (Sassoon). O teto de 75% é relativo ao espaço medido na hora, então funciona com qualquer letra.
12. **Ambiente de trabalho some:** a conversa pode ser reiniciada e perder arquivos. Por isso cada entrega vira zip na hora.

---

## 9. Testes automáticos

**Onde:** `testes/` (Node + Playwright + Chromium). Abrem o app de `../pacote-netlify` num servidor local.

**Firebase:**
- **Só o `teste-v3.js`** liga o **Firebase de mentira** (`_firebase-falso.js`: login anônimo, renovação de login e Firestore REST com `currentDocument.exists` e `updateTime`) e intercepta tudo para `*.googleapis.com`.
- As outras 5 baterias de navegador (`teste-navegador`, `teste-telas`, `teste-adversarial`, `teste-v2`, `teste-v21`) **não interceptam**. Elas carregam o `nuvem-config.js` **verdadeiro** e só não falam com o Firebase real porque o **código da família está vazio** no arquivo e elas não digitam código.
- ⚠️ **Nunca rode os testes com um código escrito no `nuvem-config.js`.** O conferente independente provou que, assim, o `teste-navegador.js` tenta logar no Firebase real.
- As 3 baterias de lógica (`teste-logica`, `teste-nuvem-logica`, `teste-formatar`) não usam navegador.
- Em 14/10/2026, com uma "guarda de rede", **nenhum pedido saiu** durante as 9 baterias.

| Bateria | Verificações | O que confere |
|---|---|---|
| `teste-logica.js` | 272 | limpeza, frases, parágrafos, Formato Coruja, quiz, pedidos à IA, silabador (direto no Node) |
| `teste-nuvem-logica.js` | 37 | juntar bibliotecas (edição, lido, quiz, lápides, texto cortado, ordem), limite de 850 KB |
| `teste-formatar.js` | 27 | Formatar de texto solto: título, frases de cartilha, falsos títulos (poema, PDF, WhatsApp), falas, subtítulos |
| `teste-navegador.js` | 64 | fluxo completo no navegador (colar, Desfazer, salvar, ler, marca-texto, dicionário, voltar do Android, offline) |
| `teste-telas.js` | 96 | layout em 6 tamanhos de tela (em pé e deitado, leitura girada, quiz) |
| `teste-adversarial.js` | 26 | casos difíceis (texto enorme, quiz comprido, entradas estranhas) |
| `teste-v2.js` | 74 | v2.0: tamanhos, sílabas, letras, Textos lidos, tela acesa, sem seleção |
| `teste-v21.js` | 41 | v2.1: marca-texto no dicionário, margem (Sílabas e Espaços), cartão girado |
| `teste-v3.js` | 179 | cadastro, 8 bichinhos em 12 tamanhos com teclado, pop-up do código, nuvem com 2 celulares (A–N), PWA, letras ≥ 12 px, padronização, correções da revisão (8) e v3.1 (9) |
| **Total** | **816** | |

**Como rodar:** `cd testes && sh rodar_todos.sh` (detalhes em `testes/COMO_RODAR.md`). Precisa de Node 18+ e do Playwright com Chromium. Variáveis opcionais: `PLAYWRIGHT_MODULE`, `CHROMIUM_PATH`, `CORUJA_ROOT`, `CORUJA_INDEX`, `CORUJA_OUT`, `CORUJA_ORIGINAIS`, `CORUJA_REF` e `CORUJA_PORT` (vale nas 6 baterias de navegador; padrões: navegador 8951, v2 8961, adversarial e v21 8981, telas 8957, v3 9071).

**Mudança feita nos testes nesta passagem** [certeza]: só os **caminhos**. Antes os testes apontavam para pastas desta conversa (`/home/claude/build`, a pasta temporária e a pasta de anexos). Agora apontam para as pastas do próprio zip, ou para as variáveis acima. **A lógica dos testes não mudou.** Os originais estão iguais na conversa antiga.

**Último resultado:** **14/10/2026, 816/816, 0 falhas** [certeza], rodado de dentro da pasta do zip (`sh rodar_todos.sh`, 3,5 min). Antes: 24/09/2026, o mesmo resultado.

**O que os testes NÃO cobrem:**
- celular de verdade (toque real, teclado real, Wake Lock real, voz real, rotação real);
- Firebase de verdade e dois celulares reais ao mesmo tempo;
- instalação real do PWA pelo Chrome;
- a qualidade dos textos que a IA devolve;
- a TV.

**Atenção:** a verificação "nuvem-sync.js e escola-pwa.js iguais aos publicados no Curiosidades, Alfabetização e Historinhas" (`teste-v3.js`) usa **cópias de 24/09/2026** (`testes/referencias-outros-apps/`). Conferido em 14/10/2026: o **Curiosidades** e o **Historinhas** publicados continuam iguais a essas cópias (`nuvem-sync.js` v3); só o **Alfabetização** publicado mudou para a 4.1. Para ele, a verificação vale só como registro de 24/09.

**Testes antigos guardados (não rodam mais como estão):** `testes/antigos/` (`teste-entrega.js` e `teste-logica-entrega.js` da v1.x, que apontam para uma pasta que não existe mais) e `testes/antigos/regressao-v2.1/` (versões dos testes antes do cadastro). **Nenhum teste foi perdido**; nada foi reescrito.

---

## 10. Como empacotar e publicar
1. Fazer as mudanças em `pacote-netlify/index.html` (e no `sw.js`, se precisar).
2. No `sw.js`, **trocar o nome do cache**: hoje `coruja-explica-v3-1`. **Próximo: `coruja-explica-v3-2`**, ou `coruja-explica-v4-0` se for o cadastro novo da família (sugestão já combinada em outra conversa [lembrança]). Atualizar também o comentário do topo do `sw.js` e o rodapé "Coruja Explica · versão X" das Configurações.
3. Se entrar arquivo novo (ex.: `escola-familia.js`), pôr na lista `FILES` do `sw.js`.
4. `node --check` nos `.js` e nos `<script>` do `index.html`. Rodar `sh testes/rodar_todos.sh` (0 falhas).
5. Zip **só com os arquivos de `pacote-netlify/`, na raiz do zip** (sem pasta por fora): `index.html`, `sw.js`, `manifest.webmanifest`, `icon-192.png`, `icon-512.png`, `nuvem-sync.js`, `escola-pwa.js`, `nuvem-config.js` (o do Pedro, md5 `1d5f060a…`). Abrir o zip e conferir os md5.
6. **Nunca publicar a pasta `testes/`.**
7. Publicar no Netlify (arrastar o zip ou a pasta no site `escolasaopedrocorujaexplica`). Para mudanças grandes, usar antes um **site de teste** (sugestão: `escolasaopedrocorujaexplicatestes` [lembrança]).
8. No celular: abrir pelo ícone, conferir a versão no rodapé das Configurações e a bolinha verde.

---

## 11. Estado atual (14/10/2026)

**Pronto e publicado:** v3.1, com tudo dos capítulos 3 a 6.

**Pendente:**
- **Cadastro novo da família** (`PLANO_CADASTRO_FAMILIA.md` v3), que é a próxima tarefa (capítulo 12).
- Não sei se o Pedro já testou a v3.1 no celular (antes da v3.1 ele disse "Não publiquei ainda e não consegui testar tudo"). O site hoje tem a v3.1.

**Defeitos e riscos conhecidos (não corrigidos, por regra desta passagem):**
1. 🔴 **Apagar criança sem conferir se tudo está na nuvem** (6.6). O cadastro novo resolve com a lixeira e o `garantirGuardado`.
2. 🟠 **`nuvem-sync.js` diferente:** o pacote usa a **v3** (`f6736f30…`); o Pedro anexou a **4.1** (`f151bb17…`). Não foi trocado. A troca vem junto com o cadastro novo.
3. 🟠 **Chip e ⚙️ só no Início** (6.5).
4. 🟡 **4 letras embutidas sem uso** (HanaBeaba, HanaMamae, HanaPlaywrite, HanaNarrow: ~160 mil caracteres) e a lista de 8 temas sem tela (só "Céu" é usado). Peso morto; tirar só com autorização.
5. 🟡 O **backup não leva os ajustes** da criança (letra, tamanho, margem, recuo), só textos e lápides. O importar ignora as lápides do arquivo.
6. 🟡 A cópia `explica_textos_antes_v3` fica para sempre (só sai se faltar espaço).
7. 🟡 Na tela de leitura, o aviso grande (`detAviso`) cobre a 1ª linha por ~1,8 s.
8. 🟡 O aviso (toast) do Preparar aparece por cima de LER AGORA/SALVAR por alguns segundos.
9. 🟡 Quem tinha (v2.x) sílabas ligadas **e** "alinhar" desligado cai no modo "Sílabas", que alinha.
10. 🟡 **Testes sem trava do Firebase:** 5 baterias antigas não interceptam `*.googleapis.com` (cap. 9). Sugestão para a conversa nova, com autorização: acrescentar `ctx.route(/googleapis\.com/, r => r.abort())` nelas.
11. 🟡 Ao abrir, o console mostra o **aviso** "Failed to execute 'requestFullscreen'… user gesture" (tentativa de tela cheia sem toque). É aviso, não erro. Já existe no publicado.
12. 🟡 **Bolinha vermelha** em todo celular novo até digitar o código (6.5). Pode assustar; o cadastro novo deve tratar.
13. 🟡 **Biblioteca gigante de textos não lidos** nunca sobe (6.10, item 8).
14. ℹ️ **Leitura do dia:** o Pedro pediu "aproximadamente 300 a 400 palavras" (v2.0); o app pede **300 a 500**. Fica para o Pedro decidir se aperta.
15. ℹ️ O documento do Projeto `claude/coruja-explica-prompt-continuacao.md` (24/09) foi **substituído** por este histórico e pelo `PROMPT_CONTINUACAO_corujaexplica.md`.
16. ℹ️ O Netlify acrescenta sozinho uma linha `<script … /.netlify/scripts/hud …>` no fim do `index.html` publicado. Não é do app.
17. ℹ️ A memória do Projeto ainda cita o endereço antigo "escolasaopedroexplica"; o certo é **escolasaopedrocorujaexplica**.
18. 🟡 **Fila que sobra depois de apagar uma criança** (6.6): sem código da família, o id dela fica em `nuvem_corujaexplica_pendentes`/`_meta` e na contagem da Situação. O `nuvem-sync.js` 4.1 tem `limparPendencia(id)` para isso (usar no cadastro novo).
19. 🟡 **Trocar nome ou bichinho sem internet ou sem código** (6.7): a ficha antiga não é juntada nem marcada "mudou para", e não há nova tentativa. O cadastro novo (com `marcarMovido` do `nuvem-sync.js` 4.1) deve tratar.

**Pedidos que ficaram para depois:** nenhum pedido do Pedro ficou sem fazer na v3.1 [lembrança].

**Ideias futuras (sugestões, nada combinado):**
- **(a)** "Conte para o papai" no fim do texto (reconto oral);
- **(b)** revisar as palavras do dicionário que a criança já tocou;
- **(c)** resumo da semana para o pai;
- **(d)** tirar as letras sem uso (arquivo menor).

[lembrança, outra conversa] A Hinata gostou do quiz do Coruja Explica.

---

## 12. Plano de desenvolvimento (ordem de prioridade)

1. **Padronizar o cadastro da família e das crianças** (código da família + crianças com nome + bichinho, telas e palavras iguais nos 7 apps), seguindo o **`PLANO_CADASTRO_FAMILIA.md` versão 3** (aprovado, D1 a D18; cópia em `documentos/referencias/`). No plano, o Coruja Explica está na parte "🦉 Coruja Explica v3.1":
   - trocar `telaUsuarios`, `telaCadastro`, `telaNuvem` e `codOv` pelas telas do `escola-familia.js` 1.2;
   - "👧 Quem está usando" sai do topo das Configurações; tudo vai para o fim;
   - **cuidado com o `popstate`** (degrau de segurança): chamar `EscolaFamilia.fecharTopo()` antes;
   - chip e ⚙️ nas outras telas principais;
   - **`completoNaNuvem(id)` = false** quando algum texto subiu cortado (limite de 850 KB). Aí tirar a criança só acontece com a cópia na lixeira;
   - trocar `nuvem-sync.js` v3 → **4.1** e acrescentar `escola-familia.js` 1.2 (cópias mestras, sem mudar; md5 em `trabalho/modelo-cadastro-novo/LEIA-ME_COMPARTILHADOS.md`);
   - **modelos:** Alfabetização v123 (publicado) e Curiosidades v2.x, com o cadastro novo feito mas, em 14/10/2026, **só no site de teste**; o site de verdade do Curiosidades ainda é a v1.8 (cap. 3, "Depois da v3.1");
   - **convivência v3 × 4.1:** enquanto isso, na mesma família da nuvem convivem apps com `nuvem-sync.js` v3 (Coruja Explica, Curiosidades publicado, Historinhas e outros) e 4.1 (Alfabetização). O documento na nuvem é o mesmo (a 4.1 é compatível com a v3);
   - **testes:** pôr a trava do Firebase nas 5 baterias antigas (cap. 11, item 10);
   - **testar a migração com um backup real** das meninas, e **também em pé** (360×740 e 412×915), porque o app é usado em pé fora da leitura;
   - site de teste antes do site de verdade;
   - **a confirmar com o Pedro** [lembrança, outra conversa]: nome do site de teste (`escolasaopedrocorujaexplicatestes`), nome do cache (`coruja-explica-v4-0`) e se a abertura passa a ser sempre "Quem vai estudar hoje?" (D2).
2. Depois, só com autorização: os itens 🟡 do capítulo 11 e as ideias futuras.

---

## 13. Sobre o Pedro e as meninas, e como trabalhar comigo

- **Pedro**, de **Mara Rosa (GO)**. **Não é programador.** O Claude escreve todo o código; ele decide a pedagogia e testa num **celular Android de verdade**, quase sempre **espelhado na TV**, com as meninas a uns 3 m. O celular dele bloqueia a tela em 1 minuto, por isso a "tela sempre acesa" é essencial [lembrança].
- **Hinata, 6 anos:** 1º ano do fundamental, mas lê e faz matemática no nível do **3º ano**. Muito curiosa (astronomia, medicina), faz corrida e natação [lembrança].
- **Hana, 4 anos:** já lê com certa fluência e faz pequenas contas de adição e subtração [lembrança]. Lê textos de cartilha no app ("Camila e o cavalo", pedido da v3.1 [certeza]).
- **Duas versões na memória:** um arquivo da memória chama a Hinata de "filha mais nova" e outro de "mais velha". **A mais nova e certa é a do pedido de passagem (versão de 07/10/2026, anexado em 14/10/2026): Hinata tem 6 e Hana tem 4.** [lembrança, memória do Projeto] No início do projeto, o nome "Renata" foi registrado por engano no lugar de Hinata. [certeza] "Renata" aparece na descrição do manifest da v1.3 **até a v2.1**; saiu na v3.0. Também aparece em exemplos dos testes ("Renata Maria").
- **Escola São Pedro**, marca Coruja 🦉, lema "Esforço Vence". 7 apps em `escolasaopedro<nome>.netlify.app`.
- **Como trabalhar com ele:**
  - português do Brasil;
  - **edições cirúrgicas**;
  - explicar **a causa de verdade** de cada problema, em palavras simples;
  - **honestidade** sobre o que foi e o que não foi testado;
  - **checklist ✅/⬜ no fim** de cada resposta;
  - **pedir autorização antes de coisas grandes**;
  - checagem em 3 etapas (autochecagem + agente conferente independente + revisor-chefe);
  - ele às vezes **fala por voz** e o texto sai trocado (ex.: "Wolf screen" = "Full screen"; "silabador você lavador" = "silabador, a palavra");
  - ele lembra de **pedir toda a documentação do próximo app antes de começar** [lembrança];
  - quer entender o "porquê"; gosta de ver capturas de tela; publica ele mesmo no Netlify.

---

## 14. Glossário
- **Formato Coruja:** o jeito combinado de a IA responder, com os rótulos `TÍTULO:`, `TAGS:`, `TEXTO:`, `PALAVRAS NOVAS:`, `PERGUNTAS:` e `PARA PENSAR:`.
- **Leitura do dia / Entender de verdade / Adaptar / Continuar / Consertar:** os 5 pedidos (prompts) que o app copia para colar na IA.
- **Preparar texto (Estúdio):** tela onde se cola e arruma o texto.
- **Formatar / ↩️ Desfazer:** arrumar o texto colado / voltar ao que estava antes.
- **Meus textos / Textos de <nome>:** biblioteca da criança (para ler).
- **Textos lidos:** histórico dos textos já lidos (✅ Lido).
- **Marca-texto:** a faixa amarela que pinta a linha tocada.
- **Dicionário:** a janelinha com a explicação da palavra sublinhada.
- **Quiz:** as perguntas de interpretação no fim do texto.
- **Para pensar:** pergunta aberta para conversar com o pai (💭).
- **Margem: Normal / Sílabas / Espaços:** os 3 jeitos de terminar a linha.
- **Recuo:** o espacinho antes da 1ª palavra do parágrafo.
- **Bichinho:** o emoji da criança (um dos 8 oficiais).
- **Código da família:** palavra de pelo menos 6 letras/números que junta os celulares da família na nuvem.
- **Nuvem:** Firebase/Firestore do Pedro (`escola-sao-pedro-5ee62`).
- **Fila (pendências):** o que espera internet para subir.
- **Lápide:** registro de um texto apagado (para a nuvem não trazê-lo de volta).
- **Versões guardadas:** a cópia de cada dia na nuvem.
- **Degrau de segurança:** a 1ª tela repetida no histórico do voltar.
- **Firebase de mentira:** o imitador usado nos testes.
- **Compartilhados:** `nuvem-config.js`, `nuvem-sync.js`, `escola-pwa.js` (e, no cadastro novo, `escola-familia.js`): iguais em todos os apps.
