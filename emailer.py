#! /usr/bin/python3

## IMPORTS

from keys import keys
import datetime
import os
import smtplib
from email.message import EmailMessage

## GLOBALS


wfile_name = "winners (2019-08-26).txt"
wfile = open(wfile_name, 'r')



emailBody = EmailMessage()
emailBody.set_content(wfile.read())
emailBody['Subject'] = "Winning Postcodes for {}".format(datetime.date.today())

smtpObj = smtplib.SMTP(keys["srv"], keys["port"])
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(keys["login"], keys["password"])

smtpObj.sendmail(
    keys["fromaddr"],keys["toaddr"], emailBody.as_string()
)

smtpObj.quit()