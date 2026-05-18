# # we can create,readmwrite,append file
# file = open("data.txt","w")
# file.write("hello python")
# file.close()


# file = open("data.txt","r")
# content = file.read()
# print(content)


# file = open("data.txt",'a')
# file.write("\n hi i am new")
# file.close()

# # file = open("newfile.txt","x")
# # file.write("this is a new file")
# # file.close()


name = input("Enter name:")
age = input("Enter age:")

with open("data.txt","a") as file:
     file.write(name + " " + age + "\n")