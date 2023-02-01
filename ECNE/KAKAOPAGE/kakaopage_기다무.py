from selenium import webdriver
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

data = []
today = datetime.today()

login_url = "https://page.kakao.com"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(login_url)


time.sleep(20)

file_path = "KAKAOPAGE/kakao기다무_href_2023-02-01 12_15_13.742046.json"
href_list =[]
fp = open(file_path)
href_list = json.load(fp)

for i, href in enumerate(href_list, 1) :
    start = time.time()
    print(f"{i}번 째 작품====================================================================")
    try :
        browser.get(href)
        time.sleep(1)
        start_title = time.time()
        try : 
            title = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[2]/span').text
        except : 
            title = ''
            print('title ERROR')
            browser.refresh()
        end_title = time.time()
        print(f"title : {end_title - start_title:.5f} sec : {title}")
        
        start_imgURL = time.time()
        try : 
            img = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/img')
            imgUrl = img.get_attribute('src')
        except : 
            imgUrl = ''
            print('imgUrl ERROR')
            browser.refresh()
        end_imgURL = time.time()
        print(f"imgURL : {end_imgURL - start_imgURL:.5f} sec : {imgUrl}")

        start_promotion = time.time()
        try : 
            promote = a = browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.flex.w-320pxr.flex-col > div.mt-4pxr.flex-1.bg-bg-a-20 > div > div.flex.items-center.h-64pxr > span')
            promotion = promote.text
        except :
            promotion = ''
            print('promotion ERROR')
            browser.refresh()
        end_promotion = time.time()
        print(f"promotion : {end_promotion - start_promotion:.5f} sec : {promotion}")
        
        start_upload_started = time.time()
        try : 
            upload_started = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/div/div/a/div/div[2]/div[2]/span').text
        except :
            upload_started = ''
            print('upload_started ERROR')
        end_upload_started = time.time()
        print(f"upload_started : {end_upload_started - start_upload_started:.5f} sec : {upload_started}")

        start_PopUp = time.time()
        try : 
            Popup = browser.find_elements(By.XPATH,'/html/body/div')
            s =len(Popup)
            if s > 1: 
                Popup = browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/button')
                print('Popup!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                Popup.click()
            else :
                pass
        except :
            print("popup ERROR")   
        end_PopUp = time.time()
        print(f"PopUp : {end_PopUp - start_PopUp:.5f} sec")

        start_order = time.time()
        try :
            order = browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div:nth-child(2) > div:nth-child(1) > div.flex.h-44pxr.w-full.flex-row.items-center.justify-between.px-15pxr.bg-bg-a-20 > div.relative.flex.h-full.items-center.space-x-16pxr.ml-16pxr > div:nth-child(2)')
            order.click()
                
            last_od = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[3]/div[2]')
            last_od.click()
        except :
            print ('order button ERROR')
            browser.refresh()
        end_order = time.time()
        print(f"OrderChange : {end_order - start_order:.5f} sec")

        start_last_upload = time.time()
        try : 
            last_upload = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/div/div/a/div/div[2]/div[2]/span').text
        except :
            last_upload = ''
            print('last_upload ERROR')
        end_last_upload = time.time()
        print(f"last_upload : {end_last_upload - start_last_upload:.5f} sec : {last_upload}")
        try :
            detail = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/a')
            detail.click()
        except :
            print('detail button ERROR')

        start_onlyAdult = time.time()
        try : 
            age_limit = browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.flex.pr-32pxr > div:nth-child(1) > div.mt-16pxr.px-32pxr > div:nth-child(3) > div').text
            if age_limit == '19세이용가' :
                onlyAdult = True
            else : 
                onlyAdult = False
        except : 
            age_limit = ''
            onlyAdult = ''
            print('age ERROR')
        end_onlyAdult = time.time()
        print(f"onlyAdult : {end_onlyAdult - start_onlyAdult:.5f} sec : {onlyAdult}")

        start_author = time.time()
        try :
            author = browser.find_element(By.CSS_SELECTOR, '#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.flex.pr-32pxr > div:nth-child(2) > div.mt-16pxr.px-32pxr > div > div').text
        except :
            author = ''
            print('author ERROR')
        end_author = time.time()
        print(f"author : {end_author - start_author:.5f} sec : {author}")

        start_genre = time.time()
        try :
            genre = browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.flex.pr-32pxr > div:nth-child(1) > div.mt-16pxr.px-32pxr > div:nth-child(1) > div > span:nth-child(3)').text
        except :
            genre = ''
            print('genre ERROR')
        end_genre = time.time()
        print(f"genre : {end_genre - start_genre:.5f} se : {genre}")

        start_label = time.time()
        try : #발행자 위에꺼 가져와서 클래스네임으로 다 가져오기
            label_rd = browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.flex.pr-32pxr > div:nth-child(1) > div.mt-16pxr.px-32pxr > div:nth-child(2)')
            labels= label_rd.find_elements(By.CLASS_NAME, 'break-all')
            label_list = []
            for label_a in labels :
                label_list.append(label_a.text)
            label = ','.join(label_list)
        except :
            label = ''
            print('label ERROR')
        end_label = time.time()
        print(f"label : {end_label - start_label:.5f} sec : {label}")


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
            'promotion': promotion,
            'distributor' : 'kakaopage',
            'onlyAdult':onlyAdult,
            'last_upload': last_upload,
                    }
        data.append(dict)
    except :
        print('렉걸림')
        browser.refresh()
        with open(f'kakaor기다무test_중간저장_{today}.json','w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

with open(f'kakao기다무_{today}.json','w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)