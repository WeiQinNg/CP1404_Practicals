"""
CP1404/CP5632 Practical 10
Wiki API
24 Sep 2023
"""
import wikipedia


def main():
    title = " "
    while title != "":
        title = input("Title: ")
        print(wikipedia.summary(title))
    print("End.")


main()
