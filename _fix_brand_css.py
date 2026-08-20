# -*- coding: utf-8 -*-
import io, re

path = 'index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

# 1. Убрать мёртвый CSS footer-credit (вчерашний, HTML удалён при мерже)
html = re.sub(r'\.footer-credit\{[^}]*\}\n?', '', html)
html = re.sub(r'\.footer-credit a\{[^}]*\}\n?', '', html)
html = re.sub(r'\.footer-credit a:hover\{[^}]*\}\n?', '', html)

# 2. Убрать старые конфликтующие правила brand-* (вчерашние: картинка 44px, pine, gold-deep)
html = re.sub(r'\.brand-mark\{width:44px;height:44px;flex:none\}\n?', '', html)
html = re.sub(r'\.brand-name\{font-family:var\(--font-display\);font-size:22px;color:var\(--pine\);line-height:1\}\n?', '', html)
html = re.sub(r'\.brand-sub\{font-size:11px;letter-spacing:\.24em;text-transform:uppercase;color:var\(--gold-deep\)\}\n?', '', html)

# 3. Добавить brand-link (ссылка-обёртка с ховером)
anchor = '.brand-sub{color:#93a08b;font-size:10.5px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;border-left:1px solid rgba(147,160,139,.35);padding-left:10px}'
assert anchor in html, 'brand-sub css anchor not found'
html = html.replace(anchor, anchor + '\n.brand-link{display:inline-flex;align-items:center;gap:10px;text-decoration:none;transition:opacity .3s}\n.brand-link:hover{opacity:.85}', 1)

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('CSS cleaned: brand-link added, stale rules removed')
