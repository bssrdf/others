from threading import Thread
from threading import Lock
from threading import Condition
import time
import random

nH, nO, nH2O = 0, 0, 0
lock = Lock()
cvH, cvO = Condition(), Condition()

class H(Thread):
    def run(self):
        self.H()

    def H(self):
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
        print 'H returning'

class O(Thread):
    def run(self):
        self.O()

    def O(self):
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
            cvH.notify()
            cvH.notify()
            cvH.release()
        else:
            lock.release()
            cvO.acquire()
            cvO.wait()
            cvO.release()
        print 'O returning'

h = H()
o = O()
h.start()
o.start()