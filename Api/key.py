import requests
class key:
    #登录接口
    def login_api(self,url,headers,data):
       return requests.post(url,headers=headers,json=data)
    #添加接口
    def add_api(self,url,headers,data):
       return requests.post(url,headers=headers,json=data)
    #获取列表
    def list_api(self,url,headers,data):
        return requests.get(url, headers=headers, params=data)
    #修改用户
    def update_api(self,url,headers,data):
        return requests.put(url, headers=headers,json=data)
    #获取用户信息
    def get_api(self, url, headers):
        return requests.get(url, headers=headers)
    #删除用户信息
    def delte_api(self, url, headers):
        return requests.delete(url, headers=headers)
    #用户资料信息
    def data_api(self, url, headers):
        return requests.post(url, headers=headers)

