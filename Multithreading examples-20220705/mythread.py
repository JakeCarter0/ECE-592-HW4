import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def run(stop):
    while(True):
        logging.debug('running')
        time.sleep(0.25)
        global stop_threads
        if stop():
            break


stop_threads = False
t1 = threading.Thread(target=run, args=(lambda: stop_threads,))
t1.start()
time.sleep(1)
stop_threads = True
t1.join()
print('thread killed')
