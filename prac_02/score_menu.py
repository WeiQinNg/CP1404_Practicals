"""
CP1404 - Practical 2
"""
MENU = "(G)et a valid score", "(P)rint result", "(S)how stars", "(Q)uit"

def main():
    """Program with menu that takes in a given score to determine status."""
    score = ""
    print(*MENU, sep="\n")
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            score = get_score()
        elif menu_choice == "P":
            print(determine_status(score))
        elif menu_choice == "S":
            print(score * "*")
        else:
            print("Invalid menu choice")
        print(*MENU, sep="\n")
        menu_choice = input(">>> ").upper()
    print("Farewell")


def get_score():
    """Get a valid score."""
    score = int(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_status(score):
    """Determine score status using a given score."""
    if score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")


main()