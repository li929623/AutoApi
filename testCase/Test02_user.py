import unittest
import app
from ddt import file_data, ddt
from Api import log
from Api.key import key
from testCase.Test01_login import _1login

from utils import Base


@ddt
class _2User(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        user_id=None
        mobile=None
    @file_data("../data/userlist.yaml")
    # 用户列表获取
    def test01_userlist(self, **kwargs):
        url = app.Base_url + kwargs["request"]["url"]
        kwargs["request"]["headers"]["Authorization"] =_1login.Token
        headers = kwargs["request"]["headers"]
        data = kwargs["request"]["data"]
        res = key().list_api(url, headers, data)
        self.assertEqual(res.json()["message"], kwargs["assert"]["message"])

    @file_data("../data/adduser.yaml")
    #添加用户
    def test02_adduser(self,**kwargs):
        log.info(f'接口测试:{kwargs["info"]}开始')
        url=app.Base_url+kwargs["request"]["url"]
        log.info(f"Url为：{url}")
        #将token赋值到headers
        kwargs["request"]["headers"]["Authorization"]=_1login.Token
        _1login.mobile=Base().random_int()
        kwargs["request"]["data"]["mobile"]=_1login.mobile
        headers = kwargs["request"]["headers"]
        log.info(f"请求头：{headers}")
        data = kwargs["request"]["data"]
        log.info(f"请求体：{data}")
        res = key().add_api(url, headers, data)
        result=res.json()["data"]
        try:
            if result:
                _2User.user_id=result["id"]
                log.info(f"获取id成功：{_2User.user_id}")
            else:
                log.info(f"获取id失败")
        except Exception as e:
            print(e)
        self.assertEqual(res.json()["message"],kwargs["assert"]["message"])
        log.info(f"{kwargs['info']}接口测试完成")

    @file_data("../data/updateuser.yaml")
    # 修改用户
    def test03_updateuser(self, **kwargs):
        log.info(f'接口测试:{kwargs["info"]}开始')
        url=app.Base_url+kwargs["request"]["url"]+f'{_2User.user_id}'
        log.info(f"Url为：{url}")
        # 将token赋值到headers
        kwargs["request"]["headers"]["Authorization"] = _1login.Token
        headers = kwargs["request"]["headers"]
        log.info(f"请求头：{headers}")
        data = kwargs["request"]["data"]
        log.info(f"请求体：{data}")
        res = key().update_api(url, headers, data)
        self.assertEqual( kwargs["assert"]["message"],res.json()["message"])
        print(res.json())
        log.info(f"'{kwargs['info']}'接口测试完成")

    #获取用户信息
    @file_data("../data/getuser.yaml")
    def test04_getuser(self, **kwargs):
        log.info(f'接口测试:{kwargs["info"]}开始')
        url = app.Base_url + kwargs["request"]["url"] + f'{_2User.user_id}'
        log.info(f"Url为：{url}")
        # 将token赋值到headers
        kwargs["request"]["headers"]["Authorization"] = _1login.Token
        headers = kwargs["request"]["headers"]
        log.info(f"请求头：{headers}")
        res = key().get_api(url, headers)
        log.info(f"断言开始")
        self.assertEqual(kwargs["assert"]["message"], res.json()["message"])
        print(res.json())
        log.info(f"'{kwargs['info']}'接口测试完成")
    #删除用户
    @file_data("../data/delete.yaml")
    def test05_deleteuser(self, **kwargs):
        log.info(f'接口测试:{kwargs["info"]}开始')
        url = app.Base_url + kwargs["request"]["url"] + f'{_2User.user_id}'
        log.info(f"Url为：{url}")
        # 将token赋值到headers
        kwargs["request"]["headers"]["Authorization"] = _1login.Token
        headers = kwargs["request"]["headers"]
        log.info(f"请求头：{headers}")
        res = key().delte_api(url, headers)
        log.info(f"断言开始")
        self.assertEqual(kwargs["assert"]["message"], res.json()["message"])
        print(res.json())
        log.info(f"'{kwargs['info']}'接口测试完成")

if __name__ == '__main__':
     unittest.main()
