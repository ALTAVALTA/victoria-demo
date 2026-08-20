# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for name, p in [('V1', r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'),
                ('V2', r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html')]:
    t = io.open(p, encoding='utf-8').read()
    # найдём v-pulse-av / v-pulse и .brand-core animation
    m_anim = re.search(r'\.brand-core\{[^}]*\}', t)
    m_kf = re.search(r'@keyframes\s+v-pulse[\w-]*\s*\{[^}]*\}', t)
    print('====', name, '====')
    print('brand-core:', m_anim.group(0) if m_anim else 'НЕТ')
    print('keyframes:', m_kf.group(0)[:150] if m_kf else 'НЕТ')
    print('свечение (text-shadow в kf):', 'text-shadow' in (m_kf.group(0) if m_kf else ''))
    print()
