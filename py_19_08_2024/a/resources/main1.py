from a.resources.demo1_resources import Car
from a.resources.demo1_resources import CarContextManager

with CarContextManager() as car:
    car.drive(80)
    car.drive(30)
    car.drive(110)

print('out of context')
