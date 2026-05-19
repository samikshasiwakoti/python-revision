# it is like chaining
class Grandparent:
    def home(self):
        print("Old House")

class Parent(Grandparent):
    def car(self):
        print("Car")

class Child(Parent):
    def bike(self):
        print("Bike")

c = Child()
c.home()
c.car()
c.bike()