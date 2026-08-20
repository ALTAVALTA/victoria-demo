# -*- coding: utf-8 -*-
import sys, urllib.request, re
sys.stdout.reconfigure(encoding='utf-8')
urls = [
    'https://altavalta.github.io/victoria-demo/2test-demo/',
    'https://altavalta.github.io/victoria-demo/polnaya-demo/',
]
for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        r = urllib.request.urlopen(req, timeout=30)
        html = r.read().decode('utf-8', 'replace')
        print(u, '->', r.status, len(html), 'bytes | v-breathe:', 'v-breathe' in html, '| v-pulse-brand:', 'v-pulse-brand' in html)
    except Exception as e:
        print(u, 'ERR', e)
