# -*- coding: utf-8 -*-
"""Апгрейд формы:
1) Чипы услуг вместо селекта (но select оставляем скрытым как value-контейнер)
2) Поле времени -> select со слотами 08:30..20:30 шаг 30 мин (пикер на мобиле игнорит step)
3) CSS чипов
"""
import io

PATH = 'index.html'
data = io.open(PATH, encoding='utf-8').read()
orig = data

# ---------- 1. ЧИПЫ УСЛУГ ----------
# Находим блок select услуги (от <div class="field full"> до </div> после select)
old_service_start = '<div class="field full">\n          <label for="fService">Услуга</label>\n          <select id="fService" name="service">'
assert data.count(old_service_start) == 1, 'service select start not found'
sel_start = data.find(old_service_start)
sel_end = data.find('</select>', sel_start) + len('</select>')
# закрывающий </div> блока field full
div_end = data.find('</div>', sel_end)

services = [
    ('Ногти', ['Маникюр и гель-лак', 'Педикюр', 'Наращивание ногтей']),
    ('Волосы', ['Стрижка женская', 'Стрижка мужская', 'Стрижка детская',
                'Окрашивание волос', 'Кератиновое выпрямление', 'Праздничная укладка']),
    ('Лицо', ['Перманентный макияж', 'Удаление татуажа лазером',
              'Карбоновый пилинг', 'Безинъекционная биоревитализация', 'Наращивание ресниц']),
    ('Тело', ['Лазерная эпиляция', 'Элос-эпиляция', 'Массаж / уход для тела']),
]

def chip_html(cat, items):
    chips = '\n'.join(
        '              <button type="button" class="chip" data-service="%s">%s</button>' % (s, s)
        for s in items)
    return (
        '<div class="field full">\n'
        '          <label for="fService">Услуга</label>\n'
        '          <div class="chips" id="serviceChips">\n'
        '            <div class="chips-group"><span class="chips-cat">%s</span>\n%s\n            </div>\n'
        '            <div class="chips-group"><span class="chips-cat">%s</span>\n%s\n            </div>\n'
        '            <div class="chips-group"><span class="chips-cat">%s</span>\n%s\n            </div>\n'
        '            <div class="chips-group"><span class="chips-cat">%s</span>\n%s\n            </div>\n'
        '            <button type="button" class="chip chip-other" data-service="Другое / подскажет администратор">Другое</button>\n'
        '          </div>\n'
        '          <select id="fService" name="service" hidden>' % (cat[0], cat[1], cat[2], cat[3]) +
        ''.join('<option>%s</option>' % s for s in
                ['Маникюр и гель-лак', 'Педикюр', 'Наращивание ногтей',
                 'Стрижка женская', 'Стрижка мужская', 'Стрижка детская',
                 'Окрашивание волос', 'Кератиновое выпрямление', 'Праздничная укладка',
                 'Перманентный макияж', 'Удаление татуажа лазером',
                 'Карбоновый пилинг', 'Безинъекционная биоревитализация', 'Наращивание ресниц',
                 'Лазерная эпиляция', 'Элос-эпиляция', 'Массаж / уход для тела',
                 'Другое / подскажет администратор']) +
        '</select>\n'
        '        </div>'
    )

new_service_block = (
    '<div class="field full">\n'
    '          <label for="fService">Услуга</label>\n'
    '          <div class="chips" id="serviceChips">\n'
    '            <div class="chips-group"><span class="chips-cat">Ногти</span>\n'
    '              <button type="button" class="chip" data-service="Маникюр и гель-лак">Маникюр и гель-лак</button>\n'
    '              <button type="button" class="chip" data-service="Педикюр">Педикюр</button>\n'
    '              <button type="button" class="chip" data-service="Наращивание ногтей">Наращивание ногтей</button>\n'
    '            </div>\n'
    '            <div class="chips-group"><span class="chips-cat">Волосы</span>\n'
    '              <button type="button" class="chip" data-service="Стрижка женская">Стрижка женская</button>\n'
    '              <button type="button" class="chip" data-service="Стрижка мужская">Стрижка мужская</button>\n'
    '              <button type="button" class="chip" data-service="Стрижка детская">Стрижка детская</button>\n'
    '              <button type="button" class="chip" data-service="Окрашивание волос">Окрашивание волос</button>\n'
    '              <button type="button" class="chip" data-service="Кератиновое выпрямление">Кератиновое выпрямление</button>\n'
    '              <button type="button" class="chip" data-service="Праздничная укладка">Праздничная укладка</button>\n'
    '            </div>\n'
    '            <div class="chips-group"><span class="chips-cat">Лицо</span>\n'
    '              <button type="button" class="chip" data-service="Перманентный макияж">Перманентный макияж</button>\n'
    '              <button type="button" class="chip" data-service="Удаление татуажа лазером">Удаление татуажа лазером</button>\n'
    '              <button type="button" class="chip" data-service="Карбоновый пилинг">Карбоновый пилинг</button>\n'
    '              <button type="button" class="chip" data-service="Безинъекционная биоревитализация">Безинъекционная биоревитализация</button>\n'
    '              <button type="button" class="chip" data-service="Наращивание ресниц">Наращивание ресниц</button>\n'
    '            </div>\n'
    '            <div class="chips-group"><span class="chips-cat">Тело</span>\n'
    '              <button type="button" class="chip" data-service="Лазерная эпиляция">Лазерная эпиляция</button>\n'
    '              <button type="button" class="chip" data-service="Элос-эпиляция">Элос-эпиляция</button>\n'
    '              <button type="button" class="chip" data-service="Массаж / уход для тела">Массаж / уход для тела</button>\n'
    '            </div>\n'
    '            <button type="button" class="chip chip-other" data-service="Другое / подскажет администратор">Другое</button>\n'
    '          </div>\n'
    '          <select id="fService" name="service" hidden>'
    '<option>Маникюр и гель-лак</option><option>Педикюр</option><option>Наращивание ногтей</option>'
    '<option>Стрижка женская</option><option>Стрижка мужская</option><option>Стрижка детская</option>'
    '<option>Окрашивание волос</option><option>Кератиновое выпрямление</option><option>Праздничная укладка</option>'
    '<option>Перманентный макияж</option><option>Удаление татуажа лазером</option><option>Карбоновый пилинг</option>'
    '<option>Безинъекционная биоревитализация</option><option>Наращивание ресниц</option>'
    '<option>Лазерная эпиляция</option><option>Элос-эпиляция</option><option>Массаж / уход для тела</option>'
    '<option>Другое / подскажет администратор</option>'
    '</select>\n'
    '        </div>'
)

data = data[:sel_start] + new_service_block + data[div_end:]

# ---------- 2. ВРЕМЯ -> SELECT СО СЛОТАМИ ----------
old_time = ('<div class="field">\n          <label for="fTime">Желаемое время</label>\n'
            '          <input id="fTime" name="time" type="time" min="08:30" max="20:30" step="1800">\n'
            '        </div>')
assert data.count(old_time) == 1, 'time input not found'
slots = []
h, m = 8, 30
while h < 20 or (h == 20 and m <= 30):
    slots.append('%02d:%02d' % (h, m))
    m += 30
    if m >= 60:
        m = 0
        h += 1
opts = '\n'.join('              <option>%s</option>' % s for s in slots)
new_time = (
    '<div class="field">\n'
    '          <label for="fTime">Желаемое время</label>\n'
    '          <select id="fTime" name="time">\n'
    '            <option value="">Удобное время</option>\n'
    + opts + '\n'
    '          </select>\n'
    '        </div>')
data = data.replace(old_time, new_time)

# ---------- 3. CSS ЧИПОВ ----------
chips_css = '''
    .chips{display:flex;flex-direction:column;gap:10px}
    .chips-group{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
    .chips-cat{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);min-width:52px}
    .chip{display:inline-block;padding:9px 14px;border-radius:999px;border:1.5px solid var(--line);background:#fff;font-family:var(--font-body);font-size:13.5px;color:var(--ink);cursor:pointer;transition:border-color .2s,background .2s,color .2s;line-height:1.2}
    .chip:hover{border-color:var(--leaf)}
    .chip.active{background:var(--leaf);border-color:var(--leaf);color:#fff}
    .chip-other{border-style:dashed}
    .chip-other.active{background:var(--pine);border-color:var(--pine);color:#fff}
'''
data = data.replace('</style>', chips_css + '</style>', 1)

# ---------- 4. JS ЧИПОВ ----------
# Хук: после serviceSelect объявления добавить логику чипов
old_js = "var serviceSelect=document.getElementById('fService');"
assert data.count(old_js) == 1, 'serviceSelect js not found'
chips_js = (
    "var serviceSelect=document.getElementById('fService');\n"
    "  var chips=document.querySelectorAll('.chip');\n"
    "  chips.forEach(function(c){c.addEventListener('click',function(){\n"
    "    chips.forEach(function(x){x.classList.remove('active');});\n"
    "    c.classList.add('active');\n"
    "    serviceSelect.value=c.getAttribute('data-service');\n"
    "  });});\n"
)
data = data.replace(old_js, chips_js)

io.open(PATH, 'w', encoding='utf-8').write(data)
print('OK, delta bytes:', len(data) - len(orig))
