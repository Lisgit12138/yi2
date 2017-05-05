#!/usr/bin/env python
# encoding=utf8
import os
from urllib.request import urlopen,quote

char = input('输入内容:  ')
char_encode = quote(char)
f = urlopen('http://qr.topscan.com/api.php?text=%s' % char_encode)
filename = '%s.jpg' % char[-2:]
w = open(filename,'wb')
w.write(f.read())
f.close()
w.close()