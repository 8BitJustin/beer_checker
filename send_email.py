import smtplib
import config

EMAIL_ADDRESS = config.email
EMAIL_PASS = config.pw


def sending(items):
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

		subject = 'Tap and Bottle Left Hand Brewery Choices'
		body = "Tap and Bottles Left Hand Brewery choices for today:\n\n\n"

		for item in items:
			body += item.text + '\n'

		msg = f'Subject: {subject}\n\n{body}'

		smtp.sendmail(EMAIL_ADDRESS, 'j.olson.digital@gmail.com', msg)

