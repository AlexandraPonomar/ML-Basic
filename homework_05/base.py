"""
Доработайте класс `Vehicle`
"""

from exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Not enough fuel to start")

    def move(self, distance):
        required_distance = self.fuel_consumption * distance
        if self.fuel >= required_distance:
            self.fuel-= required_distance
        else:
            raise NotEnoughFuel(f"Need {required_distance}, but have {self.fuel}")