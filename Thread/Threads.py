# coding:utf-8
__author__ = 'lenovo'

from time import sleep,ctime
import threading

def music(func,loop):
    for i in range(loop):
        print('I was listening to %s!%s' %(func,ctime()))
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print('I was at the %s!%s' %(func,ctime()))
        sleep(5)

threads = []

t1 = threading.Thread(target= music,args=('爱情买卖',2))
threads.append(t1)

t2 = threading.Thread(target=movie,args=('阿凡达',2))

threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for ti in threads:
        t.join()

    print('all ends:%s'%ctime())