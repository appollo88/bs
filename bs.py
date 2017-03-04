from bs4 import *

import urllib.request

# OPEN url

# url = "http://www.baidu.com"

url = "http://www.163.com"

try:
    testurl = urllib.request.urlopen(url)
except:
    print("Network is not running in a good way. Please check.")
finally:
    print(testurl.url + " is working.")

soup = BeautifulSoup(testurl, "html5lib")

# print(soup.find_all(class_="yaowen_news"))

# yaowen = soup.find_all( class_="yaowen_news")


toutiao = soup.find_all(class_="yaowen_news")

newstext = ""

for news in toutiao:
    print(news.get_text().strip().replace(' ', ''))

# print(newstext.replace(' ', ''))

'''
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)
'''

# 定义一个函数，输入网址和网页中元素class名，输出对应的内容。
# 例如： url = 'http://news.sina.com.cn'  |  getclass = 'ct_t_01'   
def getsoup(url,getclass):
    try:
        testurl = urllib.request.urlopen(url)
    except:
        print("There is something wrong when opening this url")
    finally:
        print(testurl.url + " is working.")
    getsoup = BeautifulSoup(testurl, "html5lib")
    newslist = getsoup.find_all(class_= getclass)
    for news in newslist:
        print(news.get_text().replace(' ', '').strip())
    return "From:" + url


# 中国政府网-要闻
yaowen = 'http://www.gov.cn/xinwen/yaowen.htm'
divclass = 'news_box'
getsoup(yaowen, divclass)


    
