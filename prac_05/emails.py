"""
CP1404/CP5632 Practical 5
Emails
Program to store emails and names in a dictionary
Estimate: 25 minutes
Actual: 60 minutes
"""


def main():
    """Program to store emails and names in a dictionary."""
    user_email = " "
    name_to_email = {}
    while user_email != "":
        user_email = input("Email: ")
        user_name = extract_name(user_email)
        name_confirmation = input(f"Is your name {user_name}? (Y/n) ").upper()
        if name_confirmation != "" and name_confirmation != "Y":
            user_name = input("Name: ")
        name_to_email[user_name] = user_email
        user_email = input("Email: ")

    for user_name in name_to_email:
        print(f"{user_name} ({name_to_email[user_name]})")

def extract_name(user_email):
    """Extract name from user email."""
    user_name = user_email.split('@')[0].title()
    user_name = " ".join([name for name in user_name.split(".")])
    return user_name


main()
