"""
CP1404/CP5632 - Practical 2
Broken program to determine score status
"""

# TODO: Fix this!
import random

def main():
    """Score status determining program."""
    score = float(input("Enter score: "))
    print(determine_status(score))
    score = random.randint(0, 100)
    print(determine_status(score))

def determine_status(score):
    """Determine score status using a given score."""
    if score < 0 or score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")

main()