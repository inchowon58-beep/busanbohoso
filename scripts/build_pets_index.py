# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(r"F:/보호소신규러브몽/site/pets/index.html")
OUT = ROOT / "site" / "pets" / "index.html"

NAV = """<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="../index.html">
      <img class="logo-mark" src="../assets/logo-mark.svg" alt="" width="48" height="48">
      <span class="brand-text"><span class="brand-name">부산강아지파양 보호소 포켓몽</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-label="메뉴 열기">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links" id="site-nav">
      <a href="../index.html#consult">입소 안내</a>
      <a href="../index.html#busan-guide">센터 이용</a>
      <a href="index.html" aria-current="page">입양·보호 아이</a>
      <a href="../index.html#story">보호 일상</a>
      <a href="../index.html#faq">자주 묻는 질문</a>
    </nav>
  </div>
</header>
<script>
const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");
if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    const open = navLinks.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    navToggle.setAttribute("aria-label", open ? "메뉴 닫기" : "메뉴 열기");
  });
  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "메뉴 열기");
    });
  });
}
</script>"""

HEAD = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>입양·보호 아이들 | 포켓몽보호소</title>
  <meta name="description" content="포켓몽보호소에서 가족을 기다리는 강아지·고양이 입양 안내입니다.">
  <link rel="canonical" href="https://부산강아지파양.daumzine.co.kr/pets/">
  <link rel="icon" href="../assets/favicon.png" type="image/png">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Song+Myung&amp;display=swap">
  <link rel="stylesheet" href="../assets/css/site.css">
  <link rel="stylesheet" href="../assets/css/busan.css">
</head>
<body class="pm-site">
"""

TAIL = """
<footer>
  <div class="wrap">© 2026 포켓몽보호소 · 부산강아지파양 안내</div>
</footer>
<div class="pm-fab" aria-label="빠른 문의">
  <a class="pm-fab__btn pm-fab__btn--coral" href="tel:05057070401"><span>입소</span><small>상담</small></a>
  <a class="pm-fab__btn pm-fab__btn--green" href="tel:05053007779"><span>입양</span><small>문의</small></a>
</div>
</body>
</html>
"""


def main():
    text = SRC.read_text(encoding="utf-8")
    marker = '<div class="grid" id="grid">'
    start = text.index(marker)
    end = text.index("</div>\n</main>", start) + len("</div>")
    grid = text[start:end]
    grid = grid.replace('href="../pets/', 'href="')
    grid = grid.replace('src="../photos/', 'src="../photos/')

    body = f"""{HEAD}
{NAV}
<main class="pm-section pm-section--cream pm-pets-page">
  <div class="wrap">
    <div class="section-head pm-section-head">
      <div>
        <h1>가족을 기다리는 아이들</h1>
        <p>입양 상담 <strong>0505-300-7779</strong> · 예약 방문 후 만남을 진행합니다.</p>
      </div>
    </div>
    {grid}
    <p class="pm-pets-cta"><a class="btn-pm btn-pm-coral" href="tel:05053007779">입양 상담 전화</a></p>
  </div>
</main>
{TAIL}"""

    OUT.write_text(body, encoding="utf-8")
    count = body.count('article class="card"')
    print(f"Wrote {OUT} ({count} pets)")


if __name__ == "__main__":
    main()
