#!/usr/bin/python3

## IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

## GLOBALS

def findPostcode():
    postcode = browser.find_element_by_class_name('result--postcode')
    print(postcode.text)
    
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=selenium")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://pickmypostcode.com/')

print("Logging in")
#time.sleep(30)

print("Looking for first postcode")
findPostcode()

print("Moving to next page")
next = browser.find_element_by_class_name('result--button')
next.click()

print("Waiting for page to load")
time.sleep(30)

#print("Playing video")
#play = browser.find_element_by_class_name('brid-touch-overlay')
#play.click()

#print("Waiting for video to play")
#time.sleep(60)

print("Finding postcode")
findPostcode()
'''
signin = browser.find_element_by_class_name('btn-secondary')
signin.click()

postcodeInput = browser.find_element_by_id('confirm-ticket')
postcodeInput.send_keys('NG24 4AD')

emailInput = browser.find_element_by_id('confirm-email')
emailInput.send_keys('mintyxiv@gmail.com')
emailInput.submit()
'''