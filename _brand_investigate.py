# -*- coding: utf-8 -*-
"""Сколько элементов .brand-name в HTML и где они; когда CSS .brand-name изменился."""
import io
import re
import subprocess

cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

print('=== .brand-name в HTML ===')
for m in re.finditer(r'<[^>]*class="[^"]*brand-name[^"]*"[^>]*>', cur):
    print(m.group(0)[:200])
    print('---')

print()
print('=== .brand-mark в HTML ===')
for m in re.finditer(r'<[^>]*class="[^"]*brand-mark[^"]*"[^>]*>', cur):
    print(m.group(0)[:200])
    print('---')

# CSS .brand-name
m = re.search(r'\.brand-name\s*\{[^}]*\}', cur)
print('CSS .brand-name:', m.group(0) if m else 'NOT FOUND')

m = re.search(r'\.brand-mark[^{]*\{[^}]*\}', cur)
print('CSS .brand-mark:', m.group(0) if m else 'NOT FOUND')

# когда появился текущий .brand-name — ищем в git историю
print()
print('=== git log: когда менялся .brand-name ===')
out = subprocess.check_output(['git', 'log', '--oneline', '-20', '--', 'landings/victoria/_deploy/index.html'],
                              cwd=r'C:\Users\PORTAL\.openclaw\workspace').decode('utf-8', 'replace')
print(out)
