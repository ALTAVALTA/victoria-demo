# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html'
t = io.open(p, encoding='utf-8').read()

# HTML-блок подписи в футере
i = t.find('<span class="sig-name">')
print('sig-name HTML pos:', i)
if i != -1:
    print(t[i-200:i+300].replace('\n', ' '))
print()
print('ALTAVALTA в HTML:', t.count('ALTAVALTA'))
# в футере (после <footer)
j = t.find('<footer')
foot = t[j:]
print('в футере ALTAVALTA:', foot.count('ALTAVALTA'), '| footer-brand:', foot.count('footer-brand'), '| sig-name:', foot.count('sig-name'))
