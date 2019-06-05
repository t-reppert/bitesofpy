import itertools
class Animal:
    _count = itertools.count(start=10001)
    _animals = []

    def __init__(self, name):
        self.name = name.title()
        self.id = next(self._count)
        self._animals.append(self)

    def __str__(self):
        return f'{self.id}. {self.name}'
    
    @classmethod
    def zoo(cls):
        return '\n'.join([str(animal) for animal in cls._animals])