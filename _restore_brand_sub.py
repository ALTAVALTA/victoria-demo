# -*- coding: utf-8 -*-
"""Восстановление .brand-sub: возвращаем правило в стиле А-версии (золотой)."""
import io
import re

PATH = r'landings/victoria/_deploy/index.html'
data = io.open(PATH, encoding='utf-8').read()

# Проверим: HTML шапки — есть ли span.brand-sub
print('brand-sub в HTML:', '<span class="brand-sub">' in data)

# Куда вставить: сразу после .brand-name правила (второй style)
# Ищем текущее .brand-name правило
m = re.search(r'\.brand-name\{font-family:var\(--font-display\);font-size:22px;color:var\(--pine\);line-height:1\}', data)
assert m, '.brand-name rule not found'
rule = '.brand-name{font-family:var(--font-display);font-size:22px;color:var(--pine);line-height:1}\n.brand-sub{font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-deep)}'
data = data.replace(m.group(0), rule)

io.open(PATH, 'w', encoding='utf-8').write(data)
print('OK')
