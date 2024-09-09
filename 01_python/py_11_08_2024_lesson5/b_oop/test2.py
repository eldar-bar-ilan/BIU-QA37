from oop3 import Car

print(Car.MAX_SPEED)

car: Car = Car(111, "Ford", 2020, 0, 0)
print(car)

car.speed = 110
print(car)

print(car.km)
car.drive(10)
car.drive(20)
print(car.km)
