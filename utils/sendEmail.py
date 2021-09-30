import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_mail import Mail, Message

import sentry_sdk
sentry_sdk.init(
    "https://4963b311c67b4e84812569fcc9224980@o518216.ingest.sentry.io/5627744",
    traces_sample_rate=1.0
)

def sendEmail(address, subject, content, mail):

    msg = Message("Hello", sender='support@jy.com.ua', recipients=[address, ])
    msg.body = content
    msg.subject = subject
    mail.send(msg)

    # senderAddress = 'support@jy.com.ua'
    # senderPass = 'Ukraine601'
    #
    # message = MIMEMultipart()
    # message['From'] = str(senderAddress)
    # message['To'] = str(address)
    # message['Subject'] = str(subject)
    #
    # message.attach(MIMEText(content, 'html'))
    #
    # session = smtplib.SMTP('smtp.gmail.com', 587)
    # session.starttls()
    # session.login(senderAddress, senderPass)
    # text = message.as_string()
    # session.sendmail(senderAddress, address, text)
    # session.quit()
