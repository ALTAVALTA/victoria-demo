# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for name, p in [('V1 polnaya', r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'),
                ('V2 2test', r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html')]:
    t = io.open(p, encoding='utf-8').read()
    print('════════', name, '════════')
    # все keyframes
    kfs = re.findall(r'@keyframes\s+([\w-]+)\s*\{', t)
    print('keyframes:', kfs)
    # CSS для .brand-core
    for m in re.finditer(r'\.brand-core[^{]*\{[^}]*\}', t):
        print('brand-core CSS:', m.group(0))
    # все анимации, применённые к b внутри sig-name или к brand-core
    for m in re.finditer(r'\.sig-name[^{]*\{[^}]*\}|\.sig-name b[^{]*\{[^}]*\}|\.brand-link[^{]*\{[^}]*\}', t):
        print('sig CSS:', m.group(0))
    # есть ли у нейронки глобальный b { animation } или b { color }?
    for m in re.finditer(r'(?:^|[\s}])b\s*\{[^}]*\}', t):
        print('глобальный b:', m.group(0)[:120])
    # вхождения v-pulse
    print('v-pulse вхождений:', len(re.findall(r'v-pulse', t)))
    # порядок: сколько <style> блоков, где v-pulse определён
    for i, m in enumerate(re.finditer(r'<style[^>]*>.*?</style>', t, re.S)):
        blk = m.group(0)
        if 'v-pulse' in blk or 'brand-core' in blk:
            print(f'  style#{i}: v-pulse={blk.count("v-pulse")} brand-core={blk.count("brand-core")} first100={blk[6:80]!r}')
    print()
