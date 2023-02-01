from selenium import webdriver #무한스크롤 + 작품 href 리스트 가져오기
import time
import requests
from bs4 import BeautifulSoup
import math
import json
from datetime import datetime

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager



# 브라우저 꺼짐 방지

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)



# 불필요한 에러 메시지 없애기

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])



service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=chrome_options)

url = "https://page.kakao.com/landing/series/list/page/landing/33"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

before_h = browser.execute_script("return window.scrollY")

scroll_start = time.time()
while True : 
    body = browser.find_element(By.CSS_SELECTOR,'body' )
    body.send_keys(Keys.END)

    time.sleep(1)

    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h :
        break
    before_h = after_h
scroll_end = time.time()
print(f"scroll : {scroll_end - scroll_start:.5f}sec")

save_start = time.time()
novels = browser.find_elements(By.CSS_SELECTOR,'.flex-1.cursor-pointer.css-0')
print(f'총 {len(novels)}개 작품')

href_list = []

for novel in novels :
    nov_href = novel.get_attribute('href')
    href_list.append(nov_href)

today = datetime.today()    
with open(f'kakao기다무_href_{today}.json','w') as f:
    json.dump(href_list, f, ensure_ascii=False, indent=4)
save_end = time.time()
print(f"save : {save_end - save_start:.5f}sec")