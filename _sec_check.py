# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout = io.open("_sec_check.txt", "w", encoding="utf-8")

s = io.open("index.html", encoding="utf-8").read()

# Секция «Хочу как здесь» — найди по любому из вариантов
for key in ["Хочу как здесь", "нажмите на фото", "нажми на фото"]:
    i = s.find(key)
    if i >= 0:
        print("=== НАЙДЕНО: %r на позиции %d ===" % (key, i))
        print(s[max(0,i-300):i+1800])
        print()
        break
else:
    print("Секция не найдена. Ищу 'gallery' / 'want':")
    for key in ["gallery", "want", "portfolio", "work-grid"]:
        i = s.find(key)
        print("%r -> %d" % (key, i))
