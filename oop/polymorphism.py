# the process in which same method behvaes differently in different classes or depending upon the object or context


class Cat:
    def sound(self):
        print("meow")
class Dog:
     def sound(self):
         print("Barking")   
            
def make_sound(animal):
    animal.sound()
make_sound(Cat())
make_sound(Dog())

# this is exmaple of methodoverriding where child class use same methos as paret class but get diffente implememtation
class Animal:
    def sound(self):
        print("Some sound")
class Cat:
    def sound(self):
        print("meow")
class Dog:
     def sound(self):
         print("Barking")      

a= Animal()
c = Cat()
d = Dog()

a.sound()
c.sound()
d.sound()      