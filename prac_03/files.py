"""
CP1404/CP5632 - Practical 3
"""
# Q1

FILENAME = "name.txt"
out_file = open(FILENAME, 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# Q2

in_file = open(FILENAME, 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

# Q3

FILENAME = "numbers.txt"
in_file = open(FILENAME, 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
result = first_number + second_number
print(result)
# in_file.close()

# Q4
FILENAME = "numbers.txt"
in_file = open(FILENAME, 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
