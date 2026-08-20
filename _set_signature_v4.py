# -*- coding: utf-8 -*-
# ЭТАЛОН фирменной подписи ALTAVALTA — ФИНАЛ 13.08.2026 (демо Виктории)
# Применять на ВСЕХ последующих лендингах. Стандарт:
#   created by (9.5px, lowercase, .24em) + ALTAVALTA (Jost 700, 12px, gap .08em, только V золотая, пульс 2с)
#   ссылка https://t.me/ALTAVALTA (капсом), подпись в футере на месте @@SIGNATURE@@.
# ГРАБЛИ: letter-spacing между <b> (flex) НЕ работает — только gap на родителе.
#         Класс brand-mark НЕ трогать (это логотип клиента 44px).
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

path = 'index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

# === 1. HTML: подпись (created by + ALTAVALTA с V-ядром) ===
old_html = '''<!-- @@SIGNATURE@@ -->'''
new_html = '''<div class="footer-brand">
    <span class="brand-made">created by</span>
    <a class="brand-link" href="https://t.me/ALTAVALTA" target="_blank" rel="noopener">
      <span class="brand-name"><b>A</b><b>L</b><b>T</b><b>A</b><b class="brand-core">V</b><b>A</b><b>L</b><b>T</b><b>A</b></span>
    </a>
  </div>'''

if old_html in html:
    html = html.replace(old_html, new_html)
    print('HTML: подпись вставлена на место @@SIGNATURE@@')
else:
    print('HTML: маркер @@SIGNATURE@@ не найден — ищу альтернативу...')
    # запасной вариант: вставить перед </footer>
    if '</footer>' in html:
        html = html.replace('</footer>', new_html + '\n</footer>')
        print('HTML: подпись вставлена перед </footer>')
    else:
        print('HTML: НЕ НАЙДЕН ни маркер, ни </footer> — правь руками!')

# === 2. CSS: актуальный стандарт ===
sig_css = '''
.footer-brand{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px;padding-top:14px;border-top:1px solid rgba(195,154,94,.22);flex-wrap:wrap}
.brand-made{color:#7d8a74;font-family:'Jost',sans-serif;font-size:9.5px;font-weight:500;letter-spacing:.24em;text-transform:lowercase}
.brand-link{display:inline-flex;align-items:center;text-decoration:none;transition:opacity .3s}
.brand-link:hover{opacity:.8}
.brand-name{display:inline-flex;color:#d8d2c2;font-family:'Jost',sans-serif;font-size:12px;font-weight:700;gap:.08em;text-transform:uppercase;line-height:1}
.brand-name b{font-weight:inherit}
.brand-core{color:var(--gold-bright);animation:v-pulse 2s ease-in-out infinite}
@keyframes v-pulse{0%,62%{color:var(--gold-bright);text-shadow:none}74%{color:#f5d9a8;text-shadow:0 0 10px rgba(245,217,168,.75)}84%{color:#f7e3b5;text-shadow:0 0 16px rgba(245,217,168,.95)}94%{color:#eccd97;text-shadow:0 0 6px rgba(245,217,168,.5)}100%{color:var(--gold-bright);text-shadow:none}}
'''

if '.brand-name{' in html:
    html = html.replace('.brand-name{', sig_css + '.brand-name{', 1)
    print('CSS: стандарт подписи добавлен перед .brand-name')
else:
    html = html.replace('</style>', sig_css + '</style>')
    print('CSS: стандарт подписи добавлен перед </style>')

# === 3. Шрифт Jost 700 (если нет) ===
if "jost-700" not in html:
    font_face = "@font-face{font-family:'Jost';font-style:normal;font-weight:700;font-display:swap;src:url(fonts/jost-700.woff2) format('woff2')}"
    html = html.replace('</style>', font_face + '</style>')
    print('CSS: @font-face Jost 700 добавлен')

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('ГОТОВО: подпись по стандарту 13.08 установлена')
