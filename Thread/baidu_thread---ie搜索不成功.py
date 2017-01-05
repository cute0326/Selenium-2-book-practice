from threading import Thread
from selenium import webdriver
from time import ctime,sleep

def test_baidu(browser,text):
    print('start : %s' %ctime())
    print('browser: %s' %browser)

    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'ff':
        driver = webdriver.Firefox()
    else:
        print('browser参数有误，只能为id,chrome,ff')

    driver.get('https://www.baidu.com')
    driver.implicitly_wait(10)
    driver.find_element_by_id('kw').send_keys(text)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()

if __name__ == '__main__':
    # lists = {'chrome':'threading','ie':'webdriver','ff':'python'}
    lists = {'ff':'webdriver'}
    threads = []
    files = range(len(lists))

    for browser,text in lists.items():
        t = Thread(target=test_baidu, args=(browser,text))
        threads.append(t)

    for t in files:
        threads[t].start()

    for t in files:
        threads[t].join()

    print('end:%s' %ctime())