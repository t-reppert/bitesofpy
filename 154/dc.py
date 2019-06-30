from dataclasses import dataclass,field

@dataclass(order=True)
class Bite(object):

    number: int
    title: str
    level: str = 'Beginner'
    
    def __post_init__(self):
        self.title = self.title.capitalize()
