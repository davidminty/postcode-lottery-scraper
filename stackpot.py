#!/usr/bin/python3
# IMPORTS
from lottery import *

# Instantiate the scraper
stackpot = Scraper()

#Open the Stackpot Page
stackpot.open_page('https://pickmypostcode.com/stackpot')
stackpot.find_postcodes()

# Build the Winning Postcode List
winners = stackpot.winners

# Close chrome and the driver
stackpot.close_driver()

# Send notifications
alert = Notifier(winners, "stackpot")
alert.email()
alert.pushover()