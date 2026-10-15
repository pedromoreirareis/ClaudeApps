# 📦 Próximo app a receber o novo cadastro da família — o que anexar

**Ordem combinada (Pedro, 14/10/2026):** Curiosidades (✅ feito: cadastro desde a v2.0b; v2.2 publicada; v2.3 entregue em 15/10/2026) → **🦉 Coruja Explica** → Provinha → Historinhas → Matemática → Fluência.

O próximo é o **🦉 Coruja Explica** (`escolasaopedrocorujaexplica.netlify.app`, ID na nuvem `corujaexplica`, hoje na v3.1 com `nuvem-sync.js` v3 e cadastro próprio).
**Regra:** a IA não começa se faltar algum item abaixo — ela pede antes.

> **Atalho (15/10/2026):** quase tudo abaixo já vem junto no **`kit-cadastro-coruja-explica.zip`** (entregue em 15/10/2026). Anexe o kit + o zip do Coruja Explica com os testes + o prompt de continuação dele + um backup de hoje.

## O que anexar na conversa nova
1. **Zip completo do Coruja Explica** (o mais novo, com a pasta de testes: `teste-logica.js`, `teste-v3.js`, `_firebase-falso.js` etc.).
2. **Prompt de continuação / histórico do Coruja Explica** (o do Projeto: `claude/coruja-explica-prompt-continuacao.md`, versão 3.1, ou um mais novo).
3. **`PLANO_CADASTRO_FAMILIA.md`** (versão 3) — está no zip do Curiosidades, em `documentos/referencias/`.
4. **Modelos já feitos** (para copiar o jeito de ligar o cadastro):
   - **`curiosidades-completo-v2.3.zip`** (Curiosidades: o adaptador `ADAPTADOR_CRIANCAS`, a ligação no fim do `index.html`, os testes com Firebase de mentira, os aprendizados dos capítulos 15–17 do histórico);
   - se possível, **`alfabetizacao-completo-v123.zip`** (o primeiro app que recebeu o cadastro).
5. **Cópias mestras dos compartilhados** — já vão dentro do zip do Curiosidades, em `compartilhados/`: `escola-familia.js` 1.2, `nuvem-sync.js` 4.1, `escola-pwa.js` 2 e o `LEIA-ME_COMPARTILHADOS.md` com os md5.
6. **O seu `nuvem-config.js` verdadeiro** (md5 `1d5f060a5ae8339921d3d58498807971`) — também está no zip do Curiosidades.
7. **Um backup exportado do Coruja Explica, de agora** (⚙️ › 💾 Backup › Exportar), para testar a migração com os textos reais das meninas.
8. **Decisões para eu confirmar com você:** o nome do **site de teste** (sugestão: `escolasaopedrocorujaexplicatestes`), o **nome do cache** da versão nova (sugestão: `coruja-explica-v4-0`) e se a tela de abertura também passa a ser sempre "Quem vai estudar hoje?" (decisão D2 do plano).

## Atenção específica do Coruja Explica (para a conversa nova)
- Ele usa `nuvem-sync.js` **v3** → passa para a **4.1** junto com o cadastro (como no Curiosidades).
- Tem cadastro e telas próprios (`telaUsuarios`, `telaCadastro`, `telaNuvem`, `codOv`, `confirmOv`) e backup que já **junta** — o plano e o modelo do Curiosidades mostram o que sai e o que fica.
- A biblioteca de textos de cada criança é grande (limite de ~850 KB por criança na nuvem) — testar a migração com o backup real.
- Os testes dele são em **JavaScript** (Node + Playwright), diferentes dos do Curiosidades (Python) — os dois usam Firebase de mentira.

## Texto pronto para colar na conversa nova
> Olá! Vamos colocar o **novo cadastro da família** no **🦉 Coruja Explica**, seguindo o `PLANO_CADASTRO_FAMILIA.md` (v3) e o modelo do **Curiosidades v2.3** (zip completo anexado). Anexei: o zip completo do Coruja Explica (com testes), o prompt de continuação dele, o plano, o zip do Curiosidades (com as cópias mestras e o meu `nuvem-config.js`) e um backup exportado de hoje. **Antes de começar, leia tudo; se faltar algum arquivo, me peça e não comece.** Regras de sempre: nunca perder progresso; meu `nuvem-config.js` sem nenhuma alteração; não mexer no Firebase sem eu pedir; compartilhados não se editam dentro de um app só; edições cirúrgicas; plano e autorização antes de coisa grande; testes de verdade com Firebase de mentira; checagem em 3 etapas; zip completo; explicar causas em palavras simples; terminar com checklist ✅/⬜.
