# # Dictionary is a collection of key value pairs 

student = {

"name" : "samiksha" ,
"age" : 20 ,
"course" : "BCA"

}

print(student["name"])
print(student.keys())
print(student.values())
print(student.get("name"))
print(student.items())

student["age"] = 21
print(student)

student["name"] = "Asmii"
print(student)
