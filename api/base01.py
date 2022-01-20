import json

import jmespath
import requests


class BaseApi:
    def send(self, data):
        r = requests.request(**data)
        print(json.dumps(r.json(), indent=1, ensure_ascii=False))
        return r

    def id(self):#获取id
        # data = {'method': "get",
        #         'url': "http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group",
        #         'headers': {'Content-Type': 'application/json; charset=utf-8',
        #                     'Authorization': self.get_token()},
        #         'params': {"page": 1,
        #                    "per_page": 10,
        #                    "start_time": "2021-12-30",
        #                    "end_time": "2022-01-13"}}
        data = {"page": 1,
                "per_page": 10,
                "start_time": "2021-12-30",
                "end_time": "2022-01-13"}
        r = requests.request(method='get',
                             url='http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group',
                             headers={'Authorization': self.get_token()},
                             params=data
                             )
        bb=jmespath.search("[?name=='1375'].id", r.json())
        print(bb)
        return bb


    def get_token(self):   #获取令牌
        data = {'name': 'lsj1', 'password': '123123'}
        r = requests.post('http://123.56.138.96:3012/api/ainews-user/user/login',
                          json=data)

        return r.json().get('access_token')

