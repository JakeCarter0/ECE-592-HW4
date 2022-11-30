import threading
import time
import logging

def tfun(j):
    """thread worker function"""
    print ('Function started:', threading.currentThread().getName())
    time.sleep(2)
    print ('Function exiting:', threading.currentThread().getName())
    return

def tfun2(j):
    """thread worker function"""
    print ('Function started:', threading.currentThread().getName())
    print ('Function:', j)
    time.sleep(3)
    print ('Function started:', threading.currentThread().getName())
    return

#threads = []

#for i in range(5):
t2 = threading.Thread(name='daemon', target=tfun, args=(0, ))
t2.setDaemon(True)
t23 = threading.Thread(name='non-daemon', target=tfun, args=(0, ))
#threads.append(t)
t23.start()
t2.start()

t23.join()
t2.join()
#print(threads)