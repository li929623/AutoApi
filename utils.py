import logging
import random

import yaml
import app
class Base:
    #日志
    def log(self):
        # 创建日志器
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # 创建控制，文件处理器
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            path = app.Base_Dir + '/log/log.text'
            file_handler = logging.FileHandler(path, mode='a', encoding='UTF-8')
            # 设置输出格式
            console_fmt = "%(name)s****%(levelname)s****    %(message)s"
            file_fmt = "%(name)s****%(levelname)s****    %(message)s"
            # 格式话
            fmt1 = logging.Formatter(console_fmt)
            fmt2 = logging.Formatter(file_fmt)
            # 添加处理器
            console_handler.setFormatter(fmt1)
            file_handler.setFormatter(fmt2)
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
            return logger
    #读取yaml文件参数
    def read_parms(self):
        with open("./data/parms.yaml",encoding="utf-8") as f:
            result=yaml.load(stream=f,Loader=yaml.FullLoader)
            return result
    #写入yaml文件参数
    def write_parms(self,data):
        with open ("./data/parms.yaml",encoding="utf-8",mode="w") as f:
            yaml.dump(data,stream=f,allow_unicode=True)
    #获取随机数
    def random_int(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                       "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        #随机选
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


    # #封装发送请求
    # def send_request(self,method,url,data,**kwargs):
    #     if method =="get":
    #         return request(method, url, params=data,**kwargs)
    #     else:
    #         return request(method, url, json=data,**kwargs)







