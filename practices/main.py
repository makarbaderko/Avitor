# импорт библиотек
from selenium import webdriver
from bs4 import BeautifulSoup

chromedriver = './chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless') 
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

# Переход на страницу входа
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


browser.get("https://www.avito.ru/moskva/igry_pristavki_i_programmy?cd=1")
# Получение HTML-содержимого
requiredHtml = browser.page_source
def write_to_file(name, type_of_open, object_to_write, prettify):
    if prettify:
        f = open(name, type_of_open)
        soup = BeautifulSoup(object_to_write)
        f.write(soup.prettify())
        f.close()
    else:
        f = open(name, type_of_open)
        f.write(object_to_write)
        f.close()        
'''write_to_file("igri_pristavki.html", "w", requiredHtml, True)'''


soup = BeautifulSoup(requiredHtml, features="lxml")
mydivs = soup.findAll("div", {"class_": "snippet-horizontal   item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended"})
print(mydivs)