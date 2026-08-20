# -*- coding: utf-8 -*-
"""Скриншот лендинга через headless Chrome (без browser-тула, с чистым профилем)."""
import glob
import os
import subprocess
import sys
import tempfile
import time

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(CHROME):
    CHROME = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
if not os.path.exists(CHROME):
    print('NO CHROME'); sys.exit(1)

out = os.path.abspath('_shot_headless.png')
prof = tempfile.mkdtemp(prefix='chr_headless_')
url = 'https://altavalta.github.io/victoria-demo/?nocache=%d' % int(time.time())

cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
       '--user-data-dir=' + prof, '--window-size=1440,2400',
       '--screenshot=' + out, url]
print('running:', ' '.join(cmd[:6]), '...')
r = subprocess.run(cmd, capture_output=True, timeout=90)
print('rc:', r.returncode)
print(r.stderr.decode('utf-8', 'replace')[-800:])
if os.path.exists(out):
    print('shot:', out, os.path.getsize(out), 'bytes')
else:
    print('NO SHOT')
