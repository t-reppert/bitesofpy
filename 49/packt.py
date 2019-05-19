from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    link = soup.find("div",class_="dotd-main-book-image").a.get('href')
    image = soup.find("div",class_="dotd-main-book-image").img.get('src')
    title = soup.find('div',class_="dotd-title").text.strip()
    description = soup.find("div",class_="dotd-title").find_next_sibling("div").text.strip()

    return Book(title=title,description=description,image=image,link=link)
    
