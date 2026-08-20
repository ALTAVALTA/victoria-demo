# -*- coding: utf-8 -*-
"""Проверка по байтам: совпадает ли шрифтовая часть A версии в _deploy.
Ищем в _deploy блок <style> и сравниваем наличие всех font-family из A."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

a = load(r'landings/victoria/A version.html')
cur = load(r'landings/victoria/_deploy/index.html')

# Все font-family значения в A (уникальные)
afams = set(re.findall(r'font-family:\s*([^;}]+)', a))
print('A font-family values:')
for f in sorted(afams):
    present = f.strip() in cur
    print('  %s -> %s' % (('OK ' if present else 'MISSING'), f.strip()[:80]))

# Google fonts / import / link в A
print()
print('A links/imports шрифтов:')
for m in re.finditer(r'<link[^>]+>', a):
    if 'font' in m.group(0).lower() or 'css' in m.group(0).lower():
        print('  ', m.group(0)[:200])
for m in re.finditer(r'@import[^;]+;', a):
    print('  @import', m.group(0)[:150])

# есть ли в _deploy ссылки на Google Fonts
print()
print('_deploy google fonts links:', re.findall(r'fonts\.googleapis[^"\']*', cur)[:3])
