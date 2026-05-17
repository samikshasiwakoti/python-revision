
student = {
"name" : "Samiksha",
"age" : 20,
"gpa" : 3.75,
"is_active" : True,
"courses" :["Math","IT"]

}

semister_info = ("1st semester" , 2026)

skills = {"python","html","python","css"}

print(" Student Detail")
print("Name:", student["name"])
print("age:", student["age"])
print("gpa", student["gpa"])
print("active:", student["is_active"])
print("courses:", student["courses"])

student["courses"].append("Django")

skills.add("html")

student["gpa"] = student["gpa"] + 0.05

if student ["is_active"]:
    print("\n Status:Student is active")
    
for course in student["courses"]:
    print("-",course)


print("\n Semester", semister_info[0])
print("year:" , semister_info[1])

print("\n Skills:")
for skill in skills:
    print("-",skill)


print("\n FULL DATA:")
print(student)