# -*- coding: utf-8 -*-
import io, sys, urllib.request
sys.stdout = io.open("_verify_live.txt", "w", encoding="utf-8")

url = "https://altavalta.github.io/victoria-demo/"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

print("bytes:", len(html))
checks = {
    "Реальные работы мастеров": "Реальные работы мастеров" in html,
    "НЕТ 'нажмите на фото'": "нажмите на фото" not in html,
    "НЕТ 'листайте галерею'": "листайте галерею" not in html,
    "галерея 6 фото": "PHOTO_gallery_6.jpg" in html,
    "H1 Красота в центре": "Красота в центре Калининграда" in html,
    "статус открыто": "conStatus" in html,
    "Schema.org": "application/ld+json" in html,
}
for k, v in checks.items():
    print(("OK  " if v else "FAIL"), k)
