import urllib2
import urllib
import re
from BeautifulSoup import BeautifulSoup

starturl="http://videolectures.net/site/list/events/"
baseurl="http://videolectures.net/"
page = urllib2.urlopen(starturl)
soup = BeautifulSoup(page)

#get all the event names
#soup.body(name='span',attrs={"class":"search_res"})
eventTagList=soup.body('span','search_res')

numEvents=len(eventTagList)
eventInfoList= list()
#each dict will have entries for name, date, abbr, url

for eventTag in eventTagList:
    name=eventTag.next #the event name
    relurl=eventTag.parent.attrs[0][1] #the event abbreviation, and url
    absurl=urllib.basejoin(baseurl,relurl)
    abbrev=relurl.split('/')[1].upper()    
    date=eventTag.parent.parent.contents[5].contents[0].contents[0] #the event date
    eventInfoList.append({"name":name,"abbrev":abbrev,"date":date,"url":absurl})
    


#get all the event dates
soup.body(name='span',attrs={"class":"text_bold"})
soup.body('span','text_bold')


#get all the event images
soup.body('img')
#now need to only grab event images, which all contain 
#the string "velblod"


#get all event abbreviations
soup.body(name='a',attrs={'href':re.compile('^/.*/$')})

# find all i for which res[i].contents[0].name is "img"


#get all event urls
soup.body(name='a',attrs={'href':re.compile('^/.*/$')})

