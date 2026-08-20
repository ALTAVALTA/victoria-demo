# -*- coding: utf-8 -*-
"""Проверка live после пуша чипов."""
import io
import time
import urllib.request

def fetch(url):
    req = urllib.request.Request(url,
        headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    return urllib.request.urlopen(req, timeout=30).read()

for attempt in range(6):
    raw = fetch('https://altavalta.github.io/victoria-demo/')
    has_chips = b'id="serviceChips"' in raw
    has_slots = b'<option>08:30</option>' in raw
    has_old_time = b'type="time"' in raw
    print('try %d: chips=%s slots=%s old_time_input=%s bytes=%d' % (
        attempt + 1, has_chips, has_slots, has_old_time, len(raw)))
    if has_chips and has_slots and not has_old_time:
        print('LIVE OK')
        break
    time.sleep(20)
