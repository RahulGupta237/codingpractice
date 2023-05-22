from optparse import Option
import sys
from unicodedata import name
# from unicodedata import name
class Customer:
    bankname="State Bank Of India"
    def __init__(self,name,balance=0.0) -> None:
        self.name=name
        self.balance=balance
    def deposite(self,amt):
        self.balance+=amt
        print(f"Balance after deposite: {self.balance}")
    
    def withdraw(self,amt):
        if amt > self.balance:
            print(f"Sorry Insufficient Funds cannot perform this operation")
            sys.exit()
        self.balance=self.balance-amt
        print(f"Balance after withdraw {self.balance}")
print("Welcome to ", Customer.bankname)
name=input("enter your name")
c=Customer(name)
while True:
    print(f"d-Deposite\n\n w-withdraw\n\n e-exit\n")
    Option=input("choose your option")
    if Option=="d" or Option=="D":
        try:
            amt=float(input("Enter amount"))
            c.deposite(amt)
        except:
            print(f"Hey {name} please enter amount")
    elif Option=="w" or Option=="W":
        amt=float(input("Enter amount"))
        c.withdraw(amt)
    elif Option=="e" or Option=="E":
        print(f"Thanks for banking")
        sys.exit()
    else:
        print("Invalid option please choose valid option")
