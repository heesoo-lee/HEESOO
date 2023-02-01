from datetime import datetime
import json
from select import select
import time
from urllib.request import urlopen
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Browser:
    browser, service, options = None, None, None

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
    browser = Browser('.chormedirver.exe')

  

    filename = "./ridi"+ datetime.now().strftime("%Y%m%d")+'.json'
    browser = Browser('.chormedirver.exe')
    section = []
    ridi_url = 'https://ridibooks.com'
    page_url = 'https://ridibooks.com/account/login?return_url=https%3A%2F%2Fridibooks.com%2Fselection%2F353'
    # 로그인

    time.sleep(1)
    browser.open_page(page_url)
    id= 'kimtkdgur78'
    pw ='sens0428!'
    browser.browser.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/form/input[1]').send_keys(id)
    browser.browser.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/form/input[2]').send_keys(pw)
    time.sleep(1)
    browser.browser.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/form/button').click()
    time.sleep(20)

    romance_fantasy = '367'
    romance = '353'
    fantasy = '636'
    bl = '604'
    genre_arr =['353','367','636','604']
    
    current_url = ridi_url+'/selection/353?page=0'

    data = []
    title = ''
    for genre in genre_arr : 
        try: 
            index = 1

            browser.browser.get(ridi_url+'/selection/'+genre +'?page='+ str(index))

            while  True :
            
                html = browser.browser.page_source
                soup = BeautifulSoup(html, 'html.parser')
                section = soup.select('.fig-1vmbnal > li > div > a')
                print(section.__len__())
                for item in section : 
                    print(item)
                    browser.browser.get(ridi_url+item['href'])
                    time.sleep(2)

                    detail_source = BeautifulSoup(browser.browser.page_source,'html.parser')
                    img = detail_source.select_one('.thumbnail_image > img ')
                    genre_str = ''

                    if genre == '367' : genre_str = '로판'
                    elif genre == '353' : genre_str = '로맨스'
                    elif genre == '604' : genre_str = 'BL'
                    else : 
                        a_category = detail_source.select('.info_category_wrap > a')
                        if a_category.__len__ > 1  :genre_str= a_category[2].string 
                        else : genre_str = ''
                    author = detail_source.select_one('a.author_detail_link').string
                    label = detail_source.select_one('a.publisher_detail_link').string
                    title = detail_source.select_one('h3.info_title_wrap').string
                    adult = detail_source.select_one('.badge_adult') 
                    onlyAdult = True
                    upload_started =  detail_source.select_one('li.published_date_info.Header_Metadata_Detail_Item').string
                    print(title)
                    browser.browser.find_element(By.XPATH,'//*[@id="series_list_module"]/div[1]/ul/li[2]/button').click()
                    browser.browser.implicitly_wait(1)
                    last_upload = browser.browser.find_element(By.CLASS_NAME,'info_reg_date').text
                    print(last_upload)
                    if(adult is None ): onlyAdult = False
                    novel = {
                    'imgUrl' :'https:' +img['src'],
                    'title' :title,
                    'genre' : genre_str,
                    'author' :author,
                    'label' : label,
                    'upload_started' :upload_started,
                    'promotion': '리다무',
                    'distributor' : 'ridibooks',
                    'last_upload' : last_upload,
                    'onlyAdult':onlyAdult
                    }
                    data.append(novel)

                    browser.browser.back()
                    time.sleep(1)
                    print('  ------   데이터 수 ====>  ' + str(data.__len__()) + '------')
                index +=1
                browser.browser.get(ridi_url+'/selection/'+genre +'?page='+ str(index))
                time.sleep(2)

                if current_url == browser.browser.current_url: 
                    break
                else :
                    current_url =  browser.browser.current_url

            with open(filename,'w', encoding='utf-8') as f: 
                json.dump(data,f, indent= 2,ensure_ascii=False)

        except:

            with open(filename,'w', encoding='utf-8') as f: 
                json.dump(data,f, indent= 2,ensure_ascii=False)
            browser.browser.quit()
                
        
 



    # for item in section:
    #     print('https://series.naver.com/' + item.select_one('a').attrs['href'])
    #     item.select_one('a')
    time.sleep(3)
  

    # browser.close_browser()




