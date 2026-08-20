# -*- coding: utf-8 -*-
"""Накатить правки 14.08 на свежую базу remote (ac0214d) — финальная версия."""
import io, sys, re

PATH = 'index.html'
t = io.open(PATH, encoding='utf-8').read()
orig = t

# ---------- 1. CSS: категория над чипами ----------
css_old = '.chips-group{display:flex;flex-wrap:wrap;gap:8px;align-items:center}'
css_new = ('.chips-group{display:flex;flex-direction:column;gap:8px;align-items:stretch;'
           'margin-bottom:10px}.chips-group:last-of-type{margin-bottom:0}'
           '.chips-cat{font-size:11px;font-weight:700;letter-spacing:.08em;'
           'text-transform:uppercase;color:var(--muted);margin-bottom:2px}.chips-cat::after{content:":"}')
if css_old in t:
    t = t.replace(css_old, css_new)
    print('1. CSS chips: OK')
else:
    print('1. CSS chips: NOT FOUND')

# ---------- 2. Телефон: атрибуты ----------
phone_old = '<input id="fPhone" name="phone" type="tel" placeholder="+7 (___) ___-__-__" required>'
phone_new = ('<input id="fPhone" name="phone" type="tel" inputmode="tel" autocomplete="tel" '
             'placeholder="+7 (___) ___-__-__" maxlength="18" required>')
if phone_old in t:
    t = t.replace(phone_old, phone_new)
    print('2. Phone attrs: OK')
else:
    print('2. Phone attrs: NOT FOUND')

# ---------- 3a. JS: строгая валидация в submit ----------
js_old_valid = """    var name=document.getElementById('fName');
    var phone=document.getElementById('fPhone');
    var ok=true;
    [name,phone].forEach(function(inp){
      var valid=inp.value.trim().length>=2;
      if(inp===phone)valid=(inp.value.replace(/\\D/g,'').length>=10);
      inp.style.borderColor=valid?'':'#c0533f';
      if(!valid)ok=false;
    });
    if(!ok)return;"""
js_new_valid = """    var name=document.getElementById('fName');
    var phone=document.getElementById('fPhone');
    var ok=true;
    [name,phone].forEach(function(inp){
      var valid=inp.value.trim().length>=2;
      if(inp===phone)valid=isPhoneValid(inp.value);
      inp.style.borderColor=valid?'':'#c0533f';
      if(!valid)ok=false;
    });
    if(!ok){
      if(phone && !isPhoneValid(phone.value)){
        phone.setCustomValidity('Введите номер полностью: +7 (___) ___-__-__');
        phone.reportValidity();
      }
      return;
    }"""
if js_old_valid in t:
    t = t.replace(js_old_valid, js_new_valid)
    print('3a. JS valid: OK')
else:
    print('3a. JS valid: NOT FOUND')

# ---------- 3b. JS: функции маски + антидубль перед submit ----------
anchor_submit = "  form.addEventListener('submit',function(e){"
js_tools = """  // Маска телефона: +7 (XXX) XXX-XX-XX
  var phoneInput=document.getElementById('fPhone');
  function digitsOnly(v){return v.replace(/\\D/g,'');}
  function formatPhone(v){
    var d=digitsOnly(v);
    if(d.length===0)return '';
    if(d.charAt(0)==='8')d='7'+d.slice(1);
    if(d.charAt(0)==='9')d='7'+d;
    else if(d.charAt(0)!=='7')d='7'+d;
    d=d.slice(0,11);
    var r='+7';
    if(d.length>1)r+=' ('+d.slice(1,4);
    if(d.length>=4)r+=') '+d.slice(4,7);
    if(d.length>=7)r+='-'+d.slice(7,9);
    if(d.length>=9)r+='-'+d.slice(9,11);
    return r;
  }
  function isPhoneValid(v){
    var d=digitsOnly(v);
    return d.length===11 && d.charAt(0)==='7';
  }
  if(phoneInput){
    phoneInput.addEventListener('input',function(){
      var f=formatPhone(phoneInput.value);
      if(f!==phoneInput.value)phoneInput.value=f;
      phoneInput.setCustomValidity('');
    });
    phoneInput.addEventListener('blur',function(){
      var f=formatPhone(phoneInput.value);
      if(f!==phoneInput.value)phoneInput.value=f;
      phoneInput.setCustomValidity(isPhoneValid(phoneInput.value)?'':'Введите номер полностью: +7 (___) ___-__-__');
    });
  }
  var submitting=false;
  var submitSeq=0;
  """
if anchor_submit in t:
    t = t.replace(anchor_submit, js_tools + anchor_submit, 1)
    print('3b. JS tools: OK')
else:
    print('3b. JS tools anchor: NOT FOUND')

# ---------- 3c. JS: антидубль в начале submit ----------
js_old_sub = """  form.addEventListener('submit',function(e){
    e.preventDefault();
"""
js_new_sub = """  form.addEventListener('submit',function(e){
    e.preventDefault();
    if(submitting){return;}
    submitting=true;
    var mySeq=++submitSeq;
"""
# важно: после вставки 3b anchor уже содержит js_tools — поэтому ищем оригинальный (с учётом, что он теперь после tools)
if js_old_sub in t:
    t = t.replace(js_old_sub, js_new_sub, 1)
    print('3c. JS antisub: OK')
else:
    print('3c. JS antisub: NOT FOUND')

# ---------- 3d. JS: guard в .then ----------
js_old_fetch = """    }).then(function(res){
      if(btn){btn.disabled=false;btn.classList.remove('loading');btn.querySelector('.btn-label').textContent='Отправить заявку';}
      if(res&&res.ok){"""
js_new_fetch = """    }).then(function(res){
      if(mySeq!==submitSeq){return;}
      if(btn){btn.disabled=false;btn.classList.remove('loading');btn.querySelector('.btn-label').textContent='Отправить заявку';}
      if(res&&res.ok){"""
if js_old_fetch in t:
    t = t.replace(js_old_fetch, js_new_fetch, 1)
    print('3d. JS fetch guard: OK')
else:
    print('3d. JS fetch guard: NOT FOUND')

# ---------- 3e. JS: guard в catch + сброс submitting ----------
js_old_catch = """    }).catch(function(){
      if(btn){btn.disabled=false;btn.classList.remove('loading');btn.querySelector('.btn-label').textContent='Отправить заявку';}
      alert('Не удалось отправить. Позвоните нам: +7 (911) 865-44-60');
    });"""
js_new_catch = """    }).catch(function(){
      if(mySeq!==submitSeq){return;}
      if(btn){btn.disabled=false;btn.classList.remove('loading');btn.querySelector('.btn-label').textContent='Отправить заявку';}
      submitting=false;
      alert('Не удалось отправить. Позвоните нам: +7 (911) 865-44-60');
    });"""
if js_old_catch in t:
    t = t.replace(js_old_catch, js_new_catch, 1)
    print('3e. JS catch: OK')
else:
    print('3e. JS catch: NOT FOUND')

# ---------- 3f. JS: успех — сброс submitting ----------
js_old_success = """      if(res&&res.ok){
        form.hidden=true;
        success.hidden=false;
      }else{"""
js_new_success = """      if(res&&res.ok){
        submitting=false;
        form.hidden=true;
        success.hidden=false;
      }else{
        submitting=false;"""
if js_old_success in t:
    t = t.replace(js_old_success, js_new_success, 1)
    print('3f. JS success: OK')
else:
    print('3f. JS success: NOT FOUND')

if t == orig:
    print('!!! НИЧЕГО НЕ ИЗМЕНИЛОСЬ')
    sys.exit(1)

io.open(PATH, 'w', encoding='utf-8').write(t)
print('SAVED, diff bytes:', len(t) - len(orig))

# проверка синтаксиса
ms = re.search(r'<script[^>]*>([\s\S]*?)</script>', t)
if ms:
    try:
        compile(ms.group(1), '<js>', 'exec')
        print('JS SYNTAX: OK')
    except SyntaxError as e:
        print('JS SYNTAX ERROR:', e)
