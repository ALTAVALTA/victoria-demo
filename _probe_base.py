# -*- coding: utf-8 -*-
"""Накатить правки 14.08 на свежую базу remote (ac0214d)."""
import io, sys

PATH = 'index.html'
t = io.open(PATH, encoding='utf-8').read()
orig = t

# ---------- 1. CSS: категория над чипами ----------
css_old = '.chips-group{display:flex;flex-wrap:wrap;gap:8px;align-items:center}'
css_new = ('.chips-group{display:flex;flex-direction:column;gap:8px;align-items:stretch;'
           'margin-bottom:10px}.chips-group:last-of-type{margin-bottom:0}'
           '.chips-cat{font-size:11px;font-weight:700;letter-spacing:.08em;'
           'text-transform:uppercase;color:var(--muted);margin-bottom:2px}.chips-cat::after{content:":"}')
if css_old in t:
    t = t.replace(css_old, css_new)
    print('CSS chips: OK')
else:
    print('CSS chips: NOT FOUND (ищу варианты)')
    # вариант: могли уже поправить
    for v in ['.chips-group{', '.chips-cat{']:
        import re
        for m in re.finditer(re.escape(v) + r'[^{]*\{[^}]*\}', t):
            print('   found:', m.group(0)[:120])

# ---------- 2. Телефон: атрибуты ----------
phone_old = '<input id="fPhone" name="phone" type="tel" placeholder="+7 (___) ___-__-__" required>'
phone_new = ('<input id="fPhone" name="phone" type="tel" inputmode="tel" autocomplete="tel" '
             'placeholder="+7 (___) ___-__-__" maxlength="18" required>')
if phone_old in t:
    t = t.replace(phone_old, phone_new)
    print('Phone attrs: OK')
else:
    print('Phone attrs: NOT FOUND (ищу текущий вид)')
    import re
    m = re.search(r'<input id="fPhone"[^>]*>', t)
    print('   current:', m.group(0) if m else 'none')

# ---------- 3. JS: валидация строгая ----------
# сначала посмотрим текущий блок валидации
import re
m = re.search(r"form\.addEventListener\('submit'[\s\S]*?e\.preventDefault\(\);[\s\S]{0,900}?var payload=", t)
if m:
    print('\n--- текущий submit-блок (начало) ---')
    print(m.group(0)[:1000])

io.open('_base_probe.txt', 'w', encoding='utf-8').write(t)
print('\nprobe saved, len:', len(t))
