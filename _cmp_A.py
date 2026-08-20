# -*- coding: utf-8 -*-
"""Сравнение шрифтовых правил: _deploy/index.html vs A version.html (эталон нейронки)."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

cur = load(r'landings/victoria/_deploy/index.html')
a = load(r'landings/victoria/A version.html')

print('cur len:', len(cur), '| A len:', len(a))

def fam_rules(d):
    return sorted(re.findall(r'([^{}]+)\{[^}]*font-family:[^}]*\}', d))

fc, fa = fam_rules(cur), fam_rules(a)
print('cur fam rules:', len(fc), '| A fam rules:', len(fa))
print()
print('--- только в _deploy ---')
for x in fc:
    if x not in fa:
        print(' *', x.strip()[:160])
print()
print('--- только в A version ---')
for x in fa:
    if x not in fc:
        print(' *', x.strip()[:160])

# font-display переменные
print()
print('cur --font-display:', re.search(r'--font-display:([^;]+)', cur).group(1).strip() if re.search(r'--font-display:([^;]+)', cur) else 'NONE')
print('A   --font-display:', re.search(r'--font-display:([^;]+)', a).group(1).strip() if re.search(r'--font-display:([^;]+)', a) else 'NONE')
print('cur --font-body:', re.search(r'--font-body:([^;]+)', cur).group(1).strip() if re.search(r'--font-body:([^;]+)', cur) else 'NONE')
print('A   --font-body:', re.search(r'--font-body:([^;]+)', a).group(1).strip() if re.search(r'--font-body:([^;]+)', a) else 'NONE')
