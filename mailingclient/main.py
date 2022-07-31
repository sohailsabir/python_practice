import os
import smtplib
from email.message import EmailMessage

email_id = 'sohailsabir6565@gmail.com'
email_pass = 'kbbpahfovbyeawey'


msg = EmailMessage()
msg['Subject'] = 'first mail using python'
msg['From'] = email_id
msg['To'] = email_id
msg.set_content('how about a movie tonight')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)