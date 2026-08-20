# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'
t = io.open(p, encoding='utf-8').read()

# HTML-блок отзывов (после CSS)
i = t.find('<section class="reviews"')
if i == -1:
    i = t.find('id="reviews"')
print('=== ОТЗЫВЫ HTML ===')
print(t[i:i+3500].replace('\n', ' ')[:3500])
