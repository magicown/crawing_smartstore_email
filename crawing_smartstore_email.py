from selenium import webdriver
import urllib.request
from urllib.request import urlopen
import time
import re
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse 
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def chrome_option():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR") # 한국어!
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    return options
    

def get_mail_addr(URL) :
    driver.get(url=URL)
    html_doc = driver.page_source
    
    text = html_doc.split('<script>')
    # print(text[1])
    pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.][com|co.kr|kr|net|org]+)"
    try :
        str = text[1]
        match = re.search(pattern, str)
        if match:
            # return match.group()        
            # return match.group()
            list_url.append(match.group())
    except :
        pass    

def parseFile_urlHTTPExtract(text) :
    urls = [a['href'] for a in text.find_all('a')]
    for url in urls :
        # list_url.append(url)
        time.sleep(3)        
        get_mail_addr(url)
    return list_url


def html_scroll_down(driver) :
    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script("return document.body.scrollHeight")    
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:        
        return False       
            
    last_height = new_height

list_d = ""
list_e = []
list_url = []
urls = []
options = chrome_option()
start = 1
while start < 3:
    URL = "https://search.shopping.naver.com/search/all?frm=NVSHOVS&origQuery=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&pagingIndex="+str(start)+"&pagingSize=40&productSet=overseas&query=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&sort=rel&timestamp=&viewType=list"
    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
    driver.get(url=URL)
    time.sleep(2)
    html_scroll_down(driver) # 스크롤 하단으로 내려서 해당 내용이 나오게 한다.
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    list_div = soup.select('.basicList_item__2XT81')
    for i in list_div :    
        list_d = i.select('.basicList_title__3P9Q7')
        for j in list_d :
            list_e.append(j.get_text())
            urls = parseFile_urlHTTPExtract(j)
    start = start + 1
    # driver.close()
print(urls)

time.sleep(3)
driver.close()