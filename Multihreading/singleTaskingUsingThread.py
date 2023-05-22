from threading import Thread
from time import sleep

class MyExam:
    """
    when multiple task are executed by a thread one by one then it is called single tasking 
    
    """
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()
    def q1(self):
        print("Question 1 solved")
        sleep(3)
    def q2(self):
        print("Question 2 solved")
        sleep(3)
    def q3(self):
        print("Question 3 solved")
        sleep(3)
print(MyExam.__doc__)
mye=MyExam()
thread_obj=Thread(target=mye.solve_question)
thread_obj.start()