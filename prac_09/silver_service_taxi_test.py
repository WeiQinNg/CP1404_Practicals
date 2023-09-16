"""
CP1404/CP5632 Practical 09
Ng Wei Qin
16 Sept 2023
SilverServiceTaxi test
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    old_taxi = SilverServiceTaxi("Old taxi", 100, 2)
    fancy_taxi = SilverServiceTaxi("BMW", 100, 8)
    old_taxi.drive(18)
    fancy_taxi.drive(18)
    print(f"{old_taxi}, current fare = ${old_taxi.get_fare()}")
    print(f"{fancy_taxi}, current fare = ${fancy_taxi.get_fare()}")


main()
