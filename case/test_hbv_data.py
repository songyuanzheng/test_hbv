import os
import random
import time
import sys
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class TEST_HBV(unittest.TestCase):
    def setUp(self):      #初始设置打开浏览器
        self.dr=webdriver.Firefox()
        url="https://www.celloud.cc/console/login.html"
        self.dr.maximize_window()
        self.dr.get(url)
        self.dr.implicitly_wait(20)
        self.dr.find_element_by_css_selector("#username").send_keys("lihh")
        self.dr.find_element_by_css_selector("#password").send_keys("celloud")
        self.dr.find_element_by_xpath(".//*[@id='loginForm']/div/a").click()
    def test_hbv_data(self):
        dr = self.dr
        dr.implicitly_wait(30)
        dr.find_element_by_xpath(".//*[@id='showMain']/div/div[1]/div/div[2]/ul/li[6]/button").click()
        dr.find_element_by_xpath(".//*[@id='menu']/li[6]/a").click()
        #验证搜索框功能
        dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("test")
        dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[1]/div/div[2]/a").click()
        sleep(3)
        try:
            text=self.dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[8]/td[5]").text
            self.assertIn("test",text)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            # 图片名称加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
        sleep(2)
        #选择单个文件归档
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[7]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[1]/div/div[1]/button[2]").click()
        dr.find_element_by_id("confirm-ok").click()
        try:
            text = self.dr.find_element_by_css_selector(".alert").text
            self.assertEqual("", text)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            # 图片名称加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
        sleep(3)
        #选择多个文件同时归档
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[1]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[2]/td[1]/label/span").click()
        # dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[3]/td[1]/label/span").click()
        # dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[4]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[1]/div/div[1]/button[2]").click()
        dr.find_element_by_id("confirm-ok").click()
        try:
            text = self.dr.find_element_by_css_selector(".alert").text
            self.assertEqual("", text)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            # 图片名称加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
        sleep(2)
        #运行多个文档
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[1]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[2]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[3]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[4]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[1]/div/div[1]/button[1]").click()
        sleep(2)
        #运行单个文档
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[6]/td[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[1]/div/div[1]/button[1]").click()
        sleep(3)
        #选择全选
        dr.find_element_by_xpath(".//*[@id='_data_table']/thead/tr/th[1]/label/span").click()
        dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[1]/div/div[1]/button[1]").click()
        #页面滚动条
        js1 = 'document.getElementById("showMain").scrollTop=10000'
        dr.execute_script(js1)
        time.sleep(5)
        #数字跳转按钮
        dr.find_element_by_xpath(".//*[@id='pagination-ul']/li[4]/a").click()
        sleep(1)
        try:
            text=self.dr.find_element_by_xpath(".//*[@id='pagination-ul']/li[3]/a").text
            self.assertIn("…",text)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
        #每页显示文件条数
        select = Select(dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[4]/ul[2]/li[2]/select"))
        select.select_by_index(4)
        sleep(3)
        try:
            text=self.dr.find_element_by_xpath(".//*[@id='showMain']/div[1]/div[1]/div[4]/ul[2]/li[2]/select").text
            self.assertEqual("10\n20\n30\n50\n100",text)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
        #滚动条由上到下执行一次
        js1 = 'document.getElementById("showMain").scrollTop=10000'
        dr.execute_script(js1)
        time.sleep(3)
        js1 = 'document.getElementById("showMain").scrollTop=0'
        dr.execute_script(js1)
        time.sleep(5)
        #编辑功能
        dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[1]/td[9]/a/i").click()
        dr.implicitly_wait(10)
        dr.find_element_by_css_selector(".ng-pristine.ng-untouched.ng-valid.ng-empty.ng-valid-maxlength").clear()
        sleep(2)
        dr.find_element_by_css_selector(".ng-pristine.ng-untouched.ng-valid.ng-empty.ng-valid-maxlength").send_keys("test123456")
        # select = Select(dr.find_element_by_xpath(".//*[@id='editDataForm']/div[3]/div[2]/select"))
        # select.select_by_index(4)
        # sleep(1)
        dr.find_element_by_xpath(".//*[@id='editDataForm']/div[4]/div[2]/input").clear()
        dr.find_element_by_xpath(".//*[@id='editDataForm']/div[4]/div[2]/input").send_keys("test666666")
        dr.find_element_by_xpath(".//*[@id='data-detail-modal']/div/div/div[3]/div/button[2]").click()
        sleep(5)
        try:
            text=self.dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[1]/td[3]").text
            self.assertIn("test",text)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise



    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()