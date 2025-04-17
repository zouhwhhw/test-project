import requests
///
webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=5c002637-a4ec-497b-b796-00c15a925308"


msg_data = {
    "msgtype": "text",
    "text": {

        "content": "每周五排查网站功能和购买\n reddit留评 \n Quora、openai养号 \n TW、FB发帖",
        "mentioned_list": "@all"
    }
}
response = requests.post(webhook, json=msg_data)