import unittest
from ddt import file_data, ddt
import app
from Api import log
from Api.key import key
from utils import Base

@ddt
class _1login(unittest.TestCase):
    #实例化对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.base=Base()
        cls.Token=None

    @file_data("../data/login.yaml")
    def test01_login(self,**kwargs):
        log.info("开始测试""{}""接口".format(kwargs["info"]))
        url=app.Base_url+kwargs["request"]["url"]
        log.info("请求URL:""{}".format(url))
        data=kwargs["request"]["data"]
        headers=kwargs["request"]["headers"]
        log.info("输入参数:""{}{}".format(headers, data))
        # res=key().send_request("post",url,headers,data)
        res=key().login_api(url,headers,data)
        log.info("开始断言")
        #断言
        ecp = kwargs["assert"]["message"]
        self.assertEqual(res.json()["message"],ecp)
        log.info("测试结果：""{}".format(res.json()["message"]))
        log.info("预期结果：""{}".format(kwargs["assert"]["message"]))
        token=res.json()['data']
        try:
            if token:
                _1login.Token = "Bearer " + res.json()['data']
                log.info("赋值token：""{}".format(_1login.Token))
            else:
                log.info(f"获取token失败，{ecp}")
        except Exception as e:
            print(e)


        # if Token:
        #     log.info("提取token:""{}".format(token))
        # #将提取的token值字典话
        #     dict_token={"Token":token}
        # #将Token写入parms
        #     self.base.write_parms(dict_token)
        # else:
        #     log.info("token提取失败")

        log.info(f'{kwargs["info"]}场景测试完成')

    # @file_data("../data/adduser.yaml")
    # def test02_Adduser(self,**kwargs):
    #     url=app.Base_url+kwargs["request"]["url"]
    #     print(url)
    #     #赋值token
    #     kwargs["request"]["headers"]["Authorization"]=Login.Token
    #     headers=kwargs["request"]["headers"]
    #     print(headers)
    #     data=kwargs["request"]["data"]
    #     res=key().add_api(url,headers,data)
    #     print(res.json())

#
# if __name__ == '__main__':
#      unittest.main()

