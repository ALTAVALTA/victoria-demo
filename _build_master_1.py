# -*- coding: utf-8 -*-
"""Build master-victoria.html from polished index.html (local, no deploy)."""
import io, re, shutil, sys

sys.stdout.reconfigure(encoding="utf-8")

DEP = r"C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy"
SRC = DEP + r"\index.html"
DST = DEP + r"\master-victoria.html"

shutil.copy(SRC, DST)
c = io.open(DST, encoding="utf-8").read()
orig_len = len(c)
warns = []

def rep(old, new, label):
    global c
    if old not in c:
        warns.append("NOT FOUND: " + label)
        return
    c = c.replace(old, new, 1)

# ---------- 1. title + meta ----------
rep("<title>Студия красоты «Виктория» — Калининград, Комсомольская 2А | Маникюр, стрижки, косметология</title>",
    "<title>Виктория — перманентный макияж | Студия красоты «Виктория», Калининград</title>", "title")
rep('content="Студия красоты «Виктория» в центре Калининграда: маникюр и педикюр, стрижки и окрашивание, перманентный макияж, лазерная эпиляция, косметология. Запись по телефону +7 (911) 865-44-60, ежедневно 08:30–20:30."',
    'content="Виктория — ведущий мастер перманентного макияжа в студии красоты «Виктория», Калининград: татуаж бровей, губ, глаз, стрелки. Запись по телефону +7 (911) 865-44-60."', "meta")

# ---------- 2. topbar: brand -> index, nav -> master page ----------
rep('<a class="brand" href="#top">', '<a class="brand" href="index.html">', "brand href")
rep("""    <nav class="topnav">
      <a href="#works">Работы</a>
      <a href="#prices">Услуги и цены</a>
      <a href="#team">Мастера</a>
      <a href="#reviews">Отзывы</a>
      <a href="#contacts">Контакты</a>
    </nav>""",
    """    <nav class="topnav">
      <a href="#works">Работы</a>
      <a href="#prices">Услуги</a>
      <a href="#reviews">Отзывы</a>
      <a href="#contacts">Контакты</a>
      <a class="nav-back" href="index.html">← В студию</a>
    </nav>""", "topnav")

# ---------- 3. hero ----------
rep('<span class="overline">Студия красоты «Виктория» · Калининград</span>',
    '<span class="overline">Студия красоты «Виктория» · Перманентный макияж</span>', "hero overline")
rep("<h1>Ногти, которые держатся. Стрижки, которые идут. Процедуры, которые работают.</h1>",
    "<h1>Виктория — ведущий мастер перманентного макияжа</h1>", "hero h1")
rep('<p class="lead">Маникюр и педикюр, стрижки и окрашивание, перманентный макияж, лазерная эпиляция и косметология в центре Калининграда. Работаем по предварительной записи — вы не ждёте в очереди и приходите к своему времени.</p>',
    '<p class="lead">Татуаж бровей, губ и глаз, стрелки — с индивидуальным эскизом и бережной анестезией. Виктория — руководитель студии: к ней записываются по рекомендациям и возвращаются за коррекцией. Работает по предварительной записи в центре Калининграда.</p>', "hero lead")
rep('<button class="btn btn-primary" type="button" data-open-form>Записаться</button>',
    '<button class="btn btn-primary" type="button" data-open-form>Записаться к Виктории</button>', "hero cta")
rep('<!-- @@PHOTO:hero@@ описание: тёплый салон красоты, мастер в белом фартуке выполняет процедуру на фоне светлого интерьера, спокойная атмосфера; файл: victoria_photo05.jpg -->',
    '<!-- фото: работа Виктории — перманентный макияж -->', "hero photo comment")
rep('<div class="img-wrap ar-hero"><img src="img/PHOTO_hero.jpg" alt="Салон красоты «Виктория» выполняет процедуру в тёплом интерьере"></div>',
    '<div class="img-wrap ar-hero"><img src="img/PHOTO_work_pm.jpg" alt="Работа Виктории — перманентный макияж"></div>', "hero photo")

# ---------- 4. ticker ----------
rep("""      <div class="ticker-half">
        <span>Маникюр и педикюр</span><i></i><span>Стрижки и окрашивание</span><i></i><span>Перманентный макияж</span><i></i><span>Лазерная эпиляция</span><i></i><span>Карбоновый пилинг</span><i></i><span>RF-лифтинг</span><i></i><span>Татуаж</span><i></i><span>Наращивание ресниц</span><i></i><span>Запись по времени</span><i></i>
      </div>
      <div class="ticker-half">
        <span>Маникюр и педикюр</span><i></i><span>Стрижки и окрашивание</span><i></i><span>Перманентный макияж</span><i></i><span>Лазерная эпиляция</span><i></i><span>Карбоновый пилинг</span><i></i><span>RF-лифтинг</span><i></i><span>Татуаж</span><i></i><span>Наращивание ресниц</span><i></i><span>Запись по времени</span><i></i>
      </div>""",
    """      <div class="ticker-half">
        <span>Татуаж бровей</span><i></i><span>Татуаж губ</span><i></i><span>Стрелки</span><i></i><span>Коррекция татуажа</span><i></i><span>Удаление татуажа лазером</span><i></i><span>Карбоновый пилинг</span><i></i><span>RF-лифтинг</span><i></i><span>Индивидуальный эскиз</span><i></i><span>Запись по времени</span><i></i>
      </div>
      <div class="ticker-half">
        <span>Татуаж бровей</span><i></i><span>Татуаж губ</span><i></i><span>Стрелки</span><i></i><span>Коррекция татуажа</span><i></i><span>Удаление татуажа лазером</span><i></i><span>Карбоновый пилинг</span><i></i><span>RF-лифтинг</span><i></i><span>Индивидуальный эскиз</span><i></i><span>Запись по времени</span><i></i>
      </div>""", "ticker")

io.open(DST, "w", encoding="utf-8").write(c)
print("PART 1 done, len", len(c))
print("WARNS:", warns if warns else "none")
