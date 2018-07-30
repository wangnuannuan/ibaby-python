import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    global email_host
    global password
    password = "fuutivyxfhwsbjei"
    email_host = "smtp.qq.com"
    send_user = "1961295051@qq.com"

    def send_mail(self,user_list,sub,content):
        user = "shape" + "<" + send_user + ">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP_SSL()
        server.connect(email_host,465)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

if __name__ == '__main__':
    send = SendEmail()
    user_list = ['2022437469@qq.com','nuannuan12016@outlook.com']
    sub = "测试邮件"
    content = "ceshi看看"
    send.send_mail(user_list,sub,content)
