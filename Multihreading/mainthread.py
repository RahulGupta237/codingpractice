import threading
"""
MainThread created automatically when program started it is created by PVM

"""
t=threading.current_thread().getName()
print("Hellow")
print(t)