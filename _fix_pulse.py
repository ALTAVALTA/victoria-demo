# -*- coding: utf-8 -*-
"""Фикс: уникальный keyframes v-pulse-av для подписи в V2 (не конфликтует с нейронкиным)."""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html'
t = io.open(p, encoding='utf-8').read()

OLD_KF = '@keyframes v-pulse{0%,100%{opacity:1}50%{opacity:.55}}'
NEW_KF = OLD_KF + '\n  @keyframes v-pulse-av{0%,62%{color:var(--gold);text-shadow:none}74%{color:#f5d9a8;text-shadow:0 0 10px rgba(245,217,168,.75)}84%{color:#f7e3b5;text-shadow:0 0 16px rgba(245,217,168,.95)}94%{color:var(--gold);text-shadow:none}}'

assert OLD_KF in t, 'нейронкин v-pulse не найден'
t = t.replace(OLD_KF, NEW_KF, 1)

OLD_ANIM = '.brand-core{color:var(--gold);animation:v-pulse 2s ease-in-out infinite}'
NEW_ANIM = '.brand-core{color:var(--gold);animation:v-pulse-av 2s ease-in-out infinite}'
assert OLD_ANIM in t, '.brand-core animation не найден'
t = t.replace(OLD_ANIM, NEW_ANIM, 1)

io.open(p, 'w', encoding='utf-8').write(t)
print('OK. v-pulse-av:', t.count('v-pulse-av'), 'вхождений')
print('нейронкин v-pulse остался:', t.count('@keyframes v-pulse{'))
