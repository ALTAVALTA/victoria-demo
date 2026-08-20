# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'
t = io.open(p, encoding='utf-8').read()

# 3. Отзывы (реальные 4) + аватарки
print('=== ОТЗЫВЫ (HTML) ===')
i = t.find('rev-grid')
print(t[i-200:i+3200].replace('\n', ' ')[:3400])
