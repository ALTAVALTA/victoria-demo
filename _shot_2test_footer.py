# -*- coding: utf-8 -*-
"""Скрин футера V2 (2test_demo) — проверка пульсации подписи."""
import http.server, socketserver, threading, subprocess, os, sys, time
sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo'
OUT = r'C:\Users\PORTAL\.openclaw\workspace\screenshots\desktop_2test_footer.png'
PORT = 8933

handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(*a, directory=ROOT, **kw)
httpd = socketserver.TCPServer(('127.0.0.1', PORT), handler)
th = threading.Thread(target=httpd.serve_forever, daemon=True)
th.start()

chrome = None
try:
    time.sleep(1)
    # скриншот всей страницы, потом обрежем низ? нет — Chrome умеет window-size; сделаем полный и проверим футер вручную
    chrome = subprocess.Popen([
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        '--headless=new', '--disable-gpu', '--hide-scrollbars',
        '--window-size=1280,8000',
        '--screenshot=' + OUT,
        f'http://127.0.0.1:{PORT}/',
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    chrome.wait(timeout=90)
    print('shot done:', OUT, os.path.getsize(OUT) if os.path.exists(OUT) else 'MISSING')
finally:
    if chrome and chrome.poll() is None:
        chrome.kill()
    httpd.shutdown()
