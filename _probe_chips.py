# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html', encoding='utf-8').read()
for m in re.finditer(r'chip', t, re.I):
    s = max(0, m.start()-120); e = min(len(t), m.end()+120)
    print('...', t[s:e].replace('\n', ' '), '...')
    print('---')
