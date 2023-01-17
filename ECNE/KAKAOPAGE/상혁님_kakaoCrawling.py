import json
import time
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

   

class Browser:
    browser, service, options = None, None, None
    update = ['오늘','1일전','2일전','3일전' ,'4일전', '5일전', '6일전', '7일전', '일주일']
    default_date = '2022.11.01'
    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.options = Options()
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'
        self.options.add_argument('user-agent=' + user_agent)
        self.options.add_argument('--profile-directory=Default')
        self.browser = webdriver.Chrome(service=self.service,options=self.options)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()


if __name__ == '__main__':
    file_path = "./kakaoUrllist20230106.json"
    section =[]
    fp = open(file_path)
    section = json.load(fp)
    # print(section)
    nowdate =datetime.now().strftime("%Y%m%d")+'.json'
    filename = "./kakao"+ nowdate

    browser = Browser('.chormedirver.exe')

    page_url = 'https://page.kakao.com/landing/series/list/page/landing/517'
  
    herfs = []
    browser.open_page(page_url)

    time.sleep(4)
    browser.browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div/div[1]/div[3]/img[2]').click()

    time.sleep(5)
    id= 'kimtkdgur78@naver.com'
    pw ='sens1973!'
    browser.browser.switch_to.window(browser.browser.window_handles[1])
    time.sleep(1)
    browser.browser.find_element(By.ID, 'input-loginKey').send_keys(id)
    browser.browser.find_element(By.ID, 'input-password').send_keys(pw)
    time.sleep(1)
    browser.browser.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    time.sleep(25)
    browser.browser.switch_to.window(browser.browser.window_handles[0])

    # #스크롤 내리기 전 위치
    # scroll_location = browser.browser.execute_script("return document.body.scrollHeight")
    # # try : 
    # index = 0
    # while True:
    #         # if(index == 10) :
    #         #         url_a = browser.browser.find_elements(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div/div/div')

    #         #         for item in url_a:
    #         #             a= item.find_element(By.CLASS_NAME,'css-0')
    #         #             date = a.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div/div/div[1]/a/div/a/div/div[2]/div[2]/div[2]/span[2]').text 
    #         #             herf = a.get_attribute("href")
    #         #             print(date,herf)
                        
    #         #             herfs.append({
    #         #                 "url" :herf,
    #         #                 "date" : date ,
    #         #             })
    #         #             browser.browser.execute_script("arguments[0].remove()" ,item)
    #         #             time.sleep(0.05)


    #         #         # print(a)
    #         #         browser.browser.implicitly_wait(1)                
    #         #         time.sleep(1)


    #         #         index = 0
    #         #         scroll_height = 0
    #         # else : 
    #         #전체 스크롤이 늘어날 때까지 대기“
    #     browser.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #     time.sleep(4)
    #     browser.browser.implicitly_wait(1)                
    #     #늘어난 스크롤 높이
    #     scroll_height = browser.browser.execute_script("return document.body.scrollHeight")
    

    
    #     #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
    #     if scroll_location == scroll_height:

    #         print('break',str(herfs.__len__()))
    #         break

    #     #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
    #     else:
            
    #         #스크롤 위치값을 수정
    #         index +=1 
    #         scroll_location = browser.browser.execute_script("return document.body.scrollHeight")    
                


    #     # with open(filename,'w', encoding='utf-8') as f: 
    #     #     json.dump(herfs,f, indent= 2,ensure_ascii=False)    

    #     # browser.browser.quit()
    # # with open('./kakaopageUrl.json','w', encoding='utf-8') as f: 
    # #         json.dump(herfs,f, indent= 2,ensure_ascii=False)
    # time.sleep(1)

    # html = browser.browser.page_source
    # initsoup = BeautifulSoup(html, 'html.parser')
    # data = []
    # url = []
    # section = initsoup.select('a.css-0')

    # for item in section : 
    #     href='https://page.kakao.com' +item.attrs['href']
    #     url.append(href)
    # # with open('./kakaop.json','w', encoding='utf-8') as f: 
    # #     json.dump(url,f, indent= 2,ensure_ascii=False)
    data = []
    default =0
    index = 0
    
    url = section

    with open('kakaoUrllist'+nowdate,'w', encoding='utf-8') as f: 
        json.dump(url,f, indent= 2,ensure_ascii=False)
    try : 
        for item in url : 
            novel = {
                'href' : 'null',
                'imgUrl' : 'null',
                'title' :'null',
                'genre' :'null',
                'author' :'null',
                'label' :'null',
                'upload_started' :'null',
                'promotion':'null',
                'distributor' :'null',
                'onlyAdult':'null',
                'last_upload':'null',
            }   
            try : 
            
                href=item
                browser.browser.get(href)
                time.sleep(2.5)
                html = browser.browser.page_source
                detail_source = BeautifulSoup(html, 'html.parser')
                title = ''
                upload_started = ''
                date=''
                try : 
                    title = browser.browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[2]/span').text

                except : 
                    title = ''
                try :
                    upload_started = browser.browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/div/div/a/div/div[2]/div[2]/span').text
                    print(upload_started)
                except :
                    upload_started = ''
                try : 
                    sort = browser.browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div')
                except :
                    ''
                try :
                    #광고 팝업
                    popup = browser.browser.find_elements(By.XPATH,'/html/body/div')
                    s =len(popup)
                    if s > 1: 
                        popup = browser.browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/button')
                        print(popup)
                        popup.click()
                    # 회차순서 버튼 앞에 다른 버튼 있을 경우
                    if sort is None :
                       sort= browser.browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]')
                    sort.click()
                except: 
                    ''

                try : 
                    browser.browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[3]/div[2]').click()
                    time.sleep(1)
                    try : 
                        date =browser.browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/div/div/a/div/div[2]/div[2]/span').text
                    except: 
                        date =''
                except : 
                    ''
                browser.browser.get(href+ '?tab_type=about')
                time.sleep(1)
        

                print(title)
                html = browser.browser.page_source
                detail_source = BeautifulSoup(html, 'html.parser')
                info = ''
                img = ''
                genre = ''
                author = ''
                label = ''
                promotion = ''

                try : 
                    info=browser.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[1]/div[2]/div[3]/div').text

                except : 
                    info = ''
                try :
                    img = detail_source.select_one('img.object-cover.absolute')['src']
                except:
                    img = ''
                try :
                    genres = browser.browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.flex.pr-32pxr > div:nth-child(1) > div.mt-16pxr.px-32pxr > div:nth-child(1)').find_elements(By.XPATH,'*')
                    for g in genres : 
                        genre +=g.text
                except:
                    genre = ''
                onlyAdult = False
                try:
                    author = browser.browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.flex.pr-32pxr > div:nth-child(2) > div.mt-16pxr.px-32pxr > div > div').text
                   
                except:
                    author = ''
                try:
                    labels = browser.browser.find_element(By.CSS_SELECTOR,'#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div.flex.h-full.flex-1 > div.mb-28pxr.ml-4px.flex.w-632pxr.flex-col > div.flex-1.bg-bg-a-20 > div.flex.pr-32pxr > div:nth-child(1) > div.mt-16pxr.px-32pxr > div:nth-child(2)').find_elements(By.XPATH,'*')
                    for g in labels : 
                        label +=g.text
                except:
                    label = ''
                try:
                    promotion = browser.browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/img[2]')
                except:
                    promotion =''
                if(info == '19세이용가' ): onlyAdult = True
                novel = {
                    'href' : href,
                    'imgUrl' : img,
                    'title' :title,
                    'genre' :genre,
                    'author' : author,
                    'label' : label,
                    'upload_started' :upload_started,
                    'promotion': '3다무',
                    'distributor' : 'kakaopage',
                    'onlyAdult':onlyAdult,
                    'last_upload': date,
                }
                print(img)
                data.append(novel)

                
            except :
                data.append(novel)

            index +=1
            print('  ------   데이터 수 ====>  ' + str(index) + '------')

        with open(filename,'w', encoding='utf-8') as f: 
            json.dump(data,f, indent= 2,ensure_ascii=False)

    except Exception as e  :
        with open(filename,'w', encoding='utf-8') as f: 
            json.dump(data,f, indent= 2,ensure_ascii=False)
        print( '에러러러러' , e)
         
      




