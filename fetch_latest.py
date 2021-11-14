import requests
import json
import time

# url抓一下最全的那个问卷页面好像是，反正类似下面的链接
url = "https://lightapp.wzu.edu.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code=wzu&stu_code....."

headers = {
        'Host': 'lightapp.wzu.edu.cn',
        'Content-Type': 'application/json',
        'Origin': 'https://lightapp.wzu.edu.cn',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'edu.wzu.wsnew',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'User-Agent':
            '自行抓取',
        'Referer':
            'https://lightapp.wzu.edu.cn/questionnaire/my',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate'
    }


res = requests.get(url, headers=headers)
#print(res.text)

data = json.loads(res.text)
#print(data['data'])
#拿到最新的打卡记录
new_data = data['data'][0]['private_id']
timestamp = new_data[5:-3]
time_data = time.localtime(int(timestamp))
print(time.strftime("%Y-%m-%d %H:%M:%S", time_data))

