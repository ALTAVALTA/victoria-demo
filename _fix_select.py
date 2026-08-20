# -*- coding: utf-8 -*-
"""Fix: close fService select; verify rev-card count in HTML only."""
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")

DST = r"C:\Users\PORTAL\.openclaw\workspace\landings\victoria\_deploy\master-victoria.html"
c = io.open(DST, encoding="utf-8").read()

# close the fService select (it currently ends with <select ... hidden> without </select>)
old = '<select id="fService" name="service" hidden>'
if old in c:
    # only replace the one that is NOT followed by </select> shortly
    idx = c.find(old)
    after = c[idx+len(old):idx+len(old)+200]
    if "</select>" not in after[:50]:
        c = c[:idx+len(old)] + "</select>" + c[idx+len(old):]
        print("fixed fService select close")
    else:
        print("fService select already closed")
else:
    print("fService select not found")

io.open(DST, "w", encoding="utf-8").write(c)

# recount rev-card in HTML part only (after last </style>)
body = c[c.rfind("</style>"):]
print("rev-card in HTML:", body.count("rev-card"))

# recheck select balance
o = len(re.findall(r"<select[ >]", c))
cl = len(re.findall(r"</select>", c))
print(f"select balance: open={o} close={cl}")
