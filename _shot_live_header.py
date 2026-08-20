# -*- coding: utf-8 -*-
"""Скриншот live после пуша (шапка) + ожидание CDN."""
import os
import subprocess
import sys
import tempfile
import time
import urllib.request

# ждём CDN: проверим наличие .sig-name в live
def live_has_sig():
    req = urllib.request.Request('https://altavalta.github.io/victoria-demo/',
                                 headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    raw = urllib.request.urlopen(req, timeout=30).read()
    return b'sig-name' in raw, len(raw)

for i in range(8):
    ok, size = live_has_sig()
    print('try %d: sig-name=%s bytes=%d' % (i + 1, ok, size))
    if ok:
        break
    time.sleep(20)

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(CHROME):
    CHROME = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
out = os.path.abspath('_shot_header_live.png')
prof = tempfile.mkdtemp(prefix='chr_hdrl_')
url = 'https://altavalta.github.io/victoria-demo/?hdrl=%d' % int(time.time())
cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
       '--user-data-dir=' + prof, '--window-size=1440,900',
       '--screenshot=' + out, url]
r = subprocess.run(cmd, capture_output=True, timeout=90)
print('shot rc:', r.returncode, os.path.getsize(out) if os.path.exists(out) else 'NO SHOT')
