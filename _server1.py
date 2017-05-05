#!/usr/bin/env python
#encoding=utf8

'''
from wsgiref.simple_server import make_server
from yi2.wsgi import application
server1 = make_server('',80,application)
print('Serve start forever...')
server1.serve_forever()
'''
'''
from urllib.parse import urlencode
dic1 = {'name':'John'}
dic1_encode = urlencode(dic1)
print(type(dic1_encode))
'''
from urllib.request import urlopen
f = urlopen('http://127.0.0.1:8000')
print(f.geturl())