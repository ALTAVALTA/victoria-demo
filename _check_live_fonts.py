# -*- coding: utf-8 -*-
"""Проверка live: шрифтовые файлы + заголовочные правила."""
import io
import re
import urllib.request

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    return urllib.request.urlopen(req, timeout=30).read()

base = 'https://altavalta.github.io/victoria-demo/'
raw = fetch(base)
print('index bytes:', len(raw))
print('jost-600 ref:', b'fonts/jost-600.woff2' in raw)
print('jost-700 ref:', b'fonts/jost-700.woff2' in raw)

for f in ('fonts/jost-600.woff2', 'fonts/jost-700.woff2'):
    try:
        fb = fetch(base + f)
        print(f, '-> OK', len(fb), 'bytes, woff2?', fb[:4] == b'wOF2' or fb[:4].hex() == '774f4632')
    except Exception as e:
        print(f, '-> FAIL', e)

# заголовочное правило из live
data = raw.decode('utf-8', 'replace')
m = re.search(r'h1,h2,h3[^{]*\{[^}]*\}', data)
print('h rule:', m.group(0)[:200] if m else 'NOT FOUND')
