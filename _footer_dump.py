# -*- coding: utf-8 -*-
"""Футер: как выглядит подпись ALTAVALTA сейчас (классы)."""
import io
import re

cur = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

# footer
m = re.search(r'<footer[^>]*>.*?</footer>', cur, re.S)
if m:
    print('=== FOOTER ===')
    print(m.group(0)[:2500])
else:
    print('NO FOOTER')

print()
# все CSS с brand-
for mm in re.finditer(r'\.brand[^{}]*\{[^}]*\}', cur):
    print(mm.group(0)[:220])
    print('---')
