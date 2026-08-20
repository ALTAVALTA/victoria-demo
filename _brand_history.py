# -*- coding: utf-8 -*-
"""История изменений .brand-name/.brand-mark и содержимое шапки в ключевых коммитах."""
import io
import re
import subprocess

def git_show(rev, path):
    try:
        raw = subprocess.check_output(['git', 'show', rev + ':' + path],
                                      cwd=r'C:\Users\PORTAL\.openclaw\workspace')
        return raw.decode('utf-8', 'replace')
    except Exception as e:
        return None

path = 'landings/victoria/_deploy/index.html'
out = []

# 1. Лог по файлу
log = subprocess.check_output(['git', 'log', '--oneline', '-25', '--', path],
                              cwd=r'C:\Users\PORTAL\.openclaw\workspace').decode('utf-8', 'replace')
out.append('=== git log файла ===')
out.append(log)

# 2. Шапка (header) в А-версии и в текущей
a = io.open(r'landings/victoria/A version.html', encoding='utf-8').read()
cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

def header_block(d):
    m = re.search(r'<header[^>]*>.*?</header>', d, re.S)
    return m.group(0) if m else 'NO HEADER TAG'

out.append('=== HEADER в A version ===')
out.append(header_block(a)[:1500])
out.append('')
out.append('=== HEADER в _deploy (текущая) ===')
out.append(header_block(cur)[:1500])

io.open(r'landings/victoria/_deploy/_brand_out.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written')
