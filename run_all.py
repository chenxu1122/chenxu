# -*- coding:utf-8 -*-
# @Time : 4/19/2021 1:55 PM
# @Author: 宁晨旭
# @File : run_all.py

import unittest
from HTMLTestRunner3 import HTMLTestRunner
from config import globalconfig
import time
from public.utils.mail import SendMail
now = time.strftime("%Y-%m-%d_%H_%M_%S")    # 生成时间戳
report_path = globalconfig.report_path     # 生成报告的路径
filename = report_path+"\\"+str(now)+"_ui_report.html"

# print(now)
# print(path)


def auto_run():
    suite = unittest.TestSuite()    # 创建一个套件、容器，用来装要运行的测试用例
    loader = unittest.TestLoader()  # 加载测试用例
    suite.addTest(loader.loadTestsFromName("public.pages.login.TestLogin.testLogin"))
    suite.addTest(loader.loadTestsFromName("TestCase.SetUp_Module.SetUp_Module.test001_SetUp_Module"))
    # print(suite)
    f = open(filename, "wb")
    runner = HTMLTestRunner(stream=f, title=u"Discuzz论坛项目ui自动化测试报告", description=u"用例执行情况如下")
    runner.run(suite)

def send_mail():
    sm = SendMail(send_msg=filename, attachment=filename)
    sm.send_mail()    # 调用send_mail 实例方法发邮件

if __name__ == '__main__':
    auto_run()
    send_mail()










