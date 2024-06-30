import requests
import json
import datetime

# 設定你的 LINE Channel Access Token
channel_access_token = 'aHZO9J6wiqzt+81cxgoKWH5mn2qLnYV8uFul2c7ns/HSMwk4mUJ8JHNPUwr5jrW6Uo4CLbBwTzP0T/7y1APAHh0pi+C0dskGJQq77EqPpV8SPYUnI1CfYdmbUfupfparL1zUqjhR9M3bg318FAHOhwdB04t89/1O/w1cDnyilFU='

# 設定推送訊息的 URL
url = 'https://api.line.me/v2/bot/message/push'

# 設定消息的接收者和消息內容
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {channel_access_token}'
}

# 準備訊息內容
data = {
    'to': 'YOUR_GROUP_ID',
    'messages': [
        {
            'type': 'text',
            'text': '@everyone 大家來約下個月何時吃飯!'
        }
    ]
}

# 發送訊息的函數
def send_message():
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.json())

# 檢查今天是否是每月20號，且現在時間是否是20點
now = datetime.datetime.now()
if now.day == 20 and now.hour == 20:
    send_message()
