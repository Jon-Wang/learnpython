#!/usr/bin/python
# filename: bdtb_01.py

# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

class bdtb:

    def __init__(self,seeLZ = 1):
        self.baseURL = 'http://tieba.baidu.com/p/3138733512'
        self.seeLZ = '?see_lz='+str(seeLZ)

    def getpage(self,pageNum = 1):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            pagecode = response.read().decode('utf-8')
            return pagecode
        
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print e.reason
                return None

    def gettitle(self):
        page = self.getpage()
        pattern = re.compile('<title>(.*?)_nba.*?</title>',re.S)
        result = re.search(pattern,page)
        if result:
            print result.group(1).strip()
        else:
            return None
    
bdtb = bdtb()
bdtb.gettitle()
