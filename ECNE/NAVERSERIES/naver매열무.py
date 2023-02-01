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

login_url = "https://nid.naver.com/nidlogin.login"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(login_url)
time.sleep(10)


href_list = []

for i in range(1, 200) : 
    url = f"https://series.naver.com/novel/specialFreeList.series?specialFreeTypeCode=FREEFROMTODAY&page={i}"
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url)

    if i > 1 :      
        if  first == browser.find_element(By.CSS_SELECTOR,'#content > div > div > ul > li:nth-child(1) > div > h3 > a').text :
            print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 총 작품 개수 : {len(href_list)}개 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            break
        else : 
            novels = browser.find_elements(By.CSS_SELECTOR,'.lst_list > li > a')
            first = browser.find_element(By.CSS_SELECTOR,'#content > div > div > ul > li:nth-child(1) > div > h3 > a').text

            for novel in novels :
                nov_href = novel.get_attribute('href')
                href_list.append(nov_href)

    else : 
        novels = browser.find_elements(By.CSS_SELECTOR,'.lst_list > li > a')
        first = browser.find_element(By.CSS_SELECTOR,'#content > div > div > ul > li:nth-child(1) > div > h3 > a').text

        for novel in novels :
            nov_href = novel.get_attribute('href')
            href_list.append(nov_href)


hrefs_1 = dict.fromkeys(href_list)
hrefs = list(hrefs_1)

for i, href in enumerate(hrefs, 1) :
    start = time.time()
    print(f"{i}번 째 작품====================================================================")
    #try :
    browser.get(href)
    time.sleep(2)

    start_title = time.time()
    try : 
        title = browser.find_element(By.CSS_SELECTOR,'#content > div.end_head > h2').text
        if title.find('[독점]') > -1 :
            title.replace(' [독점]', '')
        if title.find('[선공개]') > -1 :
            title.replace(' [선공개]', '')
    except : 
        title = ''
        print('title ERROR')
        browser.refresh()
    end_title = time.time()
    print(f"title : {end_title - start_title:.5f} sec  : {title}")
    
    start_imgURL = time.time()
    try : 
        html = browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        preview = soup.select_one('.pic_area > span.preview')
        if preview is None : 
            img = browser.find_element(By.CSS_SELECTOR,'#container > div.aside.NE\=a\:nvi > span > img')
        else :
            img = browser.find_element(By.CSS_SELECTOR, '#container > div.aside.NE\=a\:nvi > a > img')
        imgUrl = img.get_attribute('src')
    except : 
        imgUrl = ''
        print('imgUrl ERROR')
        browser.refresh()
    end_imgURL = time.time()
    print(f"imgURL : {end_imgURL - start_imgURL:.5f} sec  : {imgUrl}")

    start_upload_started = time.time()
    try : 
        upload_start = browser.find_element(By.CSS_SELECTOR, '#volumeList > tr._volume_row_1 > td.subj > div > em').text
        upload_starte = upload_start.replace('(','')
        upload_started = upload_starte.replace(')','')

    except :
        upload_started = ''
        print('upload_started ERROR')
    end_upload_started = time.time()
    print(f"upload_started : {end_upload_started - start_upload_started:.5f} sec : {upload_started}")

    start_order = time.time()
    try :
        order_change = browser.find_element(By.CSS_SELECTOR,'#content > table > thead > tr > th.chk > div > button')
        order_change.click()
    except :
        print ('order change ERROR')
        browser.refresh()
    end_order = time.time()
    print(f"OrderChange : {end_order - start_order:.5f} sec")

    start_last_upload = time.time()

    try :
        total = browser.find_element(By.CSS_SELECTOR, '#content > h5 > strong').text
        last_uplo = browser.find_element(By.CSS_SELECTOR, f'#volumeList > tr._volume_row_{total} > td.subj > div > em').text
        last_uploa = last_uplo.replace('(','')
        last_upload = last_uploa.replace(')','')
    except :
        last_upload = ''
        print('last_upload ERROR')
    end_last_upload = time.time()
    print(f"last_upload : {end_last_upload - start_last_upload:.5f} sec  : {last_upload}")

    start_onlyAdult = time.time()
    try :
        onlyAdult = False
        age_limit = browser.find_element(By.CSS_SELECTOR, '#content > ul.end_info.NE\=a\:nvi > li > ul > li:nth-child(5)').text
        if age_limit == '청소년 이용불가' : 
            onlyAdult = True
    except :
        onlyAdult = '' 
        print('onlyAdult ERROR')
    end_onlyAdult = time.time()
    print(f"onlyAdult : {end_onlyAdult - start_onlyAdult:.5f} sec : {onlyAdult}")

    start_author = time.time()
    try :
        author = browser.find_element(By.CSS_SELECTOR, '#content > ul.end_info.NE\=a\:nvi > li > ul > li:nth-child(3) > a').text
    except :
        author = ''
        print('author ERROR')
    end_author = time.time()
    print(f"author : {end_author - start_author:.5f} sec  : {author}")

    start_genre = time.time()
    try :
        genre = browser.find_element(By.CSS_SELECTOR,'#content > ul.end_info.NE\=a\:nvi > li > ul > li:nth-child(2) > span > a').text
    except :
        genre = ''
        print('genre ERROR')
    end_genre = time.time()
    print(f"genre : {end_genre - start_genre:.5f} sec  : {genre}")

    start_label = time.time()
    try : 
        label= browser.find_element(By.CSS_SELECTOR,'#content > ul.end_info.NE\=a\:nvi > li > ul > li:nth-child(4) > a').text
        draw = browser.find_element(By.CSS_SELECTOR,'#content > ul.end_info.NE\=a\:nvi > li > ul > li:nth-child(4) > span').text
        if draw == '그림' :
            label = browser.find_element(By.CSS_SELECTOR,'#content > ul.end_info.NE\=a\:nvi > li > ul > li:nth-child(5) > a').text
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
        'promotion': '매열무',
        'distributor' : 'naverseries',
        'onlyAdult':onlyAdult,
        'last_upload': last_upload,
                }
    data.append(dict)
    #except :
        #print('렉걸림')
        #browser.refresh()

today = datetime.today()    
with open(f'naverseries_{today}.json','w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
   



