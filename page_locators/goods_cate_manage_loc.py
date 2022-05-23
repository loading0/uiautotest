# -*- encoding: utf-8 -*-
# @Time  : 2022/5/9 15:29
# @Author: loading_f
# @File  : goods_cate_manage_loc.py


class GoodsCateManageLocator:
    # 侧边栏 商品分类管理tab
    left_cate_manage_loc = ('xpath', '/Html/body/div[2]/div[1]/div/div[2]/ul[1]/li[3]/dl/dd[2]/a')

    # 商品分类管理页面元素
    # 添加分类 按钮
    add_cate_loc = ('xpath', '/Html/body/div[2]/div[3]/div[1]/div/div[1]/div/button[1]')
    # 分类名称
    cate_name_loc = ('xpath', '//*[@id="layui-layer3"]/div[2]/form/div[1]/label[1]/input')
    # 商品分类描述
    cate_remark_loc = ('xpath', '//*[@id="layui-layer3"]/div[2]/form/div[1]/label[2]/textarea')
    # 保存数据 按钮
    save_data_btn_loc = ('xpath', '//*[@id="layui-layer3"]/div[2]/form/div[3]/button[1]')
    # 商品管理展示列表
    goods_list_loc = ('xpath', '/Html/body/div[2]/div[3]/div[1]/div/div[3]/div/div[2]')

    # 所添加的分类删除按钮
    goods_cate_del_loc = ('xpath', '/Html/body/div[2]/div[3]/div[1]/div/div[3]/div/div[2]/div/div/div[3]/div[2]/table/tbody/tr[3]/td/div/a[3]')
    # 删除弹窗确认按钮
    confirm_del_loc = ('xpath', '//*[@id="layui-layer8"]/div[3]/a[1]')
