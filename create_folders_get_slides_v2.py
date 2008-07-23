from urlgrabber import urlgrab
from urlgrabber import urlopen
from BeautifulSoup import BeautifulSoup
from urllib import basejoin
import os
import sys
import re


res=os.listdir('/home/rexa/python/event_pages_lists')
res.sort()
for fileName in res:
    pageFile=open("/home/rexa/python/event_pages_lists/"+fileName,'r')
    baseDir="/home/rexa/python/events/"
    eventName=fileName.rstrip('.txt')
    eventDirString=baseDir+eventName
    if not os.path.exists(eventDirString):
        os.mkdir(eventDirString)
    
    for pageString in pageFile.readlines():
        print pageString.rstrip()
        splitInfo=pageString.split('---')
        splitInfo[0]=splitInfo[0].split('/')[0]
        splitInfo[1]=splitInfo[1].lstrip('/')
        pageNameString=' - '.join(splitInfo[0:3])+" vid"
        pageDirString=eventDirString+"/"+pageNameString
        if not os.path.exists(pageDirString):
            os.mkdir(pageDirString)
        print pageDirString
        print "\n"
        
        #get page url
        pageURL=splitInfo[3].rstrip()
        page=urlopen(pageURL)
        soup=BeautifulSoup(page)
        slidesRes=soup.findAll(text=re.compile(r'Slides download?'))
#        slidesRes2=soup.findAll(href=re.compile(r'http.*(\.ppt|\.pdf|\.ps|\.pps)'))
        
        if slidesRes:
            slidesDirString=pageDirString+'/'+"slides"
            if not os.path.exists(slidesDirString):
                os.mkdir(slidesDirString)
            for slides in slidesRes:             
                print slides.next.contents
                slidesURL=slides.next.attrs[0][1]
                slidesFileName=slidesURL.split('/')[-1]
                slidesFilePath=slidesDirString+'/'+slidesFileName
                if not os.path.exists(slidesFilePath):
                    urlgrab(slidesURL,slidesFilePath)
    pageFile.close()