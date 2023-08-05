"""
CP1404/CP5632 Practical 4
List warm up
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]
# 3
# numbers[-1]
# 2
# numbers[3]
# 1
# numbers[:-1]
# [3, 1, 4, 1, 5, 9, 2]
# numbers[3:4]
# 1
# 5 in numbers
# True
# 7 in numbers
# False
# "3" in numbers
# False
# numbers + [6, 5, 3]
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Q1
numbers[0] = "ten"
print(numbers)

# Q2
numbers[-1] = 1
print(numbers)

# Q3
print(numbers[2:])

# Q4
print(9 in numbers)