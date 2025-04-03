import requests

webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=abc3b2b9-b812-4d82-8d13-8dac6c98e419"


msg_data = {
    "msgtype": "text",
    "text": {

        "content": "疯狂星期四",
        "mentioned_list": "@all"
    }
}
response = requests.post(webhook, json=msg_data)