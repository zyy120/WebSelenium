# coding=utf-8
# import sys
# sys.path.append("")
# 完整版
# webdriver代码封装添加ini配置文件读取element节点，注册后错截图保存

import time
import random
from selenium import webdriver
from PIL import Image
from common.ShowapiRequest import ShowapiRequest
from common.find_element import FindElement


class RegisterFunction(object):
    def __init__(self, url):
        self.driver = self.get_driver(url)

    # 获取driver 并打开url
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取用户信息
    def get_range_user(self):
        user_info = ''.join(random.sample("0123456789abcdefg", 8))
        return user_info

    # 获取图片
    def get_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        hight = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, hight))
        img.save(file_name)

    # 解析图片
    def code_online(self, file_name):
        r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        print(res.text)
        result_y = res.json()["showapi_res_body"]["Result"]
        return result_y

    def mian(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@126.com"
        file_name = "E:/code/workspace-qs-py/WebSelenium/image/imooc.png"
        self.get_image(file_name)
        code_text = self.code_online(file_name)
        self.send_user_info("user_email", user_email)
        self.send_user_info("user_name", user_name_info)
        self.send_user_info("passwed", "123456")
        self.send_user_info("code_text", code_text)
        print(code_text)
        time.sleep(2)
        self.get_user_element("register_button").click()
        code_error = self.get_user_element("code_text_error")

        if code_error is None:
            print("用户注册成功")
        else:
            self.driver.save_screenshot("E:/code/workspace-qs-py/WebSelenium/image/error.png")
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    register_function = RegisterFunction("http://www.5itest.cn/register")
    register_function.mian()
