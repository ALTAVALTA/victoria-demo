# -*- coding: utf-8 -*-
import io, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

V1 = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\polnaya_demo\index.html'
V2 = r'C:\Users\PORTAL\.openclaw\workspace\landings\victoria\2test_demo\index.html'

def analyze(p):
    t = io.open(p, encoding='utf-8').read()
    res = {}
    res['len'] = len(t)
    # секции
    secs = re.findall(r'<section[^>]*>', t)
    res['sections'] = []
    for s in secs:
        m_id = re.search(r'id="([^"]+)"', s)
        m_cls = re.search(r'class="([^"]+)"', s)
        res['sections'].append((m_id.group(1) if m_id else '', m_cls.group(1) if m_cls else ''))
    # фото
    imgs = re.findall(r'src="(img/PHOTO_[^"]+)"', t)
    res['n_imgs'] = len(imgs)
    res['uniq_imgs'] = len(set(imgs))
    # фичи
    for kw in ['lightbox', 'lb-', 'modal', 'faq', 'counter', 'chips', 'data-open-form', 'tabs', 'accordion']:
        res[kw] = len(re.findall(kw, t, re.I))
    # телефон
    tels = set(re.findall(r'\+7[\s(]*\d{1,3}[\s)\-]*\d{2,3}[\s\-]*\d{2}[\s\-]*\d{2}', t))
    res['phones'] = tels
    # шрифты
    res['fonts'] = sorted(set(re.findall(r'font-family:[\'"]?([A-Za-z ]+)[\'"]?', t)))[:8]
    # CTA
    cta = re.findall(r'<a[^>]*class="btn[^"]*"[^>]*>([^<]+)', t)
    res['cta'] = [c.strip() for c in cta][:12]
    # форма
    res['form'] = 'bookForm' in t
    res['worker'] = 'workers.dev' in t
    res['select'] = '<select' in t
    # заголовки h2
    h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', t, re.S)
    res['h2'] = [re.sub(r'<[^>]+>', '', h).strip()[:70] for h in h2[:14]]
    return res

a1 = analyze(V1)
a2 = analyze(V2)

print('════════ СРАВНЕНИЕ V1 (polnaya_demo) vs V2 (2test_demo) ════════')
print()
print('РАЗМЕР: V1 =', a1['len'], '| V2 =', a2['len'])
print()
print('СЕКЦИИ V1:', a1['sections'])
print('СЕКЦИИ V2:', a2['sections'])
print()
print('ФОТО: V1 =', a1['n_imgs'], '| V2 =', a2['n_imgs'], '(uniq', a1['uniq_imgs'], '/', a2['uniq_imgs'], ')')
print()
print('ФИЧИ:')
for kw in ['lightbox', 'modal', 'faq', 'counter', 'chips', 'tabs', 'accordion']:
    print(f'  {kw}: V1={a1[kw]} V2={a2[kw]}')
print()
print('ТЕЛЕФОНЫ V1:', a1['phones'])
print('ТЕЛЕФОНЫ V2:', a2['phones'])
print()
print('ШРИФТЫ V1:', a1['fonts'])
print('ШРИФТЫ V2:', a2['fonts'])
print()
print('CTA V1:', a1['cta'])
print('CTA V2:', a2['cta'])
print()
print('ФОРМА: V1 form=', a1['form'], 'worker=', a1['worker'], 'select=', a1['select'], '| V2 form=', a2['form'], 'worker=', a2['worker'], 'select=', a2['select'])
print()
print('H2 V1:')
for h in a1['h2']: print('  -', h)
print('H2 V2:')
for h in a2['h2']: print('  -', h)
