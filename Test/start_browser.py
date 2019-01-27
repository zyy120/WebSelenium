# coding=utf8
# import pytesseract
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from common.Config import *
from common.CommonUtil import *
from common.ShowapiRequest import ShowapiRequest
from common.RegisterApi import *

driver_init()
print(EC.title_contains("注册"))

"""
locator = (By.CLASS_NAME, "register_email")
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))  # 判断原数是否可见
b=isElementExist(driver,"register_email")
print(b)
"""
param["mail"] = get_range_user() + "@126.com"

gete_element("register_email").send_keys(param["mail"])
gete_element("register_nickname").send_keys(param["name"])
gete_element("register_password").send_keys(param["password"])

print(gete_element("register_nickname").get_attribute("value"))  # 获取对象内容值

# 验证码处理
driver.save_screenshot("E:/imooc.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
hight = code_element.size['height'] + top
im = Image.open("E:/imooc.png")
img = im.crop((left, top, right, hight))
img.save("E:/imooc_y.png")

# 验证码图片识别
# 基本验证码可以识别，但干扰线无法识别需要引入sdk
# image = Image.open("E:/imooc_y.png")
# text = pytesseract.image_to_string(image)


r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", "E:/imooc_y.png")  # 文件上传时设置
res = r.post()
print(res)
result_y = res.json()["showapi_res_body"]["Result"]
print(result_y)  # 返回信息
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys(result_y)
#driver.find_element_by_id("register-btn").click()

# time.sleep(10)
# driver.close()
