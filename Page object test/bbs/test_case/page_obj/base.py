# coding:utf-8
__author__ = 'lenovo'

class Page(object):
    '''页面基础类，用于所有页面的继承'''

    base_url = 'https://mail.qq.com'
    special_url = '/'

    def __init__(self, selenium_driver,base_url = base_url,parent = None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def open(self):
        url = self.base_url + self.special_url
        self.driver.get(url)
        assert self.on_page(),'did not on the page'

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elments(self,*loc):
        return self.dirver.find_elements(*loc)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.special_url)

    def script(self,src):
        return self.driver.execute_script(src)


