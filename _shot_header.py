# -*- coding: utf-8 -*-
"""Скриншот с акцентом на шапку: хедер + первый заголовок (h1), 1440x1000."""
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

out = os.path.abspath('_shot_header.png')
prof = tempfile.mkdtemp(prefix='chr_hdr_')
url = 'https://altavalta.github.io/victoria-demo/?hdr=%d' % int(time.time())

cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
       '--user-data-dir=' + prof, '--window-size=1440,1100',
       '--screenshot=' + out, url]
r = subprocess.run(cmd, capture_output=True, timeout=90)
print('rc:', r.returncode)
if os.path.exists(out):
    print('shot:', out, os.path.getsize(out))
