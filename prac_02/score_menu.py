"""
CP1404 - Practical 2
"""
MENU = "(G)et a valid score", "(P)rint result", "(S)how stars", "(Q)uit"

def main():
    """Program with menu to display number of stars based on a given score."""
    print(*MENU)
    menu_choice = input(">>> ")
    while menu_choice != "Q":
        if menu_choice == "G":
            score = int(input("Enter score: "))
            if score < 0 or score > 100:
                print("Invalid score")
        elif menu_choice == "P":
            print(score)
        elif menu_choice == "S":
            print(score * "*")
        else:
            print("Invalid menu choice")
        menu_choice = input(">>> ")







main()