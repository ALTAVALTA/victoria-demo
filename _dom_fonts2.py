# -*- coding: utf-8 -*-
"""DOM-проверка шрифтов: Chrome --dump-dom + JS в URL? Нет — dump-dom отдаёт HTML после JS, но computed style не увидим.
Лучше: page.evaluate через CDP с правильным Origin."""
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
if not os.path.exists(CHROME):
    print('NO CHROME'); sys.exit(1)

prof = tempfile.mkdtemp(prefix='chr_cdp2_')
proc = subprocess.Popen(
    [CHROME, '--headless=new', '--disable-gpu', '--remote-debugging-port=9344',
     '--remote-allow-origins=*', '--user-data-dir=' + prof, 'about:blank'],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    time.sleep(3)
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9344/json', timeout=5).read())
    ws_url = tabs[0]['webSocketDebuggerUrl']
    import websocket
    ws = websocket.create_connection(ws_url, timeout=20, origin='http://127.0.0.1:9344')
    req_id = 0
    def cdp(method, params=None):
        global req_id
        req_id += 1
        ws.send(json.dumps({'id': req_id, 'method': method, 'params': params or {}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get('id') == req_id:
                return msg.get('result', {})
    cdp('Page.enable')
    cdp('Runtime.enable')
    cdp('Page.navigate', {'url': 'https://altavalta.github.io/victoria-demo/?domcheck=%d' % int(time.time())})
    time.sleep(7)
    expr = """
    (function(){
      var out = {fontsLoaded: [], h1: null, h2: null, signature: null};
      document.fonts.forEach(function(f){out.fontsLoaded.push(f.family+' w'+f.weight+' '+f.status);});
      function info(el){
        if(!el) return null;
        var cs = getComputedStyle(el);
        return {family: cs.fontFamily, size: cs.fontSize, weight: cs.fontWeight};
      }
      out.h1 = info(document.querySelector('h1'));
      out.h2 = info(document.querySelector('h2'));
      var sig = document.querySelector('.footer-brand, .brand-sign');
      out.signature = info(sig);
      return out;
    })()
    """
    res = cdp('Runtime.evaluate', {'expression': expr, 'returnByValue': True})
    print(json.dumps(res.get('result', {}).get('value', res), ensure_ascii=False, indent=1))
    ws.close()
finally:
    proc.terminate()
