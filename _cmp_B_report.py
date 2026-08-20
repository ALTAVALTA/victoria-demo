# -*- coding: utf-8 -*-
"""Сравнение _deploy vs B version: полный отчёт в файл."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

cur = load(r'landings/victoria/_deploy/index.html')
b = load(r'landings/victoria/_archive_B/B version.html')

def clean(x):
    return re.sub(r'<[^>]+>', '', x).strip()

def h2s(d):
    return [clean(x) for x in re.findall(r'<h2[^>]*>(.*?)</h2>', d, re.S)]
def h3s(d):
    return [clean(x) for x in re.findall(r'<h3[^>]*>(.*?)</h3>', d, re.S)]

out = []
out.append('=== РАЗМЕРЫ ===')
out.append('_deploy: %d chars' % len(cur))
out.append('B      : %d chars' % len(b))

out.append('')
out.append('=== H2 СЕКЦИИ _deploy ===')
for h in h2s(cur):
    out.append('  * ' + h[:90])
out.append('')
out.append('=== H2 СЕКЦИИ B ===')
for h in h2s(b):
    out.append('  * ' + h[:90])

out.append('')
out.append('=== H3 _deploy ===')
for h in h3s(cur)[:30]:
    out.append('  * ' + h[:70])
out.append('')
out.append('=== H3 B ===')
for h in h3s(b)[:30]:
    out.append('  * ' + h[:70])

# CTA/кнопки
out.append('')
out.append('=== CTA кнопки _deploy ===')
for m in re.finditer(r'<button[^>]*data-open-form[^>]*>.*?</button>', cur, re.S):
    out.append('  * ' + clean(m.group(0))[:80])
out.append('=== CTA кнопки B ===')
for m in re.finditer(r'<button[^>]*data-open-form[^>]*>.*?</button>', b, re.S):
    out.append('  * ' + clean(m.group(0))[:80])
# ссылки Записаться
out.append('')
out.append('=== data-open-form кнопки _deploy ===')
out.append(str(len(re.findall(r'data-open-form', cur))))
out.append('=== data-open-form кнопки B ===')
out.append(str(len(re.findall(r'data-open-form', b))))

io.open(r'landings/victoria/_deploy/_B_report.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written')
