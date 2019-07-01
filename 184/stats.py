from csv import DictReader
from os import path
from urllib.request import urlretrieve
from collections import defaultdict
from operator import itemgetter

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        return list(DictReader(open(data)))

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        unique = set()
        for row in self.rows:
            unique.add(row['bite'])
        return len(unique)

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        unique = set()
        for row in self.rows:
            if row['completed'] == "True":
                unique.add(row['bite'])
        return len(unique)

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        unique = set()
        for row in self.rows:
            unique.add(row['user'])
        return len(unique)

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        unique = defaultdict(int)
        for row in self.rows:
            if row['completed'] == "True":
                unique[row['user']] += 1 
        return len(unique)

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        bites = defaultdict(int)
        for row in self.rows:
            bites[row['bite']] += 1
        bite_list = list(bites.items())
        return sorted(bite_list,key=lambda x:x[1],reverse=True)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        unique = defaultdict(int)
        for row in self.rows:
            if row['completed'] == "True":
                unique[row['user']] += 1
        uniq_list = list(unique.items())
        return sorted(uniq_list,key=lambda x:x[1],reverse=True)[0][0]