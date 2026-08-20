# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'
t = io.open(p, encoding='utf-8').read()

# 2. Подпись ALTAVALTA
print('=== ПОДПИСЬ (HTML) ===')
i = t.find('ALTAVALTA')
print(t[i-400:i+600].replace('\n', ' ') if i != -1 else 'нет')
print()
print('=== ПОДПИСЬ (CSS) ===')
for m in re.finditer(r'\.signature[^{]*\{[^}]*\}|\.sig-[a-z-]+\{[^}]*\}|\.brand-mark[^{]*\{[^}]*\}', t):
    print(m.group(0))
