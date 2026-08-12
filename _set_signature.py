# -*- coding: utf-8 -*-
import io

path = 'index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

# 1. HTML блока: «Разработан в ▲ ALTAVALTA» (вместо «▲ ALTAVALTA · САЙТ»)
old_html = '''  <div class="container footer-brand">
    <span class="brand-mark">▲</span>
    <a class="brand-link" href="https://altavalta.ru" target="_blank" rel="noopener">
      <span class="brand-name">ALTAVALTA</span>
      <span class="brand-sub">САЙТ</span>
    </a>
  </div>'''

new_html = '''  <div class="container footer-brand">
    <span class="brand-made">Разработан в</span>
    <span class="brand-mark">▲</span>
    <a class="brand-link" href="https://altavalta.ru" target="_blank" rel="noopener">
      <span class="brand-name">ALTAVALTA</span>
    </a>
  </div>'''

assert old_html in html, 'footer-brand html not found'
html = html.replace(old_html, new_html)

# 2. CSS: обновить (убрать brand-sub, добавить brand-made)
old_css = '''.footer-brand{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:22px;padding-top:18px;border-top:1px solid rgba(195,154,94,.25)}
.brand-mark{color:var(--gold-bright);font-size:13px;line-height:1;transform:translateY(-1px)}
.brand-name{color:#efe9da;font-size:12px;font-weight:700;letter-spacing:.28em;text-transform:uppercase}
.brand-sub{color:#93a08b;font-size:10.5px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;border-left:1px solid rgba(147,160,139,.35);padding-left:10px}
.brand-link{display:inline-flex;align-items:center;gap:10px;text-decoration:none;transition:opacity .3s}
.brand-link:hover{opacity:.85}'''

new_css = '''.footer-brand{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:22px;padding-top:18px;border-top:1px solid rgba(195,154,94,.25);flex-wrap:wrap}
.brand-made{color:#93a08b;font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase}
.brand-mark{color:var(--gold-bright);font-size:15px;line-height:1;transform:translateY(-1px)}
.brand-name{color:#efe9da;font-size:12.5px;font-weight:700;letter-spacing:.28em;text-transform:uppercase}
.brand-link{display:inline-flex;align-items:center;gap:10px;text-decoration:none;transition:opacity .3s}
.brand-link:hover{opacity:.85}'''

assert old_css in html, 'footer-brand css not found'
html = html.replace(old_css, new_css)

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('OK: подпись «Разработан в ▲ ALTAVALTA» установлена')
