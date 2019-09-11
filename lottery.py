#!/usr/bin/python3

## IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import os
import smtplib
from email.message import EmailMessage
from keys import keys

## GLOBALS

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_options)
wfile_name = "winners {}.txt".format(datetime.date.today())
wfile = open(wfile_name, 'w')
wait = WebDriverWait(driver, 180)

## FUNCTIONS

def findPostcodes(title = "Pick My Postcode"):
    wait.until(EC.title_contains(title))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result--postcode')))
    postcodes = driver.find_elements_by_class_name('result--postcode')
    for postcode in postcodes:
        p = postcode.text.split("\n")
        winners.append(" : ".join(p))
    return winners

def nextPage():
    nextbtn = driver.find_element_by_class_name('result--button')
    nextbtn.click()

def pageInteraction(element):
    page_element = wait.until(EC.presence_of_element_located((By.XPATH, element)))
    page_element.click()

def emailer(wfile, keys):
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


# Create list for winning postcodes
winners = []

# Open up PickMyPostcode
driver.get('https://pickmypostcode.com/')

# Main Daily Postcode
findPostcodes()
nextPage()

# Video Page
pageInteraction("//div[@class='brid-overlay-play-button brid-button ']")
findPostcodes("Video")
nextPage()

# Survey Page
pageInteraction("//button[@class='btn btn-secondary btn__xs']")
findPostcodes("Survey")
time.sleep(10)
nextPage()

# Stackpot Page
findPostcodes("Stackpot")

## Close Down Browser & chromedriver
driver.close()
driver.quit()

# Final list
for w in winners:
    wfile.write(w + '\n')

wfile = open(wfile_name, 'r')

## Emailer
emailer(wfile, keys)