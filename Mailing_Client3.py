# Mailing client
# Sending an email with Python
# Modified script 3
# Formatting the contents of our mail properly
# Also, we are going to prompt the user to enter their email, password, content of their amil, Subject, as well as their recipient
import smtplib
from email.message import EmailMessage

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
user_email =input("Enter your email address: ")
User_password = input("Enter your email password: ")
Recipient_email =input("Enter recipient email address: ")
Email_subject = input("Enter the subject of your mail: ")
Sender_Name =input("Enter your fullname: ")
Email_content = input("Enter the body of your mail: ")

server.login(user_email, User_password)


Message = EmailMessage()
Message["From"] = Sender_Name
Message["To"] = Recipient_email
Message["Subject"] = Email_subject
Message.set_content(Email_content)

server.send_message(Message)


