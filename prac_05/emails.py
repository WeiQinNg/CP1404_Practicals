"""
CP1404/CP5632 Practical 5
Emails
Program to store emails and names in a dictionary
Estimate: 25 minutes
Actual:  minutes
"""


def main():
    """Program to store emails and names in a dictionary."""
    while user_email != "":
        user_email = input("Email: ")
        user_name = extract_name(user_email)
        print(f"Is your name {user_name}? (Y/n)")


def extract_name(user_email):
    """Extract name from user email."""
    user_name = user_email.split('@')[0].title()
    return user_name


main()
