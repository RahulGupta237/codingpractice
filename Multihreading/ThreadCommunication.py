"""
Two or more thread communicate with each other 

1 Event
2 Condition
3 Queue

Event-->
   This is one of the simplest mechanism for communication threads:
   one thread signal an Event
   Other thread wait for it

   An Event manage internal flag that can be set to True with set() method 
   and reset to false with clear() method
   THe wait method block untill the flag is True

   from threading import Event
   e=Event


"""


from threading import *
from time import sleep
def light_switch():
   
    e.set()
    print("Green Light On")
    print(e.is_set())
    sleep(3)
    print("Red Light on")
    e.clear()
    print(e.is_set())
def traffic_light():
    e.wait()
    while e.is_set():
       
        print("You can Go Green signal Goo go....")
        sleep(.5)
       
    print("More crowd please Stoop SToop Stop Stoop Stooopp")
e=Event()
t1=Thread(target=light_switch)
t2=Thread(target=traffic_light)
t1.start()
t2.start()


