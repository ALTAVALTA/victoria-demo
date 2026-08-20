# -*- coding: utf-8 -*-
"""Фикс: лишний </div> после селекта услуг (строка 769)."""
import io

data = io.open('index.html', encoding='utf-8').read()
old = '</select>\n        </div></div>\n        <div class="field">\n          <label for="fDate">'
assert data.count(old) == 1, 'pattern not found: %d' % data.count(old)
new = '</select>\n        </div>\n        <div class="field">\n          <label for="fDate">'
data = data.replace(old, new)
io.open('index.html', 'w', encoding='utf-8').write(data)
print('fixed')
