# -*- coding: utf-8 -*-
"""Add: masters anchor bar (visible on mobile) + master sections with 'Ожидает наполнения'."""
import io, sys, re
sys.stdout.reconfigure(encoding="utf-8")

p = r"C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\index.html"
c = io.open(p, encoding="utf-8").read()
warns = []

def rep(old, new, label):
    global c
    if old not in c:
        warns.append("NOT FOUND: " + label)
        return
    c = c.replace(old, new, 1)

# ---------- 1. anchor bar after hero (before ticker) ----------
anchor_bar = """
  <nav class="masters-bar" aria-label="Мастера">
    <div class="container masters-bar-in">
      <a href="#m-victoria">Виктория</a><i></i>
      <a href="#m-tatiana">Татьяна</a><i></i>
      <a href="#m-anna">Анна</a><i></i>
      <a href="#m-nail">Nail-команда</a>
    </div>
  </nav>
"""
rep('</section>\n\n  <div class="ticker"', '</section>' + anchor_bar + '\n  <div class="ticker"', "anchor bar insert")

# ---------- 2. master sections: replace old team section ----------
i = c.find('<section class="section" id="team">')
j = c.find('<section class="section section-dark" id="why">')
if i == -1 or j == -1 or j <= i:
    warns.append("NOT FOUND: team section bounds")
else:
    masters_section = """  <section class="section" id="team">
    <div class="container">
      <div class="section-head reveal">
        <span class="overline">Команда</span>
        <h2>Мастера «Виктории»</h2>
        <p class="lead">У каждого мастера — своя страничка: услуги, работы и запись. Выберите мастера по имени — странички в наполнении.</p>
      </div>

      <article class="master-sec reveal" id="m-victoria">
        <div class="master-sec-head">
          <div class="master-sec-ava">В</div>
          <div class="master-sec-info">
            <h3>Виктория</h3>
            <div class="master-role">Ведущий мастер перманентного макияжа</div>
            <p>Татуаж бровей, губ и глаз, стрелки. Работает по предварительной записи.</p>
          </div>
          <a class="btn btn-primary btn-sm" href="master-victoria.html">Страничка мастера</a>
        </div>
        <div class="master-empty">Ожидает наполнения</div>
      </article>

      <article class="master-sec reveal" id="m-tatiana">
        <div class="master-sec-head">
          <div class="master-sec-ava">Т</div>
          <div class="master-sec-info">
            <h3>Татьяна</h3>
            <div class="master-role">Бровист</div>
            <p>Архитектура бровей, окрашивание, долговременная укладка.</p>
          </div>
        </div>
        <div class="master-empty">Ожидает наполнения</div>
      </article>

      <article class="master-sec reveal" id="m-anna">
        <div class="master-sec-head">
          <div class="master-sec-ava">А</div>
          <div class="master-sec-info">
            <h3>Анна</h3>
            <div class="master-role">Косметолог</div>
            <p>Уход за лицом, RF-лифтинг, карбоновый пилинг, аппаратная косметология.</p>
          </div>
        </div>
        <div class="master-empty">Ожидает наполнения</div>
      </article>

      <article class="master-sec reveal" id="m-nail">
        <div class="master-sec-head">
          <div class="master-sec-ava">+</div>
          <div class="master-sec-info">
            <h3>Парикмахеры и nail-команда</h3>
            <div class="master-role">Стрижки, окрашивание, маникюр, педикюр</div>
            <p>Мастера, к которым записываются по рекомендациям.</p>
          </div>
        </div>
        <div class="master-empty">Ожидает наполнения</div>
      </article>
    </div>
  </section>

"""
    c = c[:i] + masters_section + c[j:]

# ---------- 3. CSS: masters-bar + master-sec + master-empty, responsive ----------
css = """
/* Masters anchor bar */
.masters-bar{background:var(--pine-deep);border-bottom:1px solid rgba(255,255,255,.06)}
.masters-bar-in{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:12px;padding:14px 20px}
.masters-bar a{font-family:var(--font-display);font-size:16px;letter-spacing:.06em;color:#cfd8c2;text-decoration:none;transition:color .2s}
.masters-bar a:hover{color:var(--gold-bright)}
.masters-bar i{width:5px;height:5px;border-radius:50%;background:var(--gold);flex:none}
/* Master sections */
.master-sec{border:1px solid var(--line);border-radius:20px;background:var(--card);padding:22px;margin-bottom:18px}
.master-sec-head{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.master-sec-ava{width:56px;height:56px;border-radius:50%;background:var(--pine);color:var(--gold-bright);display:flex;align-items:center;justify-content:center;font-family:var(--font-display);font-size:24px;flex:none}
.master-sec-info{flex:1;min-width:200px}
.master-sec-info h3{font-family:var(--font-display);font-size:22px;color:var(--pine);margin-bottom:2px}
.master-sec-info .master-role{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:6px}
.master-sec-info p{font-size:14px;color:var(--muted)}
.master-empty{margin-top:16px;padding:14px 18px;border:1.5px dashed var(--line);border-radius:14px;background:var(--ivory);color:var(--muted);font-size:13px;font-style:italic;text-align:center;letter-spacing:.04em}
@media(max-width:767px){
  .masters-bar-in{justify-content:flex-start;overflow-x:auto;flex-wrap:nowrap;padding:12px 16px;gap:10px;-webkit-overflow-scrolling:touch}
  .masters-bar a{font-size:14px;white-space:nowrap}
  .master-sec{padding:16px}
  .master-sec-ava{width:46px;height:46px;font-size:20px}
}
"""
rep('</style>\n<style>', '</style>\n<style>' + css, "css insert")

io.open(p, "w", encoding="utf-8").write(c)
print("Masters anchors+secs done, len", len(c))
print("WARNS:", warns if warns else "none")
