# -*- coding: utf-8 -*-
"""Полное сравнение CSS правил шапки: A vs _deploy."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

def all_rules(d):
    blocks = re.findall(r'<style[^>]*>(.*?)</style>', d, re.S)
    css = '\n'.join(blocks)
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out = {}
    for mm in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        sel = ' '.join(mm.group(1).split())
        body = ' '.join(mm.group(2).split())
        out[sel] = body
    return out

a = load(r'landings/victoria/A version.html')
cur = load(r'landings/victoria/_deploy/index.html')
ra, rc = all_rules(a), all_rules(cur)

# Селекторы шапки
hdr_sels = [s for s in ra if any(x in s for x in
            ('.topbar', '.brand', '.brand-mark', '.brand-name', '.brand-sub', 'header', '.topnav', '.topbar-cta', '.topbar-phone'))]

print('=== Селекторы шапки в A, и их статус в _deploy ===')
for s in sorted(hdr_sels):
    if s not in rc:
        print('  MISSING:', s[:80], '=>', ra[s][:100])
    elif ra[s] != rc[s]:
        print('  DIFF:', s[:80])
        print('    A  :', ra[s][:130])
        print('    cur:', rc[s][:130])
    else:
        print('  ok  :', s[:80])
