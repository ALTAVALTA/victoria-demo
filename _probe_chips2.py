# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\index.html', encoding='utf-8').read()
# чипы услуг: ищем блок с chip рядом с формой/услугами
for m in re.finditer(r'service-chip|chip-item|\.chip|data-chip', t):
    s = max(0, m.start()-150); e = min(len(t), m.end()+150)
    print('...', t[s:e].replace('\n', ' '), '...')
    print('---')
    if m.start() > 40000: break
