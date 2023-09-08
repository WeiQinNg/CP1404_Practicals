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
            display_project(incomplete_projects)
            print("Completed projects: ")
            display_project(completed_projects)
        elif menu_choice == "F":
            is_valid = False    # Add a variable to initiate while loop
            while not is_valid:
                try:
                    date = input("Show projects that start after date (dd/mm/yy): ")
                    filtered_projects = filter_project(date, projects)
                    sorted_projects = sort_project(filtered_projects)
                    display_project(sorted_projects)
                    is_valid = True
                except ValueError:
                    print("Invalid date format, please enter date as dd/mm/yy: ")
                    date = input("Show projects that start after date (dd/mm/yy): ")
        elif menu_choice == "A":
            print("Let's add a new project")
            try:
                name = input("Name: ")
                start_date = input("Start date (dd/mm/yy): ")
                priority = input("Priority: ")
                cost = input("Cost estimate: ")
                cost = int(cost.replace('$', ''))
                completion = input("Percent complete: ")
                new_project = Project(str(name), str(start_date), int(priority), float(cost), int(completion))
                projects.append(new_project)
            except ValueError:
                print("Invalid input")
        elif menu_choice == "U":
            projects = sort_project(projects)
            display_project(projects)
            number_to_project = {}
            for number, project in enumerate(projects):
                number_to_project[number] = project
            try:
                project_number = input("Project choice: ")
                project_choice = number_to_project[project_number]
                print(project_choice)
                new_percent = input("New Percentage: ")
                new_priority = input("New Priority: ")
                if new_percent != "":
                    project_choice.update_percentage(new_percent)
                if new_priority != "":
                    project_choice.update_priority(new_priority)
            except KeyError:
                print("Invalid choice")
            else:
                print("Invalid choice")
            print(MENU)
            menu_choice = input(">>> ").upper()
        print("Thank you for using custom-built project management software.")

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
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}", file=out_file)


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


def display_project(projects):
    """Display information of each project."""
    for number, project in enumerate(projects):
        print(f"{number + 1}, {project}")


def filter_project(date, projects):
    """Filter and return projects that start after specified date."""
    filtered_projects = []
    for project in projects:
        if project.compare_date(date):
            filtered_projects.append(project)
    return filtered_projects


def sort_project(projects):
    """Sort projects according to project start date."""
    dates = []
    for project in projects:
        if project.start_date not in dates:
            dates.append(project.start_date)
    dates.sort()
    sorted_projects = []
    for date in dates:
        for project in projects:
            if project.start_date == date:
                sorted_projects.append(project)
    return sorted_projects


main()
