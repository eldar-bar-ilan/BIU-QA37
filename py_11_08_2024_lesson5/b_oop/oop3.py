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
