class Car:

    def start(self):
        print("This is demo of class")
c1 = Car() # object
c1.start()        


class Student:
     def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
s1 = Student("Samiksha",20)   
print(s1.name)     
print(s1.age)

class Student1 :
    def __init__(self,name1,age1):
        self.name1 = name1
        self.age1 = age1

    def show(self):
        print("Name:",self.name1) 
        print("Age:",self.age1) 
s = Student1("ASmita",20) 
s.show()       




