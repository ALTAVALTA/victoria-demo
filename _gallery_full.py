# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout = io.open("_gallery_full.txt", "w", encoding="utf-8")

s = io.open("index.html", encoding="utf-8").read()

i = s.find('id="gallery"')
if i < 0:
    # ищем секцию по overline Атмосфера
    j = s.find('Атмосфера')
    i = max(0, j - 300)
print("=== СЕКЦИЯ ГАЛЕРЕИ (html) ===")
# от начала секции до конца: найдём '</section>' после i
end = s.find('</section>', i)
print(s[i:end+10])
