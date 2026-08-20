# -*- coding: utf-8 -*-
import io, sys
sys.stdout.reconfigure(encoding='utf-8')
t = io.open(r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\call_script_v4.md', encoding='utf-8').read()
print('LEN:', len(t))
checks = ['Пакет под ключ — десять тысяч', 'самозанятый', 'договор и чек будут',
          'Это просто макет', 'пусть учится на моём', 'Сначала посмотрите']
for c in checks:
    ok = c in t
    print(('OK  ' if ok else 'NO  ') + c)
# старые фразы должны исчезнуть
old = ['Сначала посмотрите, что это. Потом обсудим условия',
       'клиенты решат, что и маникюр у вас такой же, как этот сайт',
       'уже набросал, как мог бы выглядеть ваш сайт']
for c in old:
    print(('GONE' if c not in t else 'STAY') + '  ' + c[:60])
