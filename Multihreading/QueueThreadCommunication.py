"""

The Queue class of Queue module is usefull to create a queue 
thats holds the data produced by the producer

from queue import Queue
q=Queue()
q.put()
q.get()
q.empty()
q.full()


"""

from threading import Thread
from queue import Queue
from time import sleep
x=Queue()
x.put(6)
print(x)
print(type(x))
class Producer:
    def __init__(self) -> None:
        self.q=Queue()
    def produce(self):
        for i in range(1,6):
            print("item produce",i)
            self.q.put(i)
            sleep(1)
class Consumer:
    def __init__(self,prod) -> None:
        self.prod=prod
    def Consume(self):
        for i in range(1,6):
            print("item retrieve",self.prod.q.get(i))
            
p=Producer()
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.Consume)
t1.start()
t2.start()


