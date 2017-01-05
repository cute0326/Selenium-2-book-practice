import multiprocessing
import queue
import os, time

def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put_nowait(info)

def outputQ(queue,lock):
    info = queue.get_nowait()
    lock.acquire()
    print((str(os.getpid())) + '(get):' + info)
    lock.release

if __name__  == '__main__':
    record1 = []
    record2 = []

    lock = multiprocessing.Lock()
    Myqueue = multiprocessing.Queue

    for i in range(10):
        process = multiprocessing.Process(target=inputQ,args=(Myqueue,))
        process.start()
        record1.append(process)

    for i in range(10):
        process = multiprocessing.Process(target=outputQ,args=(Myqueue,lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()

    for p in record2:
        p.join()

