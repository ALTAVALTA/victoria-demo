# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout = io.open("_imgclick_check.txt", "w", encoding="utf-8")

s = io.open("index.html", encoding="utf-8").read()

# 1) Все обработчики кликов / onclick / data-атрибуты
print("=== СКРИПТЫ: клики и data-атрибуты ===")
for m in re.finditer(r"(onclick|addEventListener\(['\"]click|data-open-form|data-service|data-photo|data-img|querySelectorAll\(['\"]\.(?:work-card|img-wrap|works-grid))", s):
    start = max(0, m.start()-80)
    print("...%s..." % s[start:m.end()+80].replace("\n", " "))
    print("---")

# 2) есть ли вообще обработчик на .img-wrap / карточке / картинке
print()
print("=== ИЩУ ОБРАБОТЧИКИ НА ФОТО ===")
for pat in ["img-wrap", "work-card", "querySelectorAll", "addEventListener"]:
    hits = [m.start() for m in re.finditer(re.escape(pat), s)]
    print("%s: %d вхождений" % (pat, len(hits)))

# 3) JS-блоки: вывести все addEventListener
print()
print("=== ВСЕ addEventListener ===")
for m in re.finditer(r"addEventListener\([^)]*\)", s):
    print(m.group(0)[:200])
