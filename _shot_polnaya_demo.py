# -*- coding: utf-8 -*-
"""Скриншот polnaya-demo (локально) — headless Chrome, полная страница."""
import http.server, socketserver, threading, subprocess, os, sys, time
sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\_deploy_polnaya'
OUT = r'C:\Users\PORTAL\.openclaw\workspace\screenshots\desktop_polnaya_demo.png'
PORT = 8931

os.makedirs(os.path.dirname(OUT), exist_ok=True)

handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(*a, directory=ROOT, **kw)
httpd = socketserver.TCPServer(('127.0.0.1', PORT), handler)
th = threading.Thread(target=httpd.serve_forever, daemon=True)
th.start()

chrome = None
try:
    time.sleep(1)
    chrome = subprocess.Popen([
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        '--headless=new', '--disable-gpu', '--hide-scrollbars',
        '--window-size=1280,8000',
        '--screenshot=' + OUT,
        f'http://127.0.0.1:{PORT}/',
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    chrome.wait(timeout=90)
    print('shot done:', OUT, os.path.getsize(OUT), 'bytes' if os.path.exists(OUT) else 'MISSING')
finally:
    if chrome and chrome.poll() is None:
        chrome.kill()
    httpd.shutdown()
