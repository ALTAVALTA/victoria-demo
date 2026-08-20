# -*- coding: utf-8 -*-
"""Пиксельный поиск золотой AVA в нижней части скрина V2."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image

im = Image.open(r'C:\Users\PORTAL\.openclaw\workspace\screenshots\desktop_2test_full.png')
w, h = im.size
print('size', w, h)

# ищем в нижних 1000px золотые пиксели (V1 использует #c19a5b / #f5d9a8 / #f7e3b5)
targets = [(193, 154, 91), (245, 217, 168), (247, 227, 181), (185, 141, 84)]
found = []
# сэмпл каждые 2px
for y in range(h - 1000, h, 2):
    for x in range(0, w, 2):
        r, g, b = im.getpixel((x, y))[:3]
        for tr, tg, tb in targets:
            if abs(r-tr) < 25 and abs(g-tg) < 25 and abs(b-tb) < 25:
                found.append((x, y, (r, g, b)))
                break
    if len(found) > 12:
        break
print('золотые пиксели найдены:', len(found))
for f in found[:12]:
    print(' ', f)
