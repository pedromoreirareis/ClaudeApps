#!/bin/bash
# Monta as pastas que os testes ANTIGOS do app usam (regressao.py, sw_test.py,
# teste_cadastro.py, teste_nuvem_v20.py), a partir do pacote-netlify/ deste zip.
#   /home/claude/z        = pacote com o nuvem-config.js VAZIO (como sem nuvem)
#   /home/claude/t/site   = pacote com o nuvem-config.js FALSO (nuvem "configurada" para o Firebase de mentira)
#   /home/claude/t        = também recebe os prints que os testes tiram
# (Os testes da pasta navegador/ servem o pacote-netlify/ direto e trocam o nuvem-config.js sozinhos.)
# Uso:  bash testes/preparar_pastas.sh
set -e
AQUI="$(cd "$(dirname "$0")" && pwd)"
PACOTE="$AQUI/../pacote-netlify"
[ -f "$PACOTE/index.html" ] || { echo "Não achei $PACOTE/index.html"; exit 1; }
rm -rf /home/claude/z /home/claude/t/site
mkdir -p /home/claude/z /home/claude/t/site
cp "$PACOTE"/* /home/claude/z/
cp "$PACOTE"/* /home/claude/t/site/
cp "$AQUI/nuvem-config-vazio.js" /home/claude/z/nuvem-config.js
cp "$AQUI/nuvem-config.js"       /home/claude/t/site/nuvem-config.js
echo "Pronto:"; ls /home/claude/z /home/claude/t/site
