# import unittest
# from unittest import runner
# from tools.HTMLTestRunner import HTMLTestRunner
#
# suite = unittest.TestSuite()
# suite.addTest(unittest.makesuite())
#
# report_file="/report/report{}.html".format(time.strftime(%Y%m%d-%H%M%S))
# with open(report_file,wb) as f:
#      HTMLTestRunner(f,title="接口测试报告"，description="test")
#      runner.run(suite)
import unittest
import time
import app
from tools.HTMLTestRunner import HTMLTestRunner
casepath="./testCase"
#创建测试套件
suite=unittest.TestSuite()
#添加用例以类
suite.addTests(unittest.TestLoader().discover(casepath,pattern="Test*.py"))
report=app.Base_Dir+"./report/report-{}.html".format(time.strftime('%Y%m%d-%H%M%S'))
#文件流形式打开文件
with open (report,"wb") as f:
    #创建运行器
    runner=HTMLTestRunner(f,title="IRHM测试报告")
    runner.run(suite)