"""CP1404/CP5632 Practical 6 - Guitar testing program."""

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 199)

    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{gibson.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
