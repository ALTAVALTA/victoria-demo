# -*- coding: utf-8 -*-
"""Part 3: replace why-grid cards 03-06, reviews, contacts, modal, payload."""
import io, sys

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

# ---------- why cards 03-06 ----------
old_why = """        <div class="why-card reveal">
          <div class="why-num">03</div>
          <h3>Центр Калининграда</h3>
          <p>Комсомольская ул., 2А — Центральный район, удобно добираться из любой точки города.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-num">04</div>
          <h3>Аппаратная косметология</h3>
          <p>Диодный лазер, элос-эпиляция, RF-лифтинг и карбоновый пилинг — процедуры на современном оборудовании.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-num">05</div>
          <h3>Всей семьёй</h3>
          <p>Женские, мужские и детские стрижки, маникюр, педикюр и косметология — всё в одной студии.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-num">06</div>
          <h3>Консультация бесплатно</h3>
          <p>Перед процедурой мастер проконсультирует и подберёт то, что подходит именно вам, а не «по прайсу».</p>
        </div>"""
new_why = """        <div class="why-card reveal">
          <div class="why-num">03</div>
          <h3>Индивидуальный эскиз</h3>
          <p>Перед процедурой рисуем эскиз, согласовываем форму и оттенок под ваш цветотип — макияж выглядит естественно.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-num">04</div>
          <h3>Комфорт и анестезия</h3>
          <p>Работаем с аппликационной анестезией — процедура проходит бережно и без неприятных ощущений.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-num">05</div>
          <h3>Стойкий результат</h3>
          <p>Пигмент держится долго, оттенок не «плывёт». Через время — коррекция, чтобы макияж оставался свежим.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-num">06</div>
          <h3>Консультация перед процедурой</h3>
          <p>Сначала обсуждаем форму и цвет, отвечаем на вопросы — и только потом приступаем к работе.</p>
        </div>"""
rep(old_why, new_why, "why cards 3-6")

# ---------- reviews ----------
rep("<h2>Клиенты о студии</h2>", "<h2>Клиенты о Виктории</h2>", "reviews h2")
# replace reviews grid: keep only Анжелика + Елена (cards 1 and 3)
i = c.find('<div class="reviews-grid">')
j = c.find('<p class="reviews-note">')
if i != -1 and j != -1 and j > i:
    rev_card = """      <div class="reviews-grid">
        <div class="rev-card">
          <svg class="rev-quote" width="34" height="28" viewBox="0 0 30 24" fill="currentColor" aria-hidden="true"><path d="M0 24V14.4C0 6.4 4.8 1.6 13 0l1.6 4C9.8 5.6 8 8 8 12h5v12H0zm17 0V14.4C17 6.4 21.8 1.6 30 0l-1.6 4C23.8 5.6 22 8 22 12h5v12H17z" transform="scale(0.94)"/></svg>
          <div class="rev-head">
            <img class="rev-ava" src="img/avatars/avatar_1.png" alt="Анжелика">
            <div class="rev-who">
              <span class="rev-name">Анжелика</span>
              <span class="rev-meta"><span class="rev-date">30 октября 2025</span><span class="rev-level">Знаток города 6 уровня</span></span>
            </div>
          </div><p class="rev-text">Первый раз была в этом салоне. Небольшой, уютный салон, но главное мастер) приходила за стрелками к Виктории, по рекомендации. Мастер очень хороший, все сделала великолепно, приятный человек, общительная. Хожу, любуюсь теперь стрелками)</p>
        </div>
        <div class="rev-card">
          <svg class="rev-quote" width="34" height="28" viewBox="0 0 30 24" fill="currentColor" aria-hidden="true"><path d="M0 24V14.4C0 6.4 4.8 1.6 13 0l1.6 4C9.8 5.6 8 8 8 12h5v12H0zm17 0V14.4C17 6.4 21.8 1.6 30 0l-1.6 4C23.8 5.6 22 8 22 12h5v12H17z" transform="scale(0.94)"/></svg>
          <div class="rev-head">
            <img class="rev-ava" src="img/avatars/avatar_3.png" alt="Елена Димитриенко">
            <div class="rev-who">
              <span class="rev-name">Елена Димитриенко</span>
              <span class="rev-meta"><span class="rev-date">16 апреля 2024</span><span class="rev-level">Знаток города 5 уровня</span></span>
            </div>
          </div><p class="rev-text">Салон посещаю часто! Маникюр, педикюр Настя и Марина супер мастера! РФ лифтинг, косметология. Аня умница. Виктория мастер: губы, брови. Все в одном салоне</p>
        </div>
      </div>
"""
    c = c[:i] + rev_card + c[j:]
else:
    warns.append("NOT FOUND: reviews grid bounds")

# ---------- contacts ----------
rep("<h2>Ждём вас в «Виктории»</h2>", "<h2>Запишитесь к Виктории</h2>", "contacts h2")
rep("<p class=\"lead\">Позвоните или оставьте заявку — администратор подберёт удобные дату и время к нужному мастеру.</p>",
    "<p class=\"lead\">Позвоните или оставьте заявку — Виктория перезвонит, подтвердит стоимость и подберёт удобное время.</p>", "contacts lead")
rep('<div class="sub">единый номер студии</div>', '<div class="sub">запись к Виктории</div>', "contacts phone sub")

# ---------- modal ----------
rep('<h3 id="modalTitle">Записаться в студию</h3>', '<h3 id="modalTitle">Записаться к Виктории</h3>', "modal title")
rep('<p class="modal-sub">Оставьте заявку — администратор перезвонит, подтвердит стоимость и подберёт удобное время.</p>',
    '<p class="modal-sub">Оставьте заявку — Виктория перезвонит, подтвердит стоимость и подберёт удобное время.</p>', "modal sub")

# replace service chips with Виктория's services
i = c.find('<div class="chips" id="serviceChips">')
j = c.find('</select>', i)
if i != -1 and j != -1 and j > i:
    chips = """<div class="chips" id="serviceChips">
            <div class="chips-group"><span class="chips-cat">Перманентный макияж</span>
              <button type="button" class="chip" data-service="Перманентный макияж (татуаж)">Перманентный макияж (татуаж)</button>
              <button type="button" class="chip" data-service="Коррекция татуажа">Коррекция татуажа</button>
              <button type="button" class="chip" data-service="Удаление татуажа лазером">Удаление татуажа лазером</button>
            </div>
            <div class="chips-group"><span class="chips-cat">Уход за лицом</span>
              <button type="button" class="chip" data-service="Карбоновый пилинг">Карбоновый пилинг</button>
              <button type="button" class="chip" data-service="Безинъекционная биоревитализация">Безинъекционная биоревитализация</button>
              <button type="button" class="chip" data-service="RF-лифтинг лица">RF-лифтинг лица</button>
              <button type="button" class="chip" data-service="Наращивание ресниц">Наращивание ресниц</button>
            </div>
            <div class="chips-group"><span class="chips-cat">Другое</span>
              <button type="button" class="chip chip-other" data-service="Другое (уточню в комментарии)">Другое</button>
            </div>
          </div>
          <select id="fService" name="service" hidden>"""
    c = c[:i] + chips + c[j + len("</select>"):]
else:
    warns.append("NOT FOUND: service chips")

# ---------- payload: add master ----------
rep("source:'victoria-demo'", "source:'victoria-demo',master:'Виктория'", "payload master")

io.open(DST, "w", encoding="utf-8").write(c)
print("PART 3 done, len", len(c))
print("WARNS:", warns if warns else "none")
