# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('https://login.taobao.com/member/login.jhtml')
driver.find_element_by_id("J_Quick2Static").click()
driver.find_element_by_id("TPL_username_1").send_keys("13687097822")
time.sleep(1)
driver.find_element_by_id("TPL_password_1").send_keys("love33261456789")

source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
# 定义鼠标拖放动作
ActionChains(driver).drag_and_drop_by_offset(source, 400, 0).perform()
# 等待JS认证运行,如果不等待容易报错
time.sleep(2)
# 查看是否认证成功，获取text值
text = driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
# 目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
time.sleep(1)
driver.find_element_by_id("J_SubmitStatic").click()

time.sleep(1)
error_text = driver.find_element_by_class_name('error').text
print(error_text)
# driver.close()
