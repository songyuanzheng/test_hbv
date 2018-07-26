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
    def test_report(self):
        dr=self.dr
        dr.find_element_by_xpath(".//*[@id='showMain']/div/div[1]/div/div[2]/ul/li[6]/button").click()
        dr.find_element_by_xpath(".//*[@id='menu']/li[7]/a").click()
        dr.find_element_by_xpath(".//*[@id='dataSpan3875318032208333357']").click()
        sleep(5)
        js1 = 'document.getElementById("showMain").scrollTop=10000'
        dr.execute_script(js1)
        time.sleep(3)
        js1 = 'document.getElementById("showMain").scrollTop=0'
        dr.execute_script(js1)
    def tearDown(self):
        self.dr.quit()



if __name__ == '__main__':
    unittest.main()

