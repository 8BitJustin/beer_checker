import smtplib
import config
from datetime import datetime

EMAIL_ADDRESS = config.email
EMAIL_PASS = config.pw


def sending(items):
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

		timestamp = datetime.now()
		now = timestamp.strftime("%m/%d/%Y")

		subject = f'Tap and Bottle Left Hand Brewery Choices for {now}'
		body = ""

		for item in items:
			body += item.text + '\n'

		msg = f'Subject: {subject}\n\n{body}'

		smtp.sendmail(EMAIL_ADDRESS, 'j.olson.digital@gmail.com', msg)
