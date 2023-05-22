
from threading import Thread,current_thread,Semaphore,BoundedSemaphore
class Flight:
    """
THread Rcae Condition-->
    Race condition is a situation that occurs when thread are acting in a unexpected sequence 
    thus leading to unreliable ouput
    This can be eliminated using thread synchronization

    Here using semaphores and give expected output


"""
    def __init__(self,available_seat) -> None:
        self.available_seat=available_seat
        self.l=BoundedSemaphore(2)
        print(f"lock--{self.l}")
    def reserve_seat(self,need_seat):
        self.l.acquire(blocking=True)
        print(f"acquire lock--{self.l}")
        print(f"available seats:{self.available_seat}")
        if self.available_seat>=need_seat:
            name=current_thread().name
            print(f"{self.available_seat} are allocated {name}")
            self.available_seat-=need_seat
        else:
            print(f"sorry all seat are alloted ")
        self.l.release()
        print(f"release lock--{self.l}")
print(Flight.__doc__)
flight_object=Flight(2)
person1_thread=Thread(target=flight_object.reserve_seat,args=(1,),name="Rahul")
person2_thread=Thread(target=flight_object.reserve_seat,args=(1,),name="Shabnam")
person3_thread=Thread(target=flight_object.reserve_seat,args=(1,),name="Sauda")
person1_thread.start()
person2_thread.start()
person3_thread.start()
print("main thread")


"""

vlaue error: semaphore release to many times 
it is invalid bcz number of release call should not exceed the number of  acquire call in Bounded semaphores

To prevent simple programming mistake it is recommended to use BoundedSemaphore





"""





        