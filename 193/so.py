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
    questions = soup.find_all('a', class_='question-hyperlink')
    votes = soup.find_all('span', class_='vote-count-post')
    views = soup.find_all('div',class_='views')
    questions_list = []
    votes_list = []
    views_list = []
    for i in votes:
        votes_list.append(i.find('strong').contents[0])
    for i in questions:
        questions_list.append(i.contents[0])
    for i in views:
        views_list.append(i.text.strip())
    temp_list = list(zip(questions_list,votes_list,views_list))
    final_list = []
    for i in temp_list:
        if 'm views' in i[2]:
            final_list.append(( i[0],int(i[1]) ))
    final_list = sorted(final_list,key=lambda x:x[1],reverse=True)
    return final_list
    