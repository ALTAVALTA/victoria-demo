# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout = io.open("_gallery_dump.txt", "w", encoding="utf-8")

s = io.open("index.html", encoding="utf-8").read()

print("=== ВСЕ ВХОЖДЕНИЯ 'галере' (без учёта регистра) ===")
for m in re.finditer(r"галере", s, re.I):
    start = max(0, m.start()-250)
    end = min(len(s), m.end()+350)
    print("--- позиция %d ---" % m.start())
    print(s[start:end].replace("\n", " "))
    print()

print()
print("=== ВСЕ ВХОЖДЕНИЯ 'листай' ===")
for m in re.finditer(r"листай", s, re.I):
    start = max(0, m.start()-200)
    end = min(len(s), m.end()+300)
    print("--- позиция %d ---" % m.start())
    print(s[start:end].replace("\n", " "))
    print()

print()
print("=== ВСЕ ВХОЖДЕНИЯ 'Загляните' ===")
for m in re.finditer(r"Загляните", s, re.I):
    start = max(0, m.start()-150)
    end = min(len(s), m.end()+400)
    print("--- позиция %d ---" % m.start())
    print(s[start:end].replace("\n", " "))
    print()
