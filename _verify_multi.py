# -*- coding: utf-8 -*-
"""Верификация мультивыбора."""
import io
import re

data = io.open(r'landings/victoria/_deploy/index.html', encoding='utf-8').read()

checks = {
    'toggle js': "c.classList.toggle('active')" in data,
    'selectedServices array': 'var selectedServices=[];' in data,
    'join comma': "serviceSelect.value=selectedServices.join(', ');" in data,
    'openModal add': 'selectedServices.indexOf(service)===-1' in data,
    'reset clears': 'selectedServices=[];chips.forEach' in data,
    'old single-select gone': 'chips.forEach(function(x){x.classList.remove(\'active\');});\n    c.classList.add' not in data,
}
for k, v in checks.items():
    print(('OK  ' if v else 'FAIL'), k)

# баланс
for tag in ('div', 'form', 'select', 'button', 'span', 'b'):
    o = len(re.findall(r'<%s[\s>]' % tag, data))
    c = len(re.findall(r'</%s>' % tag, data))
    if o != c:
        print('BALANCE FAIL', tag, o, c)
print('balance done')
