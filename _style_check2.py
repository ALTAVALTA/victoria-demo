# -*- coding: utf-8 -*-
"""Проверка второго <style> в _deploy: там основной CSS?"""
import io
import re

cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

# все style блоки
styles = re.findall(r'<style[^>]*>(.*?)</style>', cur, re.S)
print('style blocks:', len(styles))
for idx, s in enumerate(styles):
    print('--- block %d: %d chars ---' % (idx, len(s)))
    print('  :root:', ':root' in s, '| h1 rule:', 'h1,h2,h3' in s, '| .btn:', '.btn' in s, '| .chips:', '.chip' in s)
    print('  первая строка:', s.strip().split('\n')[0][:80])

# посмотрим размер ВСЕГО CSS
full_css = '\n'.join(styles)
print()
print('total css chars:', len(full_css))
