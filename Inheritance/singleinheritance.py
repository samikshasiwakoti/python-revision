# the process in which child class accquires properties and methods of parent class is
# in single inheritance there will be one parent one child

class Animal :
    def eat(self):
        print("Eating")

class Dog(Animal) :      
    def bark(self):
        print("Barking") 

d = Dog()
d.eat()
d.bark()