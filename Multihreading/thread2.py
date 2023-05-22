"""
creating thread by creating child class thread

from threading import Thread
class ClassName(Thread):
    pass
thread_object=ClassName()

"""

from threading import Thread
class Mythread(Thread):
    """
    creating thread by creating child class thread
    run() method automatically run when thread start

    this code having two thread executing simultaneously two thread at a time give inconsistence output
    
    """
    def run(self):
        for i in range(5):
            print("Run Thread")
thread_obj=Mythread()
thread_obj.start()
#thread_obj.join()  if i want to execute separate thread i will use join()

for i in range(5):
    print("Main THread")