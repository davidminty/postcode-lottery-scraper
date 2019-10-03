#!/usr/bin/python3
from lottery import *
from keys import emailkeys, pushoverkeys
import datetime

## Globals
wfile_name = "stackpot winners - {}.txt".format(datetime.date.today())
wfile = open(wfile_name, 'w')

# Stackpot Postcodes
try:
    driver.get('https://pickmypostcode.com/stackpot')
    find_postcodes()
except:
    winners.append("Unable to find Stackpot Postcodes")
    pass

## Close Down Browser & chromedriver
driver.close()
driver.quit()

# Final list
for w in winners:
    wfile.write(w + '\n')

wfile = open(wfile_name, 'r')

## Email Notification
wfile = open(wfile_name, 'r')
emailer(wfile, emailkeys)
# Pushover Notification
wfile = open(wfile_name, 'r')
pushover(wfile, pushoverkeys)