#!/usr/bin/python
# Filename: zhihu.py

import urllib
import urllib2

url = "http://www.zhihu.com/login/email"

values = {
"email" : "1575456904@qq.com",
"password" : "----"
}

headers = {
"User-agent" : "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36",
"Referer" : "https://www.zhihu.com"
}

data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

print page
