"""
CP1404/CP5632 Practical 10
Wiki API
24 Sep 2023
"""
import wikipedia


def main():
    title = " "
    title = input("Title: ").title()
    while title != "":
        try:
            print(wikipedia.summary(title))
        except wikipedia.exceptions.DisambiguationError as e:
            print("Please specify the title from the list:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"{title} does not match any pages. Try another query!")
        title = input("Title: ").title()
    print("End.")


main()
