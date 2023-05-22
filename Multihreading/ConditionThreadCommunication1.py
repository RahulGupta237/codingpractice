from threading import Thread,Condition
from time import sleep
import random

list1=[]
def producer(cv):
    while True:
        cv.acquire()
        item=random.randint(1,6)
       
        print("Producer producing items",item)
        list1.append(item)
        sleep(3)

        print("Giving Notification")
        
        cv.notify()
        cv.release()
        sleep(5)
def consumer(cv):
    while True:
        cv.acquire()
        print("Consumer waiting for updation")
        sleep(3)
        cv.wait(timeout=5)
        print("consumer consume items list",list1)
        cv.release()
        sleep(5)
cv=Condition()
consumer_thread=Thread(target=consumer,args=(cv,))
producer_thread=Thread(target=producer,args=(cv,))
producer_thread.start()
consumer_thread.start()

