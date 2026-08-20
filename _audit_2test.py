# -*- coding: utf-8 -*-
import io, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html'
t = io.open(p, encoding='utf-8').read()

print('LEN', len(t))
print('--- фенсы ``` ---')
print('начинается с ```:', t.startswith('```'))
print('содержит ```:', '```' in t)

print('--- фото ---')
imgs = re.findall(r'src="(img/PHOTO_[^"]+)"', t)
print('img PHOTO:', len(imgs), 'unique:', len(set(imgs)))
missing = [f for f in set(imgs) if not os.path.exists(os.path.join(os.path.dirname(p), f))]
print('битых (нет файла):', missing if missing else 'нет')

print('--- маркеры @@PHOTO ---')
print('@@PHOTO:', len(re.findall(r'@@PHOTO', t)))

print('--- отзывы ---')
print('Анжелика:', 'Анжелика' in t, '| Максим Гавриличев:', 'Максим Гавриличев' in t, '| Елена Димитриенко:', 'Елена Димитриенко' in t, '| Наталья Б:', 'Наталья Б' in t)
print('выдуманные (Марина/Екатерина/Ольга/Светлана как авторы):', len(re.findall(r'rev-who"><span class="ava">[МЕОС]</span><div><b>(Марина|Екатерина|Ольга|Светлана)</b>', t)))

print('--- подпись ---')
print('ALTAVALTA:', 'ALTAVALTA' in t, '| footer-brand:', 'footer-brand' in t, '| brand-core:', 'brand-core' in t)

print('--- плашка ---')
print('demo-ribbon:', 'demo-ribbon' in t, '| demoRemove:', 'demoRemove' in t)

print('--- воркер/защита ---')
print('alert Демо-режим:', 'Демо-режим' in t)

print('--- аватарки ---')
for a in ['avatar_1.jpg', 'avatar_2.jpg', 'avatar_3.jpg', 'avatar_4.jpg']:
    print(a, ':', os.path.exists(os.path.join(os.path.dirname(p), 'img', 'avatars', a)))

print('--- div баланс ---')
print('div открытий:', len(re.findall(r'<div[ >]', t)), 'закрытий:', len(re.findall(r'</div>', t)))
