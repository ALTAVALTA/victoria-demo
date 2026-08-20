# -*- coding: utf-8 -*-
"""Сборка _deploy_2test из 2test_demo."""
import io, os, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '2test_demo')
DST = os.path.join(HERE, '_deploy_2test')

if os.path.exists(DST):
    shutil.rmtree(DST)
os.makedirs(DST)

shutil.copy2(os.path.join(SRC, 'index.html'), os.path.join(DST, 'index.html'))
for sub in ('img', 'fonts'):
    src = os.path.join(SRC, sub)
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join(DST, sub))

total = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(DST) for f in fs)
print('OK ->', DST, f'{total/1024:.0f} KB')
