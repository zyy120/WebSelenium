# coding=utf-8
from util.read_ini import ReadIni
from selenium import webdriver
import time


class FindElement(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni();
        data = read_ini.get_value(key)

        if data is None:
            print("key 值为 None %s", key)
            return None

        by = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
        except:
            return None


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    Find_Element = FindElement(driver)
    element = Find_Element.get_element("user_email")
    print(element)
    time.sleep(5)
    driver.close()
