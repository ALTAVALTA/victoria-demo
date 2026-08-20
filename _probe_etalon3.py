# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'
t = io.open(p, encoding='utf-8').read()

print('=== ВЕСЬ БЛОК ПОДПИСИ ===')
i = t.find('footer-brand')
print(t[i-250:i+700].replace('\n', ' '))
print()
print('=== CSS подписи (весь) ===')
i = t.find('.footer-brand')
print(t[i-50:i+500] if i != -1 else 'нет')
