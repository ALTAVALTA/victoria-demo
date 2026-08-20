# -*- coding: utf-8 -*-
"""DOM-проверка шрифтов через headless Chrome (executablePath + CDP, без browser-тула)."""
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(CHROME):
    CHROME = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

prof = tempfile.mkdtemp(prefix='chr_cdp_')
proc = subprocess.Popen(
    [CHROME, '--headless=new', '--disable-gpu', '--remote-debugging-port=9333',
     '--remote-allow-origins=*', '--user-data-dir=' + prof, 'about:blank'],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def cdp(ws, method, params=None):
    req = json.dumps({'id': 1, 'method': method, 'params': params or {}})
    ws.send(req.encode())
    while True:
        msg = json.loads(ws.recv())
        if msg.get('id') == 1:
            return msg.get('result', {})

try:
    time.sleep(3)
    # список вкладок
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9333/json', timeout=5).read())
    page = tabs[0]
    ws_url = page['webSocketDebuggerUrl']
    import websocket  # может не быть; fallback ниже
except Exception as e:
    print('no websocket lib:', e)
    proc.terminate()
    sys.exit(1)

# Попробуем через websocket-client, если есть
try:
    import websocket
except ImportError:
    print('websocket-client not installed; using raw socket fallback')
    websocket = None

if websocket:
    ws = websocket.create_connection(ws_url, timeout=15)
    cdp(ws, 'Page.enable')
    cdp(ws, 'Runtime.enable')
    cdp(ws, 'Page.navigate', {'url': 'https://altavalta.github.io/victoria-demo/?domcheck=%d' % int(time.time())})
    time.sleep(6)
    expr = """
    (function(){
      var h1 = document.querySelector('h1');
      var h2 = document.querySelector('h2');
      function info(el){
        if(!el) return null;
        var cs = getComputedStyle(el);
        var ff = cs.fontFamily;
        var ok = document.fonts.check('600 40px Georgia, serif');
        var loaded = [];
        document.fonts.forEach(function(f){loaded.push(f.family + ' ' + f.weight + ' status=' + f.status);});
        return {fontFamily: ff, fontSize: cs.fontSize, fontWeight: cs.fontWeight,
                jostLoaded: document.fonts.check('600 12px Jost'),
                georgiaAvailable: ok, fontsStatus: loaded.slice(0,8)};
      }
      return {h1: info(h1), h2: info(h2)};
    })()
    """
    res = cdp(ws, 'Runtime.evaluate', {'expression': expr, 'returnByValue': True})
    print(json.dumps(res.get('result', {}).get('value', res), ensure_ascii=False, indent=1))
    ws.close()
proc.terminate()
