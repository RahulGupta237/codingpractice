"""
THread Rcae Condition-->
    Race condition is a situation that occurs when thread are acting in a unexpected sequence 
    thus leading to unreliable ouput
    This can be eliminated using thread synchronization

"""

from threading import Thread,current_thread
class Flight:
    """
THread Rcae Condition-->
    Race condition is a situation that occurs when thread are acting in a unexpected sequence 
    thus leading to unreliable ouput
    This can be eliminated using thread synchronization

"""
    def __init__(self,available_seat) -> None:
        self.available_seat=available_seat
    def reserve_seat(self,need_seat):
        print(f"available seats:{self.available_seat}")
        if self.available_seat>=need_seat:
            name=current_thread().name
            print(f"{self.available_seat} are allocated {name}")
            self.available_seat-=need_seat
        else:
            print(f"sorry all seat are alloted ")
print(Flight.__doc__)
flight_object=Flight(1)
person1_thread=Thread(target=flight_object.reserve_seat,args=(1,),name="Rahul")
person2_thread=Thread(target=flight_object.reserve_seat,args=(1,),name="Shabnam")
person1_thread.start()
person2_thread.start()

"""
output --> unexpected due to race condition occure 
available seats:1
1 are allocated Rahul
available seats:0
sorry all seat are alloted 

not a valid output thatswhy comes to new concept  Thread ayncronization  this concept give expected output


"""


        