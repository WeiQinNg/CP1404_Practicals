"""
CP1404/CP5632 Practical 10
Wiki API
24 Sep 2023
"""
import wikipedia


def main():
    title = " "
    while title != "":
        try:
            title = input("Title: ").title()
            print(wikipedia.summary(title))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"{title} does not match any pages. Try another query!")
    print("End.")


main()
