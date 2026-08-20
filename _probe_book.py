# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html', encoding='utf-8').read()
i = t.find('<section class="book-band"')
print('=== BOOK HTML ===')
print(t[i:i+3000].replace('\n', ' ')[:3000])
print()
print('=== ЕСТЬ ЛИ МОДАЛКА/ЧИПЫ ВООБЩЕ? ===')
for kw in ['modal', 'chip', 'data-open-form', 'dialog', 'popup', 'overlay']:
    print(kw, ':', len(re.findall(kw, t, re.I)))
