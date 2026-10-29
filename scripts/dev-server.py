"""Local static server with Vercel-like host routing (site/ root)."""
from __future__ import annotations

import http.server
import os
import socketserver
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "site"))
PORT = int(os.environ.get("PORT", "8080"))
BIND = os.environ.get("BIND", "127.0.0.1")

HOST_EXACT: dict[str, dict[str, str]] = {
    "xn--299ay81a7laj9hr5am7nvsdby4b.daumzine.co.kr": {
        "/": "/busan-goyang-bohoso/index.html",
        "/index.html": "/busan-goyang-bohoso/index.html",
        "/robots.txt": "/busan-goyang-bohoso/robots.txt",
        "/sitemap.xml": "/busan-goyang-bohoso/sitemap.xml",
    },
    "xn--939az33a7laj9hr5af5mv3iw10a.daumzine.co.kr": {
        "/": "/busan-gangaji-bohoso/index.html",
        "/index.html": "/busan-gangaji-bohoso/index.html",
        "/robots.txt": "/busan-gangaji-bohoso/robots.txt",
        "/sitemap.xml": "/busan-gangaji-bohoso/sitemap.xml",
    },
    "xn--299a782a7lc12ga110av72a.daumzine.co.kr": {
        "/": "/busan-goyang-apyang/index.html",
        "/index.html": "/busan-goyang-apyang/index.html",
        "/robots.txt": "/busan-goyang-apyang/robots.txt",
        "/sitemap.xml": "/busan-goyang-apyang/sitemap.xml",
    },
    "xn--l89at2a894aj7ccuad8ykls.daumzine.co.kr": {
        "/": "/busan-yugigyug/index.html",
        "/index.html": "/busan-yugigyug/index.html",
        "/robots.txt": "/busan-yugigyug/robots.txt",
        "/sitemap.xml": "/busan-yugigyug/sitemap.xml",
    },
}


class DevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self) -> None:
        host = (self.headers.get("Host") or "").split(":")[0].lower()
        path = self.path.split("?", 1)[0]
        rules = HOST_EXACT.get(host)
        if rules and path in rules:
            self.path = rules[path] + (("?" + self.path.split("?", 1)[1]) if "?" in self.path else "")
        return super().do_GET()

    def log_message(self, fmt: str, *args) -> None:
        host = (self.headers.get("Host") or "-").split(":")[0]
        sys.stderr.write("%s - [%s] %s\n" % (host, self.log_date_time_string(), fmt % args))


class ThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main() -> None:
    os.chdir(ROOT)
    with ThreadingServer((BIND, PORT), DevHandler) as httpd:
        print(f"Serving {ROOT}")
        print(f"  http://{BIND}:{PORT}/  (부산강아지파양)")
        print(f"  http://{BIND}:{PORT}/busan-goyang-apyang/  (부산고양이파양 미리보기)")
        print(f"  http://{BIND}:{PORT}/busan-goyang-bohoso/  (부산고양i보호소)")
        print(f"  http://{BIND}:{PORT}/busan-gangaji-bohoso/  (부산강아ji보호소)")
        print(f"  http://{BIND}:{PORT}/busan-yugigyug/  (부산유기견센터)")
        print("Host routing: 부산고양이파양 / 부산유기견센터 *.daumzine.co.kr → hosts 파일에 127.0.0.1 연결 시 루트(/)와 동일")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
