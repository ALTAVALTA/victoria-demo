# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Сверим: у V1/V2 одинаковый brand-эффект, и в _deploy_polnaya (задеплоенная) тоже
files = {
 'V1 src': r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html',
 'V2 src': r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html',
 'V1 deploy': r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\_deploy_polnaya\index.html',
}
for name, p in files.items():
    try:
        t = io.open(p, encoding='utf-8').read()
    except Exception as e:
        print(name, 'ERR', e); continue
    m = re.search(r'\.brand-core\{[^}]*\}', t)
    has_breathe = 'v-breathe' in t
    # нейронкин opacity v-pulse (не тронут)
    m_op = re.search(r'@keyframes v-pulse\{0%,100%\{opacity:1\}', t)
    print(f'{name}: brand-core={m.group(0) if m else "НЕТ"} | v-breathe={has_breathe} | нейронкин v-pulse opacity={bool(m_op)}')
