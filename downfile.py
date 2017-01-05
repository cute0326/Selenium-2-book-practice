__author__ = 'lenovo'

from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()

fp.set_preference('broswer.download.folderList',2)

fp.set_preference('broswer.download.manger.ShowWhenStarting',False)

fp.set_preference('broswer.download.dir',os.getcwd())

fp.set_preference('browser.helperApps.neverAsk.saveToDisk','application/octet-stream')

driver = webdriver.Firefox(firefox_profile = fp)

driver.get('https://pypi.Python.org/pypi/selenium')

driver.find_element_by_partial_link_text('selenium-3').click()

