#do better checking on presence/absence of pieces of data
#check to see if the initial page link leads to a series of lectures
#Log-Based Architectures lecture has malformed URL
#   maybe look for a string of numbers with a regular expression, instead?

#example video file location:
# mms://media-wm.cac.washington.edu/msr/14826/asf/14826.asf&OBT_fname=14826.asf
#use mimms?

from BeautifulSoup import BeautifulSoup
import re
import urlgrabber
import urllib
import urllib2

MSRpageURL="http://www.researchchannel.org/prog/displayinst.aspx?fID=880&pID=480"

MSRbaseURL="http://content.digitalwell.washington.edu/msr/external_release_talks_12_05_2005/"

UWCSE2007pageURL="http://www.researchchannel.org/prog/displayseries.aspx?path=1&fID=2318&pID=497"
UWCSE2008pageURL="http://www.researchchannel.org/prog/displayseries.aspx?path=1&fID=4946&pID=497"

page=urlgrabber.urlopen(MSRpageURL)
soup=BeautifulSoup(page)
lecResList=soup.findAll('a','bluelink')

for lecRes in lecResList:
    lecTitle=lecRes.contents[0]  
    print lecTitle
    
    lecInfoURL=lecRes.attrs[2][1]    
    lecPage=urlgrabber.urlopen(lecInfoURL)
    lecSoup=BeautifulSoup(lecPage)

    try:
        lecDate=lecSoup.findAll('span',{'id':'mediaGroupProductionDate'})[0].contents[0]
    except Exception, e:
        print e
        lecDate='NA'
        
    try:
        lecSpeaker=lecSoup.findAll('b')[1].contents[0]
    except Exception, e:
        print e
        lecSpeaker='unknown'
        
    print lecSpeaker
    #lecSpeaker=lecSoup.findAll(text=re.compile(r'Speaker'))[0].parent.parent.find('b').contents[0]
    try:
        lecDescription=lecSoup.findAll(text=re.compile(r'Description'))[0].parent.parent.contents[2]
    except Exception, e:
        print e
        try:
            lecDescription=lecSoup.findAll(text=re.compile(r'Description'))[0].parent.parent.nextSibling.contents[0]
        except Exception,e:
            print e
            lecDescription='NA'
    
    try:
        lecVidURL=lecSoup.findAll(text=re.compile(r'Launch'))[0].parent.parent.attrs[0][1]
        lecNumID=lecVidURL.split('/')[-2]
        lecVidURL=urllib.basejoin(MSRbaseURL,lecNumID+"/lecture.htm")
        lecSlideListURL=urllib.basejoin(MSRbaseURL,lecNumID+"/slideProofSheet.htm")
    
    
        slidePage=urlgrabber.urlopen(lecSlideListURL)
        slideSoup=BeautifulSoup(slidePage)
        slideList=slideSoup.findAll('img')
    
        print "Slide List Length = " + str(len(slideList)) + "\n"
    
        #for slideRes in slideList:
        #slideRelURL=slideRes.attrs[1][1]
        #slideAbsURL=urllib.basejoin(MSRbaseURL,lecNumID+"/"+slideRelURL)
        #urlgrabber.urlgrab(slideAbsURL)
    except Exception,e:
        print e
        lecVidURL='NA'
        lecNumID='NA'
        lecSlideListURL='NA'
        slideList=list()
        print "Slide List Length = " + str(len(slideList)) + "\n"
