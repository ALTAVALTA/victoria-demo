# -*- coding: utf-8 -*-
"""Все отличия правил для h1/h2/h3/.serif между A и _deploy."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

cur = load(r'landings/victoria/_deploy/index.html')
a = load(r'landings/victoria/A version.html')

def hdict(d):
    out = {}
    for m in re.finditer(r'([^{}]*?)(h1|h2|h3|\.serif)[^{}]*?\{([^}]*)\}', d):
        sel = (m.group(1).strip() + ' ' + m.group(2)).strip()
        out.setdefault(sel, []).append(m.group(3).strip())
    return out

hc, ha = hdict(cur), hdict(a)
print('=== только в _deploy (заголовки) ===')
for k, v in hc.items():
    if k not in ha:
        print(' *', k, '=>', v)
print()
print('=== только в A (заголовки) ===')
for k, v in ha.items():
    if k not in hc:
        print(' *', k, '=>', v)
print()
print('=== совпадают, но разные значения ===')
for k in hc:
    if k in ha and hc[k] != ha[k]:
        print(' *', k)
        print('   cur:', hc[k])
        print('   A  :', ha[k])
