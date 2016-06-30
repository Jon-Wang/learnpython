#!/usr/bin/python
# Filename: headers.py

# -*- coding: utf-8 -*-

import urllib  
import urllib2  

url = 'http://www.server.com/login'
values = {'username' : 'cqc',  'password' : 'XXXX' }
data = urllib.urlencode(values)
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'Referer':'https://www.zhihu.com/question/46296660'}  

request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)

page = response.read() 
