"""CP1404/CP5632 Practical 7 - Guitar class."""
CURRENT_YEAR = 2023
VINTAGE_THRESHOLD = 50


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
        """Print details of a guitar in string format."""
        return f"{self.name} ({self.year} : ${self.cost})"

    def get_age(self):
        """Calculate age of a guitar."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Check if guitar is vintage."""
        age = self.get_age()
        if age >= VINTAGE_THRESHOLD:
            return True
        else:
            return False

    def __lt__(self, other):
        """Compare guitars by year."""
        return self.year < other.year
