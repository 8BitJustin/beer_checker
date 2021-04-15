from selenium import webdriver
from datetime import datetime
from email.message import EmailMessage
import smtplib
import config
import time

print('\nRunning beer grabber...\n')

# driver = webdriver.Chrome()
# Delete below three lines and uncomment above driver line to show browser
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

"""SEARCH FUNCTION SECTION"""
# This was created so multiple searches can be performed when running script


def search(*args):

	body = ''

	for arg in args:

		driver.get("https://thetapandbottle.com/northstore")

		print("\nAccessing website...\n")

		time.sleep(5)

		frame = driver.find_elements_by_tag_name('iframe')[0]

		driver.switch_to.frame(frame)
		driver.find_element_by_class_name('search-label').click()

		driver.find_element_by_id("search").send_keys(arg)

		print(f'\nSearching for requested brew... {arg.title()}\n')

		time.sleep(8)

		titles = driver.find_elements_by_css_selector('div.name.bold')
		prices = driver.find_elements_by_css_selector('span.price')

		print(f'\nLocated {len(titles)} items for {arg.title()}\n')

		fulldesc = dict(zip(titles, prices))

		body += f"You searched for: {arg.title()}\n\n"

		for t, p in zip(titles, prices):
			body += f"\t{t.text} - ${p.text}\n\n"

	return body


"""END SEARCH FUNCTION SECTION"""

"""EMAIL SECTION"""

timestamp = datetime.now()
now = timestamp.strftime("%m/%d/%Y")

EMAIL_ADDRESS = config.email
EMAIL_PASS = config.pw

msg = EmailMessage()
msg['Subject'] = f'Tap and Bottle selections for {now}'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'j.olson.digital@gmail.com'

# Add what items to search for here
msg.set_content(search('left hand', 'firestone walker'))

print('\nPutting email together...\n')

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

smtp.send_message(msg)

"""END EMAIL SECTION"""

print('\nEmail sent!\n')

print('\nClosing!\n')

# Closes python box after program finishes
driver.quit()
