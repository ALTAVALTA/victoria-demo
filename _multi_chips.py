# -*- coding: utf-8 -*-
"""Мультивыбор чипов:
1. Клик по чипу — toggle (можно несколько)
2. При открытии формы с data-service — добавить чип в выбор
3. В payload service = выбранные через запятую
"""
import io
import re

PATH = r'landings/victoria/_deploy/index.html'
data = io.open(PATH, encoding='utf-8').read()
orig = data

# --- 1. JS: клик по чипу: toggle вместо single-select ---
old_click = """  var chips=document.querySelectorAll('.chip');
  chips.forEach(function(c){c.addEventListener('click',function(){
    chips.forEach(function(x){x.classList.remove('active');});
    c.classList.add('active');
    serviceSelect.value=c.getAttribute('data-service');
  });});"""
assert data.count(old_click) == 1, 'chips click js not found'
new_click = """  var chips=document.querySelectorAll('.chip');
  var selectedServices=[];
  chips.forEach(function(c){c.addEventListener('click',function(){
    c.classList.toggle('active');
    var svc=c.getAttribute('data-service');
    var idx=selectedServices.indexOf(svc);
    if(idx>-1){selectedServices.splice(idx,1);}else{selectedServices.push(svc);}
    serviceSelect.value=selectedServices.join(', ');
  });});"""
data = data.replace(old_click, new_click)

# --- 2. JS: openModal с service — добавить чип в выбор (не снимая другие) ---
old_open = """    if(service){
      serviceSelect.value=service;
      var chip=document.querySelector('.chip[data-service="'+service+'"]');
      if(chip){chips.forEach(function(x){x.classList.remove('active');});chip.classList.add('active');}
    }"""
assert data.count(old_open) == 1, 'openModal service js not found'
new_open = """    if(service){
      if(selectedServices.indexOf(service)===-1){
        selectedServices.push(service);
        var chip=document.querySelector('.chip[data-service="'+service+'"]');
        if(chip){chip.classList.add('active');}
      }
      serviceSelect.value=selectedServices.join(', ');
    }"""
data = data.replace(old_open, new_open)

# --- 3. Submit payload: service уже берётся из serviceSelect (теперь через запятую) — ок.
# Но надо убедиться: payload.service = serviceSelect.value (строка через запятую) — уже так.
# Также при закрытии формы/успехе — сброс выбора
old_reset = "setTimeout(function(){if(!success.hidden){form.reset();form.hidden=false;success.hidden=true;}},300);"
assert data.count(old_reset) == 1, 'reset js not found'
new_reset = ("setTimeout(function(){if(!success.hidden){form.reset();form.hidden=false;success.hidden=true;"
             "selectedServices=[];chips.forEach(function(x){x.classList.remove('active');});serviceSelect.value='';}},300);")
data = data.replace(old_reset, new_reset)

io.open(PATH, 'w', encoding='utf-8').write(data)
print('OK, delta:', len(data) - len(orig))
