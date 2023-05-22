"""
Creating Thread without creating child class to thread class


class ClassName():
    statement
object_name=ClassName()
thread_object=Thread(target=object_name.function_name,args=(arg1,args2,....))

"""
from threading import Thread
class Mythread():
    def __init__(self,a,b) -> None:
        self.xy=a
        self.za=b
    def display(self):
        new_val=self.xy+self.za
        print("Child Thread",new_val)
object=Mythread(45,67)
thread_obj=Thread(target=object.display)
thread_obj.start()
