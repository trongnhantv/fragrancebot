import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def sendemail(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("nhaphanguscom@gmail.com", "Lochobame77!!jft")
    #prepare the content
    body = content
    #prepare the email presentation
    fromaddr = "nhaphanguscom@gmail.com"
    toaddr = "nhannthuynh@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Fragrancenet Alert"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
sendemail("nhan")
