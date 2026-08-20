# -*- coding: utf-8 -*-
"""Верификация фикса коллизии .brand-name."""
import io
import re

data = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

checks = {
    'footer sig .sig-name': '<span class="sig-name">' in data,
    'no footer .brand-name span': '<span class="brand-name"><b>A</b>' not in data,
    'header brand-name intact': '<span class="brand-name">Виктория</span>' in data,
    'brand-name css = A-style': ".brand-name{font-family:var(--font-display);font-size:22px;color:var(--pine);line-height:1}" in data,
    'sig-name css exists': '.sig-name{display:inline-flex;color:#d8d2c2;' in data,
    'brand-core still there': '.brand-core{color:var(--gold-bright);' in data,
    'no old jost brand-name css': "font-size:12px;font-weight:700;gap:.08em;text-transform:uppercase;line-height:1}" not in data.replace('.sig-name{display:inline-flex;color:#d8d2c2;font-family:\'Jost\',sans-serif;', ''),
}
for k, v in checks.items():
    print(('OK  ' if v else 'FAIL'), k)

# Вывести оба правила
print()
for m in re.finditer(r'\.brand-name\{[^}]*\}', data):
    print('brand-name:', m.group(0))
for m in re.finditer(r'\.sig-name\{[^}]*\}', data):
    print('sig-name  :', m.group(0))

# Баланс тегов
import subprocess
r = subprocess.run(['python3', 'landings/victoria/_deploy/_balance.py'], capture_output=True, text=True)
print()
print(r.stdout[-500:] if r.returncode == 0 else 'balance script err')
