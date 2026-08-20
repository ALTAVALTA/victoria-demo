# -*- coding: utf-8 -*-
"""Сбор промптов трёх версий: v4 (наша), B, свежая."""
import io
import glob
import os
import re

out = []

# 1. Промпт нашей (v4)
for p in [r'landings/victoria/prompt_v4.md', r'landings/victoria/prompt_victoria_v4_A.md']:
    if os.path.exists(p):
        out.append('===== %s (%d байт) =====' % (os.path.basename(p), os.path.getsize(p)))
        data = io.open(p, encoding='utf-8').read()
        out.append(data[:6000])
        out.append('')
        out.append('...[далее %d символов]...' % max(0, len(data) - 6000))

# 2. Промпт B
p = r'landings/victoria/_archive_B/prompt_victoria_v4_B.md'
if os.path.exists(p):
    out.append('===== %s (%d байт) =====' % (os.path.basename(p), os.path.getsize(p)))
    data = io.open(p, encoding='utf-8').read()
    out.append(data[:6000])

io.open(r'landings/victoria/_deploy/_prompts_dump.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written')
