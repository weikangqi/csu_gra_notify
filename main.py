import request
import shutil
import time
import schedule
import smtplib
from email.mime.text import MIMEText
import logging
import json
import sqlite3
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
    # message['To'] = receivers[0] 
    try:
        smtpObj = smtplib.SMTP() 
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        for i in receivers:
            smtpObj.sendmail(
                sender,i,message.as_string()) 
        #退出
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误
def main():
    with open('set.json', 'r') as file:
        config = json.load(file)
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    schedule.every(30).minutes.do(job,(config,cursor,conn))
    while True:
        schedule.run_pending()
        time.sleep(1)
    

def job(parm):
    
    config,cursor,conn = parm
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    test = request.get_html(config["website"])
    print(test)
    buffer = []
    for i in test: 
        cursor.execute(f"SELECT * FROM my_table WHERE string1 = ?  OR string2 = ?",i)
        result = cursor.fetchall()
        if result == []:
            buffer.append(i)
            cursor.execute(f"INSERT INTO my_table (string1, string2) VALUES (?, ?)",i)
            conn.commit()
        else:
            print("no news")
    for i in buffer:
        email(config,i[0],i[1])

if __name__ == '__main__':
    with open('set.json', 'r') as file:
        config = json.load(file)
    email(config,"hello","I am 1163")
    
    # main()