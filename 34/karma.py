from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:
    def __init__(self,name):
        self.name = name
        self._transactions = []

    @property
    def fans(self):
        return len({ x.giver for x in self._transactions })

    @property
    def points(self):
        return [ x.points for x in self._transactions ]
    
    @property
    def karma(self):
        return sum(self.points)

    def __add__(self, transaction):
        self._transactions.append(transaction)
    
    def __str__(self):
        plural = ''
        if self.fans > 1:
            plural = 's'
        return f'{self.name} has a karma of {self.karma} and {self.fans} fan{plural}'