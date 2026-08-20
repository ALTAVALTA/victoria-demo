# -*- coding: utf-8 -*-
"""Полировка 2TEST_TOJE_SAMOE_POLNAYA: фото, отзывы, подпись, плашка, воркер-защита."""
import io, os, re, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria'
SRC = os.path.join(BASE, '2TEST_TOJE_SAMOE_POLNAYA_clean.html')
ETALON = os.path.join(BASE, 'polnaya_demo', 'index.html')
OUT = os.path.join(BASE, '2test_demo', 'index.html')
IMGDIR = os.path.join(BASE, '2test_demo', 'img')
AVDIR = os.path.join(IMGDIR, 'avatars')
FONTS = os.path.join(BASE, '2test_demo', 'fonts')

os.makedirs(IMGDIR, exist_ok=True)
os.makedirs(AVDIR, exist_ok=True)
os.makedirs(FONTS, exist_ok=True)

t = io.open(SRC, encoding='utf-8').read()
et = io.open(ETALON, encoding='utf-8').read()

# ---------- 1. ФОТО: копируем файлы ----------
mapping = {
 'hero-entrance':'21','hero-interior':'02','hero-door':'25',
 'about-room':'05','about-redwall':'06','about-street':'03',
 'svc-hair':'20','svc-nails':'07','svc-cosmo':'04','svc-laser':'08','svc-body':'17','svc-pmu':'14',
 'laser-cabinet':'18','laser-detail':'22','team-happy':'12','team-work':'16',
 'gal-street':'01','gal-manicure':'09','gal-autumn':'10','gal-warm':'11','gal-parking':'13',
 'gal-trees':'15','gal-path':'19','gal-sign':'23','gal-redhouse':'24','gal-white-door':'26',
 'map-entrance':'26'  # дубль -> заменим
}
POLIMG = os.path.join(BASE, 'polnaya_demo', 'img')
for name, num in mapping.items():
    src = os.path.join(POLIMG, 'PHOTO_%s.jpg' % num)
    dst = os.path.join(IMGDIR, 'PHOTO_%s.jpg' % name)
    shutil.copy2(src, dst)

# дубль photo26 в map-entrance -> заменить на photo24 (красный дом) для разнообразия
shutil.copy2(os.path.join(POLIMG, 'PHOTO_24.jpg'), os.path.join(IMGDIR, 'PHOTO_map-entrance.jpg'))
# поправим подпись в маркере map-entrance
t = t.replace('файл: victoria_photo26.jpg | подпись: Вход в с', 'файл: victoria_photo24.jpg | подпись: Красный дом с зелёными деревьями')

# аватарки
for a in ['avatar_1.jpg', 'avatar_2.jpg', 'avatar_3.jpg', 'avatar_4.jpg']:
    shutil.copy2(os.path.join(BASE, 'polnaya_demo', 'img', 'avatars', a), os.path.join(AVDIR, a))

# шрифты (Jost для подписи)
for f in ['jost-600.woff2', 'jost-700.woff2']:
    shutil.copy2(os.path.join(BASE, 'polnaya_demo', 'fonts', f), os.path.join(FONTS, f))
print('фото + аватарки + шрифты скопированы')

# ---------- 2. ОТЗЫВЫ: заменяем выдуманные на реальные ----------
# находим блок <section class="reviews" ...> ... </section>
m = re.search(r'<section class="reviews".*?</section>', t, re.S)
assert m, 'reviews section not found'
real_reviews = '''<section class="reviews" id="reviews">
  <div class="container">
    <div class="rev-head rv">
      <div class="sec-head" style="margin-bottom:0">
        <span class="kicker">Отзывы</span>
        <h2 class="h-disp">Нас рекомендуют <em class="it">друзьям</em></h2>
      </div>
      <div class="ya-badge">
        <span class="y">Я</span>
        <div>
          <b>4,4</b>
          <span class="stars">★★★★☆</span>
          <small>Яндекс Карты · 24 оценки · 7 отзывов · 26 фото</small>
        </div>
      </div>
    </div>
    <div class="rev-grid">
      <article class="rev-card rv">
        <div class="stars">★★★★★</div>
        <p>«Первый раз была в этом салоне. Небольшой, уютный, но главное — мастер. Приходила за стрелками к Виктории по рекомендации: всё сделала великолепно, приятный человек, общительная. Хожу, любуюсь теперь стрелками)»</p>
        <div class="rev-who"><span class="ava" style="background-image:url('img/avatars/avatar_1.jpg');background-size:cover;background-position:center;color:transparent">А</span><div><b>Анжелика</b><small>перманентный макияж · 30 октября 2025</small></div></div>
      </article>
      <article class="rev-card rv rv-d1">
        <div class="stars">★★★★★</div>
        <p>«Отличный салон. Все мастера улыбчивые и приветливые. Особенно хочется отметить мастера Ольгу — профессионал своего дела. И покрасит бомбезно, и подстрижёт красиво!»</p>
        <div class="rev-who"><span class="ava" style="background-image:url('img/avatars/avatar_2.jpg');background-size:cover;background-position:center;color:transparent">М</span><div><b>Максим Гавриличев</b><small>парикмахерский зал · 8 октября 2024</small></div></div>
      </article>
      <article class="rev-card rv rv-d2">
        <div class="stars">★★★★★</div>
        <p>«Салон посещаю часто! Маникюр и педикюр — Настя и Марина супер-мастера. РФ-лифтинг, косметология — Аня умница. Виктория — губы, брови. Всё в одном салоне!»</p>
        <div class="rev-who"><span class="ava" style="background-image:url('img/avatars/avatar_3.jpg');background-size:cover;background-position:center;color:transparent">Е</span><div><b>Елена Димитриенко</b><small>ногтевая студия · 16 апреля 2024</small></div></div>
      </article>
      <article class="rev-card rv rv-d3">
        <div class="stars">★★★★★</div>
        <p>«Услуги косметолога Анны понравились, да и сама она очень приятная девушка.»</p>
        <div class="rev-who"><span class="ava" style="background-image:url('img/avatars/avatar_4.jpg');background-size:cover;background-position:center;color:transparent">Н</span><div><b>Наталья Б</b><small>косметология · 27 сентября 2024</small></div></div>
      </article>
    </div>
  </div>
</section>'''
t = t[:m.start()] + real_reviews + t[m.end():]
print('отзывы заменены на реальные')

# ---------- 3. ПОДПИСЬ ALTAVALTA ----------
# вставить в footer перед закрывающим </footer>
sig_html = '''  <div class="footer-brand">
    <span class="brand-made">created by</span>
    <a class="brand-link" href="https://t.me/ALTAVALTA" target="_blank" rel="noopener">
      <span class="sig-name"><b>A</b><b>L</b><b>T</b><b>A</b><b class="brand-core">V</b><b>A</b><b>L</b><b>T</b><b>A</b></span>
    </a>
  </div>'''
i_foot = t.rfind('</footer>')
assert i_foot != -1
t = t[:i_foot] + sig_html + '\n' + t[i_foot:]

# CSS подписи — добавить перед </style> последним (или в head). Найдём конец CSS: </style>
css_sig = '''  .footer-brand{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:18px;padding-top:14px;border-top:1px solid rgba(193,154,91,.22);flex-wrap:wrap}
  .brand-made{color:#7d8a74;font-family:'Jost',sans-serif;font-size:9.5px;font-weight:500;letter-spacing:.24em;text-transform:lowercase}
  .brand-link{display:inline-flex;align-items:center;text-decoration:none;transition:opacity .3s}
  .brand-link:hover{opacity:.8}
  .sig-name{display:inline-flex;color:#d8d2c2;font-family:'Jost',sans-serif;font-size:12px;font-weight:700;gap:.08em;text-transform:uppercase;line-height:1}
  .sig-name b{font-weight:inherit}
  .brand-core{color:var(--gold);animation:v-pulse 2s ease-in-out infinite}
  @keyframes v-pulse{0%,100%{opacity:1}50%{opacity:.55}}
  @font-face{font-family:'Jost';src:url('fonts/jost-600.woff2') format('woff2');font-weight:600;font-display:swap}
  @font-face{font-family:'Jost';src:url('fonts/jost-700.woff2') format('woff2');font-weight:700;font-display:swap}
'''
# вставляем перед последним </style>
i_style = t.rfind('</style>')
t = t[:i_style] + css_sig + t[i_style:]
print('подпись ALTAVALTA вставлена')

# ---------- 4. ДЕМО-ПЛАШКА ----------
ribbon_html = '''<div class="demo-ribbon" id="demoRibbon" role="note">
  <span class="demo-label"><b>Демо-версия</b><i></i><span class="dl-sub">сделано для вас </span><b class="dl-love">с любовью</b></span>
  <button type="button" class="demo-remove" id="demoRemove">Убрать метку</button>
</div>'''
# после <body ...>
m_body = re.search(r'<body[^>]*>', t)
assert m_body
t = t[:m_body.end()] + '\n' + ribbon_html + t[m_body.end():]

css_ribbon = '''  .demo-ribbon{position:fixed;top:0;left:0;right:0;z-index:120;display:flex;align-items:center;justify-content:center;gap:16px;background:var(--pine-deep);border-bottom:1px solid rgba(193,154,91,.45);padding:10px 16px;color:#efe9da}
  .demo-label{display:inline-flex;align-items:center;gap:10px;font-size:12.5px;font-weight:700;letter-spacing:.22em;text-transform:uppercase}
  .demo-remove{background:transparent;border:1px solid rgba(193,154,91,.55);color:var(--gold);border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;cursor:pointer;font-family:inherit}
  .demo-ribbon{display:none}
  .demo-label{font-size:10.5px;letter-spacing:.12em}
  .demo-remove{padding:5px 10px;font-size:11px}
  body.demo-off .demo-ribbon{display:none}
'''
i_style = t.rfind('</style>')
t = t[:i_style] + css_ribbon + t[i_style:]

# JS: клик по Убрать метку
js_ribbon = '''
  (function(){
    var demo = document.getElementById('demoRibbon');
    var demoBtn = document.getElementById('demoRemove');
    if (demo && demoBtn){
      demoBtn.addEventListener('click', function(){
        document.body.classList.add('demo-off');
      });
    }
  })();
'''
i_script = t.rfind('</script>')
t = t[:i_script] + js_ribbon + t[i_script:]

# ---------- 5. ДЕМО-ЗАЩИТА ФОРМЫ (на случай показа) ----------
# у формы id=bookForm; добавим обработчик: демо-алерт вместо отправки
guard = '''
  (function(){
    var form = document.getElementById('bookForm');
    if (!form) return;
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var name = (document.getElementById('inName')||{}).value || '';
      var phone = (document.getElementById('inPhone')||{}).value || '';
      var svc = (document.getElementById('inService')||{}).value || '';
      alert('Демо-режим: заявка не отправляется. На боевом сайте она уйдёт администратору.\\n\\n' + name + ', ' + phone + ' — ' + svc);
    });
  })();
'''
i_script = t.rfind('</script>')
t = t[:i_script] + guard + t[i_script:]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
io.open(OUT, 'w', encoding='utf-8').write(t)
print('SAVED:', OUT, len(t), 'chars')
