#!/usr/bin/python3
import lottery

# Instantiate the scraper
stackpot = lottery.Scraper()

# Stackpot Draw
stackpot.open_page('https://pickmypostcode.com/stackpot')
stackpot.find_postcodes()

# Close chrome and the driver
stackpot.close_driver()

# Send notifications
alert = lottery.Notifier(stackpot.winners, "stackpot")
alert.email()
alert.pushover()