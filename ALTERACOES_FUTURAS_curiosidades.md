# 🗺️ Alterações futuras — 🌍 Curiosidades do Mundo (o que ainda NÃO foi feito)

Atualizado em 15/10/2026, depois da **v2.3** (versão final desta rodada). Cada item precisa de **plano + autorização do Pedro** antes de começar.
Tempo = trabalho da IA na conversa (fazer + testar + checagem em 3 etapas), sem contar o teste do Pedro no celular; é o mínimo (cada rodada costuma ter ~1–2 h de acertos depois do teste no celular). Referência: v2.1 ≈ 3h30, v2.2 ≈ 3h, v2.3 ≈ 4h.

## 1. Ideias pedagógicas escolhidas pelo Pedro (14/10/2026)
| Ideia | O que é | Tamanho | Tempo |
|---|---|---|---|
| 🗣️ **Conte para o papai** | No fim de um cartão (ou a cada 5 lidas no dia), a coruja convida: "Conte para o papai uma coisa que você aprendeu!". Botões "Contei! ✅" e "Depois". Soma nas Conquistas (medalha). Sem gravar voz. | pequena | ~1h30 |
| 📖 **Revisar o Dicionário** | Jogo com as palavras difíceis que a criança já tocou: palavra ↔ significado (3 opções); as que ela erra voltam mais vezes. Progresso por criança, na nuvem. | média | ~2h30 |
| 🔗 **Leia também** | No fim de cada cartão, 2–3 cartões ligados (ex.: Marie Curie → Químicos Famosos). Lista escrita à mão para os 295 cartões (só dados). | média (conteúdo) | ~3h |
| 📊 **Resumo da semana** | Na ⚙️: leituras por dia (barrinhas), seções preferidas, palavras novas, acertos no Desafio, "contou para o papai". Precisa de uma chave nova com a **data de cada leitura** — só conta a partir da versão que trouxer isso. | média | ~2h30 |
| 🕰️ **Linha do Tempo** | Faixa que rola com 40–60 pessoas/fatos (Sócrates 470 a.C. → Hipátia → Leonardo → Galileu → Newton → Marie Curie → Einstein → Lua 1969); toque abre o cartão; lidos acesos. Ensina "a.C." e séculos. | grande | ~3h30 |

## 2. Ideias sugeridas (o Pedro ainda vai decidir)
| Ideia | O que é | Tamanho | Tempo |
|---|---|---|---|
| 🧠 **Perguntas de compreensão** | 3 perguntas por cartão (o que o texto diz / por quê / o que você acha). Para os 295 cartões são ~885 perguntas: começar pelos 30 cartões favoritos. | muito grande | ~4h a 1ª leva (+~3h por leva de 30–40 cartões) |
| 🗺️ **Mapa do mundo** | Mapa desenhado dentro do app (sem internet), países lidos coloridos, toque abre o cartão; o arquivo cresce ~100–300 KB. | grande | ~4h |
| 🎙️ **Eu leio primeiro** | A criança lê em voz alta e depois toca 🔊 para conferir com a voz do app (fluência). Sem gravar. | pequena | ~1h30 |
| ✍️ **Minha curiosidade** | A criança dita ou escreve uma curiosidade dela (produção de texto), num cantinho dela. | média | ~2h30 |

**Tudo de uma vez:** ~25–30 h — **não recomendado** (a conversa pode acabar no meio; difícil testar tudo; difícil achar a causa se algo der errado).
**Ordem recomendada:** v2.4 = Conte para o papai + Revisar o Dicionário + Leia também (~7h) → v2.5 = Linha do Tempo + Resumo da semana (~6h) → v2.6 = Mapa do mundo + Perguntas de compreensão, 1ª leva (~8h).

## 3. Conteúdo
- **Mais curiosidades** quando o Pedro quiser (o método da v2.2 funciona: guia de escrita → agentes escritores → conferentes de fatos independentes → parser; cartões novos sempre **no fim**, curiosidade nova sempre **no fim do cartão**).
- Pendências 🟡 de conteúdo da v2.2 (pequenas): algumas anedotas sem "conta-se que" (Davy, Goodall); algumas repetições de fatos entre cartões novos (sem contradição).
- Revisar frases antigas que dependem de data ("hoje", "agora", "ainda") de vez em quando (ex.: missões espaciais).

## 4. Técnico / acessibilidade
- **A3/A4 (da v2.0):** botões antigos do app com 40–44 px (o mínimo combinado é 48 px) e textos de ajuda de 13 px; "Continuar de onde parei" usa letras de 13/11 px como os vizinhos. Só desenho; precisa de teste em vários tamanhos. ~1h30.
- **Dias seguidos com 2 celulares:** o celular que lê hoje manda na sequência; um celular parado pode baixar a sequência do outro na nuvem (limitação conhecida, igual às versões anteriores). Corrigir exige uma regra de junção própria para `ultimoDia/seqDias`. ~1h30.
- **"Ler ao tocar" com celular antigo:** um celular ainda numa versão antiga (v1.8/v2.0b) que envia a ficha tira o `sayTap`, `margem`, `recuo` e `palavra` da nuvem; o celular novo devolve na próxima sincronização (só preferências; nada de leitura se perde). Some sozinho quando todos os celulares estiverem na v2.3.
- **Pequenos (🟢 da rodada 8 do conferente e do revisor-chefe):** alguns nomes estrangeiros fora da lista `NAO_CORTAR` ainda podem ser cortados errado com "✂️ Sílabas" (ex.: NEIL, 4 vezes; "JACQUES-LOUIS") — basta acrescentar na lista; o segundo destaque pode "sobrar" depois de apertar o 🔊 ou de segurar e rolar o Ler Mais (um toque resolve); segurar uma palavra do Dicionário não abre o significado (só o toque curto abre); tocar na margem da linha (fora das palavras) não tira o segundo destaque; com o celular em pé, o título do Ler Mais aparece cortado (a ⚙️ nova ocupa espaço). ~1h para tudo.
- **Android:** se o navegador do celular **não** mandar o "clique" depois de segurar o dedo, um toque de propósito na mesma palavra no primeiro segundo é ignorado (só o celular real mostra; se acontecer, é um ajuste de 1 linha).
- **Karaokê:** se uma voz do Android avisar a palavra só uma vez, o destaque pode parar na 1ª palavra (só o celular real mostra).
- **Puxar para atualizar do Chrome** ao arrastar o dedo com o celular em pé, no navegador (não no app instalado em tela cheia). Se acontecer: `overscroll-behavior:none` (1 linha + teste).
- **Testes perdidos da v1.7** (`valida.py`, suíte funcional) — hoje cobertos em boa parte pelos testes novos; recriar só se fizer falta.
- Os prints de referência antigos (`documentos/referencias/v1.8_prints/`) podem ser apagados quando não forem mais úteis.

## 5. Outros apps (fora deste)
- Próximo a receber o cadastro: **🦉 Coruja Explica** (kit pronto: `kit-cadastro-coruja-explica.zip`, entregue em 15/10/2026; cópia em `trabalho/kit-cadastro-coruja-explica/`). Depois: Provinha → Historinhas → Matemática → Fluência.
- O **Alfabetização** tem no `nuvemMesclar` a mesma regra de "celular recém-chegado" que causou o defeito da preferência que voltava (achado da v2.0b) — vale levar a correção quando ele for mexido de novo.
