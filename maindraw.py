#!/usr/bin/python3
import lottery

# Instantiate scraper
maindraw = lottery.Scraper()

# Main Draw
maindraw.open_page('https://pickmypostcode.com/')
maindraw.find_postcodes()

# Video Draw
maindraw.open_page('https://pickmypostcode.com/video')
maindraw.page_interaction("//div[@class='brid-overlay-play-button brid-button ']")
maindraw.find_postcodes()

# Survey Draw
maindraw.open_page('https://pickmypostcode.com/survey-draw')
maindraw.page_interaction("//button[@class='btn btn-secondary btn__xs']")
maindraw.find_postcodes()

# Bonus Draw
maindraw.open_page("https://pickmypostcode.com/your-bonus")
maindraw.find_postcodes()

# Close chrome and the driver
maindraw.close_driver()

# Winners list
winners = maindraw.winners

# Send notifications
alert = lottery.Notifier(winners, "main")
alert.email()
alert.pushover()