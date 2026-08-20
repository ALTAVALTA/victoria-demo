# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2TEST_TOJE_SAMOE_POLNAYA.html'
t = io.open(p, encoding='utf-8').read()

print('=== ФОРМА: куда шлёт? ===')
i = t.find('bookForm')
# ищем fetch/workers/lead рядом
for m in re.finditer(r'fetch\(|workers\.dev|LEAD|lead|X-Lead', t):
    s = max(0, m.start()-120); e = min(len(t), m.end()+200)
    print('...', t[s:e].replace('\n', ' '), '...')
    print('---')

print('=== ФУТЕР ===')
i = t.rfind('<footer')
print(t[i:i+1500].replace('\n', ' ') if i != -1 else 'нет footer')
