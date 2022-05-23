# -*- encoding: utf-8 -*-
# @Time  : 2022/5/11 12:49
# @Author: loading_f
# @File  : case_count.py


from configure.config import Config
from testcases.mall_manage.test_goods_data_manage import TestGoodsDataManage
from testcases.mall_manage.test_goods_cate_manage import TestGoodsCateManage

mall_manage_case_class_list = [
    TestGoodsCateManage,
    TestGoodsDataManage
]
user_manage_case_class_list = []
case_path = Config().get_conf("case_path", 'case_path')


def get_nums() -> tuple:
    """
    统计所测模块所有用例数目，和用例名称
    :return:
    """
    case_list = []
    count_list = []
    if case_path == 'testcases/mall_manage':  # 商城管理模块用例
        count_list = mall_manage_case_class_list
    elif case_path == 'testcases/user_manage':  # 用户管理的用例
        count_list = user_manage_case_class_list
    for case in count_list:
        case_list.extend([func for func in dir(case) if func.startswith("test")])
    case_nums = len(case_list)
    return case_nums, case_list


if __name__ == '__main__':
    print(get_nums())
