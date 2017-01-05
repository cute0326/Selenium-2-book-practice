__author__ = 'lenovo'

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://videojs.com/')

# video = driver.find_element_by_xpath('/html/body/section[1]/div[1]/video')
video = driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')

url = driver.execute_script('return arguments[0].currentSrc;',video)

print(url)

print('start for 15s')
driver.execute_script('return arguments[0].play()',video)

sleep(15)

print('pause for 5s')
driver.execute_script('return arguments[0].pause()',video)
sleep(5)

print('start for 5s')
driver.execute_script('return arguments[0].play()',video)
sleep(5)

print('pause for 5s')
driver.execute_script('return arguments[0].pause()',video)

sleep(5)

print('quit')

driver.quit()