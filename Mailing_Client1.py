# Mailing client
# Sending an email with Python
# Original copy

import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    password = input("Enter your generated gmail password: ")
    smtp.login("hodote76@gmail.com", password)
    Subject = "Dinner on Friday"
    Body = " Hey pal, we shall be having dinner tomorrow"
    Message = f"Subject: {Subject} \n\n Body: {Body}"
    smtp.sendmail("hodote76@gmail.com", "temitopeomisore235@gmail.com", Message)