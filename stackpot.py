#!/usr/bin/python3
from lottery import *
import datetime

stackpot = Scraper()
stackpot.open_page('https://pickmypostcode.com/stackpot')
winners = stackpot.find_postcodes()

stackpot.close_driver()

wfile_name = "{} - stackpot.txt".format(datetime.date.today())
wfile = open(wfile_name, 'w')

for w in winners:
    wfile.write(w + '\n')

wfile = open(wfile_name, 'r')
alert = Notifier(wfile)
alert.emailer()
alert.pushover()