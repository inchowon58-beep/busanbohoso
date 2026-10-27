# -*- coding: utf-8 -*-
from pathlib import Path

PETS = Path(__file__).resolve().parents[1] / "site" / "pets"

NAV_OLD_START = '<header class="nav">'
NAV_OLD_END = '</script>'

NEW_NAV = """<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="../../index.html">
      <img class="logo-mark" src="../../assets/logo-mark.svg" alt="" width="48" height="48">
      <span class="brand-text"><span class="brand-name">부산강아지파양 보호소 포켓몽</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-label="메뉴 열기">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links" id="site-nav">
      <a href="../../index.html#consult">입소 안내</a>
      <a href="../../index.html#busan-guide">센터 이용</a>
      <a href="../../pets/index.html">입양·보호 아이</a>
      <a href="../../index.html#story">보호 일상</a>
      <a href="../../index.html#faq">자주 묻는 질문</a>
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


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    if "러브몽" not in text and "pm-site" in text and NEW_NAV[:40] in text:
        return False

    text = text.replace(" — 러브몽 보호소</title>", " | 포켓몽보호소</title>")
    text = text.replace("러브몽 보호소", "포켓몽보호소")
    text = text.replace("LOVE MONG", "POCKET MONG · BUSAN")
    text = text.replace("© 2026 러브몽보호소 · LOVEMONG SHELTER", "© 2026 포켓몽보호소 · 부산강아지파양 안내")

    if 'href="../../assets/css/site.css">' in text and "busan.css" not in text:
        text = text.replace(
            '<link rel="stylesheet" href="../../assets/css/site.css">',
            '<link rel="stylesheet" href="../../assets/css/site.css">\n  <link rel="stylesheet" href="../../assets/css/busan.css">',
        )

    if '<body>' in text:
        text = text.replace("<body>", '<body class="pm-site">', 1)

    if NAV_OLD_START in text:
        start = text.index(NAV_OLD_START)
        end = text.index(NAV_OLD_END, start) + len(NAV_OLD_END)
        text = text[:start] + NEW_NAV + text[end:]

    # Hide default callbar if present
    if "callbar" in text and "pm-fab" not in text:
        text = text.replace(
            '<div class="callbar">',
            '<div class="callbar" hidden>',
            1,
        )
        fab = """
<div class="pm-fab" aria-label="빠른 문의">
  <a class="pm-fab__btn pm-fab__btn--coral" href="tel:05057070401"><span>입소</span><small>상담</small></a>
  <a class="pm-fab__btn pm-fab__btn--green" href="tel:05053007779"><span>입양</span><small>문의</small></a>
</div>
"""
        text = text.replace("</body>", fab + "\n</body>")

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    n = 0
    for path in PETS.rglob("index.html"):
        if path.parent == PETS:
            continue
        if patch_file(path):
            n += 1
    print(f"Patched {n} pet detail pages")


if __name__ == "__main__":
    main()
