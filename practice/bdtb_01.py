#!/usr/bin/python
# filename: bdtb_01.py

# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

class tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD= re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)

        return x.strip()
    
class bdtb:

    def __init__(self,seeLZ = 1):
        self.baseURL = 'http://tieba.baidu.com/p/3138733512'
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = tool()
        
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

    def gettitle(self,page):
        pattern = re.compile('<title>(.*?)_nba.*?</title>',re.S)
        result = re.search(pattern,page)
        if result:
            print "title: %s" % (result.group(1).strip())
        else:
            return None
        
    def getpagenum(self,page):
        pattern = re.compile('<input theme="4" id="jumpPage4" max-page="(.*?)" type="text"',re.S)
        result = re.search(pattern,page)
        if result:
            print "pagenum: %s" % (result.group(1).strip())
        else:
            return None
        
    def getcontent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            #print item
            print self.tool.replace(item)
        
bdtb = bdtb()
page = bdtb.getpage()
bdtb.gettitle(page)
bdtb.getpagenum(page)
bdtb.getcontent(page)
