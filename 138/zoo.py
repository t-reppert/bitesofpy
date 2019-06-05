import itertools
class Animal:
    count = itertools.count(start=10001)
    animals = {}

    def __init__(self, name):
        self.name = name.title()
        self.id = next(self.count)
        self.animals[self.id] = self.name

    def __str__(self):
        return f'{self.id}. {self.name}'
    
    @classmethod
    def zoo(cls):
        return [f'{i}. {n}' for i,n in cls.animals.items()]