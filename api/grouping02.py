# from 第二层 import BaseApi
from api.base01 import BaseApi


class Grouping(BaseApi):
    def tjfz(self):   #添加分组
        data = {'method':'post',
                'url':'http://123.56.138.96:3012/api/ainews-user/company-group/create',
                'headers':{'Authorization': self.get_token()},
                'json':{"name":"1375"}
        }
        return self.send(data)

    def tjgs(self):#添加公司
        data = {'method':'post',
                'url':'http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
                'headers':{'Authorization': self.get_token()},
                'json':{"company_code": "000001", "group_id":self.id()}}

        return self.send(data)

    def scfz(self):#删除分组
        data = {'method':'get',
                'url':'http://123.56.138.96:3012/api/ainews-user/company-group/delete',
                'headers':{'Authorization': self.get_token()},
                'params':{"id":self.id()}}
        return  self.send(data)






















