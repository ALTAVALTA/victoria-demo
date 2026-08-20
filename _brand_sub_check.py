# -*- coding: utf-8 -*-
"""Сравнение .brand-sub в A и _deploy."""
import io
import re

a = io.open(r'landings/victoria/A version.html', encoding='utf-8').read()
cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

print('=== A: .brand-sub ===')
for m in re.finditer(r'\.brand-sub[^{]*\{[^}]*\}', a):
    print(m.group(0))
print()
print('=== _deploy: .brand-sub ===')
for m in re.finditer(r'\.brand-sub[^{]*\{[^}]*\}', cur):
    print(m.group(0))
print()
print('_deploy содержит .brand-sub:', '.brand-sub' in cur)
