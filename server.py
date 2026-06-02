#!/usr/bin/env python3
import http.server, os

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} → {fmt % args}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("MÔI site rodando em: http://localhost:8000")
http.server.HTTPServer(('', 8000), Handler).serve_forever()
