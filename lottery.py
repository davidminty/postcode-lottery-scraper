#!/usr/bin/python3

## IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

    def __init__(self):
        self.chrome_options.add_argument("--user-data-dir=selenium")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.set_page_load_timeout(30)
        self.wait = WebDriverWait(self.driver, 180)
        self.winners = []

    def open_page(self, url):
        if url == 'https://pickmypostcode.com/':
            self.page = "Main"
        else:
            self.page = url.split(".com/")[1].strip()
        try:
            self.driver.get(url)
        except TimeoutException:
            pass
        
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

    def next_page(self):
        nextbtn = self.driver.find_element_by_class_name('result--button')
        nextbtn.click()

    def close_driver(self):
        self.driver.quit()


class Notifier():
    def __init__(self, winners, draw):
        self.emailkeys = emailkeys
        self.pushkeys = pushkeys
        self.winners = winners
        self.draw = draw
        self.wfile_name = "{}.txt".format(self.draw)
        self.write_text_file()

    def write_text_file(self):
        wfile = open(self.wfile_name, 'w+')
        for w in self.winners:
            wfile.write(w + '\n')
        wfile.close()

    def email(self):
        emailBody = EmailMessage()
        with open(self.wfile_name, 'r') as wf:
            emailBody.set_content(wf.read())
            wf.close()
        emailBody['Subject'] = "Winning {} Postcodes for {}".format(self.draw.capitalize(), datetime.date.today())

        smtpObj = smtplib.SMTP(self.emailkeys["srv"], self.emailkeys["port"])
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(self.emailkeys["login"], self.emailkeys["password"])
        smtpObj.sendmail(self.emailkeys["fromaddr"],self.emailkeys["toaddr"], emailBody.as_string())
        smtpObj.quit()

    def pushover(self):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        with open(self.wfile_name, 'r') as wf:
            conn.request("POST", "/1/messages.json",
                urllib.parse.urlencode({
                "token": self.pushkeys["apptoken"],
                "user": self.pushkeys["userkey"],
                "message": (wf.read())}), 
                { "Content-type": "application/x-www-form-urlencoded" })
            wf.close()
        conn.getresponse()