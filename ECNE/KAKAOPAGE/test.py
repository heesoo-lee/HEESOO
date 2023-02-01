import requests
from bs4 import BeautifulSoup

response = requests.get('https://ridibooks.com/books/372010782?_rdt_sid=romance_webnovel_selection&_rdt_idx=0')
html = response.text
soup = BeautifulSoup(html,'html.parser')
#detail = soup.select_one('.header_thumbnail_wrap')
adultbadge = soup.select_one('span.badge_adult')
print (adultbadge)