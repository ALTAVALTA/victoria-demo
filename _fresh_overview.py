# -*- coding: utf-8 -*-
"""Обзор свежего файла нейронки + сравнение с _deploy."""
import io
import re
import glob
import os

# найти свежий файл
files = [f for f in glob.glob(r'landings/victoria/*.html') if os.path.getmtime(f) > 0]
fresh = max(files, key=os.path.getmtime)
print('FRESH:', os.path.basename(fresh), os.path.getsize(fresh))

data = io.open(fresh, encoding='utf-8').read()

def clean(x):
    return re.sub(r'<[^>]+>', '', x).strip()

out = []
out.append('ФАЙЛ: %s (%d байт)' % (os.path.basename(fresh), os.path.getsize(fresh)))
out.append('')
out.append('=== H1 ===')
m = re.search(r'<h1[^>]*>(.*?)</h1>', data, re.S)
out.append('  ' + (clean(m.group(1)) if m else 'нет'))
out.append('')
out.append('=== H2 СЕКЦИИ ===')
for h in re.findall(r'<h2[^>]*>(.*?)</h2>', data, re.S):
    out.append('  * ' + clean(h)[:100])
out.append('')
out.append('=== H3 (карточки) ===')
for h in re.findall(r'<h3[^>]*>(.*?)</h3>', data, re.S)[:35]:
    out.append('  * ' + clean(h)[:80])
out.append('')
out.append('=== CTA/кнопки ===')
for m in re.finditer(r'<button[^>]*>.*?</button>', data, re.S):
    out.append('  * ' + clean(m.group(0))[:70])
out.append('')
out.append('=== data-open-form ===')
out.append('  count: %d' % len(re.findall(r'data-open-form', data)))
out.append('=== форма/запись ===')
out.append('  bookForm: %s' % ('bookForm' in data))
out.append('  фраза "записаться": %s' % ('аписаться' in data))
out.append('=== шрифты ===')
out.append('  @font-face: %d' % len(re.findall(r'@font-face', data)))
out.append('  google fonts: %s' % bool(re.findall(r'fonts\.googleapis', data)))
out.append('  font-display: %s' % (re.search(r'--font-display:([^;]+)', data).group(1).strip() if re.search(r'--font-display:([^;]+)', data) else 'нет'))
out.append('=== палитра ===')
m = re.search(r':root\s*\{([^}]*)\}', data)
if m:
    out.append('  ' + m.group(1).strip()[:300])

io.open(r'landings/victoria/_deploy/_fresh_report.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written')
