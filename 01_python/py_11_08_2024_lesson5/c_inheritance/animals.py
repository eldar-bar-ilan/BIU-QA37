class Animal:
    def speak(self):
        print(f"speak like an animal")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cow(Animal):
    def speak(self):
        print("Moo")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def print_animals(self):
        for a in self.animals:
            print(type(a))

    def make_animals_speak(self):
        for a in self.animals:
            a.speak()
