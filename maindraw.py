#!/usr/bin/python3
from lottery import *
from keys import emailkeys, pushoverkeys
import datetime

## Globals
wfile_name = "main winners - {}.txt".format(datetime.date.today())
wfile = open(wfile_name, 'w')

# Main Postcode
try:
    driver.get('https://pickmypostcode.com/')
    find_postcodes()
except:
    winners.append("Unable to find Main Postcode")
    pass

# Video Postcode
try:
    driver.get('https://pickmypostcode.com/video')
    page_interaction("//div[@class='brid-overlay-play-button brid-button ']")
    find_postcodes()
except:
    winners.append("Unable to find Video Postcode")
    pass

# Survey Postcode
try:
    driver.get('https://pickmypostcode.com/survey-draw')
    page_interaction("//button[@class='btn btn-secondary btn__xs']")
    find_postcodes()
except:
    winners.append("Unable to find Survey Postcode")
    pass

# Bonus Postcode
try:
    driver.get("https://pickmypostcode.com/your-bonus/")
    find_postcodes()
except:
    winners.append("Unable to find Bonus Postcode")
    pass

## Close Down Browser & chromedriver
driver.close()
driver.quit()

# Final list
for w in winners:
    wfile.write(w + '\n')


## Email Notification
wfile = open(wfile_name, 'r')
emailer(wfile, emailkeys)
# Pushover Notification
wfile = open(wfile_name, 'r')
pushover(wfile, pushoverkeys)