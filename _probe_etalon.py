# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'
t = io.open(p, encoding='utf-8').read()

# 1. ПЛАШКА
print('=== ПЛАШКА (HTML) ===')
m = re.search(r'<div class="demo-ribbon".*?</div>\s*</div>', t, re.S)
print(m.group(0)[:1200] if m else 'нет')
print()
print('=== ПЛАШКА (CSS) ===')
m = re.search(r'\.demo-ribbon\{[^}]*\}', t)
print(m.group(0) if m else 'нет')
for m2 in re.finditer(r'\.demo-[a-z-]+\{[^}]*\}', t):
    print(m2.group(0))
