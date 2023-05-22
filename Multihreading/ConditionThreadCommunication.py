"""

Condition THread communication--->

condition class is used to improve speed of communication between thread
The condition class onject is called condition variable
A condition variable is always associated with some kind of lock
THe lock is part of the condition object you dont have it track it separately

Condition is more advance version of the event object


from threading import Condition


cv=Condition
cv.notify(n=1)-- n--> number of thread need to wakup
cv.notify_all()--> this method is used to wakeup all threads waiting on the condition
cv.wait(timeout=None)-- this method wait untill notify or untill timout occur
                        if the calling threads has not acquired the lock
                         when this method is called RunTime Error
                        wait invoked notify() method or notify_all() 
                        the return value True unless a given timeout expired,
                         in whhich case it is false

            
"""

from threading import Thread,Condition
from time import sleep
list1=[]
def producer(cv):
    cv.acquire()
    print("Producer producing items")
    for i in range(1,6):
        sleep(2)
        list1.append(i)
        print("Item Produce")
        # cv.notify_all()
        # cv.release()
       
    cv.notify_all()
    cv.release()
def consumer(cv):
    cv.acquire()
    cv.wait(timeout=0)
    print("consumer consume items list",list1)
    cv.release()
cv=Condition()
producer_thread=Thread(target=producer,args=(cv,))
consumer_thread=Thread(target=consumer,args=(cv,))
producer_thread.start()
consumer_thread.start()


