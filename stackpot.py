#!/usr/bin/python3
from lottery import *

# Instantiate the scraper
stackpot = Scraper()

# Stackpot Draw
stackpot.open_page('https://pickmypostcode.com/stackpot')
stackpot.find_postcodes()

# Close chrome and the driver
stackpot.close_driver()

# Winners List
winners = stackpot.winners

# Send notifications
alert = Notifier(winners, "stackpot")
alert.email()
alert.pushover()