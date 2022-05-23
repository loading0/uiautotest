# -*- encoding: utf-8 -*-
# @Time  : 2022/5/8 22:26
# @Author: loading_f
# @File  : test_goods_data_manage.py

import os
import pytest
import allure
from time import sleep
from common.driver_init import driver_init
from configure.config import Config
from page_actions.goods_data_manage_action import GoodsDataMangeAction


@allure.feature("商品数据管理测试")
class TestGoodsDataManage:
    def setup(self):
        self.driver = GoodsDataMangeAction(driver_init())
        self.driver.login()
        sleep(1)

    def teardown(self):
        sleep(3)
        self.driver.quit_Browser()

    @allure.story("检验商品数据搜索功能")
    def test_goods_data_search(self):
        """
        1.进入商品数据管理tab页
        2.输入商品名称 test1
        3.点击搜索按钮
        4.校验商品编号
        :return:
        """
        exp = True
        case_name = "商品数据管理搜索测试"
        expect = "商品数据搜索成功"
        flag, pngs = self.driver.check_goods_search()
        if flag is True:
            result = "1.成功搜索指定内容；  2.成功校验结果内容"
        else:
            result = "测试失败，详情查看errMsg"
        self.driver.Assert.assert_equal(res=flag, expect=exp)
        self.driver.allure_report(func=self.test_goods_data_search, case_name=case_name, pic_list=pngs, res=result,
                                  expect=expect)


if __name__ == '__main__':
    conf = Config()
    json_report_path = conf.json_report_path
    html_report_path = conf.html_report_path
    pytest.main(["-s", "-v", f"--alluredir={json_report_path}", "--clean-alluredir"])
    os.system(f"allure generate {json_report_path} -o {html_report_path} --clean")
