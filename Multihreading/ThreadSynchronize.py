synchronization="""
Thread Synchronization-->
many Thread trying to access the same object can lead to be problem
like maikng data inconsistent data or getting unexpected output
so when thread is already access an object preventing any other thread accessing
the same object is called THread Synchronization

Synchronization nothing but lock the code in which thread are acting

Thread synchronization recommended 
when multiple threading are acting on the same object simultaneously


There are following Thechnique to do synchronize:--
1 Locks--->  two state lock(acquire()) and unlock (release())
2 R Lock---> number of lock == number of unlock i.e acquire==release
3 Semaphores--->number of lock <<number of unlock or any order



Lock----->
    from threading Lock
    a=Lock()
    a.acquire(blocking=True,timeout=-1)
    a.release() this method is used to release a lock


"""


print(synchronization)