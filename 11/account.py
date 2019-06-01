class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'

    def __len__(self):
        return len(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __getitem__(self, position):
        return self._transactions[position]

    def __add__(self, value):
        if type(value) != int:
            raise ValueError
        return self._transactions.append(value)
    
    def __sub__(self, value):
        if type(value) != int:
            raise ValueError
        return self._transactions.append(-value)