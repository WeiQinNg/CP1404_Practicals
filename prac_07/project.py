"""CP1404/CP5632 Practical 07
Project class
Start time: 03 Sept 2023 1515
End time: 04 Sept 2023
"""
import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name="", start_date="", priority=int, cost=float, completion=int):
        """Construct a line based on the information of a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string representation of a project."""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost:,.2f}, {self.completion}"