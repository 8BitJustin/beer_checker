import smtplib
import config

EMAIL_ADDRESS = config.email
EMAIL_PASS = config.pw


def sending():
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

		subject = 'Test'
		body = 'Test text.'

		msg = f'Subject: {subject}\n\n{body}'

		smtp.sendmail(EMAIL_ADDRESS, 'j.olson.digital@gmail.com', msg)


sending()
