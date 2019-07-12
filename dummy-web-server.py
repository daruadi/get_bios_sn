#!/usr/bin/env python
"""
this file was originally from this url:
https://gist.githubusercontent.com/bradmontgomery/2219997/raw/813c95911b47d255fd21b940e155c7921d290ea2/dummy-web-server.py

Run this command first:
python -m http.server 8080

Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # self._set_headers()
        # self.wfile.write(bytes("<html><body><h1>hi!</h1></body></html>", "utf-8"))
        params = parse_qs(self.path)
        print("\n\n======", params['sn'][0], "\n", params['bios'][0], "======\n\n")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=9999):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
