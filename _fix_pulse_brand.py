# -*- coding: utf-8 -*-
"""Бренд-эффект подписи v2: ПУЛЬС (удар света + пауза) вместо дыхания.
Логика Кэпа: подпись маленькая -> её работа сигналить, «даже будучи маленькими — заметны»."""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

PULSE = '@keyframes v-pulse-brand{0%,68%{color:var(--gold);text-shadow:0 0 0 rgba(245,217,168,0)}85%{color:#f7e3b5;text-shadow:0 0 18px rgba(245,217,168,.9),0 0 42px rgba(245,217,168,.45)}100%{color:var(--gold);text-shadow:0 0 0 rgba(245,217,168,0)}}'

def apply(p):
    t = io.open(p, encoding='utf-8').read()
    # заменить v-breathe keyframes (дышащий) на пульс
    m = re.search(r'@keyframes\s+v-breathe\{[^}]*\{[^}]*\}[^}]*\{[^}]*\}[^}]*\}', t)
    if not m:
        # попробуем шире: от @keyframes v-breathe до конца блока (сбалансированно)
        start = t.find('@keyframes v-breathe')
        if start != -1:
            i = t.find('{', start)
            depth = 0
            while i < len(t):
                if t[i] == '{': depth += 1
                elif t[i] == '}':
                    depth -= 1
                    if depth == 0:
                        m = None
                        t = t[:start] + PULSE + t[i+1:]
                        break
                i += 1
    else:
        t = t.replace(m.group(0), PULSE, 1)

    # переключить .brand-core на пульс
    m2 = re.search(r'\.brand-core\{color:var\(--gold\);animation:v-breathe [^}]*\}', t)
    if m2:
        t = t.replace(m2.group(0), '.brand-core{color:var(--gold);animation:v-pulse-brand 2.8s ease-in-out infinite}', 1)

    io.open(p, 'w', encoding='utf-8').write(t)
    m3 = re.search(r'\.brand-core\{[^}]*\}', t)
    print(p.split('\\')[-2] + '/' + p.split('\\')[-1])
    print('  brand-core:', m3.group(0) if m3 else 'НЕТ')
    print('  v-pulse-brand:', t.count('v-pulse-brand'), '| v-breathe:', t.count('v-breathe'))

apply(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html')
apply(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html')
print('OK')
