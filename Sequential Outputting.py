from threading import Condition
from threading import Thread

cv = Condition()
isOdd = True

def odd():
    global isOdd
    for i in range(1,21,2):
        cv.acquire()
        if not isOdd: cv.wait()
        print i,
        isOdd = not isOdd
        cv.notify()
        cv.release()

def even():
    global isOdd
    for i in range(2,21,2):
        cv.acquire()
        if isOdd: cv.wait()
        print i,
        isOdd = not isOdd
        cv.notify()
        cv.release()

t = Thread(target=odd)
d = Thread(target=even)
t.start()
d.start()
