from selenium import webdriver
from datetime import datetime
from email.message import EmailMessage
import smtplib
import config
import time

print('Running beer grabber...\n')

# driver = webdriver.Chrome()
# Delete below three lines and uncomment above driver line to show browser
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get("https://thetapandbottle.com/northstore")

print("Accessing website...\n")

time.sleep(5)

search = 'left hand'

frame = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(frame)
driver.find_element_by_class_name('search-label').click()

driver.find_element_by_id("search").send_keys(search)

print('Searching for requested brew...\n')

time.sleep(8)

titles = driver.find_elements_by_css_selector('div.name.bold')

print('Requested items found!\n')

print('Putting email together...\n')

"""EMAIL SECTION"""

timestamp = datetime.now()
now = timestamp.strftime("%m/%d/%Y")

EMAIL_ADDRESS = config.email
EMAIL_PASS = config.pw

body = f"Your results for: {search}\n\n"
for title in titles:
	body += '\t' + title.text + '\n\n'

msg = EmailMessage()
msg['Subject'] = f'Tap and Bottle Left Hand Brewery Choices for {now}'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'j.olson.digital@gmail.com'
msg.set_content(body)

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

smtp.send_message(msg)

"""END EMAIL SECTION"""

print('Email sent!\n')

print('Closing!\n')

# Closes python box after program finishes
driver.close()
driver.quit()