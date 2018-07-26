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
    def setUp(self):     #初始设置打开浏览器
        self.dr=webdriver.Firefox()
        url="https://www.celloud.cc/console/login.html"
        self.dr.maximize_window()
        self.dr.get(url)
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_css_selector("#username").send_keys("lihh")
        self.dr.find_element_by_css_selector("#password").send_keys("celloud")
        self.dr.find_element_by_xpath(".//*[@id='loginForm']/div/a").click()
    def test_hbv_uploadingdata(self):
        dr = self.dr
        dr.implicitly_wait(30)
        dr.find_element_by_xpath(".//*[@id='showMain']/div/div[1]/div/div[2]/ul/li[6]/button").click()
        dr.find_element_by_xpath(".//*[@id='menu']/li[5]/a").click()  #点击上传数据
        dr.find_element_by_xpath(".//*[@id='batch-info-input']").click()
        p = ["hbv","2","3","4","5","6","7"]        #随机输入数据标签
        random.shuffle(p)
        dr.find_element_by_id("batch-info-input").send_keys(p)
        dr.find_element_by_id("upload-next").click()
        dr.find_element(By.ID,"plupload-content").click()
        os.system(r"C:\\Users\\Administrator\\Desktop\\upload.exe")  #上传本地数据
        dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/div/div[3]/div[2]/div/a[1]").click()
        dr.find_element(By.ID,"plupload-content").click()
        os.system(r"C:\\Users\\Administrator\\Desktop\\upload1.exe")
        time.sleep(3)
        dr.find_element_by_xpath(".//*[@id='menu']/li[6]/a/span").click()
        try:
            text=self.dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[2]/td[2]").text
            self.assertEqual("23YMDD_G12_21.ab1",text)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            # 图片名称加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
        sleep(1)
        try:
            text=self.dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[1]/td[5]").text
            self.assertIn("hbv",text)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            # 图片名称加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.dr.get_screenshot_as_file('./Image/%s.jpg' % nowTime)
            raise
    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()