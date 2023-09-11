"""
CP1404/CP5632 Practical 09
Ng Wei Qin
11 Sept 2023
Taxi object
"""
from taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)


main()
