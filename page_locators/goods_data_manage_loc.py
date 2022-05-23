# -*- encoding: utf-8 -*-
# @Time  : 2022/5/8 22:11
# @Author: loading_f
# @File  : goods_data_manage_loc.py

from common.base import PageBase


class GoodsDataManageLocator:
    # 侧边栏 数据管理tab元素
    left_data_manage_loc = ('xpath', '/Html/body/div[2]/div[1]/div/div[2]/ul[1]/li[1]/a')
    # ('xpath', "//a[text()='数据管理']")
    # left_user_manage_loc = ('xpath', '/Html/body/div[2]/div[1]/div/div[2]/ul[1]/li[2]/a')
    # ('xpath', "//a[text()='用户管理']")

    # 商品数据管理 tab页 元素
    goods_data_manage_loc = ('xpath', '/Html/body/div[2]/div[1]/div/div[2]/ul[1]/li[3]/dl/dd[1]/a')  # ('xpath', "//a[text()='商品数据管理']")
    goods_name_input_loc = ('xpath', '//input[@placeholder="请输入编号或名称"]') # ('xpath', '/html/body/div[2]/div[3]/div[1]/div/div[3]/div/div/div/form/div[1]/label[2]/input')  # ('xpath', '//input[@placeholder="请输入商品名称"]')
    goods_search_bth_loc = ('xpath', '/html/body/div[2]/div[3]/div[1]/div/div[3]/div/div/div/form/div[8]/button')  # ('xpath', "//button//span[text()='搜 索']")
    goods_result_no_loc = ('xpath', '/html/body/div[2]/div[3]/div[1]/div/div[3]/div/div/div/table/tbody/tr[1]/td[3]/div[2]/div[2]/span')

    # 页面公共元素
    control_board_loc = ('xpath', '/Html/body/div[2]/div[2]/ul[1]/li[3]/a')
    wechat_admin_loc = ('xpath', '/Html/body/div[2]/div[2]/ul[1]/li[4]/a')
    system_admin_loc = ('xpath', '/Html/body/div[2]/div[2]/ul[1]/li[5]/a')