from selenium import webdriver
from datetime import datetime
from email.message import EmailMessage
from search import search
import smtplib
import config
import time

print('\nRunning beer grabber...\n')

# driver = webdriver.Chrome()
# Delete below three lines and uncomment above driver line to show browser
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

"""EMAIL SECTION"""

timestamp = datetime.now()
now = timestamp.strftime("%m/%d/%Y")

EMAIL_ADDRESS = config.email
EMAIL_PASS = config.pw

msg = EmailMessage()
msg['Subject'] = f'Tap and Bottle Left Hand Brewery Choices for {now}'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'j.olson.digital@gmail.com'

# Add search keywords here
msg.set_content(search('left hand', 'stone'))

print('\nPutting email together...\n')

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

smtp.send_message(msg)

"""END EMAIL SECTION"""

print('\nEmail sent!\n')

print('\nClosing!\n')

# Closes python box after program finishes
driver.close()
driver.quit()