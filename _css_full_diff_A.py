# -*- coding: utf-8 -*-
"""Полный diff: ВЕСЬ CSS _deploy (оба style) vs A version."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

def all_css(d):
    blocks = re.findall(r'<style[^>]*>(.*?)</style>', d, re.S)
    return '\n'.join(blocks)

def rules(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out = {}
    for mm in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        sel = ' '.join(mm.group(1).split())
        body = ' '.join(mm.group(2).split())
        out[sel] = body
    return out

a = load(r'landings/victoria/A version.html')
cur = load(r'landings/victoria/_deploy/index.html')
ra, rc = rules(all_css(a)), rules(all_css(cur))

print('A rules:', len(ra), '| cur rules:', len(rc))
only_a = {k: v for k, v in ra.items() if k not in rc}
only_cur = {k: v for k, v in rc.items() if k not in ra}
diff = {k: (ra[k], rc[k]) for k in ra if k in rc and ra[k] != rc[k]}
print()
print('=== только в A: %d ===' % len(only_a))
for k, v in sorted(only_a.items())[:30]:
    print(' -', k[:90], '=>', v[:110])
print()
print('=== только в _deploy: %d ===' % len(only_cur))
for k, v in sorted(only_cur.items())[:30]:
    print(' +', k[:90], '=>', v[:110])
print()
print('=== отличаются: %d ===' % len(diff))
for k, (va, vc) in sorted(diff.items())[:30]:
    print(' *', k[:90])
    print('   A  :', va[:140])
    print('   cur:', vc[:140])
