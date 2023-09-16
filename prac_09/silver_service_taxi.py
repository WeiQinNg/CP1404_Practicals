"""
CP1404/CP5632 Practical 09
Ng Wei Qin
16 Sept 2023
SilverServiceTaxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs based on fanciness."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverService Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

