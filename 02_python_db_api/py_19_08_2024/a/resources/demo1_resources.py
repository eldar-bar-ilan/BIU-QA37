class Car:
    def __init__(self):
        self.speed = 0

    def drive(self, speed):
        self.speed = speed
        print(f'car is moving at {self.speed} km/h')

    def chek_oil(self):
        print('checking oil')

    def turn_lights_off(self):
        print('lights turned off')


class CarContextManager:
    def __init__(self):
        self.car = Car()

    def __enter__(self):
        print("=== enter")
        self.car.chek_oil()
        return self.car

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("=== exit")
        self.car.turn_lights_off()
  