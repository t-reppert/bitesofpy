from math import floor
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict
import re

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


def encode(record: int) -> str:
    """Encodes an integer into Base62"""
    queue = record
    result = ''
    while queue:
        remainder = queue % 62
        queue = floor(queue / 62)
        result = CODEX[remainder] + result
    return result


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    value = 0
    for char in short_url:
        value = 62 * value + CODEX.find(char)
    return value


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    if SITE not in url:
        return "Not a valid PyBites shortened url"
    encoded = re.sub(r'https://pybit.es/','',url)
    decoded = decode(encoded)
    result = LINKS.get(decoded, "Not a valid shortened url")
    return result
    

def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    encoded = encode(next_record)
    LINKS[next_record] = url
    return f"https://pybit.es/{encoded}"

