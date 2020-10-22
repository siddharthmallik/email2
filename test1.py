"""
def send_simple_message():
	return requests.post(
		"https://",
		auth=("api", ""),
		data={"from": "",
			"to": ["siddharthmallik404@gmail.com", "malliksiddharth@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
"""

import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hello"
msg['From']    = ""
msg['To']      = "siddharthmallik404@gmail.com"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('', 'password')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
