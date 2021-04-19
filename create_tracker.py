from os import error
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
link = input("Input a link: ").strip()
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.get(link)
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

_type = input('What is the type (eg div): ').strip()
_subtype = input("'class' or 'id': ").strip()
_identifier = input('Enter the identifier text: ').strip()


if (_subtype == "class"):
    span = soup.find(_type,class_=_identifier)
else:
    span = soup.find(_type,id=_identifier)
results = span.text.strip()
yOrN = input('\nResult = '+ results+ "\nIs this correct 'y' or 'n'? ").strip()
if (yOrN == 'y'):
    email = input("Please enter your email address for updates: ")
    with open('tracked_sites.csv', encoding='UTF-8',mode='a', newline='') as tracker_file:
        tracker_file_writer = csv.writer(tracker_file)
        export = [link,_type,_subtype,_identifier,results,email]
        tracker_file_writer.writerow(export)
else:
    exit()
       

