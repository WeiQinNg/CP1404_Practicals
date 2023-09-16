"""
CP1404/CP5632 Practical 09
Ng Wei Qin
11 Sept 2023
Unreliable car test
Compare two cars with different reliabilities and drive them for various distances
"""

from unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("Benz Patent Motorcar", 100, 25)
    more_reliable_car = UnreliableCar("Toyota", 100, 80)

    for i in range(1, 5):
        print(f"Drive {i}km:")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i)}km")
        print(f"{more_reliable_car.name} drove {more_reliable_car.drive(i)}km")

    print(unreliable_car)
    print(more_reliable_car)


main()
