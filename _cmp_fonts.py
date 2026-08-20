# -*- coding: utf-8 -*-
"""Сравнение шрифтов с прошлой версией (из корня workspace)."""
import io
import re
import subprocess

def fontinfo(data):
    res = {}
    m = re.search(r'--font-display:([^;]+)', data)
    res['font-display'] = m.group(1).strip() if m else 'NOT FOUND'
    m = re.search(r'--font-body:([^;]+)', data)
    res['font-body'] = m.group(1).strip() if m else 'NOT FOUND'
    res['jost_faces'] = len(re.findall(r"font-family:'Jost'", data))
    rules = re.findall(r'([^{}]+)\{([^}]*font-family:[^}]*)\}', data)
    res['display_users'] = [r[0].strip() for r in rules if 'var(--font-display)' in r[1]]
    return res

raw = subprocess.check_output(['git', 'show', 'ef77bc5c:landings/victoria/_deploy/index.html'])
old = raw.decode('utf-8')
cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

for label, data in (('CURRENT', cur), ('PREV ef77bc5c', old)):
    print('=== %s ===' % label)
    fi = fontinfo(data)
    print('font-display:', fi['font-display'])
    print('font-body:', fi['font-body'])
    print('jost_faces:', fi['jost_faces'])
    for x in fi['display_users']:
        print('  disp:', x)
    print()
