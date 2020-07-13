from parser import main
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
all_ads = []
for i in range(100):
    try:
        ad = main("https://www.avito.ru/moskva/igry_pristavki_i_programmy/igry_dlya_pristavok-ASgBAgICAUSSAsYJ?q=%D0%B8%D0%B3%D1%80%D1%8B+ps4")
        all_ads.append(ad)
        print(ad)
    except:
        print("Caught it!")
        break
pd.Series(all_ads).to_csv("./output/all_ads.csv")