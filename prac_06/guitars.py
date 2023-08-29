"""CP1404/CP5632 Practical 6 - Guitars program."""

from prac_06.guitar import Guitar

WELCOME_MESSAGE = "My guitars!"


def main():
    print(WELCOME_MESSAGE)
    guitars = []
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append([name, year, cost])
    print(f"{name} ({year}) : ${cost} added.")

