from urllib.request import urlretrieve
from pathlib import Path
from collections import Counter
import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup
import re

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
if not PYCON_HTML.exists():
    urlretrieve('https://bit.ly/2O5Bik7', PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()
    speaker_spans = soup.find_all('span',{'class':'speaker'})
    speaker_text = [ s.get_text().strip() for s in speaker_spans ]
    speakers = []
    for text in speaker_text:
        if ',' in text or '/' in text:
            l = re.split(',|/', text)
            speakers += [ x.strip() for x in l ]
        else:
            speakers.append(text.strip())
    return [ x.split()[0] for x in speakers ]


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers, rounded to 2 decimal places."""
    d = gender.Detector()
    total = len(first_names)
    genders = Counter([ d.get_gender(x) for x in first_names ])
    return round(((genders['female']+genders['mostly_female'])/total)*100,2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)