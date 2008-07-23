import urllib2
import urllib
import re
from BeautifulSoup import BeautifulSoup

starturl="http://videolectures.net/site/list/events/"
baseurl="http://videolectures.net/"
page = urllib2.urlopen(starturl)
soup = BeautifulSoup(page)

#get all the event names
#full version: 
#soup.body(name='span',attrs={"class":"search_res"})
eventTagList=soup.body('span','search_res')

numEvents=len(eventTagList)
eventInfoList= list()
#eventInfoList will be a list of dicts
#each dict will have entries for event name, date, abbr, and url

for eventTag in eventTagList:
    relurl=eventTag.parent.attrs[0][1] #the event abbreviation, and url
    absurl=urllib.basejoin(baseurl,relurl)


    name=eventTag.next #the event name
    name=name.encode('ascii','ignore')
    abbrev=relurl.split('/')[1].upper()    
    date=eventTag.parent.parent.contents[5].contents[0].contents[0] #the event date
    eventInfoList.append({"name":name,"abbrev":abbrev,"date":date,"url":absurl})

f=open(r'/home/rexa/python/PASCAL_Events.txt','w')
breaker="---"

for eventInfo in eventInfoList:  
    #leave out event name to avoid unicode problems
    eventString=eventInfo["abbrev"]+breaker+ eventInfo["name"]+breaker+ eventInfo["date"]+breaker+ eventInfo["url"]+"\n"
    #eventString=eventInfo["abbrev"]+breaker+ eventInfo["date"]+breaker+ eventInfo["url"]+"\n"    
    print eventString
    f.write(eventString)

f.close()


#for future development, the sections of an event can be grabbed thus:
# sects=soup.body('span','sections_title')
# if sects is nonempty, then we can find the individual sections, since
#the relative urls listed in:
# sects[0].nextSibling.nextSibling.findAll('a')