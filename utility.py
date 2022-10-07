import random
import smtplib
import os
import requests
from email.message import EmailMessage

def generateRandomNumber():
    return random.randint(1,10)

def getBlogData():
    # https://mocki.io/fake-json-api --> json website
     #return requests.get("https://mocki.io/v1/f4aff8ed-6d04-43e1-ac4f-ce373a4a64e0").json()
    return requests.get(os.getenv("BLOG_END_POINT")).json()


def send_mail(name,mail,mobile,msg):
    senderMail = 'thanigaisolutions@gmail.com'
    receipient_mail = 'thanigaifacts@gmail.com'

    mailMsg = EmailMessage()

    mailMsg['Subject'] = 'Thanigai Facts - New Contact Form!'
    mailMsg['From'] = senderMail
    mailMsg['To'] = receipient_mail
    msgfile = f"Name : {name}\nMail : {mail}\nMobile : {mobile}\nMessage : {msg}"
    mailMsg.set_content(msgfile)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("MAIL_USER_NAME"), os.getenv("MAIL_PASSWORD"))
        smtp.send_message(mailMsg)

    return True,"Message Sent Successfully!"


def contact_admin(request):
    if request.method == 'POST':
        Name = request.POST.get('userName')
        Mail = request.POST.get('userMail')
        Mobile = request.POST.get('userMobile')
        Message = request.POST.get('userMessage')
        if len(Name) == 0 or len(Mail) == 0 or len(Mobile) == 0:
            return False, ""
        else:
            MsgSent, msgStatus = send_mail(Name, Mail, Mobile, Message)
        return MsgSent, msgStatus
    return False, ''
