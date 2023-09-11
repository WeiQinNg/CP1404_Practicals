"""
CP1404/CP5632 Practical 09
Ng Wei Qin
11 Sept 2023
Unreliable car class
"""
from car import Car


class UnreliableCar:
    """Specialised version of a Car that drives based on a percentage chance."""

    def __init__(self, name="", fuel=0, reliability=0.0):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
