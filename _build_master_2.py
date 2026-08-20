# -*- coding: utf-8 -*-
"""Build master-victoria.html part 2: works/prices/team/why/reviews/contacts/modal/payload."""
import io, re, sys

sys.stdout.reconfigure(encoding="utf-8")

DST = r"C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\master-victoria.html"
c = io.open(DST, encoding="utf-8").read()
warns = []

def rep(old, new, label):
    global c
    if old not in c:
        warns.append("NOT FOUND: " + label)
        return
    c = c.replace(old, new, 1)

# ---------- hero media ----------
rep("""      <div class="hero-media">
        <!-- @@PHOTO:hero@@ описание: светлая студия, мастер в чёрной форме выполняет процедуру клиенту на кушетке, профессиональная атмосфера; файл: victoria_photo05.jpg -->
        <div class="img-wrap ar-hero"><img src="img/PHOTO_hero.jpg" alt="Мастер студии «Виктория» выполняет процедуру в светлом кабинете"></div>
      </div>""",
    """      <div class="hero-media">
        <!-- фото: работа Виктории — перманентный макияж -->
        <div class="img-wrap ar-hero"><img src="img/PHOTO_work_pm.jpg" alt="Работа Виктории — перманентный макияж"></div>
      </div>""", "hero media")

# ---------- ticker ----------
old_tick = """        <span>Маникюр и педикюр</span><i></i><span>Стрижки и окрашивание</span><i></i><span>Перманентный макияж</span><i></i><span>Диодная лазерная эпиляция</span><i></i><span>Карбоновый пилинг</span><i></i><span>RF-лифтинг</span><i></i><span>Массаж</span><i></i><span>Наращивание ресниц</span><i></i><span>Запись по времени</span><i></i>"""
new_tick = """        <span>Татуаж бровей</span><i></i><span>Татуаж губ</span><i></i><span>Стрелки</span><i></i><span>Коррекция татуажа</span><i></i><span>Удаление татуажа лазером</span><i></i><span>Карбоновый пилинг</span><i></i><span>RF-лифтинг</span><i></i><span>Индивидуальный эскиз</span><i></i><span>Запись по времени</span><i></i>"""
rep(old_tick, new_tick, "ticker 1")
rep(old_tick, new_tick, "ticker 2")

# ---------- works section (replace whole) ----------
i = c.find('<section class="section" id="works">')
j = c.find('<section class="section section-tint" id="prices">')
if i == -1 or j == -1 or j <= i:
    warns.append("NOT FOUND: works section bounds")
else:
    new_works = """  <section class="section" id="works">
    <div class="container">
      <div class="section-head reveal">
        <span class="overline">Работы Виктории</span>
        <h2>Перманентный макияж</h2>
        <p class="lead">Татуаж бровей, губ, глаз и стрелки. Нажмите «Хочу так» — откроется форма записи с уже выбранной услугой.</p>
      </div>
      <div class="works-grid">
        <article class="work-card reveal">
          <!-- фото: работа Виктории — перманентный макияж -->
          <div class="img-wrap ar-mani"><img src="img/PHOTO_work_pm.jpg" alt="Перманентный макияж — работа Виктории"></div>
          <div class="work-body">
            <h3>Перманентный макияж (татуаж)</h3>
            <p>Брови, губы, глаза и стрелки. Эскиз согласовываем до процедуры, работаем с аппликационной анестезией — комфортно и безопасно.</p>
            <div class="work-foot">
              <span class="work-price">цена по запросу</span>
              <button class="btn-want" type="button" data-open-form data-service="Перманентный макияж (татуаж)">Хочу так</button>
            </div>
          </div>
        </article>
      </div>
      <p class="zones-note reveal">Портфолио работ Виктории покажем при записи — приходите, обсудим форму и цвет под вас.</p>
    </div>
  </section>

"""
    c = c[:i] + new_works + c[j:]

# ---------- prices ----------
rep("""      <div class="section-head reveal">
        <span class="overline">Прайс-лист</span>
        <h2>Услуги и цены</h2>
        <p class="lead">Все направления студии — в одном месте. Точную стоимость мастер подтвердит при записи: она зависит от длины волос, состояния ногтей и зоны процедуры.</p>
      </div>""",
    """      <div class="section-head reveal">
        <span class="overline">Прайс-лист</span>
        <h2>Услуги Виктории</h2>
        <p class="lead">Перманентный макияж и уход за лицом. Точную стоимость Виктория подтвердит при записи — она зависит от зоны и сложности процедуры.</p>
      </div>""", "prices head")

# replace zones block with single zone (Лицо)
i = c.find('<div class="zones">')
j = c.find('</div>', i)
j2 = c.find('<p class="zones-note')
if i != -1 and j2 != -1:
    new_zones = """      <div class="zones">
        <div class="zone reveal">
          <div class="zone-head">
            <span class="zone-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="8" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M5 20c1.2-3.6 3.8-5.5 7-5.5s5.8 1.9 7 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span>
            <h3>Перманентный макияж и уход за лицом</h3>
          </div>
          <div class="price-row"><span class="name">Перманентный макияж (татуаж)</span><span class="dots"></span><span class="price req">по запросу</span></div>
          <div class="price-row"><span class="name">Коррекция татуажа</span><span class="dots"></span><span class="price req">по запросу</span></div>
          <div class="price-row"><span class="name">Удаление татуажа лазером</span><span class="dots"></span><span class="price req">по запросу</span></div>
          <div class="price-row"><span class="name">Карбоновый пилинг</span><span class="dots"></span><span class="price real">1 500 ₽</span></div>
          <div class="price-row"><span class="name">Безинъекционная биоревитализация</span><span class="dots"></span><span class="price real">от 800 ₽</span></div>
          <div class="price-row"><span class="name">RF-лифтинг лица</span><span class="dots"></span><span class="price req">по запросу</span></div>
          <div class="price-row"><span class="name">Наращивание ресниц</span><span class="dots"></span><span class="price req">по запросу</span></div>
        </div>
      </div>
"""
    c = c[:i] + new_zones + c[j2:]
else:
    warns.append("NOT FOUND: zones block")

# ---------- team: remove section ----------
i = c.find('<section class="section" id="team">')
j = c.find('<section class="section section-dark" id="why">')
if i != -1 and j != -1 and j > i:
    c = c[:i] + c[j:]
else:
    warns.append("NOT FOUND: team bounds")

# ---------- why ----------
rep('<span class="overline" style="color:var(--gold-bright)">Почему мы</span>',
    '<span class="overline" style="color:var(--gold-bright)">Почему Виктория</span>', "why overline")
rep('<h2>Почему выбирают «Викторию»</h2>', '<h2>Почему выбирают Викторию</h2>', "why h2")
# why cards 03-06 -> PM-specific
rep("""        <div class="why-card reveal">
          <div class="why-num">03</div>
          <h3>Стойкое покрытие</h3>""",
    """        <div class="why-card reveal">
          <div class="why-num">03</div>
          <h3>Индивидуальный эскиз</h3>""", "why card 3 head")
rep("""          <p>Пигмент держится долго, а мастер подбирает оттенок под цветотип — макияж выглядит естественно и не «плывёт».</p>""",
    """          <p>Перед процедурой рисуем эскиз, согласовываем форму и оттенок под ваш цветотип — макияж выглядит естественно.</p>""", "why card 3 body")

io.open(DST, "w", encoding="utf-8").write(c)
print("PART 2 done, len", len(c))
print("WARNS:", warns if warns else "none")
