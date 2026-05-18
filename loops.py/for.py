#loop is used to repeate a block of code mutilpiles times instead of writing it again and again
# for loop is used to reapeate a block of code when we know how many times we have to repaet it
# for loop is used in list,string,tuple,set,else dict

for i in range(5):
    print(i)
else :
    print("Loop finished")


fruits =["mango","litchi","orange"]   
for fruit in fruits :
    print(fruit) 

# break loop
# loop stops immediately

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 2:
        continue
    print(i)

for i in range(3):

    for j in range(2):
        print(i, j)