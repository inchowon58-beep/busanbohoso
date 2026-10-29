# 부산강아지파양 · 포켓몽보호소

정적 랜딩 사이트 (`site/`). 운영 도메인:
- **https://부산강아지파양.daumzine.co.kr/** → `site/index.html`
- **https://부산유기견센터.daumzine.co.kr/** → `site/busan-yugigyug/index.html` (호스트별 rewrite + middleware)

## 로컬 미리보기

```bash
cd site
python -m http.server 8080
```

브라우저: http://127.0.0.1:8080/

## GitHub

저장소: [inchowon58-beep/busanbohoso](https://github.com/inchowon58-beep/busanbohoso)

## Vercel 배포

1. [Vercel](https://vercel.com) → **Add New Project** → GitHub에서 `busanbohoso` 연결
2. 설정은 `vercel.json` 사용 (Root / Output Directory: **`site`**)
3. **Deploy** 후 Production URL 확인
4. **Project → Settings → Domains** 에 `부산강아지파양.daumzine.co.kr` 추가
5. Vercel이 안내하는 **DNS 레코드**를 daumzine(또는 DNS 관리처)에 등록  
   - 보통 `CNAME` → `cname.vercel-dns.com` (또는 Vercel 대시보드에 표시된 값)
6. SSL 발급 후 도메인 상태가 **Valid** 인지 확인

## 유지보수 스크립트

- `scripts/build_pets_index.py` — 입양 목록 재생성
- `scripts/patch_pet_pages.py` — 개별 입양 페이지 헤더 패치
- `scripts/update_brand_header.py` — 상단 브랜드 문구 일괄 변경
