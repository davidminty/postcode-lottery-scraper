#!/usr/bin/python3

from lottery import *


wfile_name = "main winners - {}.txt".format(datetime.date.today())
wfile = open(wfile_name, 'w')

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

## Close Down Browser & chromedriver
driver.close()
driver.quit()

# Final list
for w in winners:
    wfile.write(w + '\n')

wfile = open(wfile_name, 'r')

## Emailer
emailer(wfile, keys)