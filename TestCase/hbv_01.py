import os
import random
import time
from distutils.command import upload

from appium.webdriver.webelement import WebElement
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

dr=webdriver.Firefox()
url="https://www.celloud.cc"
dr.maximize_window()
dr.implicitly_wait(30)
dr.get(url)
currentWin=dr.current_window_handle
dr.find_element_by_xpath('.//*[@id="nav-close"]/div/div/div/div[3]/a').click()
time.sleep(3)
handles = dr.window_handles
for i in handles:
    if currentWin == i:
        continue
    else:
        driver = dr.switch_to_window(i)
dr.find_element_by_id("username").send_keys("lihh")
dr.find_element_by_id("password").send_keys("celloud")
dr.find_element_by_xpath(".//*[@id='loginForm']/div/a").click()
time.sleep(3)
dr.find_element_by_xpath("/html/body/div[1]/ng-include[1]/header/nav/div/ul[1]/li[1]/a").click()
dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/ul/li[5]/button").click()
p = ["1","2","3","4","5","6","7","8","9"]
random.shuffle(p)
dr.find_element_by_id("batch-info-input").send_keys(p)
dr.find_element_by_id("upload-next").click()
dr.find_element(By.ID,"plupload-content").click()
os.system(r"C:\\Users\\Administrator\\Desktop\\upload.exe")
dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/div/div[3]/div[2]/div/a[1]").click()
dr.find_element(By.ID,"plupload-content").click()
os.system(r"C:\\Users\\Administrator\\Desktop\\upload1.exe")
time.sleep(5)
dr.find_element_by_xpath("/html/body/div[1]/ng-include[2]/aside/nav/ul/li[6]").click()
"""
sta = dr.find_elements_by_css_selector(".ng-binding.ng-scope").text
for i in sta:
    if i.text == "未运行":
       sel=dr.find_element_by_partial_link_text("未运行")
       sel.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[1]/label").click()
       dr.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[1]/button[1]").click()
"""
time.sleep(2)
dr.find_element_by_xpath(".//*[@id='_data_table']/tbody/tr[1]/td[1]/label/span").click()
dr.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[1]/button[1]").click()
dr.find_element_by_xpath(".//*[@id='menu']/li[7]").click()
dr.find_element_by_id("dataSpan3857018071708605494").click()
time.sleep(5)

dr.quit()
