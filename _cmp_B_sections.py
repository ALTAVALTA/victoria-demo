# -*- coding: utf-8 -*-
"""Сравнение _deploy/index.html (наша доведённая) с B version.html (вторая нейронка)."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

cur = load(r'landings/victoria/_deploy/index.html')
b = load(r'landings/victoria/_archive_B/B version.html')

print('=== РАЗМЕРЫ ===')
print('_deploy:', len(cur), 'chars')
print('B      :', len(b), 'chars')

def h2s(d):
    return re.findall(r'<h2[^>]*>(.*?)</h2>', d, re.S)
def h3s(d):
    return re.findall(r'<h3[^>]*>(.*?)</h3>', d, re.S)

def clean(x):
    return re.sub(r'<[^>]+>', '', x).strip()

print()
print('=== H2 СЕКЦИИ в _deploy ===')
for h in h2s(cur):
    print('  *', clean(h)[:90])
print()
print('=== H2 СЕКЦИИ в B ===')
for h in h2s(b):
    print('  *', clean(h)[:90])

print()
print('=== H3 в _deploy (карточки) ===')
for h in h3s(cur)[:30]:
    print('  *', clean(h)[:70])
print()
print('=== H3 в B (карточки) ===')
for h in h3s(b)[:30]:
    print('  *', clean(h)[:70])
