from threading import *
from time import sleep
def producer():
    sleep(5)
    print("Producer thread producing items:")
    print("Producer thread giving notification bet setting event")
    Event.set()
def consumer():
    print("Consumer thread is waiting for updation")
    Event.wait()
    print("Consumer thread got notification and consuming items")
Event=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()