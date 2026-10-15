#!/bin/bash
# Monta as pastas que os testes usam, a partir do pacote-netlify/ deste zip.
#   /home/claude/z        = pacote com o nuvem-config.js VAZIO (como sem nuvem)
#   /home/claude/t/site   = pacote com o nuvem-config.js FALSO (nuvem "configurada" para o Firebase de mentira)
#   /home/claude/z18      = cópia exata do pacote (usada pelos testes de testes/extras_v1.8/)
#   /home/claude/t        = também recebe os prints que os testes tiram
# Uso:  bash testes/preparar_pastas.sh      (rodar de dentro da pasta aberta do zip ou de qualquer lugar)
set -e
AQUI="$(cd "$(dirname "$0")" && pwd)"
PACOTE="$AQUI/../pacote-netlify"
[ -f "$PACOTE/index.html" ] || { echo "Não achei $PACOTE/index.html"; exit 1; }
rm -rf /home/claude/z /home/claude/t/site /home/claude/z18
mkdir -p /home/claude/z /home/claude/t/site /home/claude/z18
cp "$PACOTE"/* /home/claude/z/
cp "$PACOTE"/* /home/claude/t/site/
cp "$PACOTE"/* /home/claude/z18/
cp "$AQUI/nuvem-config-vazio.js" /home/claude/z/nuvem-config.js
cp "$AQUI/nuvem-config.js"       /home/claude/t/site/nuvem-config.js
echo "Pronto:"; ls /home/claude/z /home/claude/t/site /home/claude/z18
