# -*- coding: utf-8 -*-
"""Проверка шрифтов: @font-face, Google Fonts, font-family переменные."""
import io
import re

data = io.open('index.html', encoding='utf-8').read()

print('=== @font-face ===')
for m in re.finditer(r'@font-face\s*{[^}]+}', data):
    print(m.group(0)[:300])
    print('---')

print('=== google fonts / @import ===')
for m in re.finditer(r'@import[^;]+;', data):
    print(m.group(0)[:200])

print('=== links на шрифты ===')
for m in re.finditer(r'<link[^>]+fonts[^>]*>', data):
    print(m.group(0)[:200])

print('=== :root переменные шрифтов ===')
m = re.search(r':root\s*{[^}]+}', data)
if m:
    for line in m.group(0).split(';'):
        if 'font' in line.lower():
            print(line.strip()[:120])

print('=== font-family в CSS (уникальные) ===')
fams = set(re.findall(r'font-family:\s*([^;}]+)', data))
for f in sorted(fams):
    print(' *', f.strip()[:120])
