import urllib2
import urllib
import re
from BeautifulSoup import BeautifulSoup

baseurl="http://videolectures.net/"
eventFile=open("/home/rexa/python/PASCAL_Events.txt",'r')

for eventString in eventFile.readlines():
    eventurl=eventString.split('---')[-1].rstrip()
    eventAbbrev=eventString.split('---')[0]
    #eventurl="http://videolectures.net/epsrcws08_sheffield/"
    
    #page = urllib2.urlopen(http://videolectures.net/epsrcws08_rasmussen_lgp/)
    page = urllib2.urlopen(eventurl)
    soup = BeautifulSoup(page)
    
    
    
    
    #get all the event names
    #full version: 
    #soup.body(name='div',attrs={"class":"author"})
    vidPageList=soup.body('div','lec_thumb_click')
    
    
    numVidPages = len(vidPageList)
    vidPageInfoList = list()
    #vidPageInfoList will be a list of dicts
    #each dict will have entries for vidpage title, and vidpage url
    
    for vidPage in vidPageList:
        #authorName=authorTag.contents[0].string
        relurl = vidPage.next.attrs[0][1]
        absurl = urllib.basejoin(baseurl,relurl)
        page   = urllib2.urlopen(absurl)
        soup   = BeautifulSoup(page)
        title  = soup.head.title.string
        title  = title.encode('ascii','ignore') 
        author = relurl.split('_')[-2].capitalize()
        videoCountInfo = soup.findAll(onclick=re.compile(r'setvideo\(\'[\d]\'\)'))
        if len(videoCountInfo) == 0:
            numVideos=1
        else:
            numVideos=len(videoCountInfo)     
        vidPageInfoList.append({"title":title,"url":absurl,"author":author,"numVideos":numVideos})


    eventFileName=eventAbbrev+".txt"
    print eventFileName
    f2=open(eventFileName,'w')
    breaker="---"

    for vidPageInfo in vidPageInfoList:
        #leave out event name to avoid unicode problems
        #eventString=eventInfo["abbrev"]+breaker+ str(eventInfo["name"])+breaker+ eventInfo["date"]+breaker+ eventInfo["url"]+"\n"
        vidPageString=vidPageInfo["title"]+breaker+ vidPageInfo["author"]+breaker+ str(vidPageInfo["numVideos"]) +breaker+vidPageInfo["url"]+"\n"    
        print vidPageString
        f2.write(vidPageString)
        
    f2.close()
f.close()
