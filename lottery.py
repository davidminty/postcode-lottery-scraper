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
from keys import *
import http.client
import urllib

class Scraper:
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 180)
    
    def __init__(self):
        self.chrome_options.add_argument("--user-data-dir=selenium")
        self.winners = []

    def open_page(self, url):
        self.page = url.split(".com/", -1)
        self.driver.get(url)
    
    def page_interaction(self, element):
        try:
            page_element = self.wait.until(EC.presence_of_element_located((By.XPATH, element)))
            page_element.click()
        except:
            pass

    def find_postcodes(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result--postcode')))
            self.postcodes = self.driver.find_elements_by_class_name('result--postcode')
            for self.postcode in self.postcodes:
                p = self.postcode.text.split("\n")
                self.winners.append(" : ".join(p))
        except:
            self.winners.append("Unable to find Postcodes for {} draw".format(self.page))
        return self.winners

    def next_page(self):
        nextbtn = self.driver.find_element_by_class_name('result--button')
        nextbtn.click()

    def close_driver(self):
        self.driver.close()
        self.driver.quit()


class Notifier():
    def __init__(self, wfile):
        self.emailkeys = emailkeys
        self.pushkeys = pushkeys
        self.wfile = wfile

    def emailer(self):
        emailBody = EmailMessage()
        emailBody.set_content(self.wfile.read())
        emailBody['Subject'] = "Winning Postcodes for {}".format(datetime.date.today())

        smtpObj = smtplib.SMTP(self.emailkeys["srv"], self.emailkeys["port"])
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(self.emailkeys["login"], self.emailkeys["password"])
        smtpObj.sendmail(self.emailkeys["fromaddr"],self.emailkeys["toaddr"], emailBody.as_string())
        smtpObj.quit()

    def pushover(self):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
            urllib.parse.urlencode({
            "token": self.pushkeys["apptoken"],
            "user": self.pushkeys["userkey"],
            "message": (self.wfile.read())}), 
            { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()