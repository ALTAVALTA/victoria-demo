# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\index.html', encoding='utf-8').read()
print('LEN', len(t))
# модалка
for kw in ['modal', 'dialog', 'overlay', 'chip']:
    print(kw, ':', len(re.findall(kw, t, re.I)))
i = t.find('modal')
if i == -1:
    i = t.find('dialog')
print('=== КОНТЕКСТ МОДАЛКИ ===')
print(t[i-300:i+2500].replace('\n', ' ')[:2800])
