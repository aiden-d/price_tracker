from os import error
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import sys
link = 'https://koodoo.co.za/collections/sony-playstation-5-ps5/products/playstation-5-ps5?variant=35259384332455'
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.get(link)
#wait = WebDriverWait(browser, 10)
#wait.until(EC.visibility_of_element_located((By.ID, "payment-buttons payment-buttons--small")))
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
_type = input('What is the type (eg div): ')
_subtype = input("'class' or 'id': ")
_identifier = input('Enter the identifier text: ')


if (_subtype == "class"):
    span = soup.find(_type,class_=_identifier)
else:
    span = soup.find(_type,id=_identifier)


results = span.text
yOrN = input('\nResult = '+ results+ "\nIs this correct 'y' or 'n'? ")
if (yOrN == 'y'):
    with open('tracked_sites.csv', encoding='UTF-8',mode='w', newline='') as tracker_file:
        tracker_file_writer = csv.writer(tracker_file)
        export = [link,_type,_subtype,_identifier,results]
        print(export)
        tracker_file_writer.writerow(export)
else:
    exit()
       

