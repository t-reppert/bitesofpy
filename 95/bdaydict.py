MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        for bdate in list(self.values()):
            if bdate.day == birthday.day and bdate.month == birthday.month:
                print(f'Hey {name}, there are more people with your birthday!')
        super(BirthdayDict, self).__setitem__(name, birthday)