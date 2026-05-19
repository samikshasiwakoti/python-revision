# many parents one child

class Father:
    def skills(self):
        print("Driving")
class Mother:
    def cooking(self):
        print("cooking")
class Child(Father,Mother):
    def study(self)  :
        print("studying") 

c = Child()
c.skills()
c.cooking()
c.study()