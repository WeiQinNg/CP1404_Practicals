"""CP1404/CP5632 Practical 6 - Guitar class."""


class Guitar:
    """Guitars."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar.

        name: string, reference to guitar name
        year: integer, reference to the year in which the guitar was made
        cost: float, reference to the cost of the guitar
        """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : ${self.cost})"

    def get_age(self):
        current_year = 2023
        age = current_year - self.year
        return age
