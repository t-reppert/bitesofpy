import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    response = requests.get(cached_so_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    questions = soup.select('.question-summary')
    answer = []
    for q in questions:
        question = q.select_one('.question-hyperlink').get_text()
        votes = q.select_one('.vote-count-post').get_text()
        views = q.select_one('.views').get_text()
        if 'm views' not in views:
            continue
        answer.append((question,int(votes)))
    return sorted(answer, key=lambda x:x[1], reverse=True)
    