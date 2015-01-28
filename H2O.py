# http://www.fgdsb.com/2015/01/03/h2o-problem/
# linkedin
# concurrency

from threading import Thread
from threading import Lock
from threading import Condition
import time
import random

nH, nO, nH2O = 0, 0, 0
lock = Lock()
cvH, cvO = Condition(), Condition()

def H():
    global nH, nO, nH2O, lock, cvH, cvO

    lock.acquire()
    nH += 1
    if nH >= 2 and nO >= 1:
        nH -= 2
        nO -= 1
        nH2O += 1
        print 'generating H2O molecule NO.%d' % nH2O
        lock.release()
        cvH.acquire()
        cvH.notify()
        cvH.release()
        cvO.acquire()
        cvO.notify()
        cvO.release()
    else:
        lock.release()
        cvH.acquire()
        cvH.wait()
        cvH.release()

def O():
    global nH, nO, nH2O, lock, cvH, cvO

    lock.acquire()
    nO += 1
    if nH >= 2 and nO >= 1:
        nH -= 2
        nO -= 1
        nH2O += 1
        print 'generating H2O molecule NO.%d' % nH2O
        lock.release()
        cvH.acquire()
        cvH.notify_all()
        cvH.release()
    else:
        lock.release()
        cvO.acquire()
        cvO.wait()
        cvO.release()

h1 = Thread(target=H)
h2 = Thread(target=H)
o = Thread(target=O)
h1.start()
h2.start()
o.start()