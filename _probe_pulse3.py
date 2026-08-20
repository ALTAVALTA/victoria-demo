# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Полный v-pulse из V1
t1 = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html', encoding='utf-8').read()
m1 = re.search(r'@keyframes\s+v-pulse\s*\{[^}]*\}', t1)
print('V1 v-pulse:', repr(m1.group(0)) if m1 else 'нет')

# Что сейчас в V2
t2 = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html', encoding='utf-8').read()
m2 = re.search(r'@keyframes\s+v-pulse\s*\{[^}]*\}', t2)
print('V2 v-pulse:', repr(m2.group(0)) if m2 else 'нет')
# все вхождения v-pulse в V2 с позициями
for mm in re.finditer(r'v-pulse', t2):
    print('  pos', mm.start(), 'ctx:', repr(t2[max(0,mm.start()-40):mm.end()+40]))
