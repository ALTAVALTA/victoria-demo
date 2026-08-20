# -*- coding: utf-8 -*-
"""Проверка: где footer-brand в DOM V2 и что вокруг."""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html'
t = io.open(p, encoding='utf-8').read()

# найдём позицию footer-brand и что до/после
i = t.find('footer-brand')
print('footer-brand pos:', i)
print('контекст:')
print(t[i-300:i+400].replace('\n', ' '))
print()
# есть ли sig-name / brand-core
print('sig-name:', 'sig-name' in t, '| brand-core:', 'brand-core' in t)
# где footer закрывается
j = t.rfind('</footer>')
print('</footer> pos:', j, '| footer-brand до </footer>:', i < j)
# сколько всего footer
print('всего <footer:', len(re.findall(r'<footer', t)))
