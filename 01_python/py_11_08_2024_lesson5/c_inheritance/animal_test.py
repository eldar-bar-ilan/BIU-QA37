from animals import *

animal = Animal()
animal.speak()

cat = Cat()
cat.speak()

dog = Dog()
dog.speak()

print("=================")
animals = [Dog(), Dog(), Cat(), Dog(), Animal()]

for animal in animals:
    animal.speak()
