# Mailing client
# Sending an email with Python
# Modified script 4
# Formatting the contents of our mail properly
# Also, we are going to prompt the user to enter their email, password, content of their amil, Subject, as well as their recipient
# In this script, we have included images

from smtplib import SMTP_SSL
from email.message import EmailMessage
import imghdr

server = SMTP_SSL("smtp.gmail.com", 465)

User_email =(input("Enter your email address: ")).lower()
User_password = input("Enter your email password: ")
Recipient_email =(input("Enter recipient email address: ")).lower()
Email_subject = (input("Enter the subject of your mail: ")).title()
Sender_Name =(input("Enter your fullname: ")).title()
Email_content = input("Enter the body of your mail: ")
server.login(User_email, User_password)

Cat_images =["cat1.jpg", "cat2.jpg"]


Message = EmailMessage()
Message["From"] = Sender_Name
Message["To"] = Recipient_email
Message["Subject"] = Email_subject
Message.set_content(Email_content)
for cat_image in Cat_images:
    Cat_image = open(cat_image, "rb")
    Image_attachment = Cat_image.read()
    file_type = imghdr.what(Cat_image.name)
    filename = Cat_image.name
    Message.add_attachment(Image_attachment, maintype="image", subtype=file_type, filename=filename)


server.send_message(Message)


