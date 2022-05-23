# -*- encoding: utf-8 -*-
# @Time  : 2022/5/8 22:33
# @Author: loading_f
# @File  : goods_data_manage_action.py

from common.base import PageBase
from page_locators.goods_data_manage_loc import GoodsDataManageLocator


class GoodsDataMangeAction(PageBase):
    def check_goods_search(self):
        pics = []
        flag = False
        try:
            self.click(GoodsDataManageLocator.left_data_manage_loc)
            self.click(GoodsDataManageLocator.goods_data_manage_loc)
            self.send_keys(GoodsDataManageLocator.goods_name_input_loc, "手机")
            self.click(GoodsDataManageLocator.goods_search_bth_loc)
            if "G7475045156611480120" == self.get_text(GoodsDataManageLocator.goods_result_no_loc):
                flag = True
                pic = self.get_png()
                pics.append(pic)
                return flag, pics
        except Exception as e:
            self.log.warning("案例失败，详情：" % e)
            return flag, pics
