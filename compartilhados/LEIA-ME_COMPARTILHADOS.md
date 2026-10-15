# 📦 Cópias mestras dos arquivos compartilhados — Escola São Pedro

**Geradas com o 📚 Alfabetização v123 em 08/10/2026.** São os arquivos que vão, **sem mudar**, para os outros 6 apps
quando chegar a vez de cada um (ordem da decisão D10: Curiosidades → Coruja Explica → Provinha → Historinhas → Matemática → Fluência).
Antes de usar num app, **confira o md5** (no Linux: `md5sum arquivo`; no Windows: `certutil -hashfile arquivo MD5`).

| Arquivo | Versão | md5 | Muda de app para app? |
|---|---|---|---|
| `escola-familia.js` | 1.2 | `c12df6caa652787d9e083abb3be436b9` | **Não.** Telas da família e das crianças (T1–T8), chip, bolinha, seção "☁️ Família e nuvem", migração, trava do adulto, ⚙️ na "Quem vai estudar hoje?" |
| `nuvem-sync.js` | 4.1 | `f151bb171add2d25af870a4c7ccbec46` | **Não.** Nuvem (Firestore REST), família por criança, fila, cópias de cada dia, `movidoPara`; 4.1 = não regrava criança tirada |
| `escola-pwa.js` | 2 | `ec31bf4a195ccf6a28f70e4fe3748c5f` | **Não.** Tela sempre acesa, tela cheia, convite para instalar, os 8 bichinhos |
| `nuvem-config.js` | — | `1d5f060a5ae8339921d3d58498807971` | **Não.** O do Pedro, byte a byte (chaves do Firebase). Nunca usar o `testes/nuvem-config.js` (falso) |
| `modelos/sw_alfabetizacao_v123.js` | modelo | `36b1a361f707846d9d4191914ec44a62` | **Sim:** é o `sw.js` do Alfabetização, só como **modelo**. Cada app tem o seu `sw.js` (nome do cache próprio, lista de arquivos com `escola-familia.js`, `nuvem-config.js` buscado na internet primeiro) |

## O que mudou em cada versão

- `escola-familia.js` **1** (v122, 07/10/2026): nasceu no Alfabetização (plano `PLANO_CADASTRO_FAMILIA.md`, D1–D16).
- `escola-familia.js` **1.1** (v122b): só desenho — respiro e largura deitado; caixa do código no meio com o teclado; "Achei a sua família" largo; site de teste = qualquer endereço com "teste".
- `escola-familia.js` **1.2** (v123): ⚙️ na "Quem vai estudar hoje?" (opções `abrirConfig(aoFechar)` e `fecharConfig()` no `EscolaFamilia.iniciar`); bolinha 🟡 enquanto uma criança tirada estiver guardada só na lixeira do celular.
- `nuvem-sync.js` **4** (v122): família por criança, `existeFamilia`, `garantirGuardado`, `marcarMovido`, `limparPendencia`, `semVigiar`; junta antes de enviar quando o celular não conhece a ficha; se a lista de crianças der erro, não mexe na fila.
- `nuvem-sync.js` **4.1** (v123): antes de juntar o que veio da nuvem, confere **na hora** se a criança ainda está no celular (resposta atrasada não regrava criança tirada).

## Como ligar num app

**Atualização 15/10/2026:** o 🌍 Curiosidades já recebeu o cadastro (v2.0 → v2.3) usando estas mesmas cópias, sem mudar nada nelas. O jeito dele está em `MODELO_LIGACAO_CURIOSIDADES_v2.2.js` (a ligação do cadastro não mudou na v2.3) e os aprendizados em `GUIA_IMPLANTAR_CADASTRO_NOVO_APP.md` — os dois na pasta de cima do kit `kit-cadastro-coruja-explica`. Próximo: 🦉 Coruja Explica.

Siga a parte 5.2 e a parte 14 do `PLANO_CADASTRO_FAMILIA.md` (versão 3) e copie o jeito do Alfabetização (ou do Curiosidades): o `ADAPTADOR_CRIANCAS` e o bloco "liga o cadastro da família, a nuvem e o escola-pwa.js" no fim do `index.html` dele. No `sw.js` do app, acrescente `./escola-familia.js` à lista de arquivos e **suba o nome do cache**.

**Regra:** quem precisar mudar um destes arquivos **para** e pergunta ao Pedro; mudança sobe a versão e vale para todos os apps.
