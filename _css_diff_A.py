# -*- coding: utf-8 -*-
"""Полный diff стилевых правил A vs _deploy (нормализованных)."""
import io
import re

def load(p):
    return io.open(p, encoding='utf-8').read()

def css_rules(d):
    """Правила вида селектор { ... } — только из <style>."""
    m = re.search(r'<style>(.*?)</style>', d, re.S)
    css = m.group(1) if m else d
    rules = {}
    # убираем комментарии
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    for mm in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        sel = ' '.join(mm.group(1).split())
        body = ' '.join(mm.group(2).split())
        rules[sel] = body
    return rules

a = load(r'landings/victoria/A version.html')
cur = load(r'landings/victoria/_deploy/index.html')
ra, rc = css_rules(a), css_rules(cur)

print('A rules:', len(ra), '| cur rules:', len(rc))
print()
# В cur есть правила, которых нет в A ИЛИ значения отличаются
only_cur = {k: v for k, v in rc.items() if k not in ra}
only_a = {k: v for k, v in ra.items() if k not in rc}
diff = {k: (ra[k], rc[k]) for k in ra if k in rc and ra[k] != rc[k]}

print('=== правил только в _deploy: %d ===' % len(only_cur))
for k, v in list(only_cur.items())[:40]:
    print(' +', k[:90], '=>', v[:100])
print()
print('=== правил только в A: %d ===' % len(only_a))
for k, v in list(only_a.items())[:40]:
    print(' -', k[:90], '=>', v[:100])
print()
print('=== отличаются значения (A vs cur): %d ===' % len(diff))
for k, (va, vc) in list(diff.items())[:40]:
    print(' *', k[:80])
    print('   A  :', va[:130])
    print('   cur:', vc[:130])
