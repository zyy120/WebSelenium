# coding=utf-8
# 用户注册
import time
import random
from selenium import webdriver
from PIL import Image
from common.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()


# 初始化
def driver_init():
    # 最大化窗口
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(1)


# 获取用户节点
def gete_element(id):
    element = driver.find_element_by_id(id)
    return element


# 获取用户信息
def get_range_user():
    user_info = ''.join(random.sample("0123456789abcdefg", 8))
    return user_info


# 获取图片
def get_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    hight = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, hight))
    img.save(file_name)


# 解析图片
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    print(res.text)
    result_y = res.json()["showapi_res_body"]["Result"]
    return result_y


def run_main():
    mailName = get_range_user()
    driver_init()
    gete_element("register_email").send_keys(mailName + "@126.com")
    gete_element("register_nickname").send_keys(mailName)
    gete_element("register_password").send_keys("123456")
    file_name = "E:/code/workspace-qs-py/WebSelenium/image/imooc.png"
    get_image(file_name)
    text = code_online(file_name)
    print("用户名： %s ,验证码：%s" % (mailName, text))
    gete_element("captcha_code").send_keys(text)
    gete_element("register-btn").click()
    time.sleep(5)
    driver.close()


run_main()
