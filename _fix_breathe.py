# -*- coding: utf-8 -*-
"""Бренд-эффект подписи: «дышащее свечение» (цвет -> свечение -> цвет) в V1 и V2.
Решение Кэпа 16.08: V дышит светом, не мигает прозрачностью."""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BREATHE = '@keyframes v-breathe{0%,100%{color:var(--gold);text-shadow:0 0 0 rgba(245,217,168,0)}50%{color:#f7e3b5;text-shadow:0 0 14px rgba(245,217,168,.85),0 0 34px rgba(245,217,168,.4)}}'

def apply(p):
    t = io.open(p, encoding='utf-8').read()
    changed = []

    # 1. заменить старые keyframes подписи (v-pulse светящийся / v-pulse-av)
    # светящийся v-pulse (V1): 0%,62%...94%
    m = re.search(r'@keyframes\s+v-pulse\{0%,62%\{color:var\(--gold\);text-shadow:none\}.*?\}', t)
    if m:
        t = t.replace(m.group(0), BREATHE, 1)
        changed.append('V1: v-pulse(светящийся) -> v-breathe')

    # v-pulse-av (V2, я добавил ранее)
    m = re.search(r'@keyframes\s+v-pulse-av\{0%,62%\{color:var\(--gold\);text-shadow:none\}.*?\}', t)
    if m:
        t = t.replace(m.group(0), BREATHE, 1)
        changed.append('V2: v-pulse-av -> v-breathe')

    # 2. переключить .brand-core animation на v-breathe
    m = re.search(r'\.brand-core\{color:var\(--gold\);animation:v-pulse[\w-]* [^}]*\}', t)
    if m:
        t = t.replace(m.group(0), '.brand-core{color:var(--gold);animation:v-breathe 3.4s ease-in-out infinite}', 1)
        changed.append('brand-core -> v-breathe 3.4s')

    io.open(p, 'w', encoding='utf-8').write(t)
    print(p.split('\\')[-2] + '/' + p.split('\\')[-1])
    for c in changed:
        print('  ', c)
    # контроль
    m2 = re.search(r'\.brand-core\{[^}]*\}', t)
    print('  brand-core теперь:', m2.group(0) if m2 else 'НЕТ')
    print('  v-breathe:', t.count('v-breathe'), 'вхождений')
    return len(changed)

n1 = apply(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html')
n2 = apply(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html')
print()
print('ИТОГ: V1 изменений =', n1, '| V2 изменений =', n2)
