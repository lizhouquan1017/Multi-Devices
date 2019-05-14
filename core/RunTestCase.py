# -*- coding: utf-8 -*-
__author__ = "无声"

import unittest
import time
# from BeautifulReport import BeautifulReport
from tools import Config
import os
from airtest.core.api import *
from tools import  File
from tools import Time
from TestCase import *

def RunTestCase(starttime,devices):
    print("进入",devices,"的RunTestCase")
    # 获取路径
    configPath = "./config.ini"
    package = Config.getValue(configPath, "packName")[0]
    casepath = os.path.join(os.getcwd(), "TestCase")
    if not os.path.exists(casepath):
        print("测试用例需放到‘TestCase’文件目录下")
    reportpath = os.path.join(os.getcwd(), "Report")
    if not os.path.exists(reportpath):
        os.mkdir(reportpath)
        os.mkdir(reportpath+"/Screen")
    #读取ini文件，获得期望测试的用例列表
    TestList=Config.getValue(configPath, "testcase")
    # 通过GetPyList方法，取得目录里可测试的用例列表
    scriptList = File.GetPyList(casepath)
    suite = unittest.TestSuite()
    for i in range(len(TestList)):
        fileName = "TC_" + TestList[i]
        if fileName in scriptList:
            result = globals()[fileName].Main(devices)
            suite.addTests(result)
    unittestReport = BeautifulReport(suite)
    #处理模拟器端口用的冒号
    if ":" in devices:
        devices=devices.split(":")[1]
    print("devices=",devices)
    nowtime=time.strftime("%H%M%S")
    unittestReport.report(filename=devices+"_"+str(nowtime),description=package, report_dir=reportpath)
    stop_app(package)


#RunTestCase(time.time(),"127.0.0.1:62001")
