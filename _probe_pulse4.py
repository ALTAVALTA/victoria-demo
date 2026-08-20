# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

def extract_kf(t, name):
    m = re.search(r'@keyframes\s+' + name + r'\s*\{', t)
    if not m:
        return None
    i = m.end() - 1
    depth = 0
    while i < len(t):
        if t[i] == '{':
            depth += 1
        elif t[i] == '}':
            depth -= 1
            if depth == 0:
                return t[m.start():i+1]
        i += 1
    return None

t1 = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html', encoding='utf-8').read()
t2 = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html', encoding='utf-8').read()

k1 = extract_kf(t1, 'v-pulse')
k2 = extract_kf(t2, 'v-pulse')
print('=== V1 v-pulse (полный) ===')
print(k1)
print()
print('=== V2 v-pulse (полный) ===')
print(k2)
print()

# где в V2 мой CSS (светящийся) уже вставлен? может, я вставил и он есть, но перекрыт?
print('V2: есть ли светящийся v-pulse (text-shadow):', 'text-shadow' in (k2 or ''))
# есть ли в V2 вообще второй @keyframes v-pulse
print('V2: сколько @keyframes v-pulse:', len(re.findall(r'@keyframes\s+v-pulse', t2)))
