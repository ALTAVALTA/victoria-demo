# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2TEST_TOJE_SAMOE_POLNAYA.html'
t = io.open(p, encoding='utf-8').read()

print('=== ALTAVALTA / подпись / плашка ===')
for kw in ['ALTAVALTA', 'altavalta', 'Демо-версия', 'demo-ribbon', 'demoRibbon', 'Убрать метку']:
    print(kw, ':', len(re.findall(re.escape(kw), t)))

print()
print('=== ФОРМА (booking) ===')
i = t.find('<section class="booking"')
print(t[i:i+2500].replace('\n', ' ')[:2500])
