# -*- coding: utf-8 -*-
"""Проверка live: мультивыбор (selectedServices в live-версии)."""
import time
import urllib.request

def live_has():
    req = urllib.request.Request('https://altavalta.github.io/victoria-demo/',
                                 headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    raw = urllib.request.urlopen(req, timeout=30).read()
    return b'selectedServices=[]' in raw, len(raw)

for i in range(8):
    ok, size = live_has()
    print('try %d: multiselect=%s bytes=%d' % (i + 1, ok, size))
    if ok:
        print('LIVE OK')
        break
    time.sleep(20)
