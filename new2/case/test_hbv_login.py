import os
import random
import time
import sys
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
class TEST_HBV(unittest.TestCase):
    def setUp(self):      #初始设置打开浏览器
        self.dr=webdriver.Firefox()

        url="https://www.celloud.cc/console/login.html"
        self.dr.maximize_window()
        self.dr.get(url)
        self.dr.implicitly_wait(2)

    def test_hbv_login(self):
        dr = self.dr
        try:

            dr.find_element_by_css_selector("#username").send_keys("lihh")
            dr.find_element_by_css_selector("#password").send_keys("celloud")
            dr.find_element_by_xpath(".//*[@id='loginForm']/div/a").click()
            time.sleep(3)
            text=dr.find_element_by_css_selector(".type-head>h5").text
            self.assertEqual("我的产品",text)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            # 图片名称可以加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
        time.sleep(3)
    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()
