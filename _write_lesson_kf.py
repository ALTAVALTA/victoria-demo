# -*- coding: utf-8 -*-
"""Append урока про keyframes-конфликт в LESSONS.md."""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\PORTAL\.openclaw\workspace\landings\LESSONS.md'
t = io.open(p, encoding='utf-8').read()

lesson = '''

### ⚠️ Keyframes-конфликт: кастомная анимация в чужом HTML (16.08 15:45, подпись ALTAVALTA)
- **Инцидент:** вставил в 2test_demo (HTML нейронки) CSS подписи `.brand-core{animation:v-pulse 2s ...}`, но НЕ проверил, есть ли в файле свой `@keyframes v-pulse`. У нейронки он был (opacity-мигание) — и перекрыл мой «светящийся» (в CSS при одинаковых именах побеждает последний объявленный). Подпись мигала прозрачностью вместо свечения.
- **Причина:** копировал CSS из V1 в V2 по памяти, не сверившись с целевым файлом.
- **Фикс (стандарт):** кастомные keyframes называть УНИКАЛЬНЫМИ именами с суффиксом бренда (`v-pulse-av`, `v-breathe`) — никогда не `v-pulse`/`fade`/`pulse` (нейронка их генерит в каждом HTML). Перед вставкой — `grep @keyframes <имя>` в целевом файле.
- **Решение Кэпа (16.08 15:49):** «дышащее свечение» вместо мигания/чистого свечения: цикл от цвета (золото, без glow) до свечения (светлее + text-shadow) и обратно, медленно (3.4s ease-in-out). Эталон-эффект подписи = плавное дыхание светом.
- Проверка результата — руками Кэпа, НЕ вижном (правило Кэпа).

'''
t = t.rstrip() + '\n' + lesson
io.open(p, 'w', encoding='utf-8').write(t)
print('LESSONS.md дописан:', len(t), 'chars')
