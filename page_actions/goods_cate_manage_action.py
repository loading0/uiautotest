# -*- encoding: utf-8 -*-
# @Time  : 2022/5/9 15:40
# @Author: loading_f
# @File  : goods_cate_manage_action.py

from time import sleep
from common.base import PageBase
from page_locators.goods_cate_manage_loc import GoodsCateManageLocator


class GoodsCateManageAction(PageBase):
    def check_goods_add(self):
        pics = []
        flag = False
        try:
            self.click(GoodsCateManageLocator.left_cate_manage_loc)
            self.click(GoodsCateManageLocator.add_cate_loc)
            self.send_keys(GoodsCateManageLocator.cate_name_loc, "cateName1")
            self.send_keys(GoodsCateManageLocator.cate_remark_loc, "cateRmark1")
            self.click(GoodsCateManageLocator.save_data_btn_loc)
            sleep(3)
            if "cateName1" in self.get_text(GoodsCateManageLocator.goods_list_loc):
                flag = True
                pic = self.get_png()
                pics.append(pic)
                self.refresh()
                # self.click(GoodsCateManageLocator.goods_cate_del_loc)
                # self.click(GoodsCateManageLocator.confirm_del_loc)
                return flag, pics
        except Exception as e:
            self.log.warning("案例失败，详情：" % e)
            return flag, pics
