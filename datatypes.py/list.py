# List is one of the datatype that is used to  store multiple items in single variable which can be changed. It is a container that can store values of different datatypes Its method are:
# 1)	Append() – name.append(“Samiksha”) it adds in last 
# 2)	Insert() – add item at specific position, indexing and insert value
# 3)	Remove()-remove specific value
# 4)	Pop()- it remove last or index item
# 5)	Clear() – remove all items
# 6)	Sort()- to ascending or desciding
# 7)	Reverse() reverse list
# 8)	Index() to find position of value
# 9)	Count() to count


demo = [1,"samii",7.8,"True",55]

demo.append(65)
print(demo)

demo.remove(1)
print(demo)

demo.insert(1, "asmii")
print(demo)

print(demo.copy())

demo.reverse()
print(demo)

print(demo.pop(4))
print(demo)

demo.clear()
print(demo)

