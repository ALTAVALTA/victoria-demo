# -*- coding: utf-8 -*-
"""Показать отличие font-family правил текущей vs ef77bc5c."""
import io
import re
import subprocess

def fams(d):
    return sorted(re.findall(r'([^{}]+)\{[^}]*font-family:[^}]*\}', d))

raw = subprocess.check_output(['git', 'show', 'ef77bc5c:landings/victoria/_deploy/index.html'])
old = raw.decode('utf-8')
cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

fo, fc = fams(old), fams(cur)
print('--- только в СТАРОЙ ---')
for x in fo:
    if x not in fc:
        print(' *', x[:150])
print('--- только в НОВОЙ ---')
for x in fc:
    if x not in fo:
        print(' *', x[:150])
