from selenium import webdriver
import urllib.request
from urllib.request import urlopen
import time
import re
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.common.keys import Keys

def chrome_option():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR") # 한국어!
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    return options
    

def get_mail_addr() :
    text = html_doc.split('<script>')
    # print(text[1])
    pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
    str = text[1]
    match = re.search(pattern, str)
    if match:
        return match.group()        


def get_html_source(URL) :
    list_url = []
    # 네이버 쇼핑에서 인테리어 검색 -> 해외구매 탭 선택 합니다.    
    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
    driver.get(url=URL)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    list_div = soup.select('.basicList_item__2XT81')
    print(list_div)
    for list_d in list_div :
        print(list_d)
    # //*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[1]/a



options = chrome_option()
# URL = "https://smartstore.naver.com/blossom82/products/2643752178?NaPm=ct%3Dkizkrtyw%7Cci%3Df8e9652b315e7323334bce1297266b74551404cd%7Ctr%3Dslsl%7Csn%3D669077%7Chk%3D912eb9754eebee0f42aa2ccb46647a25a0db1d43"
URL = "https://search.shopping.naver.com/search/all?frm=NVSHOVS&origQuery=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&pagingIndex=1&pagingSize=1000&productSet=overseas&query=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&sort=rel&timestamp=&viewType=list"
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
driver.get(url=URL)
time.sleep(5)
start = 1
SCROLL_PAUSE_TIME = 3
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while start < 2:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            start = start + 1
            get_html_source("https://search.shopping.naver.com/search/all?frm=NVSHOVS&origQuery=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&pagingIndex=" + str(start) + "&pagingSize=1000&productSet=overseas&query=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&sort=rel&timestamp=&viewType=list")
        except:
            break
    # last_height = new_height


# res = True
# URL = "https://smartstore.naver.com/blossom82/products/2643752178?NaPm=ct%3Dkizkrtyw%7Cci%3Df8e9652b315e7323334bce1297266b74551404cd%7Ctr%3Dslsl%7Csn%3D669077%7Chk%3D912eb9754eebee0f42aa2ccb46647a25a0db1d43"
# start = 1
# while True:
#     res = get_html_source("https://search.shopping.naver.com/search/all?frm=NVSHOVS&origQuery=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&pagingIndex="+ str(start)+ "&pagingSize=4010000&productSet=overseas&query=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&sort=rel&timestamp=&viewType=list")
#     if res == False :
#         break
#     else :
#         start = start + 1