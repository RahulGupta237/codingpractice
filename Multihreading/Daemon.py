"""
Daemon thread is a thread which runs continously in the background.
it provide support to non-daemon threads

daemon threads are not require to terminate explicity 
i.e automatically terminate

thread.setDaemon(True)
thread.daemon=True
thread.isDaemon()

if thread.start():
    it can not be change status RuntimeException
    unable to change thread to daemon thread



"""

from threading import Thread,current_thread
from time import sleep

def teacher():
    for i in range(1,11):
        print("Teaching Session",i)
        sleep(1)
t1=Thread(target=teacher)
t1.setDaemon(True)
t1.start()
sleep(6)
print("Exam finished ",current_thread().name)



"""
case 1--> without daemon thread occur below output 
   this below output is not expected because teaching session statrt eventhough exam finished 
    thats why we need to support this support provide daemon thread


Teaching Session 1
Exam finished  MainThread
Teaching Session 2
Teaching Session 3
Teaching Session 4
Teaching Session 5
Teaching Session 6
Teaching Session 7



"""