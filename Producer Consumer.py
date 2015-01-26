from threading import Thread
from threading import Lock
from threading import Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM: 
                print 'Queue is full, Producer is waiting'
                condition.wait() # wait for consumer to consume
                print 'Queue is not full, Consumer notified Producer'
            num = random.choice(nums)
            queue.append(num)
            print 'Produced', num
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue: 
                print 'Queue is empty, Consumer is waiting'
                condition.wait() # wait for producer to produce
                print 'Queue is not empty, Producer notified Consumer'
            num = queue.pop(0)
            print 'Consumed', num
            condition.notify()
            condition.release()
            time.sleep(random.random())

consumer = ConsumerThread()
producer = ProducerThread()
consumer.start()
producer.start()
