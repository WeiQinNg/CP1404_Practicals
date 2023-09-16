"""
CP1404/CP5632 Practical 09
Ng Wei Qin
16 Sept 2023
Band class
"""


class Band:
    """Band class."""

    def __init__(self, name=""):
        """Initialise a band with a name and an empty musician lineup."""
        self.name = name
        self.musicians = []

