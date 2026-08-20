# -*- coding: utf-8 -*-
"""Ожидание CDN + скриншот live (шапка с золотой подписью)."""
import os
import subprocess
import sys
import tempfile
import time
import urllib.request

def live_has_sub():
    req = urllib.request.Request('https://altavalta.github.io/victoria-demo/',
                                 headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    raw = urllib.request.urlopen(req, timeout=30).read()
    return b'--gold-deep' in raw and b'brand-sub' in raw, len(raw)

for i in range(8):
    ok, size = live_has_sub()
    print('try %d: brand-sub+gold=%s bytes=%d' % (i + 1, ok, size))
    if ok:
        break
    time.sleep(20)

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(CHROME):
    CHROME = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
out = os.path.abspath('_shot_live_header2.png')
prof = tempfile.mkdtemp(prefix='chr_hdr2_')
url = 'https://altavalta.github.io/victoria-demo/?hdr2=%d' % int(time.time())
cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
       '--user-data-dir=' + prof, '--window-size=1440,700',
       '--screenshot=' + out, url]
r = subprocess.run(cmd, capture_output=True, timeout=90)
print('shot rc:', r.returncode, os.path.getsize(out) if os.path.exists(out) else 'NO SHOT')
