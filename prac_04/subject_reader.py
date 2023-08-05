"""
CP1404/CP5632 Practical 4
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Get subject details and print in organized format."""
    data = get_data()
    print(display_subject_details(data))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_lists = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subject_lists.append(parts)
    input_file.close()
    return subject_lists


def display_subject_details(data):
    """Display subject details from each list."""
    for subject_list in data:
        print(f"{subject_list[0]} is taught by {subject_list[1]:12} and has {subject_list[2]:3} students")


main()
