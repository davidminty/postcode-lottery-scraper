#!/usr/bin/python3
import lottery

# Instantiate scraper
maindraw = lottery.Scraper()

pages = [
    # Main Draw
    {"page": "https://pickmypostcode.com/"},
    # Video Draw
    {"page": 'https://pickmypostcode.com/video',
        "interaction": "//div[@class='brid-overlay-play-button brid-button ']"},
    # Survey Draw
    {"page": "https://pickmypostcode.com/survey-draw",
        "interaction": "//button[@class='btn btn-secondary btn__xs']"},
    # Bonus Draw
    {"page": "https://pickmypostcode.com/your-bonus"}
]

for p in pages:
    maindraw.open_page(p["page"])
    if p["interaction"]:
        maindraw.page_interaction(p["interaction"])
    maindraw.find_postcodes()

# Close chrome and the driver
maindraw.close_driver()

# Send notifications
alert = lottery.Notifier(maindraw.winners, "main")
alert.email()
alert.pushover()
