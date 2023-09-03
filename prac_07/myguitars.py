"""CP1404/CP5632 Practical 7 - my guitars program."""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file with details of guitars, save as objects, and display."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().strip(',')
        guitar = Guitar(parts[0], int(parts[1]), int(parts[2]))
        guitars.append(guitar)
