# the process of hiding implementation details and showing only the essential features.
#Abstract class defines rules, child class implements, object executes.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class Esewa(Payment): 
    def pay(self,amount):
        print(f"Paid{amount} using Esewa")

class Khalti(Payment):
    def pay(self,amount):
        print(f"Paid{amount}using kHalti")

P1 = Esewa()
P2 = Khalti()      

P1.pay(500)
P2.pay(100)
