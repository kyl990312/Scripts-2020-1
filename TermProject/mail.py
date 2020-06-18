import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class Mail:
    def SendMail(self, datas):
        host = "smtp.gmail.com"
        port = "587"
        htmlFileName = "map.html"

        senderAddr = "rhdiddlwls@gmail.com"
        recipientAddr = "rhdiddlwls@naver.com"

        msg = MIMEMultipart()

        msg['Subject'] = "취업 어디까지 알아봤니"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        htmlFD = open(htmlFileName, 'rb')
        HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
        htmlFD.close()

        msg.attach(MIMEText("학과 : " +  datas.major, 'plain', _charset='utf-8'))
        msg.attach(MIMEText('학과 계열 : ' + datas.majorData.subject, 'plain', _charset="utf-8"))
        msg.attach(MIMEText('세부 학과 : ' + datas.majorData.department, 'plain', _charset="utf-8"))

        msg.attach(MIMEText('취업률', 'plain', _charset="utf-8"))
        for i in datas.jobData.employmentRate:
            msg.attach(MIMEText('    ' + i + ' - ' + datas.jobData.employmentRate[i], 'plain', _charset="utf-8"))

        msg.attach(MIMEText('관련 직업 : ' + datas.jobData.job, 'plain', _charset="utf-8"))
        msg.attach(MIMEText('관련 자격 : ' + datas.jobData.qualification, 'plain', _charset="utf-8"))

        s = smtplib.SMTP(host, port)
        s.ehlo()
        s.starttls()
        s.login(senderAddr, "rkddkwltjs125@")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()
