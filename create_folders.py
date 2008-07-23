import os
import sys
import re


res=os.listdir('/home/rexa/python/event_pages_lists')
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