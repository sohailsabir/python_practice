import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server=smtplib.SMTP('smtp.gmail.com',25)

server.ehlo()

with open('password.text','r')as f:
    password=f.read()

server.login('sohailsabir6565@gmail.com',password)


msg=MIMEMultipart()
msg['From']='sohailsabir'
msg['TO']='sohailsabir6666@gmail.com'
msg['Subject']='Just a test'
