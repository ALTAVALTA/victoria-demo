# -*- coding: utf-8 -*-
"""Фикс 2 багов (ассерты по факту): textarea CSS + payload из selectedServices."""
import io

PATH = r'landings/victoria/_deploy/index.html'
data = io.open(PATH, encoding='utf-8').read()
orig = data

old_css = '.field input,.field select{width:100%;padding:14px 15px;border-radius:12px;border:1.5px solid var(--line);background:#fff;font-family:var(--font-body);font-size:15px;color:var(--ink);transition:border-color .2s,box-shadow .2s;appearance:none;-webkit-appearance:none}'
assert data.count(old_css) == 1, 'field input css count %d' % data.count(old_css)
new_css = '.field input,.field select,.field textarea{width:100%;padding:14px 15px;border-radius:12px;border:1.5px solid var(--line);background:#fff;font-family:var(--font-body);font-size:15px;color:var(--ink);transition:border-color .2s,box-shadow .2s;appearance:none;-webkit-appearance:none}'
data = data.replace(old_css, new_css)

old_focus = '.field input:focus,.field select:focus{outline:none;border-color:var(--leaf);box-shadow:0 0 0 4px rgba(95,125,84,.15)}'
assert data.count(old_focus) == 1, 'focus css count %d' % data.count(old_focus)
new_focus = '.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--leaf);box-shadow:0 0 0 4px rgba(95,125,84,.15)}'
data = data.replace(old_focus, new_focus)

old_payload = "service:document.getElementById('fService')?document.getElementById('fService').value:'',"
assert data.count(old_payload) == 1, 'payload service not found'
new_payload = "service:selectedServices.length?selectedServices.join(', '):'Другое / подскажет администратор',"
data = data.replace(old_payload, new_payload)

io.open(PATH, 'w', encoding='utf-8').write(data)
print('OK, delta:', len(data) - len(orig))
