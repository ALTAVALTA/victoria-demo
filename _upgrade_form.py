# -*- coding: utf-8 -*-
"""Апгрейд плашки записи: rows=4, step=1800, спиннер на кнопке."""
import io

PATH = 'index.html'
data = io.open(PATH, encoding='utf-8').read()
orig = data

# 1. Комментарий rows=2 -> 4
old_ta = 'rows="2" placeholder="Пожелания: мастер, услуга, удобное время (необязательно)"'
new_ta = 'rows="4" placeholder="Пожелания: мастер, услуга, удобное время (необязательно)"'
assert data.count(old_ta) == 1, 'textarea pattern not found'
data = data.replace(old_ta, new_ta)

# 2. Время: шаг 30 минут
old_t = 'type="time" min="08:30" max="20:30"'
new_t = 'type="time" min="08:30" max="20:30" step="1800"'
assert data.count(old_t) == 1, 'time pattern not found'
data = data.replace(old_t, new_t)

# 3. Кнопка: спиннер + лейбл
old_btn = '<button class="btn btn-primary" type="submit" style="width:100%">Отправить заявку</button>'
new_btn = ('<button class="btn btn-primary" type="submit" style="width:100%">'
           '<span class="spinner" aria-hidden="true"></span>'
           '<span class="btn-label">Отправить заявку</span></button>')
assert data.count(old_btn) == 1, 'button pattern not found'
data = data.replace(old_btn, new_btn)

# 4. JS: переключение loading-класса вместо textContent
old_js1 = "btn.disabled=true;btn.textContent='Отправляем...';"
new_js1 = "btn.disabled=true;btn.classList.add('loading');btn.querySelector('.btn-label').textContent='Отправляем...';"
assert data.count(old_js1) == 1, 'js loading pattern not found'
data = data.replace(old_js1, new_js1)

old_js2 = "btn.disabled=false;btn.textContent='Отправить заявку';"
new_js2 = "btn.disabled=false;btn.classList.remove('loading');btn.querySelector('.btn-label').textContent='Отправить заявку';"
assert data.count(old_js2) == 2, 'js reset pattern x2 expected, got %d' % data.count(old_js2)
data = data.replace(old_js2, new_js2)

# 5. CSS спиннера
spinner_css = (
    '\n    .btn .spinner{display:none;width:16px;height:16px;'
    'border:2px solid rgba(255,255,255,.35);border-top-color:#fff;'
    'border-radius:50%;animation:spin .7s linear infinite;'
    'margin-right:8px;vertical-align:-2px}\n'
    '    .btn.loading .spinner{display:inline-block}\n'
    '    .btn.loading .btn-label{vertical-align:middle}\n'
    '    @keyframes spin{to{transform:rotate(360deg)}}\n'
)
assert data.count('</style>') >= 1, 'style close not found'
data = data.replace('</style>', spinner_css + '</style>', 1)

io.open(PATH, 'w', encoding='utf-8').write(data)
print('OK, bytes:', len(data) - len(orig), 'delta')
