import random
# a dictionary is a collection of key-value pairs
# dictionary operator is {}

# map numbers to letters
number_to_letters = {1: "A", 2: "B", 3: "C"}
print(number_to_letters)

key = random.randint(1, 3)
val = number_to_letters[key]
print(f"{key} -> {val}")

print(f"1 -> {number_to_letters[1]}")
