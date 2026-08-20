# -*- coding: utf-8 -*-
"""Сколько <style> в _deploy и где они; длина каждого; где заканчивается CSS."""
import io
import re

cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

print('count <style>:', cur.count('<style>'))
print('count </style>:', cur.count('</style>'))
for m in re.finditer(r'<style[^>]*>', cur):
    print('style open at', m.start(), repr(m.group(0)[:80]))

# Посмотрим первые 300 символов первого style
i = cur.find('<style>')
print()
print('--- первый style, первые 400 символов ---')
print(cur[i:i+400])

# А теперь поищем :root в _deploy
print()
print(':root в _deploy:', ':root' in cur)
print('h1,h2,h3 правило:', 'h1,h2,h3,.serif' in cur)
print('--font-display:', cur.count('--font-display'))
print('--pine:', cur.count('--pine'))
