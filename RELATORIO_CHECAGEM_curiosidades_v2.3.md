# ✅ RELATÓRIO DE CHECAGEM — 🌍 Curiosidades do Mundo v2.3 (Ler Mais com margem e recuo, destaque duplo)

**Data:** 15/10/2026 · **Cache:** `curiosidades-mundo-v2-3` · Como foi feito: histórico, capítulo 18.

| Arquivo do pacote (9 arquivos) | md5 |
|---|---|
| `index.html` | `fbf346c640155b0a68cad21d274d5133` |
| `sw.js` | `3e7ccdcdbf1533986f6c02e5d69262c6` |
| `nuvem-config.js` (o do Pedro, sem mudança) | `1d5f060a5ae8339921d3d58498807971` |
| `escola-familia.js` 1.2 · `nuvem-sync.js` 4.1 · `escola-pwa.js` 2 | `c12df6caa652787d9e083abb3be436b9` · `f151bb171add2d25af870a4c7ccbec46` · `ec31bf4a195ccf6a28f70e4fe3748c5f` (sem mudança) |
| `manifest.webmanifest` · `icon-192.png` · `icon-512.png` | `7bc096a1…` · `3b076500…` · `6b759818…` (sem mudança) |

**O que mudou (v2.2 → v2.3):**
- **Ler Mais:** ganhou a ⚙️ "Ajustes da leitura", com a margem direita (☰ Normal / ✂️ Sílabas / ↔️ Espaços) e o recuo no começo do parágrafo. O código foi copiado do Coruja Explica v3.1.
- **Destacar por sílabas:** saiu.
- **Destaque duplo:** com o destaque por linha ligado, segurar o dedo numa palavra dá a ela um segundo destaque.
- **Conteúdo:**
  - Júpiter #11 e Netuno #8 corrigidos.
  - Nosso Cerrado #3 ganhou um fato novo, com o emoji 🗺️.
  - Brasil Colônia #5 e Idade Média #17 perderam 3 hífens invisíveis.
  - Os 238 cartões que não tinham agora têm a frase do símbolo grande.
- **Chaves por criança:** `CHAVES_NUVEM` passou a ter 26.
- **Lidas:** nenhuma curiosidade mudou de lugar, então as lidas continuam valendo.

## 1. Etapa 1 — autochecagem
| Pedido do Pedro | Prova |
|---|---|
| Margem com sílabas e recuo no Ler Mais, ligados nas configurações como no Coruja | teste_v23 seções 2 e 3: os 3 modos foram medidos (pontos de corte, linhas rentes, teto de espaço, recuo). Os ajustes ficam por criança no celular, na nuvem e no backup, abrindo pela ⚙️ do Ler Mais e pelas Configurações. Os blocos do Coruja estão idênticos (conferido pelo revisor). |
| Tirar as sílabas | teste_v23 seção 2: a opção sumiu das Configurações e da barra, e o Dicionário voltou a sublinhar as palavras. Uma criança que tinha `cfgSyl=1` guardado não é afetada (conferido pelo revisor). |
| Destaque duplo (segurar a palavra) | teste_v23 seções 4, 5 e 6. Testado no cartão e no Ler Mais, e só funciona com o destaque por linha. O toque rápido não marca. O menu do navegador não abre. O contraste é bom no tema Noite. Segurar 3,5 s ou 6 s mantém o destaque. |
| Nunca perder progresso | `patch23.py` e teste_v23 seção 1: mesmos 295 cartões, mesmas 4.254 curiosidades, mesma ordem. Só as 5 curiosidades autorizadas mudaram de texto. |
| Correções | Júpiter, Netuno, Cerrado, frase do símbolo (238), hífens escondidos, Laticínios (AL5) |

## 2. Etapa 2 — conferente
- **Rodada 7** (`revisao_independente/RELATORIO_CONFERENTE_v2.3_rodada7.md`): 2 🟠, os dois corrigidos.
  - Com "✂️ Sílabas" e o destaque por linha, o marca-texto ficava com o dobro da altura e o Ler Mais rolava de lado. **Causa:** a função antiga media a palavra cortada como se fosse um bloco só, juntando os dois pedaços. Foi trocada pela do Coruja, que mede cada pedaço.
  - Segurar o dedo no modo normal deixava a palavra muda. **Causa:** o "segurar" era armado mesmo sem o destaque por linha. Agora só é armado com ele.
  - 🟡 corrigidos: contraste no tema Noite e nomes estrangeiros cortados errado (lista `NAO_CORTAR`).
- **Rodada 8:** ✅ 0 🔴 · 0 🟠 · 0 🟡. Os 6 🟢 foram anotados em `ALTERACOES_FUTURAS_curiosidades.md`.
- **Rodada 9** (só as correções depois do revisor-chefe, `…_rodada9.md`): ✅ 0 🔴 · 0 🟠.
  - Reproduziu o patch e chegou ao mesmo md5.
  - Simulou 13 casos do "segurar e soltar".
  - Seus 🟡 foram corrigidos: o teste do "toque de propósito" agora prova de verdade (com `pointercancel`), e os textos do histórico e do pedido foram acertados.

## 3. Etapa 3 — revisor-chefe
`revisao_independente/RELATORIO_REVISOR_CHEFE_v2.3.md`: **✅ pode publicar.** 0 🔴 e 0 🟠 no app.
- **O que ele conferiu:**
  - Reproduziu o patch.
  - Leu as 238 frases inteiras e os itens corrigidos.
  - Fez 320 aberturas do Ler Mais sem rolar de lado.
  - Rodou teste_v23 (63/63) e teste_v22 (28/28).
- **🟠 só no kit do Coruja Explica e nos documentos, todos corrigidos:**
  - nomes de arquivos que não existiam no kit;
  - mistura de v2.2 com v2.3;
  - cópia velha do histórico dentro do kit;
  - passo do `sw.js` faltando no guia.
- **🟡 no app, todos corrigidos e testados de novo:**
  - **Segurar a palavra mais de ~3 s fazia o destaque sumir ao soltar.** Causa: o "clique" que vem ao soltar o dedo só era ignorado até 2,5 s depois de o destaque aparecer, e não depois de o dedo subir.
  - Emoji 💧 → 🗺️ no Cerrado #3.
  - 3 hífens invisíveis antigos ("OREL-HAS" seria corte errado) e "NUMA ARMAÇÃO".
  - Laticínios: "o leite não é derivado dele mesmo".
- **🟡 que ficam:** estão em `ALTERACOES_FUTURAS_curiosidades.md`, seção 4.

## 4. O que foi RODADO e o que foi só LIDO
- **Rodado** no Chromium sem tela, com o Firebase de mentira: a suíte inteira no pacote final, uma suíte de cada vez. O revisor ainda fez a varredura do Ler Mais e as capturas em 984×432 e 360×740.
- **Não testado** (só o celular do Pedro mostra; o passo 7 das INSTRUCOES diz o que olhar):
  - celular Android de verdade;
  - TV espelhada;
  - a voz lendo as palavras cortadas;
  - o menu de segurar do Android;
  - se o navegador do celular manda o "clique" depois de segurar;
  - o Firebase real.

## 5. Resultados da suíte (pacote final, `index.html` `fbf346c6…`; saídas em `trabalho/saida_testes/`)
- `node --check`: ok (5 .js e os 2 scripts do index)
- regressão: **10/10**
- SW offline: ok
- cadastro: **41/41**
- nuvem: **94/94**
- família: **167/167**
- desenho: **151/151**
- v20: **40/40**
- v21: **43/43**
- v22: **28/28**
- **v23: 72/72** (novo)
- **prova: 19/19**. Itens novos:
  - destaque duplo e Ler Mais com sílabas, comparados à versão sem a correção;
  - marca-texto de uma linha e "segurar sem linha fala", comparados à v2.3 de antes da rodada 7;
  - segurar 3,5 s e toque de propósito depois do `pointercancel`, comparados à v2.3 da rodada 8.

Todos os testes falham na versão de antes e passam na atual.
