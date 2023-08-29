"""CP1404/CP5632 Practical 6 - Guitars program."""

from prac_06.guitar import Guitar

WELCOME_MESSAGE = "My guitars!"


def main():
    print(WELCOME_MESSAGE)
    # name = input("Name: ")
    guitars = []
    # while name != "":
        # year = int(input("Year: "))
        # cost = float(input("Cost: $"))
        # guitars.append(Guitar(name, year, cost))
        # print(f"{name} ({year}) : ${cost} added.")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
