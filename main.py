import request
import shutil
import time
import schedule
import smtplib
from email.mime.text import MIMEText
import logging
import json

last_news = ""



def email(config,title,content):
    mail_host = config['mail']['mail_host'] #设置服务器
    mail_user = config['mail']['mail_user'] #用户名
    mail_pass = config['mail']['mail_pass'] #口令
    sender = config['mail']['sender']
    receivers  = config['mail']['receivers']
    
    message = MIMEText(content,'plain','utf-8')
    #邮件主题       
    message['Subject'] = title
    #发送方信息
    message['From'] = sender 
    #接受方信息     
    message['To'] = receivers[0]  

    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP() 
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        #退出
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误
def main():
    with open('set.json', 'r') as file:
        config = json.load(file)
    schedule.every(4).hours.do(job,config)
    while True:
        schedule.run_pending()
        time.sleep(1)

def job(config):
    global last_news
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    test = request.get_html(config["website"])
    news = test[0]
    if news != last_news:
        email(config,news,f"{test[0]}\n{test[1]}")
        print("send email")
        last_news = news
    else:
        print("no news")
if __name__ == '__main__':
    # with open('set.json', 'r') as file:
    #     config = json.load(file)
    # email(config,"hello","I am 1163")
    main()