"""CP1404/CP5632 Practical 07
Project management program
Start time: 03 Sept 2023 1515
End time: 07 Sept 2023
"""
from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    menu_choice = input(">>> ")
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Enter filename: ")
            if filename != '':
                try:
                    projects = read_file(filename)
                    print(projects)
                except FileNotFoundError:
                    print('Invalid filename')


def read_file(filename):
    """Read txt file, create project objects and store them in a list."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().replace("\t", ",")
            parts = parts.split(",")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects



main()