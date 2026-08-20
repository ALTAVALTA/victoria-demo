# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

POL = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\img'
# 26 файлов PHOTO_01..26
missing = []
for i in range(1, 27):
    f = os.path.join(POL, 'PHOTO_%02d.jpg' % i)
    if not os.path.exists(f):
        missing.append(f)
print('missing in polnaya_demo:', missing if missing else 'нет, все 26 на месте')

# в 2TEST маркеры используют victoria_photoNN.jpg — файлы нужны как PHOTO_<название>.jpg
# названия маркеров 2TEST:
names = ['hero-entrance','hero-interior','hero-door','about-room','about-redwall','about-street',
         'svc-hair','svc-nails','svc-cosmo','svc-laser','svc-body','svc-pmu',
         'laser-cabinet','laser-detail','team-happy','team-work',
         'gal-street','gal-manicure','gal-autumn','gal-warm','gal-parking','gal-trees','gal-path','gal-sign','gal-redhouse','gal-white-door',
         'map-entrance']
# маппинг по описаниям из промпта (порядок 1-26)
mapping = {
 'hero-entrance':'21','hero-interior':'02','hero-door':'25',
 'about-room':'05','about-redwall':'06','about-street':'03',
 'svc-hair':'20','svc-nails':'07','svc-cosmo':'04','svc-laser':'08','svc-body':'17','svc-pmu':'14',
 'laser-cabinet':'18','laser-detail':'22','team-happy':'12','team-work':'16',
 'gal-street':'01','gal-manicure':'09','gal-autumn':'10','gal-warm':'11','gal-parking':'13',
 'gal-trees':'15','gal-path':'19','gal-sign':'23','gal-redhouse':'24','gal-white-door':'26',
 'map-entrance':'26'
}
print('mapping size:', len(mapping))
# проверим уникальность (26 должно быть уникальных)
from collections import Counter
c = Counter(mapping.values())
dups = [k for k, v in c.items() if v > 1]
print('дубли в маппинге:', dups)
