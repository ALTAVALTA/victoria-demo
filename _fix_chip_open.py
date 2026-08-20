# -*- coding: utf-8 -*-
"""Добавляем подсветку чипа при открытии формы с data-service (кнопки "Записаться" в карточках)."""
import io

data = io.open('index.html', encoding='utf-8').read()

old = """    if(service){
      for(var i=0;i<serviceSelect.options.length;i++){
        if(serviceSelect.options[i].text===service){serviceSelect.selectedIndex=i;break;}
      }
    }"""
assert data.count(old) == 1, 'openModal service block not found'
new = """    if(service){
      serviceSelect.value=service;
      var chip=document.querySelector('.chip[data-service="'+service+'"]');
      if(chip){chips.forEach(function(x){x.classList.remove('active');});chip.classList.add('active');}
    }"""
data = data.replace(old, new)

io.open('index.html', 'w', encoding='utf-8').write(data)
print('OK')
