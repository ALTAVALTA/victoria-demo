# -*- coding: utf-8 -*-
import re, io, sys

old_path = r"index_backup_20260815.html"  # ДО апгрейда (14.08) — та, в которой Кэп был уверен
new_path = r"index.html"                  # ПОСЛЕ апгрейда (15.08) — гибрид

def read(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def headings(html):
    # h1, h2, h3 с текстом
    out = []
    for m in re.finditer(r"<h([123])[^>]*>(.*?)</h\1>", html, re.S | re.I):
        txt = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        txt = re.sub(r"\s+", " ", txt)
        if txt:
            out.append((int(m.group(1)), txt))
    return out

old = read(old_path)
new = read(new_path)

import sys
sys.stdout = io.open("_diff_show_out.txt", "w", encoding="utf-8")

print("=== РАЗМЕРЫ ===")
print("ДО  (14.08): %d байт" % len(old))
print("ПОСЛЕ (15.08): %d байт" % len(new))
print()

print("=== ЗАГОЛОВКИ: ДО (14.08) ===")
for lvl, t in headings(old):
    print("  h%d: %s" % (lvl, t))
print()

print("=== ЗАГОЛОВКИ: ПОСЛЕ (15.08) ===")
for lvl, t in headings(new):
    print("  h%d: %s" % (lvl, t))
print()

# Ключевые маркеры
for name, pat in [("галерея", r"gallery"), ("рейтинг", r"24 оценки|4\.\d|рейтинг"), 
                  ("статус открыто", r"conStatus|открыто|закрыто"), ("Schema.org", r"application/ld\+json"),
                  ("штамп в hero", r"запись\s*08:30|08:30–20:30|штамп|stamp")]:
    o = bool(re.search(pat, old, re.I))
    n = bool(re.search(pat, new, re.I))
    print("  %-18s ДО: %s | ПОСЛЕ: %s" % (name, "+" if o else "-", "+" if n else "-"))
