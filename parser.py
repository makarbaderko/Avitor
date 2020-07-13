def write_to_file(name, object_to_write):
    f = open(name, 'w')
    f.write(object_to_write)
    f.close()        
def get_ad_info(requiredHtml, browser):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import pandas as pd
    soup = BeautifulSoup(requiredHtml, features="lxml")
    mydivs = soup.findAll("div", {"class": "item_table-wrapper"})
    print(mydivs)
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
    browser.get(ads_page_adress)
    requiredHtml = browser.page_source
    ads_soup = BeautifulSoup(requiredHtml, features="lxml")
    first_ad_picture = str(ads_soup.find('img', {"elementtiming":"bx.gallery"}))
    left = first_ad_picture.find('''src="//''')+7
    first_ad_picture = first_ad_picture[left:-3]
    first_ad_decription = str(ads_soup.find('div', {"class":"item-description-text"}))
    left = first_ad_decription.find('<p>')+3
    right = first_ad_decription.find('</p>')
    first_ad_decription = first_ad_decription[left:right]
    ad = {}
    ad["title"] = first_ad_title
    ad["price"] = first_ad_price
    ad["description"] = first_ad_decription
    ad["adress"] = first_ad_adress
    ad["picture"] = first_ad_picture
    ad["url"] = ads_page_adress
    return ad

def get_info_from_ads_page(requiredHtml):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import pandas as pd
    soup = BeautifulSoup(requiredHtml)
    #<div class="item-description"> <div class="item-description-html" itemprop="description">
    description = soup.find
    ('div', 
    {'class': 'item-description-html',
    'itemprop': 'description'})
    left = str(description).find('<p>')+3
    right = str(description).find('</p>')
    description = str(description)[left:right]
    #<span class="js-item-price" content="41400" itemprop="price">41 400</span>
    price = soup.find('span', {'class': 'js-item-price', 'itemprop':'price'})
    left = str(price).find('>')+1
    right = str(price).find('</span>')
    price=str(price)[left:right]
    #<span class="item-address__string"> Москва, Совхозная ул., 39 </span>
    adress = soup.find('span', {'class':"item-address__string"})
    left = str(adress).find('>')+1
    right = str(adress).find('</span>')
    adress = str(adress)[left:right]
    #<img elementtiming="bx.gallery" src="//77.img.avito.st/640x480/8763146877.jpg" alt="Игры на ps4">
    picture = str(soup.find('img', {"elementtiming":"bx.gallery"}))
    left = picture.find('''src="//''')+7
    picture = picture[left:-3]
    print(picture)

all_ads = {
    "Title":[],
    "Price": [],
    "Description": [],
    "Adress": [],
    "Picture": [],
    "Url": []
}
def save_ad_info(ad):
    global all_ads
    all_ads["Title"].append(ad["title"])
    all_ads["Price"].append(ad["price"])
    all_ads["Description"].append(ad["description"])
    all_ads["Adress"].append(ad["adress"])
    all_ads["Picture"].append(ad["picture"])
    all_ads["Url"].append(ad["url"])

def main(adress):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import pandas as pd
    chromedriver = './chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless') 
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    browser.get(adress)
    # Получение HTML-содержимого
    requiredHtml = browser.page_source
    return get_ad_info(requiredHtml, browser)

import pandas as pd

'''for i in range(100):
    try:
        ad = main("https://www.avito.ru/moskva/igry_pristavki_i_programmy/igry_dlya_pristavok-ASgBAgICAUSSAsYJ?q=%D0%B8%D0%B3%D1%80%D1%8B+ps4")
        all_ads.append(ad)
        #print(ad)
    except:
        print("Caught it!")
        break
pd.Series(all_ads).to_csv("./output/all_ads.csv")'''

from selenium import webdriver
from bs4 import BeautifulSoup
chromedriver = './chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless') 
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
browser.get('https://www.avito.ru/moskva/igry_pristavki_i_programmy/igry_na_ps4_1927747792')
# Получение HTML-содержимого
requiredHtml = browser.page_source

get_info_from_ads_page(requiredHtml)