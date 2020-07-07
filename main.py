# импорт библиотек
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

chromedriver = './chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless') 
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

'''# Переход на страницу входа
browser.get('https://www.avito.ru/moskva#login?authsrc=h')
# Поиск тегов по имени
email = browser.find_element_by_name('login')
password = browser.find_element_by_name('password')
login = browser.find_element_by_name('submit')
#Данные учетной записи
my_login = '8 985 346-23-82'
my_pass = 'M9853462382'

email.send_keys(my_login)
password.send_keys(my_pass)
login.click()
'''

browser.get("https://www.avito.ru/moskva/knigi_i_zhurnaly?i=1")
# Получение HTML-содержимого
requiredHtml = browser.page_source
def write_to_file(name, object_to_write):
    f = open(name, 'w')
    f.write(object_to_write)
    f.close()        

soup = BeautifulSoup(requiredHtml, features="lxml")

mydivs = soup.findAll("div", {"class": "item_table-wrapper"})
write_to_file('item_look.html', str(mydivs))
list_of_ads = list(mydivs)
first_ad = list_of_ads[-1]
first_ad_soup = BeautifulSoup(str(first_ad), features="lxml")
first_ad_price = str(first_ad_soup.findAll("span", {"data-marker":"item-price"}))
first_ad_price = ''.join([n for n in first_ad_price if n.isdigit()])
first_ad_title = str(first_ad_soup.find("h3", {"data-marker": "item-title"}))
left = first_ad_title.find("title=")
first_ad_title = first_ad_title[left:]
right = first_ad_title.find('>')
first_ad_title = first_ad_title[7:right-1]
first_ad_adress = str(first_ad_soup.find('span', {"class":"item-address-georeferences-item__content"}))
left = first_ad_adress.find('>')+1
first_ad_adress = first_ad_adress[left:]
right = first_ad_adress.find('<')
first_ad_adress = first_ad_adress[:right]
ads_page_adress = str(first_ad_soup.find("a", {"itemprop":"url"}))
left = ads_page_adress.find('''href=''')+6
ads_page_adress = ads_page_adress[left:]
right = ads_page_adress.find('''"''')
ads_page_adress = "https://www.avito.ru/" + ads_page_adress[:right]
#print(first_ad_price)
#print(first_ad_picture)
print(ads_page_adress)