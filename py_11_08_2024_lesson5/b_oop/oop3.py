class Car:
    MAX_SPEED: int = 110

    def __init__(self, number: int, brand: str, year: int, speed: int, km: int):
        self.number = number
        self.brand = brand
        self.year = year
        self.speed = speed
        self.km = km

    def __str__(self):
        return f"Car[number={self.number}, brand={self.brand}, year={self.year}, speed={self.speed}]"


class Person:
    # class variable
    count = 0

    def __init__(self, pid: int, name: str, age: int):
        # instance variables
        self.pid = pid
        self.name = name
        self.age = age
        Person.count += 1

    def __str__(self):
        return f"Person[id={self.pid}, name={self.name}, age={self.age}]"

    def speak(self):
        print(f"{self.name} is speaking")
