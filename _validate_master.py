# -*- coding: utf-8 -*-
"""Validate master-victoria.html structure."""
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")

DST = r"C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\master-victoria.html"
c = io.open(DST, encoding="utf-8").read()

checks = [
    ("title Victoria", "Виктория — перманентный макияж" in c),
    ("hero h1", "Виктория — ведущий мастер перманентного макияжа" in c),
    ("cta Записаться к Виктории", "Записаться к Виктории" in c),
    ("works Работы Виктории", "Работы Виктории" in c),
    ("prices Услуги Виктории", "Услуги Виктории" in c),
    ("reviews Клиенты о Виктории", "Клиенты о Виктории" in c),
    ("contacts Запишитесь к Виктории", "Запишитесь к Виктории" in c),
    ("modal Записаться к Виктории", "Записаться к Виктории" in c),
    ("payload master", "master:'Виктория'" in c),
    ("nav-back", "nav-back" in c),
    ("photo PM", "PHOTO_work_pm.jpg" in c),
    ("reviews only 2", c.count("rev-card") == 2),
    ("no team section", 'id="team"' not in c),
    ("no old hero", "Ногти, которые держатся" not in c),
    ("no old works", "Хочу как здесь" not in c),
    ("no old reviews h2", "Клиенты о студии" not in c),
    ("no old modal", "<h3 id=\"modalTitle\">Записаться в студию</h3>" not in c),
    ("no mani ticker", "Маникюр и педикюр" not in c),
    ("no hero old photo", "PHOTO_hero.jpg" not in c),
]
for name, ok in checks:
    print(("OK  " if ok else "FAIL") + " " + name)

# tag balance
for tag in ["section", "div", "form", "select", "button", "script", "style"]:
    o = len(re.findall(r"<" + tag + r"[ >]", c))
    cl = len(re.findall(r"</" + tag + r">", c))
    print(f"balance {tag}: open={o} close={cl} {'OK' if o==cl else 'MISMATCH'}")
