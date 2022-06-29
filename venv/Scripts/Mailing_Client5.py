# Mailing client
# Sending an email with Python
# Modified script 4
# Formatting the contents of our mail properly
# Also, we are going to prompt the user to enter their email, password, content of their amil, Subject, as well as their recipient
# In this script, we have included pdf 



from smtplib import SMTP_SSL
from email.message import EmailMessage


server = SMTP_SSL("smtp.gmail.com", 465)

User_email =(input("Enter your email address: ")).lower()
User_password = input("Enter your email password: ")
Recipient_email =(input("Enter recipient email address: ")).lower()
Email_subject = (input("Enter the subject of your mail: ")).title()
Sender_Name =(input("Enter your fullname: ")).title()
Email_content = input("Enter the body of your mail: ")
server.login(User_email, User_password)

Pdf_Files =["pdf1.pdf", "pdf2.pdf", "pdf3.pdf"]


Message = EmailMessage()
Message["From"] = Sender_Name
Message["To"] = Recipient_email
Message["Subject"] = Email_subject
Message.set_content(Email_content)

for pdf in Pdf_Files:
    opened_pdf = open(pdf, "rb")
    pdf_attachment = opened_pdf.read()
    Message.add_attachment(pdf_attachment, maintype="image", subtype="octet-stream")


server.send_message(Message)


