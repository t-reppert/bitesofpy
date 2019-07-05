import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin:
        line = line.strip()
        if 'http' in line and line.count(',') == 1:
            http, text = line.split(',')
            if 'pybit.es' in http or 'codechalleng.es' in http:
                target = ""
            else:
                target = ' target="_blank"'
            print(f'<a href="{http.strip()}"{target}>{text.strip()}</a>')
    


if __name__ == '__main__':
    make_html_links()