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
    total_bill = 0
    current_taxi = None
    while menu_choice != "q":
        taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
        if menu_choice == "c":
            print("Taxis available:")
            display_taxi(taxis)
            try:
                index_choice = int(input("Choose taxi: "))
                current_taxi = taxis[index_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            current_bill = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${current_bill:.2f}")
            total_bill += current_bill
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    display_taxi(taxis)


def display_taxi(taxis):
    for number, taxi in enumerate(taxis):
        print(f"{number} - {taxi}")


main()
