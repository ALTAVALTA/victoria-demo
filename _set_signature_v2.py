# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

path = 'index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

# === 1. ПОДКЛЮЧИТЬ JOST (700) локальным @font-face ===
font_css = '''@font-face{font-family:'Jost';font-style:normal;font-weight:700;font-display:swap;src:url(fonts/jost-700.woff2) format('woff2')}
'''
# вставить в <head> после открывающего тега или перед <style>
if "@font-face{font-family:'Jost'" not in html:
    # найти <style> и вставить перед ним
    m = re.search(r'<style>', html)
    if m:
        html = html[:m.start()] + '<style>\n' + font_css + '</style>\n' + html[m.start():]
        print('Jost @font-face добавлен')
    else:
        print('!!! <style> не найден')

# === 2. ЗАМЕНИТЬ HTML-блок подписи ===
old_html = '''  <div class="container footer-brand">
    <span class="brand-made">Разработан в</span>
    <span class="brand-mark">▲</span>
    <a class="brand-link" href="https://altavalta.ru" target="_blank" rel="noopener">
      <span class="brand-name">ALTAVALTA</span>
    </a>
  </div>'''

new_html = '''  <div class="container footer-brand">
    <span class="brand-made">created by</span>
    <a class="brand-link" href="https://t.me/altavalta" target="_blank" rel="noopener">
      <span class="brand-name"><b>A</b><b>L</b><b>T</b><b>A</b><b class="brand-axis">V</b><b>A</b><b>L</b><b>T</b><b>A</b></span>
    </a>
  </div>'''

assert old_html in html, 'HTML подписи не найден'
html = html.replace(old_html, new_html)
print('HTML подписи заменён (created by + Jost + зеркальная V)')

# === 3. ОБНОВИТЬ CSS ===
old_css = '''.footer-brand{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:22px;padding-top:18px;border-top:1px solid rgba(195,154,94,.25);flex-wrap:wrap}
.brand-made{color:#93a08b;font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase}
.brand-mark{color:var(--gold-bright);font-size:15px;line-height:1;transform:translateY(-1px)}
.brand-name{color:#efe9da;font-size:12.5px;font-weight:700;letter-spacing:.28em;text-transform:uppercase}
.brand-link{display:inline-flex;align-items:center;gap:10px;text-decoration:none;transition:opacity .3s}
.brand-link:hover{opacity:.85}'''

new_css = '''.footer-brand{display:flex;align-items:center;justify-content:center;gap:12px;margin-top:24px;padding-top:18px;border-top:1px solid rgba(195,154,94,.25);flex-wrap:wrap}
.brand-made{color:#93a08b;font-family:'Jost',sans-serif;font-size:11px;font-weight:600;letter-spacing:.3em;text-transform:lowercase}
.brand-link{display:inline-flex;align-items:center;text-decoration:none;transition:opacity .3s}
.brand-link:hover{opacity:.85}
.brand-name{display:inline-flex;color:#efe9da;font-family:'Jost',sans-serif;font-size:17px;font-weight:700;letter-spacing:.42em;text-transform:uppercase;line-height:1}
.brand-name b{font-weight:inherit}
.brand-axis{color:var(--gold-bright)}'''

assert old_css in html, 'CSS подписи не найден'
html = html.replace(old_css, new_css)
print('CSS подписи обновлён')

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('OK: index.html сохранён')
