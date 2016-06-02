#!/usr/bin/Python
# filename: bdtb_10.py

# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

class Tool:
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
    
class Bdtb:

    def __init__(self,baseURL,seeLZ = 1):
        self.baseURL = baseURL
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()
        
    def getPage(self,pageNum = 1):
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

    def getTitle(self,page):
        pattern = re.compile('<title>(.*?)</title>',re.S)
        result = re.search(pattern,page)
        if result:
            #return "Title: %s" % (result.group(1).strip())
            return result.group(1).strip()
        else:
            return None
        
    def getPageNum(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
        
    def getContent(self,page,title,num):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        floor = 1
        file = open(title+'.txt','w+')
        file.write("Title:" + title.encode('utf-8')+"\n")
        file.write("PageNum:" + num.encode('utf-8')+"\n")       
        for item in items:
            file.write("\n" + str(floor) + " floor-------------------------------\n\n")
            file.write(self.tool.replace(item).encode('utf-8'))
            floor += 1

    def start(self):
        Page = self.getPage()
        Title = self.getTitle(Page)
        PageNum = self.getPageNum(Page)
        self.getContent(Page,Title,PageNum)


baseURL =raw_input("Please input URL:")
bdtb = Bdtb(baseURL)
bdtb.start()
