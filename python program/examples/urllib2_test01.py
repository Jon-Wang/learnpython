#!/usr/bin/python
# Filename: urllib2_test01.py

# -*- coding: utf-8 -*-

import urllib2

response = urllib2.urlopen('http://www.baidu.com/')  
#html = response.read()

print response.read()
