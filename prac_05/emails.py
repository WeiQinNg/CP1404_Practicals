"""
CP1404/CP5632 Practical 5
Emails
Program to store emails and names in a dictionary
Estimate: 25 minutes
Actual:  minutes
"""


def main():
    while user_email != "":
        user_email = input("Email: ")
        user_name = user_email.split('@')[0].title()
        print(f"Is your name {user_name}? (Y/n)")


main()
