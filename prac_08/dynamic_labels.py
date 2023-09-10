"""
CP1404/CP5632 Practical 08
Ng Wei Qin
10 Sept 2023
"""
from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Main program - Kivy app for dynamic label creation."""

    def __init__(self, names):
        """Construct a name from a list of names."""
        names = ["Alice", "Bob", "Charlie"]
        self.names = names
