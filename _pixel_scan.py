# -*- coding: utf-8 -*-
"""Пиксельный скан логотипа: проверяем наличие золотого (#d8b078) и тёмно-зелёного (#1c3527) в шапке."""
from PIL import Image
import io

img = Image.open('_shot_live_header2.png').convert('RGB')
w, h = img.size
print('size:', w, h)

# Зона шапки: верхние 120px, левая треть
crop = img.crop((0, 0, int(w * 0.45), 140))
px = crop.load()
cw, ch = crop.size

gold = (216, 176, 120)  # #d8b078
gold_deep = (186, 145, 82)  # #ba9152 примерно (--gold-deep может отличаться)
pine = (28, 53, 39)  # #1c3527

def count_near(target, tol=25):
    cnt = 0
    for y in range(0, ch, 2):
        for x in range(0, cw, 2):
            r, g, b = px[x, y]
            if abs(r - target[0]) <= tol and abs(g - target[1]) <= tol and abs(b - target[2]) <= tol:
                cnt += 1
    return cnt

print('gold-ish px:', count_near(gold))
print('gold_deep-ish px:', count_near(gold_deep))
print('pine-ish px:', count_near(pine))

# Ищем оба цвета в зоне
