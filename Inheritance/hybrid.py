#combination of two or more inheritance
class A:
    def show(self):
        print("A class")
class B(A):   # single + multilevel part
    def showB(self):
        print("B class")

class C:
    def showC(self):
        print("C class")

class D(B, C):  # multiple inheritance + hybrid
    def showD(self):
        print("D class")


d = D()
d.showA()
d.showB()
d.showC()
d.showD()
