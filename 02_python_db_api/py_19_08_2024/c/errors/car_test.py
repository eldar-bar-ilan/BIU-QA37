from demo3 import Car, CarIllegalSpeedError

car = Car()
print(car)

try:
    speed = int(input("enter speed to drive: "))
    car.drive(speed)
except ValueError as e:
    print('Error: input must be a number')
except CarIllegalSpeedError as e:
    print(f'Error: speed must be in the range {Car.MIN_SPEED} - {Car.MAX_SPEED}')
except Exception as e:
    print("Some ether error: ", e)

print("rest of program")
print(car)
