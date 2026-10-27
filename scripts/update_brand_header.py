# -*- coding: utf-8 -*-
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site"
old = (
    '<span><span class="brand-name">포켓몽보호소</span>'
    '<span class="brand-sub">POCKET MONG · BUSAN</span></span>'
)
new = '<span class="brand-text"><span class="brand-name">부산강아지파양 보호소 포켓몽</span></span>'
old_alt = 'alt="포켓몽보호소"'
new_alt = 'alt="부산강아지파양 보호소 포켓몽"'

n = 0
for path in root.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    orig = text
    text = text.replace(old, new)
    text = text.replace(old_alt, new_alt)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        n += 1
print(f"updated {n} files")
