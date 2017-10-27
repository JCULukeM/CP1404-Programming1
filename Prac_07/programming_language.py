
class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection='', year=''):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True

    def __str__(self):
        return "{}, {} typing, reflection = {}, first appeared in {}".format(self.name, self.typing, self.is_dynamic(), self.year )

