# coding:utf-8
__author__ = 'lenovo'

from time import sleep,ctime

def music(func,loop):
    for i in range(loop):
        print('I was listening to %s ! %s' %(func,ctime()))
        sleep(2)
def movie(func,loop):
    for i in range(loop):
        print('I was at the %s ! %s' %(func,ctime()))
        sleep(5)

if __name__ == '__main__':
    music('爱情买卖',2)
    movie('阿凡达',2)
    print('all ends:',ctime())

