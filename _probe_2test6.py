# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2TEST_TOJE_SAMOE_POLNAYA.html'
t = io.open(p, encoding='utf-8').read()

print('=== ВСЕ ТЕЛЕФОНЫ ===')
for m in re.finditer(r'\+7[\s(]*\d{1,3}[\s)\-]*\d{2,3}[\s\-]*\d{2}[\s\-]*\d{2}', t):
    print(repr(m.group(0)))
print('tel: ссылки:', re.findall(r'tel:[+\d]+', t))
print()
print('=== АДРЕСА ===')
for m in re.finditer(r'[Кк]омсомольск[а-я]*[^<]{0,20}|[Кк]алининград', t):
    pass
print(set(re.findall(r'[Кк]омсомольск\w*[^<\n]{0,25}', t)))
print()
print('=== ЧАСЫ ===')
print(set(re.findall(r'\d{1,2}[:.]\d{2}\s*[–—-]\s*\d{1,2}[:.]\d{2}', t)))
print()
print('=== СКИДКА 10% ===')
i = t.find('Скидка 10%')
print(t[i-150:i+150].replace('\n', ' ') if i != -1 else 'нет')
print()
print('=== CSS-переменные (палитра) ===')
m = re.search(r':root\{[^}]*\}', t)
print(m.group(0)[:600] if m else 'нет')
