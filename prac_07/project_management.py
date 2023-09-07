"""CP1404/CP5632 Practical 07
Project management program
Start time: 03 Sept 2023 1515
End time: 07 Sept 2023
"""
from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = read_file('projects.txt')
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Enter filename: ")
            if filename != '':
                try:
                    projects = read_file(filename)
                    print(projects)
                except FileNotFoundError:
                    print('Invalid filename')
        elif menu_choice == "S":
            filename = input("Enter filename to save to: ")
            save_file(projects, filename)
        elif menu_choice == "D":
            completed_projects, incomplete_projects = process_project(projects)
            print("Incomplete projects: ")
            print("Completed projects: ")


def read_file(filename):
    """Read txt file, create project objects and store them in a list."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_file(projects, filename):
    """Save current information to user specified file."""
    with open(filename, 'w') as out_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}")


def process_project(projects):
    """Store completed and incomplete projects in separate lists."""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    completed_projects.sort()
    incomplete_projects.sort()
    return completed_projects, incomplete_projects


main()
