# -*- coding: utf-8 -*-
"""Fix Victoria page: remove rating & address, keep hours, add individual booking."""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")

p = r"C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\master-victoria.html"
c = io.open(p, encoding="utf-8").read()
warns = []

def rep(old, new, label):
    global c
    if old not in c:
        warns.append("NOT FOUND: " + label)
        return
    c = c.replace(old, new, 1)

# 1. hero facts: drop rating (star) and address (pin), keep hours, add individual booking
old_facts = """      <div class="hero-facts">
          <span class="hero-fact">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17l-6.1 3.6 1.4-6.8L2.2 9.1l6.9-.8L12 2z"/></svg>
            4,4 — рейтинг на Яндекс Картах
          </span>
          <span class="hero-fact">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3.5 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            Ежедневно 08:30–20:30
          </span>
          <span class="hero-fact">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="10" r="2.6" stroke="currentColor" stroke-width="1.8"/></svg>
            Комсомольская ул., 2А
          </span>
        </div>"""
new_facts = """      <div class="hero-facts">
          <span class="hero-fact">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3.5 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            Ежедневно 08:30–20:30
          </span>
          <span class="hero-fact">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="10" r="2.6" stroke="currentColor" stroke-width="1.8"/></svg>
            Возможна индивидуальная запись
          </span>
        </div>"""
rep(old_facts, new_facts, "hero facts")

# 2. contacts: remove address row, keep hours + phone
old_addr = """          <div class="visit-row">
            <span class="visit-ico"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="10" r="2.6" stroke="currentColor" stroke-width="1.8"/></svg></span>
            <div>
              <div class="lbl">Адрес</div>
              <div class="val">Калининград, Комсомольская ул., 2А</div>
              <div class="sub">Центральный район, 1 этаж</div>
            </div>
          </div>
"""
rep(old_addr, "", "contacts address row")

io.open(p, "w", encoding="utf-8").write(c)
print("Victoria page fixed, len", len(c))
print("WARNS:", warns if warns else "none")
