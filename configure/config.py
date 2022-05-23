# -*- encoding: utf-8 -*-
# @Time  : 2022/4/28 16:38
# @Author: loading_f
# @File  : config.py

import os
from configparser import ConfigParser


class Config:
    path = os.path.dirname(os.path.dirname(__file__))
    print("path: ", path)

    def __init__(self):
        self.json_report_path = Config.path + '/report/Json'
        self.html_report_path = Config.path + '/report/Html'
        self.pic_path = Config.path + '/report/Pic'

        self.config = ConfigParser()
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        if not os.path.exists(self.config_path):
            raise FileNotFoundError('config.ini文件不存在！')

        self.config.read(self.config_path)

        # domain
        self.domain = self.get_conf('domain', 'domain')

        # case_path
        self.case_path = self.get_conf('case_path', 'case_path')

        # 用户登录账号
        self.username = self.get_conf('username', 'username')
        self.password = self.get_conf('password', 'password')

    def get_conf(self, title, value):
        """
        read .ini
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        change .ini
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        add .ini
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)


if __name__ == '__main__':
    print(Config().html_report_path)
    print(Config().config_path)


