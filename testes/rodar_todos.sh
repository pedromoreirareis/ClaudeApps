#!/bin/bash
# Roda TODOS os testes, uma suíte de cada vez (rodar juntas deixa a máquina lenta e testes de tempo falham à toa).
# Uso: bash testes/rodar_todos.sh   (precisa de Python 3 + Playwright com Chromium)
AQUI="$(cd "$(dirname "$0")" && pwd)"
SAIDA="${1:-$AQUI/../trabalho/saida_testes}"
mkdir -p "$SAIDA"
bash "$AQUI/preparar_pastas.sh" > /dev/null
for f in node_check; do :; done
echo "== node --check"; ( for j in "$AQUI"/../pacote-netlify/*.js; do node --check "$j" && echo "ok $(basename $j)"; done
  python3 -c "
import re,sys,subprocess,tempfile,os
s=open('$AQUI/../pacote-netlify/index.html',encoding='utf-8').read()
for i,b in enumerate(re.findall(r'<script>([\s\S]*?)</script>',s)):
    t=tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8'); t.write(b); t.close()
    r=subprocess.run(['node','--check',t.name]); print('ok index.html <script>',i+1) if r.returncode==0 else print('ERRO index.html <script>',i+1); os.unlink(t.name)
" ) > "$SAIDA/node_check.txt" 2>&1; cat "$SAIDA/node_check.txt"
cd "$AQUI"
for t in regressao.py sw_test.py teste_cadastro.py teste_nuvem_v20.py; do
  echo "== $t"; timeout 1200 python3 $t > "$SAIDA/${t%.py}.txt" 2>&1; tail -1 "$SAIDA/${t%.py}.txt"
done
cd "$AQUI/navegador"
for t in teste_familia.py teste_desenho.py teste_v20.py teste_v21.py teste_v22.py teste_v23.py prova_testes_pegam.py; do
  echo "== $t"; timeout 1800 python3 $t > "$SAIDA/${t%.py}.txt" 2>&1; tail -1 "$SAIDA/${t%.py}.txt"
done
