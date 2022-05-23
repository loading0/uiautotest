# -*- encoding:utf-8 -*-

import os
import sys
import pytest
from configure.config import Config
from utils.log import LogInfo
from common.case_count import get_nums

if __name__ == '__main__':
    conf = Config()
    log = LogInfo()
    # 集成到jenkins时/控制台执行时，通过传递参数到main函数，
    if len(sys.argv) > 2:
        # jenkins自动化执行时，控制台传入报告路径与测试域名
        xml_report_path = os.path.join(sys.argv[1])
        headless = os.path.join(sys.argv[2])
        test_host = os.path.join(sys.argv[3])
        driver = os.path.join(sys.argv[4])
        case_path = os.path.join(sys.argv[5])

        # config文件初始化
        conf.set_conf('chrome_driver', 'chrome_driver', driver)
        conf.set_conf('headless', 'headless', headless)
        conf.set_conf('domain', 'domain', test_host)
        conf.set_conf('case_path', 'case_path', case_path)
    else:
        json_report_path = conf.json_report_path
        html_report_path = conf.html_report_path

    case_path = Config().get_conf("case_path", 'case_path')
    case_nums = get_nums()[0]
    case_list = get_nums()[1]
    # -s 关闭捕捉，不输出打印信息; -v 详细打印; -n 6 6个进程; -case_path 测试地址
    # -x:出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
    # args = ["-n 2", "-s", "-v", f"--alluredir=./temp", "--clean-alluredir", case_path]
    # os.system("allure generate ./temp -o ./report --clean")

    pytest.main(["-s", "-v", f"--alluredir={json_report_path}", "--clean-alluredir", case_path])
    os.system(f"allure generate {json_report_path} -o {html_report_path} --clean")

