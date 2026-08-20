# -*- coding: utf-8 -*-
import io, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

SRC = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2TEST_TOJE_SAMOE_POLNAYA.html'
DST = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2TEST_TOJE_SAMOE_POLNAYA_clean.html'
t = io.open(SRC, encoding='utf-8').read()

# 1. Срезать ```html ... ```
assert t.startswith('```html'), 'не начинается с ```html'
t = t[len('```html'):]
assert t.rstrip().endswith('```'), 'не заканчивается на ```'
t = t.rstrip()[:-3].rstrip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(t)
print('clean saved:', len(t), 'chars')
