# -*- coding: utf-8 -*-
"""Make Victoria's team card on main index.html link to master-victoria.html."""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")

DEP = r"C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy"
idx = io.open(DEP + r"\index.html", encoding="utf-8").read()

# Victoria's master-card block: wrap in <a href="master-victoria.html">
old = """          <div class="master-card">
            <span class="master-ava">В</span>
            <div>
              <b>Виктория</b>
              <div class="master-role">Ведущий мастер перманентного макияжа</div>
              <p>Татуаж бровей, губ и глаз, стрелки. Работает по предварительной записи — записывайтесь заранее.</p>
            </div>
          </div>"""

if old not in idx:
    # try to find actual block text via regex on name
    import re
    m = re.search(r'<div class="master-card">.*?<b>Виктория</b>.*?</div>\s*</div>', idx, re.S)
    if m:
        old = m.group(0)
    else:
        print("FAIL: Victoria card block not found")
        sys.exit(1)

new = ('<a class="master-card-link" href="master-victoria.html" style="display:block;text-decoration:none;color:inherit">'
       + old + '</a>')

idx = idx.replace(old, new, 1)
io.open(DEP + r"\index.html", "w", encoding="utf-8").write(idx)
print("OK: Victoria card linked to master-victoria.html")
print("link present:", 'href="master-victoria.html"' in idx)
