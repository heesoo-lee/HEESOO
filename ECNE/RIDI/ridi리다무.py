from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import math
import json
from datetime import datetime
import clipboard

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

data = []

login_url = "https://ridibooks.com/account/login?return_url=https%3A%2F%2Fridibooks.com%2Fromance%2Fwebnovel"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(login_url)
id= 'heesoo624'
pw ='@@gltn0118'
browser.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/form/input[1]').send_keys(id)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/form/input[2]').send_keys(pw)
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/form/button').click()
time.sleep(1)


href_list = []
genre_code = [353, 367, 604, 636]
for x in genre_code :
    for i in range(1, 200) : 
        url = f"https://ridibooks.com/selection/{x}?page={i}"
        browser.implicitly_wait(10)
        browser.maximize_window()
        browser.get(url)

        if i > 1 :
            if  first == browser.find_element(By.CSS_SELECTOR,'#__next > main > section > div.fig-12atcmq > ul > li:nth-child(1) > div > div.fig-111ugxm > h3 > a').text :
                break

            else : 
                novels = browser.find_elements(By.CSS_SELECTOR,'.fig-13606cb')
                first = browser.find_element(By.CSS_SELECTOR,'#__next > main > section > div.fig-12atcmq > ul > li:nth-child(1) > div > div.fig-111ugxm > h3 > a').text

                for novel in novels :
                    nov_href = novel.get_attribute('href')
                    href_list.append(nov_href)
        else :
            novels = browser.find_elements(By.CSS_SELECTOR,'.fig-13606cb')
            first = browser.find_element(By.CSS_SELECTOR,'#__next > main > section > div.fig-12atcmq > ul > li:nth-child(1) > div > div.fig-111ugxm > h3 > a').text

            for novel in novels :
                nov_href = novel.get_attribute('href')
                href_list.append(nov_href)
                print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 총 작품 개수 : {len(href_list)}개 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for i, href in enumerate(href_list, 1) :
    start = time.time()
    print(f"{i}번 째 작품====================================================================")
    #try :
    browser.get(href)
    time.sleep(2)

    start_title = time.time()
    try : 
        title = browser.find_element(By.CSS_SELECTOR,'#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_info_wrap > div.info_title_wrap > h1').text
    except : 
        title = ''
        print('title ERROR')
        browser.refresh()
    end_title = time.time()
    print(f"title : {end_title - start_title:.5f} sec  : {title}")
    
    start_imgURL = time.time()
    try : 
        img = browser.find_element(By.CSS_SELECTOR,'#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_thumbnail_wrap > div.header_thumbnail.book_macro_200.detail_scalable_thumbnail > div > div > div > img')
        imgUrl = img.get_attribute('src')
    except : 
        imgUrl = ''
        print('imgUrl ERROR')
        browser.refresh()
    end_imgURL = time.time()
    print(f"imgURL : {end_imgURL - start_imgURL:.5f} sec  : {imgUrl}")

    start_upload_started = time.time()
    try : 
        upload_started = browser.find_element(By.CSS_SELECTOR, '#SeriesListWrap > ul.module_compact_book_list.white_theme.js_compact_book_list > li:nth-child(1) > div > div > div.table_cell.book_info > div:nth-child(2) > ul > li.info_reg_date').text
    except :
        upload_started = ''
        print('upload_started ERROR')
    end_upload_started = time.time()
    print(f"upload_started : {end_upload_started - start_upload_started:.5f} sec : {upload_started}")

    start_order = time.time()
    try :
        order_change = browser.find_element(By.CSS_SELECTOR,'#series_list_module > div.option_wrap.js_series_list_option_wrap > ul > li:nth-child(2) > button')
        order_change.click()
    except :
        print ('order button ERROR')
        browser.refresh()
    end_order = time.time()
    print(f"OrderChange : {end_order - start_order:.5f} sec")

    start_last_upload = time.time()

    try : 
        last_upload = browser.find_element(By.CSS_SELECTOR, '#SeriesListWrap > ul.module_compact_book_list.white_theme.js_compact_book_list > li:nth-child(1) > div > div > div.table_cell.book_info > div:nth-child(2) > ul > li.info_reg_date').text
    except :
        last_upload = ''
        print('last_upload ERROR')
    end_last_upload = time.time()
    print(f"last_upload : {end_last_upload - start_last_upload:.5f} sec  : {last_upload}")

    start_onlyAdult = time.time()
    try :
        html = browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        detail = soup.select('.header_thumbnail_wrap')
        onlyAdult = False
        for ab in detail :
            adultbadge = ab.select_one('.badge_adult')
            if adultbadge is not None :
                onlyAdult = True
                print(adultbadge)
    except :
        onlyAdult = '' 
        print('onlyAdult ERROR')
    end_onlyAdult = time.time()
    print(f"onlyAdult : {end_onlyAdult - start_onlyAdult:.5f} sec : {onlyAdult}")

    start_author = time.time()
    try :
        author = browser.find_element(By.CSS_SELECTOR, '#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_info_wrap > div:nth-child(4) > p.metadata.metadata_writer > span > a').text
    except :
        author = ''
        print('author ERROR')
    end_author = time.time()
    print(f"author : {end_author - start_author:.5f} sec  : {author}")

    start_genre = time.time()
    try :
        genre1 = browser.find_element(By.CSS_SELECTOR,'#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_info_wrap > p > a:nth-child(1)').text
        genre2 = browser.find_element(By.CSS_SELECTOR,'#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_info_wrap > p > a:nth-child(3)').text
        genre = f'{genre1}, {genre2}'
    except :
        genre = ''
        print('genre ERROR')
    end_genre = time.time()
    print(f"genre : {end_genre - start_genre:.5f} sec  : {genre}")

    start_label = time.time()
    try : 
        label= browser.find_element(By.CSS_SELECTOR,'#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_info_wrap > div:nth-child(4) > p.metadata.file_info.publisher_info > a').text
    except :
        label = ''
        print('label ERROR')
    end_label = time.time()
    print(f"label : {end_label - start_label:.5f} sec  : {label}")


    end = time.time()
    print(f"{i}번 째 작품 총 시간 : {end - start:.5f} sec")
    dict = {
        'href' : href,
        'imgUrl' : imgUrl,
        'title' :title,
        'genre' :genre,
        'author' : author,
        'label' : label,
        'upload_started' :upload_started,
        'promotion': '리다무',
        'distributor' : 'RIDI',
        'onlyAdult':onlyAdult,
        'last_upload': last_upload,
                }
    data.append(dict)
    #except :
        #print('렉걸림')
        #browser.refresh()

result1 = dict.fromkeys(data)
result2 = list(result1)
today = datetime.today()    
with open(f'RIDI{today}.json','w') as f:
    json.dump(result2, f, ensure_ascii=False, indent=4)
   



