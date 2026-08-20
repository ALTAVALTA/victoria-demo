# -*- coding: utf-8 -*-
"""B version: как открывается форма, что с модалкой, контактами, футером."""
import io
import re

b = io.open(r'landings/victoria/_archive_B/B version.html', encoding='utf-8').read()

def clean(x):
    return re.sub(r'<[^>]+>', '', x).strip()

out = []
out.append('=== ФОРМА/МОДАЛКА в B ===')
out.append('bookForm: %s' % ('bookForm' in b))
out.append('id=modal: %s' % ('id="modal"' in b or "id='modal'" in b))
out.append('formSuccess: %s' % ('formSuccess' in b))
out.append('data-open-form: %d' % len(re.findall(r'data-open-form', b)))
out.append('href=#form / #book: %s' % re.findall(r'href="#[a-zA-Z]*form[a-zA-Z]*"', b)[:5])
out.append('onclick открыть: %s' % bool(re.search(r'onclick\s*=\s*["\']?[^"\']*open', b)))
# что за кнопки/ссылки с 'Записаться'/'запись'
out.append('')
out.append('=== ВСЕ ссылки/кнопки со словом запис ===')
for m in re.finditer(r'<(?:a|button)[^>]*>[^<]*(?:апис|Занять|Онлайн)[^<]*</(?:a|button)>', b, re.S | re.I):
    out.append('  * ' + clean(m.group(0))[:100])
out.append('')
out.append('=== ТЕЛЕФОН ===')
out.append('  tel:+: %s' % re.findall(r'tel:\+?[\d\s()-]+', b)[:3])
out.append('  +7 в тексте: %s' % re.findall(r'\+7[\s(]*\d{3}[\s)]*\d{3}[\s-]*\d{2}[\s-]*\d{2}', b)[:3])
out.append('')
out.append('=== АДРЕС ===')
for m in re.finditer(r'[^<>]{0,60}(?:Комсомольская|Калининград|центр)[^<>]{0,60}', b):
    t = m.group(0).strip()
    if len(t) > 8:
        out.append('  * ' + t[:120])
out.append('')
out.append('=== ФУТЕР ===')
m = re.search(r'<footer[^>]*>.*?</footer>', b, re.S)
out.append(m.group(0)[:800] if m else 'нет footer')
out.append('')
out.append('=== ЧАСЫ РАБОТЫ ===')
for m in re.finditer(r'[^<>]{0,50}(?:08:30|8:30|20:30|ежедневно|график)[^<>]{0,50}', b):
    out.append('  * ' + m.group(0).strip()[:110])

io.open(r'landings/victoria/_deploy/_B_deep.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written')
