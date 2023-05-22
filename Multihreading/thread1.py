"""
Creating Thread Without using class

thread_object=Thread(target=function,args=(arg1,arg2,...))

"""
from threading import Thread
def learn_thread(a,b):
    print("Running Thread",a,b)
    for i in range(4):
        print("Child Thread")
    
thread_object=Thread(target=learn_thread,args=(3,5))
print(thread_object)
thread_object.start()
for i in range(5):
    print("main thread")
