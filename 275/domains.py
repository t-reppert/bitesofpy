from collections import Counter

import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    table = soup.find('div', class_="content").find('table')
    common_domains = []
    for r in table.find_all('tr'):
        col = r.find_all('td')
        common_domains.append(col[2].text)
    return common_domains

def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    domains = [s.split('@')[1] for s in emails if s.split('@')[1] not in common_domains]
    count = Counter(domains)
    return count.most_common()