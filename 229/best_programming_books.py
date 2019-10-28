from pathlib import Path
from urllib.request import urlretrieve
from dataclasses import dataclass
import operator
from bs4 import BeautifulSoup
from pprint import pprint as pp

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)

@dataclass
class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    title: str
    author: str
    year: int
    rank: int
    rating: float

    def __str__(self):
        return f'[{self.rank:03}] {self.title} ({self.year:04})\n      {self.author} {float(self.rating)}'


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    i = 0
    if limit > len(books):
        limit = len(books)
    while limit > 0:
        if year:
            if books[i].year >= year:
                print(books[i])
                limit -= 1
        else:
            print(books[i])
            limit -= 1
        i += 1

def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    soup = _get_soup(html_file)
    books_soup = soup.find('div',{'class':'books'})
    rank = 1
    books = []
    for book in books_soup:
        author = year = title = rating = None
        if book.find('span',{'class':'date'}):
            year = book.find('span',{'class':'date'}).get_text()[-4:]
        if book.find('h2',{'class':'main'}):
            title = book.find('h2',{'class':'main'}).get_text()
            if 'python' not in title.lower():
                title = None
        if book.find('h3',{'class':'authors'}).find('a'):
            author_raw = book.find('h3',{'class':'authors'}).find('a').text
            author_fields = author_raw.split()
            author = author_fields[-1]+", " + " ".join(author_fields[0:len(author_fields)-1])
        if book.find('span',{'class':'our-rating'}):
            rating = book.find('span',{'class':'our-rating'}).get_text()
        if author and year and title and rating:
            books.append(Book(rank=int(rank), title=title, author=author, year=int(year), rating=float(rating)))
            rank += 1
    books = sorted(books, key=lambda x: (x.year,x.title.lower(),x.author) )
    books = sorted(books, key=operator.attrgetter("rating"), reverse=True)
    for i in range(len(books)):
        books[i].rank = i + 1
    return books

def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""