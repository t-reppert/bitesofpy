import re


class DomainException(Exception):
    """Raised when an invalid domain is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if re.match(r'.*\.[a-z]{2,3}$', name):
            self.name = name
        else:
            raise DomainException()
        
    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively
    def __str__(self):
        return f"{self.name}"

    @classmethod
    def parse_url(cls, url):
        url_regex = re.compile(r'^https*\:\/\/([a-z0-9\-\_\.]*)\/*', re.I)
        if url:
            name = url_regex.search(url).group(1)
            return cls(name)
        else:
            raise DomainException()

    @classmethod
    def parse_email(cls, email):
        if '@' in email:
            name = email.split('@')[1]
            return cls(name)
        else:
            raise DomainException()