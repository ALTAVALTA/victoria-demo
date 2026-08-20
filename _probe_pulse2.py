# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# ГЛАВНОЕ: V1 vs V2 — разница в CSS-переменных, от которых зависит цвет подписи!
for name, p in [('V1', r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'),
                ('V2', r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html')]:
    t = io.open(p, encoding='utf-8').read()
    m = re.search(r':root\s*\{[^}]*\}', t)
    print('════', name, '════')
    print(m.group(0)[:500] if m else 'нет :root')
    # ищем определение v-pulse
    m2 = re.search(r'@keyframes\s+v-pulse\s*\{[^}]*\}', t)
    print('v-pulse:', m2.group(0) if m2 else 'нет')
    print()
