# -*- encoding: utf-8 -*-
# @Time  : 2022/4/28 15:42
# @Author: loading_f
# @File  : log.py

import logging
import os
import sys
import time
# from cloghandler import ConcurrentRotatingFileHandler  # 这个包会导致windows下单个进程报错的情况
# from urllib3.connectionpool import log as urllibLogger
# from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
from concurrent_log_handler import ConcurrentRotatingFileHandler

logger = logging.getLogger()


class LogInfo:
    if not logger.handlers:
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_file = path + '/logs/log.log'
        err_file = path + '/logs/err.log'

        # 等级
        # logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.INFO)
        # urllibLogger.setLevel(logging.WARNING)
        # seleniumLogger.setLevel(logging.WARNING)

        # 格式
        # formatter = '%(message)s - %(pathname)s[line:%(lineno)d]'
        formatter = '%(message)s'

        # # 两个handler用于写入不同文件
        # info_handler = logging.FileHandler(log_file, encoding='utf-8')
        # err_handler = logging.FileHandler(err_file, encoding='utf-8')
        # info_handler.setFormatter(logging.Formatter(formatter))
        # err_handler.setFormatter(logging.Formatter(formatter))
        info_handler = ConcurrentRotatingFileHandler(log_file, encoding='utf-8')
        err_handler = ConcurrentRotatingFileHandler(err_file, encoding='utf-8')
        err_handler.setFormatter(logging.Formatter(formatter))
        info_handler.setFormatter(logging.Formatter(formatter))

    @staticmethod
    def message(message):
        logger.addHandler(LogInfo.info_handler)
        # logger.info(message)
        logger.info("[INFO " + get_current_time() + "]"
                    + '[' + sys._getframe().f_back.f_code.co_filename + '::'  # filename
                    + sys._getframe().f_back.f_code.co_name + '()'  # func
                    + ':' + str(sys._getframe().f_back.f_lineno) + '] '  # line
                    + message)
        logger.removeHandler(LogInfo.info_handler)
        print("[INFO][" + get_current_time() + "] " + message)

    @staticmethod
    def info(message):
        logger.addHandler(LogInfo.info_handler)
        # logger.info("[INFO " + get_current_time() + "]" + message) #, stack_info=True
        logger.info("[INFO " + get_current_time() + "]"
                    + '[' + sys._getframe().f_back.f_code.co_filename + '::'  # filename
                    + sys._getframe().f_back.f_code.co_name + '()'  # func
                    + ':' + str(sys._getframe().f_back.f_lineno) + '] '  # line
                    + message)
        logger.removeHandler(LogInfo.info_handler)
        print("[INFO][" + get_current_time() + "] " + message)

    @staticmethod
    def error(message):
        logger.addHandler(LogInfo.err_handler)
        logger.addHandler(LogInfo.info_handler)
        # logger.error("[ERROR " + get_current_time() + "]") #, stack_info=True
        logger.error("[ERROR " + get_current_time() + "]"
                     + '[' + sys._getframe().f_back.f_code.co_filename + '::'  # filename
                     + sys._getframe().f_back.f_code.co_name + '()'  # func
                     + ':' + str(sys._getframe().f_back.f_lineno) + '] '  # line
                     + message)
        logger.removeHandler(LogInfo.err_handler)
        logger.removeHandler(LogInfo.info_handler)
        print("[ERROR][" + get_current_time() + "] " + message)

    @staticmethod
    def debug(message):
        logger.addHandler(LogInfo.info_handler)
        logger.debug("[DEBUG " + get_current_time() + "]"
                     + '[' + sys._getframe().f_back.f_code.co_filename + '::'  # filename
                     + sys._getframe().f_back.f_code.co_name + '()'  # func
                     + ':' + str(sys._getframe().f_back.f_lineno) + '] '  # line
                     + message)
        print("[DEBUG][" + get_current_time() + "] " + message)
        logger.removeHandler(LogInfo.info_handler)

    @staticmethod
    def warning(message):
        logger.addHandler(LogInfo.info_handler)
        logger.warning("[WARNING " + get_current_time() + "]"
                       + '[' + sys._getframe().f_back.f_code.co_filename + '::'  # filename
                       + sys._getframe().f_back.f_code.co_name + '()'  # func
                       + ':' + str(sys._getframe().f_back.f_lineno) + '] '  # line
                       + message)
        print("[WARNING][" + get_current_time() + "] " + message)
        logger.removeHandler(LogInfo.info_handler)

    @staticmethod
    def critical(message):
        logger.addHandler(LogInfo.info_handler)
        logger.addHandler(LogInfo.err_handler)
        logger.critical("[CRITICAL " + get_current_time() + "]"
                        + '[' + sys._getframe().f_back.f_code.co_filename + '::'  # filename
                        + sys._getframe().f_back.f_code.co_name + '()'  # func
                        + ':' + str(sys._getframe().f_back.f_lineno) + '] '  # line
                        + message)
        logger.removeHandler(LogInfo.info_handler)
        logger.removeHandler(LogInfo.err_handler)
        print("[CRITICAL][" + get_current_time() + "] " + message)


def get_current_time():
    date_format = '%Y-%m-%d %H:%M:%S'
    return time.strftime(date_format, time.localtime(time.time()))


if __name__ == '__main__':
    print(LogInfo.info_handler)
