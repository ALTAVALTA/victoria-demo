# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout = io.open("_js_dump.txt", "w", encoding="utf-8")

s = io.open("index.html", encoding="utf-8").read()

# Найти все <script>...</script> и вывести
scripts = re.findall(r"<script[^>]*>(.*?)</script>", s, re.S)
print("=== СКРИПТОВ: %d ===" % len(scripts))
for i, sc in enumerate(scripts):
    print("\n--- SCRIPT %d (%d симв) ---" % (i+1, len(sc)))
    print(sc[:6000])
