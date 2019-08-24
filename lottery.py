#!/usr/bin/python3

## IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

## GLOBALS

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=selenium")
browser = webdriver.Chrome(options=chrome_options)


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




## Create list for winning postcodes
winners = []

## Open up PickMyPostcode
browser.get('https://pickmypostcode.com/')

## Main Daily Postcode
findPostcodes()
nextPage()

## Video Page
time.sleep(5)
browser.find_element_by_xpath("//div[@class='brid-overlay-play-button brid-button ']").click()
time.sleep(60)
findPostcodes()
nextPage()

## Survey Page
browser.find_element_by_xpath("//button[@class='btn btn-secondary btn__xs']").click()
findPostcodes()
nextPage()

## Stackpot Page
findPostcodes()

for w in winners:
    print(w)

## Close Down Browser & chromedriver
browser.close()
browser.quit()
