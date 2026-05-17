#  It is a unordered collection, mutable, doenst allow duplicate
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

nums = [1, 2, 2, 3, 3, 4]

unique = set(nums)

print(unique)

a.add(4)
print(a)

# f = frozenset([1,2,3,4])
# f.add(4)
# print(f) we can make set immutable when we nned fiex data 