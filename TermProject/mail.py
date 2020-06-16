import mimetypes
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import smtplib, ssl


host = "smtp.gmail.com"
port = "587"
htmlFileName = "map.html"

senderAddr = "rhdiddlwls@gmail.com"
recipientAddr = "rhdiddlwls@naver.com"

msg = MIMEBase("multiple", "alternative")

msg['Subject'] = "Test email in Python"
msg['From'] = senderAddr
msg['To'] = recipientAddr

htmlFD = open(htmlFileName,'rb')
HtmlPart = MIMEText(htmlFD.read(),'html',_charset='UTF-8')
htmlFD.close()


s = smtplib.SMTP(host, port)
s.ehlo()
s.starttls()
s.login(senderAddr,"rkddkwltjs125@")
s.sendmail(senderAddr, [recipientAddr], msg.as_string())
s.close()