#!/usr/bin/env python3
from wsgiref.simple_server import make_server

from yi2.wsgi import application

httpd = make_server('127.0.0.1',80,application)
print('Serving HTTP on port 80...')

httpd.serve_forever()
