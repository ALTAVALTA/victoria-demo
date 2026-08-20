# -*- coding: utf-8 -*-
"""Где используется font-display (заголовки) и есть ли файлы шрифтов."""
import io
import os
import re

data = io.open('index.html', encoding='utf-8').read()

print('=== файлы fonts/ ===')
fonts_dir = 'fonts'
if os.path.isdir(fonts_dir):
    for f in sorted(os.listdir(fonts_dir)):
        print(' *', f, os.path.getsize(os.path.join(fonts_dir, f)))
else:
    print('NO fonts dir!')

print()
print('=== font-display использования ===')
for m in re.finditer(r'[^{}]{0,80}var\(--font-display\)[^{}]{0,40}\{[^}]*\}', data):
    print(m.group(0)[:200])
    print('---')

print()
print('=== заголовки h1/h2/h3 и их font-family в inline-стилях? ===')
for m in re.finditer(r'<h[123][^>]*>', data):
    print(m.group(0)[:160])
