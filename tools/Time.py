# -*- coding: utf-8 -*-
__author__ = "无声"

import time

def nowtime():
    nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return nowtime