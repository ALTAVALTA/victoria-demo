# -*- coding: utf-8 -*-
import io, re
t = io.open('index.html', encoding='utf-8').read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', t, re.S)
js = scripts[0]
print('JS len:', len(js))
print('balance {}:', js.count('{') - js.count('}'))
print('balance ():', js.count('(') - js.count(')'))
needles = ['isPhoneValid', 'formatPhone', 'submitting', 'chips-cat::after', 'maxlength="18"',
           'chips-group{display:flex;flex-direction:column']
for n in needles:
    print(n, '->', 'OK' if n in t else 'MISSING')
# проверка: нет ли двойных определений function
print('isPhoneValid defs:', js.count('function isPhoneValid'))
print('formatPhone defs:', js.count('function formatPhone'))
print('submitting defs:', js.count('var submitting'))
