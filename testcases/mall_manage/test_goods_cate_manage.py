# -*- encoding: utf-8 -*-
# @Time  : 2022/5/9 15:52
# @Author: loading_f
# @File  : test_goods_cate_manage.py.py

import os
import pytest
import allure
from time import sleep
from common.driver_init import driver_init
from configure.config import Config
from page_actions.goods_cate_manage_action import GoodsCateManageAction


@allure.feature("商品分类管理测试")
class TestGoodsCateManage:
    def setup(self):
        self.driver = GoodsCateManageAction(driver_init())
        self.driver.login()
        sleep(1)

    def teardown(self):
        sleep(3)
        self.driver.quit_Browser()

    @allure.story("商品分类添加")
    def test_goods_cate_add(self):
        """
        1.点击添加分类按钮
        2.输入商品分类名称
        3.输入商品分类描述
        4.点击保存按钮
        5.校验新添加商品分类成功展示
        :return:
        """
        exp = True
        case_name = "商品分类添加测试"
        expect = "商品分类添加成功"
        flag, pngs = self.driver.check_goods_add()
        if flag is True:
            result = "1.添加商品分类成功 2.校验所加分类成功"
        else:
            result = "测试失败，详情查看errMsg"
        self.driver.Assert.assert_equal(res=flag, expect=exp)
        self.driver.allure_report(func=self.test_goods_cate_add, case_name=case_name, pic_list=pngs, expect=expect,
                                  res=result)


if __name__ == '__main__':
    conf = Config()
    json_report_path = conf.json_report_path
    html_report_path = conf.html_report_path
    pytest.main(["-s", "-v", f"--alluredir={json_report_path}", "--clean-alluredir"])
    os.system(f"allure generate {json_report_path} -o {html_report_path} --clean")
    # args = ["-n 1", "-s", "-v", f'--alluredir=./temp']
    # pytest.main(args)
    # os.system("allure generate ./temp -o ./report --clean")

