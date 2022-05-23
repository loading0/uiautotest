# -*- encoding: utf-8 -*-
# @Time  : 2022/4/28 15:52
# @Author: loading_f
# @File  : driver_init.py

import os
import time
from selenium import webdriver
from utils.log import LogInfo
from configure.config import Config
from selenium.webdriver.chrome.service import Service

# chrome驱动path
DriverPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          Config().get_conf('chrome_driver', 'chrome_driver'))
# chrome是否无头模式
headless = eval(Config().get_conf("headless", 'headless'))
case_path = Config().get_conf("case_path", 'case_path')
log = LogInfo()


def driver_init():
    try:
        service = Service(DriverPath)
        service.start()
        opt = webdriver.ChromeOptions()

        if headless:
            opt.add_argument('--headless')
        # 某个业务需要启用无痕模式时使用
        # if case_path == 'testcases/xxx':
        #     opt.add_argument("–incognito")

        # 指定浏览器分辨率
        opt.add_argument('--window-size=1920,1080')
        opt.add_argument('--no-sandbox')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--disable-crash-reporter')
        opt.add_argument('--disable-extensions')
        opt.add_argument('--disable-in-process-stack-traces')
        opt.add_argument('--disable-logging')
        # options.AddArgument('--disable-dev-shm-usage')  //for vm
        opt.add_argument('--log-level=3')
        # opt.add_argument('--output=/dev/null')
        # 指定浏览器为中文
        opt.add_argument("-lang=zh-cn")
        # 添加沙盒模式
        opt.add_argument("--no-sandbox")
        opt.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome(executable_path=DriverPath, options=opt)
        driver = webdriver.Remote(service.service_url, options=opt)
        driver.implicitly_wait(10)

        # return driver
        return driver, service
    except Exception as e:
        log.error(str(e))
        log.error('启动浏览器发生错误!')


if __name__ == '__main__':
    print(driver_init())
