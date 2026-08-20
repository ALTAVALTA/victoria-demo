# -*- coding: utf-8 -*-
import io

path = 'index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

old = '''<<<<<<< HEAD
  <div class="container footer-brand">
    <span class="brand-mark">▲</span>
    <span class="brand-name">ALTAVALTA</span>
    <span class="brand-sub">САЙТ</span>
  </div>
=======

  <div class="footer-credit"><a href="https://altavalta.ru" target="_blank" rel="noopener">Разработано в ALTAVALTA</a></div>
>>>>>>> 85f3a4bdfea2705ab2ad1eeec2c30706d41cdda8'''

new = '''  <div class="container footer-brand">
    <span class="brand-mark">▲</span>
    <a class="brand-link" href="https://altavalta.ru" target="_blank" rel="noopener">
      <span class="brand-name">ALTAVALTA</span>
      <span class="brand-sub">САЙТ</span>
    </a>
  </div>'''

assert old in html, 'conflict block not found'
html = html.replace(old, new)

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('conflict resolved')
