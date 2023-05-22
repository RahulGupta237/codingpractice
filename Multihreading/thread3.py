"""
Thread Child class with Constructor

"""
from threading import Thread
class Mythread(Thread):
    def __init__(self,a) -> None:
        Thread.__init__(self)
        self.a=a
        print(self.a)
    def run(self) -> None:
        return self.a
thread_obj=Mythread(56)
print(thread_obj)
thread_obj.start()