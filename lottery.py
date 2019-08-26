#!/usr/bin/python3

## IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os
import smtplib
from email.message import EmailMessage
from keys import keys

## GLOBALS

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=selenium")
browser = webdriver.Chrome(options=chrome_options)
wfile_name = "winners {}.txt".format(datetime.date.today())
wfile = open(wfile_name, 'w')

## FUNCTIONS

def findPostcodes():
    postcodes = browser.find_elements_by_class_name('result--postcode')
    for postcode in postcodes:
        p = postcode.text.split("\n")
        winners.append(" : ".join(p))
    return winners

def nextPage():
    nextbtn = browser.find_element_by_class_name('result--button')
    nextbtn.click()


# Create list for winning postcodes
winners = []

# Open up PickMyPostcode
browser.get('https://pickmypostcode.com/')

# Main Daily Postcode
findPostcodes()
nextPage()

# Video Page
time.sleep(5)
browser.find_element_by_xpath("//div[@class='brid-overlay-play-button brid-button ']").click()
time.sleep(60)
findPostcodes()
nextPage()

# Survey Page
browser.find_element_by_xpath("//button[@class='btn btn-secondary btn__xs']").click()
findPostcodes()
nextPage()

# Stackpot Page
findPostcodes()

## Close Down Browser & chromedriver
browser.close()
browser.quit()

# Final list
for w in winners:
    wfile.write(w + '\n')

wfile = open(wfile_name, 'r')

## Emailer
emailBody = EmailMessage()
emailBody.set_content(wfile.read())
emailBody['Subject'] = "Winning Postcodes for {}".format(datetime.date.today())

smtpObj = smtplib.SMTP(keys["srv"], keys["port"])
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(keys["login"], keys["password"])

smtpObj.sendmail(
    keys["fromaddr"],keys["toaddr"], emailBody.as_string()
)

smtpObj.quit()