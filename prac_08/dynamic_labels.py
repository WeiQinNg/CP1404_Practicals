"""
CP1404/CP5632 Practical 08
Ng Wei Qin
10 Sept 2023
"""
from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Main program - Kivy app for dynamic label creation."""

    def __init__(self):
        """Construct a name from a list of names."""
        self.names = ["Alice", "Bob", "Charlie"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()

    def create_widgets(self):
