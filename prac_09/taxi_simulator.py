"""
CP1404/CP5632 Practical 09
Ng Wei Qin
17 Sept 2023
Taxi simulator program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's drive!")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        total_bill = 0
        taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
        current_taxi = None
        if menu_choice == "c":
            for number, taxi in enumerate(taxis):
                print(f"{number} - {taxi}")
            try:
                index_choice = input("Choose taxi: ")
                current_taxi = taxis[index_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            distance = int(input("Drive how far? "))
            current_taxi.



main()
