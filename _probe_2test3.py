# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2TEST_TOJE_SAMOE_POLNAYA.html'
t = io.open(p, encoding='utf-8').read()

print('=== ДУБЛЬ victoria_photo26 ===')
for m in re.finditer(r'@@PHOTO:[^@]+@@\s*файл:\s*([^\s|]+)', t):
    pass
# найдём все вхождения 26
idxs = [m.start() for m in re.finditer(r'victoria_photo26', t)]
print('вхождений photo26:', len(idxs))
for i in idxs:
    print('...', t[i-90:i+40].replace('\n', ' '), '...')
    print()

print('=== БЛОК ОТЗЫВОВ (HTML) ===')
i = t.find('<section class="reviews"')
print(t[i:i+2600].replace('\n', ' ')[:2600])
