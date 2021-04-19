from os import error
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
gmail_user = 'aidendawes.spammail@gmail.com'
gmail_password = '9meidoring'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

def send_mail(result, url, email):
    mail_from = gmail_user
    mail_to = email
    mail_subject = "Update on Tracked website"
    mail_message_body = 'There was a change on ' + url + '\n the new text = ' + result
    mail_message = '''\
    From:%s
    To:%s
    Subject:%s
    %s
    ''' % (mail_from, mail_to, mail_subject, mail_message_body)
    header='To:'+mail_to+'\n'+'From:'+mail_from+'\n'+'subject:'+mail_subject+'\n'
    message = MIMEMultipart('alternative')
    message['Subject'] = "Update on Tracked website"
    message['From'] = gmail_user
    message['To'] = email
    message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain')
    content=header+mail_message_body
    server.login(gmail_user, gmail_password)
    server.sendmail(mail_from, mail_to, content)
    server.close()


def check_changes(row):
    link = row[0]
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    #wait = WebDriverWait(browser, 10)
    #wait.until(EC.visibility_of_element_located((By.ID, "payment-buttons payment-buttons--small")))
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    _type = row[1]
    _subtype = row[2]
    _identifier = row[3]
    ##wrap in try except
    if (_subtype == "class"):
        span = soup.find(_type,class_=_identifier)
    else:
        span = soup.find(_type,id=_identifier)
    print("done")
    ##
    if (span == None):
        print("No result")
        send_mail("Item Removed", row[0], row[5])
        return True
    results = span.text.strip()
    print('result = ' + results)
    if (results == row[4]):
        return False
    else:
        send_mail(results, row[0], row[5])
        return True
with open('tracked_sites.csv', encoding='UTF-8',mode='r', newline='') as tracker_file:
    csv_reader = csv.reader(tracker_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(check_changes(row))
        