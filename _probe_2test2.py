# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2TEST_TOJE_SAMOE_POLNAYA.html'
t = io.open(p, encoding='utf-8').read()

print('=== ВСЕ PHOTO-маркеры (файл: имя) ===')
for m in re.finditer(r'@@PHOTO:([^@]+)@@\s*файл:\s*([^\s|]+)', t):
    print(m.group(1).strip(), '->', m.group(2))

print()
print('=== img src (все) ===')
for m in re.finditer(r'<img[^>]+src="([^"]+)"', t):
    print(m.group(1))

print()
print('=== ОТЗЫВЫ в коде ===')
i = t.find('reviews')
print(t[i-100:i+1800].replace('\n', ' ')[:1900])
