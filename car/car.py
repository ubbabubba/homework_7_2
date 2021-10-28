class Car:

    # example from https://confluence.jetbrains.com/display/PYH/Creating%20and%20running%20a%20Python%20unit%20test

    def __init__(self, speed=0, time=0, odometer=0):
        self.speed = speed
        self.odometer = odometer
        self.time = time

    def say_speed(self):
        return self.speed

    def say_odometer(self):
        return self.odometer

    def say_time(self):
        return self.time

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            return 0