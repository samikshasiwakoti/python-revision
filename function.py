def greet(): # is is user defined fucntion
    print("Hello,welcome")
greet()    

def greet ( name = "samiksha"): # fucntion with  default paramtere
    print("hello",name)
greet()  



def greet(name): # fucntion with arguments
    print("hello",name)
greet("Asmita")    


def login(username,password):
    if username == "Admin" and password == "1234":
        return "Login success"
    else:
        return"invalid credentials"
print(login("admin","1234"))

add = lambda a, b: a + b# lambda fucntion

print(add(5, 3))

def add(a, b):
    return a + b

def result():
    total = add(5, 10)
    print(total)

result()