# -*- coding: utf-8 -*-
"""Когда пропал .brand-sub: проверка по коммитам."""
import io
import re
import subprocess

path = 'landings/victoria/_deploy/index.html'
revs = ['9bc25b50', 'b678eb84', 'deb51311', 'dc86bfb3', 'a5f01c10', '68a44a99', 'ef77bc5c',
        '8f1a7d03', 'da0bc56d']

for rev in revs:
    try:
        raw = subprocess.check_output(['git', 'show', rev + ':' + path],
                                      cwd=r'C:\Users\PORTAL\.openclaw\workspace')
        data = raw.decode('utf-8', 'replace')
        has = '.brand-sub' in data
        m = re.search(r'\.brand-sub[^{]*\{[^}]*\}', data)
        rule = m.group(0)[:120] if m else '-'
        print('%-10s .brand-sub=%s  %s' % (rev, has, rule))
    except Exception:
        print('%-10s FILE NOT IN REV' % rev)
