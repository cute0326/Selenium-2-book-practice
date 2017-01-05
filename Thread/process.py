# *-* coding=utf-8 *-*
from time import sleep, ctime
import multiprocessing

def super_player(file,time):
	for i in range(5):
		print('start playing: %s!%s' %(file,ctime()))
		sleep(time)

# lists = {'aiqingmaimai.mp3':3,'afanda.mp4':5,'You and I.mp3':4}
lists = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}

threads = []

files = range(len(lists))

for file,time in lists.items():
	t = multiprocessing.Process(target=super_player,args=(file,time))
	threads.append(t)

if __name__ == '__main__':
	for t in files:
		threads[t].start()
	for t in files:
		threads[t].join()

	print('ends:%s' %ctime())