#coding:utf-8
__author__ = 'lenovo'

import threading
from time import sleep,ctime

class MyThread(threading.Thread):

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args


    def run(self):
        self.func(*self.args)


def super_player(file,time):
    for i in range(2):
        print('starting playing: %s!%s' %(file,ctime()))
        sleep(time)

lists = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}

threads = []
files = range(len(lists))

for file,time in lists.items():
    t = MyThread(super_player,(file,time))
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print('%s' %(super_player.__name__))
    print('ends: %s' %ctime())
