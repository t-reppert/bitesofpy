from statistics import mean, median
import decimal
class IntList(list):
    
    def append(self, *args):
        for arg in args:
            if type(arg) == list:
                for i in arg:
                    if type(i) not in [int, float, decimal.Decimal]:
                        raise TypeError
            elif type(arg) not in [int, float, decimal.Decimal]:
                raise TypeError
            super().append(*args)

    def __add__(self, other):
        if type(other) == list:
            for i in other:
                if type(i) not in [int, float, decimal.Decimal]:
                    raise TypeError
        else:
            raise TypeError
        return super().__add__(other)

    def __iadd__(self, other):
        if type(other) == list:
            for i in other:
                if type(i) not in [int, float, decimal.Decimal]:
                    raise TypeError   
        else:
            raise TypeError
        return super().__iadd__(other)

    @property
    def mean(self):
        total = 0
        for i in self:
            total += float(i)
        return total/len(self)

    @property
    def median(self):
        return median(self)

# mylist = IntList([1, 3, 5])
# mylist.append(7)
# mylist.append([2, 5])
# print(mylist)