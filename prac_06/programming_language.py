"""CP1404/CP5632 Practical 6 - Programming language class."""


class ProgrammingLanguage:
    """Programming languages."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a programming language.

        name: string, reference to programming language name
        typing: string, reference to static or dynamic nature
        reflection: boolean
        year: integer, reference for year implemented
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if language is dynamic."""
        if self.typing == "Dynamic":
            return True

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

