# -*- coding: utf-8 -*-
"""Полные правила для h1/h2/h3 в текущей и старой версии + наличие Georgia у системы."""
import io
import re
import subprocess

def hrules(data):
    out = {}
    for m in re.finditer(r'([^{}]*h[123][^{}]*)\{([^}]*)\}', data):
        sel = m.group(1).strip()
        body = m.group(2)
        out[sel] = body
    return out

cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()
raw = subprocess.check_output(['git', 'show', 'ef77bc5c:landings/victoria/_deploy/index.html'])
old = raw.decode('utf-8')

print('=== CURRENT h-rules ===')
for k, v in hrules(cur).items():
    if 'font' in v or 'color' in v:
        print(k, '=>', v.strip()[:160])
print()
print('=== OLD h-rules ===')
for k, v in hrules(old).items():
    if 'font' in v or 'color' in v:
        print(k, '=>', v.strip()[:160])
