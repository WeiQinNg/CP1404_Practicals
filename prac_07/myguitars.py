"""CP1404/CP5632 Practical 7 - my guitars program."""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file with details of guitars, save as objects, and display."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ")

    out_file = open(FILENAME, 'w', encoding="utf-8-sig")
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, {guitar.cost}", file=out_file)
    out_file.close()


main()
