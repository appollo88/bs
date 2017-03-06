 
from bs4 import *

import urllib.request

class webgetter(object):

    def __init__(self, url, getclass):
        self.url = url
        self.getclass = getclass
        self.testurl = None

    def get_web(url,getclass):
        try:
            testurl = urllib.request.urlopen(url)
        except:
            print("There is something wrong when opening this url")
        finally:
            print("Getting from url: " + url)
        getsp = BeautifulSoup(testurl, "html5lib")
        newslist = getsp.find_all(class_= getclass)
        for news in newslist:
            print(news.get_text().strip().replace(' ', ''))
        return "Finished from url: " + url


    
# testing
get_wangyi = webgetter
get_wangyi.get_web('http://www.163.com', 'yaowen_news')
