# -*- coding: utf8 -*-
import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


with open('wzu_payload.json', encoding='utf-8') as js:
    wzu_payload_dict = json.load(js)
    wzu_payload_json = json.dumps(wzu_payload_dict, ensure_ascii=False)

print(wzu_payload_json)


def sign_in():
    url = "https://lightapp.wzu.edu.cn/api/questionnaire/questionnaire/addMyAnswer"

    # 提交的json, 自己抓包
    payload = wzu_payload_json

    # headers通过抓包获取即可， 需要保持原样， 注意Cookie和User-Agent
    headers = {
        'Host': 'lightapp.wzu.edu.cn',
        'Content-Type': 'application/json',
        'Origin': 'https://lightapp.wzu.edu.cn',
        'Cookie': '自行抓取',
        'Content-Length': '5910',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'edu.wzu.wsnew',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'User-Agent':
            '自行抓取',
        'Referer':
            'https://lightapp.wzu.edu.cn/questionnaire/addanswer?page_from=onpublic&activityid=2241&can_repeat=1',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload.encode('utf-8'))
    responseBody = json.loads(response.text)
    return responseBody


def send_mail(title, message):
    ''' title:邮件标题'''
    ''' message:邮件正文'''
    my_sender = ''  # 发件人邮箱账号
    my_pass = ''  # 发件人qq邮箱授权码，获取方法自己百度
    my_user = ''  # 收件人邮箱账号，可以发送给自己
    ret = True
    try:
        mail_msg = """
            <p>""" + message + """ </p>
            """
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(
            ["", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["",
                                my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com",
                                  465)  # 发件人邮箱中的SMTP服务器，端口是465，固定的，不能更改
        server.login(my_sender,
                     my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.set_debuglevel(1)
        server.sendmail(my_sender, [
            my_user,
        ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as err:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(err)
        ret = False
    return ret

def main_handler():
    result = sign_in()
    print(result)
    title = '今日健康打卡结果'
    if result['errcode'] == 0:
        title += "<提交成功>"
    else:
        title += "<提交失败>"

    ret = send_mail(title, str(result))
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

if __name__ == "__main__":
    print("运行了要")
    main_handler()
