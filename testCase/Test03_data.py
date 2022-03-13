import unittest
from ddt import ddt, file_data
import app
from Api import log
from Api.key import key
from testCase.Test01_login import _1login


@ddt
class _3data(unittest.TestCase):
    @file_data("../data/userdata.yaml")
    #获取用户资料
    def test01_data(self,**kwargs):
        url=app.Base_url+kwargs["request"]["url"]
        log.info(f"url为：{url}")
        kwargs["request"]["headers"]["Authorization"] = _1login.Token
        headers = kwargs["request"]["headers"]
        log.info(f"请求头：{headers}")
        res=key().data_api(url,headers)
        log.info(res.json())
        self.assertEqual(kwargs["assert"]["message"],res.json()["message"])

if __name__ == '__main__':
     unittest.main()


