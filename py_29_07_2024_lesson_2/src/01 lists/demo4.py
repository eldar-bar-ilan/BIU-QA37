# changing lists
names = ["aaa", "bbb", "ccc"]
print(names)

# change an element
names[1] = "Dan"
print(names)

# add element to the end of the list
names.append("Nira")
print(names)

# add element to a specific index of the list
names.insert(1, "Amos")
print(names)

# remove an element from the list
del names[2]
print(names)

# print the length of the list - the number of elements
print(len(names))

# remove the firs instance of a value
codes = ["aaa", "bbb", "aaa", "ccc", "bbb", "aaa"]
print(codes)
codes.remove("aaa")
print(codes)
