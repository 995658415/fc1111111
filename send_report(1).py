import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://admin:Aa123456!@47.93.114.83:9000/job/AI/allure/widgets/suites.json"
        self.ding = "https://oapi.dingtalk.com/robot/send?access_token=975e532346e100e15cb606ee1332b64cdfff5e9c3a868e48390fc56740d30668"
        self.error = self.get_allure_error()

    def get_allure_error(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号admin,密码Aa123456!",
                    "title": "业务报警" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://admin:Aa123456!@http://47.93.114.83:9000/job/AI/allure/"
                }
            }
            requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    print(DingRobot().get_allure_error())
