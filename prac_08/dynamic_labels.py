"""
CP1404/CP5632 Practical 08
Ng Wei Qin
10 Sept 2023
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app for dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct a name from a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            self.root.ids.main_labels.add_widget(temp_label)


DynamicLabelsApp().run()
