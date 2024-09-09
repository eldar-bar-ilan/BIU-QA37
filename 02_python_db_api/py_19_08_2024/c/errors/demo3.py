# our custom made error
class CarIllegalSpeedError(Exception):
    pass


class Car:
    MIN_SPEED = 0
    MAX_SPEED = 110

    def __init__(self):
        self.speed = 0

    def drive(self, speed: int):
        # before assigning the new speed check that it is legal
        if Car.MIN_SPEED <= speed <= Car.MAX_SPEED:
            self.speed = speed
        else:
            error = CarIllegalSpeedError(f'speed {speed} is illegal')
            raise error

    def __str__(self):
        return f'Car at speed {self.speed}'
