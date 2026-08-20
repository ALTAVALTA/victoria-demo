# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html = open('index.html', encoding='utf-8').read()

# HTML-блок footer-brand (не CSS)
for m in re.finditer(r'<div class="container footer-brand".*?</div>\s*</div>', html, re.S):
    print('HTML BLOCK:')
    print(m.group(0)[:700])
