# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

path = 'index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

# === 1. HTML: AVA-ядро (4-6 буквы) золотым классом ===
old_html = '''      <span class="brand-name"><b>A</b><b>L</b><b>T</b><b>A</b><b class="brand-axis">V</b><b>A</b><b>L</b><b>T</b><b>A</b></span>'''

new_html = '''      <span class="brand-name"><b>A</b><b>L</b><b>T</b><b class="brand-core">A</b><b class="brand-core">V</b><b class="brand-core">A</b><b>L</b><b>T</b><b>A</b></span>'''

assert old_html in html, 'HTML подписи не найден'
html = html.replace(old_html, new_html)
print('HTML: AVA-ядро выделено')

# === 2. CSS: скромнее, Jost 600, AVA золотом ===
old_css = '''.footer-brand{display:flex;align-items:center;justify-content:center;gap:12px;margin-top:24px;padding-top:18px;border-top:1px solid rgba(195,154,94,.25);flex-wrap:wrap}
.brand-made{color:#93a08b;font-family:'Jost',sans-serif;font-size:11px;font-weight:600;letter-spacing:.3em;text-transform:lowercase}
.brand-link{display:inline-flex;align-items:center;text-decoration:none;transition:opacity .3s}
.brand-link:hover{opacity:.85}
.brand-name{display:inline-flex;color:#efe9da;font-family:'Jost',sans-serif;font-size:17px;font-weight:700;letter-spacing:.42em;text-transform:uppercase;line-height:1}
.brand-name b{font-weight:inherit}
.brand-axis{color:var(--gold-bright)}'''

new_css = '''.footer-brand{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px;padding-top:14px;border-top:1px solid rgba(195,154,94,.22);flex-wrap:wrap}
.brand-made{color:#7d8a74;font-family:'Jost',sans-serif;font-size:9.5px;font-weight:500;letter-spacing:.24em;text-transform:lowercase}
.brand-link{display:inline-flex;align-items:center;text-decoration:none;transition:opacity .3s}
.brand-link:hover{opacity:.8}
.brand-name{display:inline-flex;color:#d8d2c2;font-family:'Jost',sans-serif;font-size:13px;font-weight:600;letter-spacing:.3em;text-transform:uppercase;line-height:1}
.brand-name b{font-weight:inherit}
.brand-core{color:var(--gold-bright)}'''

assert old_css in html, 'CSS подписи не найден'
html = html.replace(old_css, new_css)
print('CSS: скромнее + Jost 600 + AVA золотом')

# === 3. Jost: подключить 600 вместо 700 ===
old_font = "@font-face{font-family:'Jost';font-style:normal;font-weight:700;font-display:swap;src:url(fonts/jost-700.woff2) format('woff2')}"
new_font = "@font-face{font-family:'Jost';font-style:normal;font-weight:600;font-display:swap;src:url(fonts/jost-600.woff2) format('woff2')}"
if old_font in html:
    html = html.replace(old_font, new_font)
    print('Jost: 600 подключён')
else:
    print('Jost @font-face 700 не найден (проверю)')

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('OK: сохранено')
