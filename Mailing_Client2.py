# Mailing client
# Sending an email with Python
# Modified script 1
# Rather than TLS, we are using SSL.

import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
gmail_password =input("Enter your generated password: ")
server.login("hodote76@gmail.com", gmail_password)

Head = " Testing smtp server with SSl"
Body = "Hello, this is me testing how smtp server works using SSL"

Message = f"Subject: {Head} \n\n Body: {Body}"
server.sendmail("hodote76@gmail.com", "temitopeomisore235@gmail.com", Message)


