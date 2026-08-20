# -*- coding: utf-8 -*-
import sys, urllib.request, re
sys.stdout.reconfigure(encoding='utf-8')
base = 'https://altavalta.github.io/victoria-demo/polnaya-demo/'
req = urllib.request.Request(base, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8')
imgs = re.findall(r'src="(img/PHOTO_[^"]+)"', html)
print('PHOTO imgs:', len(imgs), 'unique:', len(set(imgs)))
print('isDemoPath in code:', 'isDemoPath' in html)
for f in ['img/PHOTO_25.jpg', 'img/PHOTO_13.jpg', 'img/avatars/avatar_1.jpg', 'fonts/jost-600.woff2']:
    try:
        r = urllib.request.urlopen(base + f, timeout=30)
        print(f, '->', r.status, r.headers.get('Content-Length'))
    except Exception as e:
        print(f, 'ERR', e)
