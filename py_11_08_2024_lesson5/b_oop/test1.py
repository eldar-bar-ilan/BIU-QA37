from oop3 import Person


print(f"count is {Person.count}")  # 0
p1 = Person(1, "aaa", 11)
p2 = Person(2, "bbb", 22)
print(f"count is {Person.count}")  # 2

print(p1)
print(p2)

