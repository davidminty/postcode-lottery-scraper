#!/usr/bin/python3
import lottery

# Instantiate the scraper
stackpot = lottery.Scraper()



# Stackpot Draw
stackpot.open_page('https://pickmypostcode.com/stackpot')
stackpot.login('stackpot')
stackpot.find_postcodes()

# Close chrome and the driver
stackpot.close_driver()

# Winners List
winners = stackpot.winners

# Send notifications
alert = lottery.Notifier(winners, "stackpot")
alert.pushover()
