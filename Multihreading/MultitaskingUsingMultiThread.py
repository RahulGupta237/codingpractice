
from threading import Thread
class Hotel:
    """
When multiple task are executed at a time then it is called Multi-Tasking
We need more than one thread and when we use more than thread it is called multi threading
Race condition occur give unexpected output
"""
    def __init__(self,t) -> None:
        self.t=t
    def food(self):
        for i in range(4):
            print(self.t,i)
print(Hotel.__doc__)
order_object=Hotel("Take order from Table")
servefood_object=Hotel("Serve Food to Table")
order_thread_object=Thread(target=order_object.food)
servefood_thread_object=Thread(target=servefood_object.food)
order_thread_object.start()
servefood_thread_object.start()

"""
Take order from Table 0
Take order from Table 1
Take order from Table 2
Serve Food to Table 0
Serve Food to Table 1
Serve Food to Table 2
Serve Food to Table 3
Serve Food to Table 4
Serve Food to Table 5
Take order from Table 3
Take order from Table 4
Take order from Table 5

this give inconsistence or unexpected output thats why give Race Condition


"""
        