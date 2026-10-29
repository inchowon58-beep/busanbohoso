# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "site"

cat_path = ROOT / "busan-goyang-bohoso" / "index.html"
text = cat_path.read_text(encoding="utf-8")
text = text.replace("https://부산고양이파양.daumzine.co.kr", "https://부산고양이보호소.daumzine.co.kr")
text = text.replace("0efeeca61e7e566c91e519c5aabef6c13afd9c3b", "a22e2c44e10089c33f33b7afd58197ac6eee2de2")
text = text.replace("부산고양이파양", "부산고양이보호소")
text = text.replace("고양이 파양을 검색하신", "고양이 보호소를 검색하신")
text = text.replace(
    "부산에서 고양이 보호소·입소를 찾으실 때, 먼저 확인할 것은",
    "부산에서 고양이보호소를 찾으실 때, 먼저 확인할 것은",
)
text = text.replace(
    "<p class=\"pm-kicker\">부산 · 고양i보호소 · 고양i 입양</p>",
    "<p class=\"pm-kicker\">부산 · 고양i 보호 · 고양i 입양</p>",
)
text = text.replace("고양i보호소 · 고양i 입양을 찾", "고양i보호소·고양i 입양 안내를 찾")
text = text.replace("고양이보호소·고양i 입양을 찾", "고양i보호소·고양i 입양 안내를 찾")
text = text.replace("고양이보호소·고양이 입양을 찾", "고양i보호소·고양i 입양 안내를 찾")
# fix accidental 고양i
text = text.replace("고양i", "고양이")
text = text.replace(
    "        <h2>부산고양이보호소 · 부산고양i보호소</h2>",
    "        <h2>부산고양i보호소 · 입양·입소</h2>",
)
text = text.replace("부산고양i보호소 · 입양·입소", "부산고양이보호소 · 입양·입소")
cat_path.write_text(text, encoding="utf-8")

dog_path = ROOT / "busan-gangaji-bohoso" / "index.html"
d = dog_path.read_text(encoding="utf-8")
d = d.replace('href="assets/', 'href="/assets/')
d = d.replace('src="assets/', 'src="/assets/')
d = d.replace('href="pets/', 'href="/pets/')
d = d.replace('src="photos/', 'src="/photos/')
d = d.replace('src="stories/', 'src="/stories/')
d = d.replace('href="index.html"', 'href="./"')
d = re.sub(
    r'<meta name="naver-site-verification" content="[^"]+"',
    '<meta name="naver-site-verification" content="c2417d963fba5a4d109a5f124b1dc59543918eef"',
    d,
    count=1,
)
domain = "https://부산강아지보호소.daumzine.co.kr"
d = re.sub(r'<link rel="canonical" href="[^"]+"', f'<link rel="canonical" href="{domain}/"', d, count=1)
d = re.sub(r'<meta property="og:url" content="[^"]+"', f'<meta property="og:url" content="{domain}/"', d, count=1)
d = d.replace("https://부산강아지파양.daumzine.co.kr", domain)
d = d.replace("부산강아지파양 보호소 포켓몽", "부산강아지보호소 보호소 포켓몽")
d = d.replace('alt="부산강아지파양 보호소 포켓몽"', 'alt="부산강아지보호소 보호소 포켓몽"')
d = d.replace('<h1 class="pm-title">부산강아지파양</h1>', '<h1 class="pm-title">부산강아지보호소</h1>')
d = d.replace("포켓몽보호소 · 부산강아지파양", "포켓몽보호소 · 부산강아지보호소")
d = d.replace("© 2026 포켓몽보호소 · 부산강아지파양", "© 2026 포켓몽보호소 · 부산강아지보호소")
d = re.sub(
    r"<title>[^<]+</title>",
    "<title>부산강아지보호소 · 강아지 입양 · 입소 | 포켓몽보호소</title>",
    d,
    count=1,
)
d = d.replace("부산강아지파양 입소", "부산강아지보호소 입소")
d = d.replace("#top\">부산강아지파양</a>", "#top\">부산강아지보호소</a>")
dog_path.write_text(d, encoding="utf-8")
print("patched ok")
