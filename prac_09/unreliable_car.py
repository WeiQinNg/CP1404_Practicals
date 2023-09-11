"""
CP1404/CP5632 Practical 09
Ng Wei Qin
11 Sept 2023
Unreliable car class
"""
from car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that drives based on a percentage chance."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance, reliability):
        """Drive like parent Car but only if reliability > random number."""
        distance_driven = super().drive(distance)
        if reliability > random.randint(0, 100):
            return distance_driven
        else:
            return 0
