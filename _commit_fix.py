# -*- coding: utf-8 -*-
"""Коммит фикса коллизии .brand-name + урок в LESSONS.md."""
import io
import subprocess

# 1. Проверим LESSONS.md
lessons_path = r'landings/LESSONS.md'
data = io.open(lessons_path, encoding='utf-8').read()
print('LESSONS.md len:', len(data))

# 2. Урок про коллизию классов
lesson = '''
### ⚠️ Коллизия CSS-классов: подпись сломала логотип в шапке (14 авг 2026)
- **Симптом:** логотип студии «Виктория» в шапке стал мелким бежевым капсом вместо крупного зелёного Georgia.
- **Причина:** футерная подпись ALTAVALTA и логотип в шапке использовали **один и тот же класс `.brand-name`**. При создании подписи CSS перезаписали под футер (Jost 12px, капсом, #d8d2c2) → молча ударило по шапке.
- **Дополнительно:** `.brand-sub` (золотая подпись «студия красоты» под логотипом) вообще пропал в коммите b678eb84 при фиксе .brand-mark — восстановлен.
- **Правило:** перед перезаписью существующего CSS-класса — проверить, где он ещё используется (`grep` по HTML). Общие классы не перезаписывать — давать подписи/новым блокам **отдельные классы** (`.sig-name` для подписи, `.brand-name` оставить шапке).
- **Проверка после правок:** сравнить CSS шапки с А-эталоном (скрипт _header_css_diff.py), пиксельный скан цветов (vision врёт на мелком тексте).
'''
io.open(lessons_path, 'a', encoding='utf-8').write(lesson)
print('lesson appended')

# 3. Git коммит
subprocess.run(['git', 'add', '-A'], cwd=r'C:\Users\PORTAL\.openclaw\workspace', check=True)
r = subprocess.run(['git', 'commit', '-m',
                    'victoria: фикс коллизии .brand-name (подпись vs логотип шапки), восстановлен .brand-sub золотой; урок в LESSONS'],
                   cwd=r'C:\Users\PORTAL\.openclaw\workspace', capture_output=True, text=True)
print(r.stdout[-500:])
print(r.stderr[-300:])
