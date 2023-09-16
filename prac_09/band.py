"""
CP1404/CP5632 Practical 09
Ng Wei Qin
16 Sept 2023
Band class
"""


class Band:
    """Band class."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty musician lineup."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of Band."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add a musician to the Band lineup."""
        self.musicians.append(musician)

    def play(self):
        """Call play() method from Musician."""
        musician_plays = [self.musician.play() for self.musician in self.musicians]
        return "\n".join(musician_plays)
