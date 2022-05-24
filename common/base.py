# -*- encoding: utf-8 -*-
# @Time  : 2022/4/28 15:30
# @Author: loading_f
# @File  : base.py

import json
import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from utils.log import LogInfo
from configure.config import Config
from utils.assertion import Assertion
from common.driver_init import driver_init


class PageBase:
    input_username = ('xpath', '/Html/body/div[2]/form/ul/li[1]/label/input')  # 账号输入path
    input_password = ('xpath', '/Html/body/div[2]/form/ul/li[2]/label/input')  # 密码输入path
    click_login = ('xpath', '/Html/body/div[2]/form/ul/li[4]/button')  # 确认按钮path

    log = LogInfo()
    Assert = Assertion()
    config = Config()

    def __init__(self, driver):
        # self.driver = driver
        self.driver = driver[0]
        self.chrome_service = driver[1]

    def set_browser_size(self):
        """
        默认全屏
        """
        try:
            self.driver.maximize_window()
        except Exception as e:
            self.log.error(str(e))

    def go_back(self):
        """
        回退
        """
        self.driver.back()

    # def open_url(self):
    #     # print("*******driver type:*******", type(self.driver))
    #     # print("driver of values:", self.driver)
    #     self.driver.get("https://www.baidu.com")

    def select_all(self, locator):
        """
        全选
        """
        try:
            ele = self.find_element(locator)
            if ele:
                ele.send_keys(Keys.CONTROL, 'a')
        except Exception as e:
            self.log.error(str(e))

    def copy(self, locator):
        """
        复制
        """
        try:
            ele = self.find_element(locator)
            if ele:
                ele.send_keys(Keys.CONTROL, 'c')
        except Exception as e:
            self.log.error(str(e))

    def get_current_window_url(self):
        url_result = self.driver.current_url
        self.log.info(f'获取到的url：{url_result}')
        return url_result

    def hover(self, locator):
        """
        元素hover事件
        :param locator:
        :return:
        """
        try:
            ele = self.find_element(locator)
            if ele:
                ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as err:
            self.log.error(str(err))

    def paste(self, locator):
        """
        粘贴
        """
        try:
            ele = self.find_element(locator)
            if ele:
                ele.send_keys(Keys.CONTROL, 'v')
        except Exception as e:
            self.log.error(str(e))

    def press_enter(self, locator, timeout=5):
        """
        模拟键盘回车键操作
        """
        try:
            ele = self.find_element(locator, timeout)
            if ele:
                ele.send_keys(Keys.ENTER)
        except Exception as e:
            self.log.error(str(e))

    def back_space(self, locator):
        """
        模拟键盘的删除键
        """
        try:
            ele = self.find_element(locator)
            if ele:
                ele.send_keys(Keys.BACK_SPACE)
        except Exception as e:
            self.log.error(str(e))

    def press_right(self, locator):
        """
        模拟键盘回车键操作
        """
        try:
            ele = self.find_element(locator)
            if ele:
                ele.send_keys(Keys.RIGHT)
        except Exception as e:
            self.log.error(str(e))

    def scrollIntoView(self, la: tuple):
        """
        滑动界面
        """
        try:
            ele = self.find_element(la)
            if ele:
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        except Exception as e:
            self.log.error(str(e))

    def send_script(self, js: str):
        """
        录入js
        """
        try:
            self.driver.execute_script(js)
        except Exception as e:
            self.log.error(e)

    def send_script_new(self, js: str, element):
        """
        录入js(重载)
        """
        try:
            self.driver.execute_script(js, element)
        except Exception as e:
            self.log.error(e)

    def quit_Browser(self):
        """
        退出Browser
        """
        try:
            self.driver.quit()
            self.chrome_service.stop()
        except Exception as e:
            self.log.error(str(e))

    def ActionChainsClick(self, locator: tuple):
        """
        模擬鼠标点击
        """
        try:
            element = self.find_element(locator)
            if element:
                ActionChains(self.driver).move_to_element(element).click().perform()
        except Exception as e:
            self.log.error(str(e))

    def ActionChainsSend_Keys(self, locator: tuple, key: str):
        """
        模拟鼠标录入
        """

        try:
            element = self.find_element(locator)
            if element:
                ActionChains(self.driver).move_to_element(element).click().send_keys(key).perform()
        except Exception as e:
            self.log.error(str(e))

    def ActionChainsOffsetClick(self, x, y, element=None):
        """
        坐标点击
        """
        try:
            if element:
                ActionChains(self.driver).move_to_element_with_offset(element, 0, 0).click().perform()
                time.sleep(1)
            ActionChains(self.driver).move_by_offset(x, y).click().perform()
        except Exception as e:
            self.log.error(str(e))
            self.log.error("坐标错误")

    def Js_clear(self, locator):
        """
        js clear input
        """
        try:
            self.click(locator)
            js = f'document.querySelector("#{locator[1]}").value="";'
            self.driver.execute_script(js)
        except Exception as e:
            self.log.error(e)

    def get_url(self, url):
        """
        go url
        """
        try:
            self.driver.get(url)
            print(f"get{url}")
        except Exception as e:
            self.log.error(str(e))

    def find_elements(self, locator: tuple, timeout=10):
        """
        定位一組元素,
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return element
        except Exception as e:
            self.log.error("未找到: {}".format(locator[1]))
            self.log.error(str(e))

    def find_element(self, locator: tuple, timeout=5):
        """
        定位元素,
        """
        try:
            time.sleep(1)
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except Exception as e:
            self.log.error("未找到: {}".format(locator[1]))
            allure.attach(self.get_png(), "errPNG", allure.attachment_type.PNG)
            allure.attach("未找到: {}".format(locator[1]), "errMsg")
            raise e

    def not_find_element(self, locator: tuple, timeout=5):
        """
        定位元素不存在时返回,
        """
        try:
            element = WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
            return element
        except Exception as e:
            self.log.error("元素一直存在: {}".format(locator[1]))
            allure.attach(self.get_png(), "errPNG", allure.attachment_type.PNG)
            allure.attach("元素一直存在: {}".format(locator[1]), "errMsg")
            raise e

    def click(self, locator: tuple, t=None, timeout=5):
        element = self.find_element(locator, timeout)
        try:
            if element:
                if t:
                    time.sleep(t)
                element.click()
        except Exception as e:
            self.log.error(str(e))
            self.log.error(f"{locator} 点击失败")
            self.log.error("未找到元素: {}".format(locator[1]))
            allure.attach(self.get_png(), "errPNG", allure.attachment_type.PNG)
            raise e

    def double_click(self, locator: tuple):
        element = self.find_element(locator)
        try:
            if element:
                action = ActionChains(self.driver)
                action.double_click(element).perform()
        except Exception as e:
            self.log.error(str(e))
            self.log.error("未找到: {}".format(locator[1]))
            allure.attach(self.get_png(), "errPNG", allure.attachment_type.PNG)
            raise e

    def refresh(self):
        """
        刷新
        """
        self.driver.refresh()

    def clear(self, locator: tuple):
        """
        清空
        """
        try:
            ele = self.find_element(locator)
            ele.send_keys(Keys.CONTROL, "a")
            ele.send_keys(Keys.DELETE)
        except TimeoutException:
            self.log.error("clear失敗 {}".format(str(locator)))
            return False

    def get_text(self, locator: tuple, timeout=5):
        """
        获取文本
        """
        try:
            time.sleep(1)
            ele = self.find_element(locator, timeout)
            return ele.text
        except TimeoutException:
            self.log.error('元素 {element} 没有找到'.format(element=locator))

    def get_attribute(self, locator: tuple, name: str):
        """
        获取属性
        """
        element = self.find_element(locator)
        try:
            if element:
                return element.get_attribute(name)
        except Exception as err:
            self.log.error(err)

    def send_keys(self, locator: tuple, text: str):
        """
        传参
        """
        element = self.find_element(locator)
        if element:
            try:
                element.clear()
                element.send_keys(text)
            except WebDriverException as e:
                self.log.error(str(e))
                self.log.error('元素  {element}不可编辑'.format(element=locator))

    def switch_to_window(self, new_window=None):
        """
        切换新窗口
        :param new_window: 新窗口句柄
        :return: 当前窗口句柄
        """
        if new_window is None:
            current_handle = self.driver.window_handles
            try:
                self.driver.switch_to.window(current_handle[-1])
                return current_handle
            except TimeoutException as e:
                self.log.error("切换窗口失败或无新窗口被打开, 无需切换窗口")
                raise e
        else:
            self.driver.switch_to.window(new_window)

    def get_png(self):
        """
        获取当前窗口的屏幕截图作为二进制数据
        """
        pic = self.driver.get_screenshot_as_png()
        time.sleep(1)
        return pic

    def perform_svg(self, xpath):
        """
        操作svg元素
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
        except Exception as e:
            raise Exception(print(e))

    def judge_if_enable(self, xpath):
        """
        判断元素是否可用
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if element.is_enabled():
                return True
            else:
                return False
        except Exception as e:
            raise Exception(print(e))

    def get_alert_msg(self, timeout=5):
        """
        获得弹窗信息
        """
        return self.get_text(('xpath', "//div[@class='ant-message']//span[2]"), timeout)

    def allure_report(self, func, case_name=None, pic_list=None, expect=None, res=None):
        """
        allure 报告生成
        @func :测试用例函数
        @case_name : 测试用例名称
        @pic_list : 截图
        @expect : 预期结果
        @res : 实际结果
        """
        if case_name:
            allure.dynamic.title(case_name)
        allure.attach(json.dumps(func.__name__, ensure_ascii=False), 'case_name',
                      allure.attachment_type.JSON)
        allure.attach(func.__doc__.strip(), 'step',
                      allure.attachment_type.JSON)
        n = 0
        if pic_list is not None:
            for i in pic_list:
                n += 1
                allure.attach(i, name='screenshot => step{}'.format(n), attachment_type=allure.attachment_type.PNG)

        if expect and res:
            allure.attach(json.dumps(expect, ensure_ascii=False), 'expected_result', allure.attachment_type.JSON)
            allure.attach(json.dumps(res, ensure_ascii=False), 'actual_result', allure.attachment_type.JSON)
        self.log.info(f"===============  {func.__name__} 测试完成  ===============")

    def mouse_to(self):
        """
        鼠标位置归0
        """
        ele = self.find_element(('xpath', "//Html"))
        self.ActionChainsOffsetClick(element=ele, x=0, y=0)
        self.log.debug("鼠标归0")
        return ele

    @staticmethod
    def print_pngs(pics=None, pic=None):
        """
        打印截图
        """
        n = 0
        if pics is not None:
            for i in pics:
                n += 1
                allure.attach(i, name=f'step{n}', attachment_type=allure.attachment_type.PNG)
        if pic is not None:
            allure.attach(pic, name='测试正确截图', attachment_type=allure.attachment_type.PNG)

    def login(self, user=None, passw=None, url=None):
        """
        用户登录
        :param user:
        :param url:
        :param passw:
        :return:
        """
        # 获取登录相关数据
        exec_url = self.config.domain
        username = self.config.username
        password = self.config.password
        # case_path = self.config.case_path

        # 未传url参数则打开配置的url
        if url is None:
            self.driver.get(exec_url)
            # self.getUrl(exec_url)
        else:
            self.driver.get(url)
            # self.getUrl(url)

        time.sleep(2)

        if user is None:
            self.send_keys(self.input_username, username)  # 输入账号
            self.send_keys(self.input_password, password)  # 输入密码
        else:
            self.send_keys(self.input_usercode, user)  # 输入自定义账号和密码
            self.send_keys(self.input_password, passw)
        self.click(self.click_login)  # 点击登录


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    page = PageBase(driver_init())


