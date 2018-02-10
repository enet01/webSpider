#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import urllib
def getHtml(url):
   page=urllib.urlopen(url)
   html=page.read()
   return html
def getImg(html):
   reg=r'src="(.*?\.jpg)" pic_ext='
   imgre=re.compile(reg)
   imglist=re.findall(imgre,html)
   x=0
   for imgurl in imglist:
      urllib.urlretrieve(imgurl,'M.%s.jpg'%x)
      x+=1
      print '第 %s 张图片已下载' %x
   print '共 %s 张图片' %x
html= getHtml("http://tieba.baidu.com/p/4044289707")
getImg(html)