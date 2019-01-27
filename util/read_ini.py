# coding=utf-8
import configparser


class ReadIni(object):

    def __init__(self, file_name=None, node=None):
        if file_name == None:
            file_name = "E:\code\workspace-qs-py\WebSelenium\confing\LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_init(file_name)

    def load_init(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        self.cf.get(self.node, key)
        print(self.cf.get(self.node, key))


if __name__ == '__main__':
    read_init = ReadIni()
    read_init.get_value("user_email")
