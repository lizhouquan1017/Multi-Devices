# -*- coding: utf-8 -*-
__author__ = "无声"


import os
import time

def GetScreen(startTime,devices,action):
    reportpath = os.path.join(os.getcwd(), "Report")
    screenpath = os.path.join(reportpath, "Screen")
    print("screenpath=",screenpath)
    png = screenpath +"\\"+ time.strftime('%Y%m%d_%H%M%S', time.localtime(startTime)) + "_" +  "_" + action+ ".png"
    print("png=",png)
    os.system("adb -s " + devices + " shell screencap -p /sdcard/screencap.png")
    fp = open(png, "a+", encoding="utf-8")
    fp.close()
    os.system("adb -s " + devices + " pull /sdcard/screencap.png " + png)
    print("<img src='" + png + "' width=600 />")
    return png

