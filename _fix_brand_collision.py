# -*- coding: utf-8 -*-
"""Фикс коллизии .brand-name:
1. Футерная подпись получает отдельный класс .sig-name (вместо .brand-name)
2. .brand-name возвращается к A-стилю (22px Georgia pine) — для шапки
3. .brand-name b (лишнее для шапки) → .sig-name b
4. .brand-core остаётся (V в подписи)
"""
import io
import re

PATH = r'landings/victoria/_deploy/index.html'
data = io.open(PATH, encoding='utf-8').read()
orig = data

# --- 1. HTML: футерная подпись: span.brand-name -> span.sig-name ---
old_sig = '<span class="brand-name"><b>A</b><b>L</b><b>T</b><b>A</b><b class="brand-core">V</b><b>A</b><b>L</b><b>T</b><b>A</b></span>'
assert data.count(old_sig) == 1, 'footer sig span not found'
new_sig = '<span class="sig-name"><b>A</b><b>L</b><b>T</b><b>A</b><b class="brand-core">V</b><b>A</b><b>L</b><b>T</b><b>A</b></span>'
data = data.replace(old_sig, new_sig)

# --- 2. CSS: .brand-name -> шапка (A-стиль) ---
old_css = ".brand-name{display:inline-flex;color:#d8d2c2;font-family:'Jost',sans-serif;font-size:12px;font-weight:700;gap:.08em;text-transform:uppercase;line-height:1}"
assert data.count(old_css) == 2, 'brand-name css count %d' % data.count(old_css)
new_css = ".brand-name{font-family:var(--font-display);font-size:22px;color:var(--pine);line-height:1}"
data = data.replace(old_css, new_css)

# --- 3. CSS: .brand-name b -> .sig-name b (подпись) ---
old_b = ".brand-name b{font-weight:inherit}"
assert data.count(old_b) == 2, 'brand-name b css count %d' % data.count(old_b)
new_b = ".sig-name{display:inline-flex;color:#d8d2c2;font-family:'Jost',sans-serif;font-size:12px;font-weight:700;gap:.08em;text-transform:uppercase;line-height:1}\n.brand-name b,.sig-name b{font-weight:inherit}"
data = data.replace(old_b, new_b)

io.open(PATH, 'w', encoding='utf-8').write(data)
print('OK, delta:', len(data) - len(orig))
