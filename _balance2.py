# -*- coding: utf-8 -*-
"""Баланс тегов после фикса."""
import io
import re

data = io.open(r'index.html', encoding='utf-8').read()
for tag in ('div', 'form', 'select', 'button', 'label', 'span', 'b', 'a'):
    opens = len(re.findall(r'<%s[\s>]' % tag, data))
    closes = len(re.findall(r'</%s>' % tag, data))
    status = 'OK' if opens == closes else 'MISMATCH'
    print('%s: %d/%d %s' % (tag, opens, closes, status))
