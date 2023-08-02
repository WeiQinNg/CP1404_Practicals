"""
CP1404/CP5632 Practical 4
Quick pick program
"""
import random

MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
NUMBER_OF_VALUES = 6

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    numbers = []
    while len(numbers) < NUMBER_OF_VALUES:
        number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print(*[f"{number:>2}" for number in numbers], sep=" ")
