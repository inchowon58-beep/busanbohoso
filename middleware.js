const YUGIGYUG_HOSTS = new Set([
  "xn--l89at2a894aj7ccuad8ykls.daumzine.co.kr",
  "부산유기견센터.daumzine.co.kr",
]);

export const config = {
  matcher: ["/", "/index.html", "/robots.txt", "/sitemap.xml"],
};

export default function middleware(request) {
  const host = (request.headers.get("host") || "").split(":")[0].toLowerCase();
  if (!YUGIGYUG_HOSTS.has(host)) {
    return;
  }

  const url = new URL(request.url);
  const path = url.pathname;

  if (path === "/robots.txt") {
    url.pathname = "/busan-yugigyug/robots.txt";
    return Response.rewrite(url);
  }
  if (path === "/sitemap.xml") {
    url.pathname = "/busan-yugigyug/sitemap.xml";
    return Response.rewrite(url);
  }
  if (path === "/" || path === "/index.html") {
    url.pathname = "/busan-yugigyug/index.html";
    return Response.rewrite(url);
  }
}
