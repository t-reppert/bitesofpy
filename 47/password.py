import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    elif not re.search(r'\d+',password):
        return False
    elif not re.search(r'[a-z][a-z]',password):
        return False
    elif not re.search(r'[A-Z]',password):
        return False
    elif not any(char in PUNCTUATION_CHARS for char in password):
        return False
    elif password in used_passwords:
        return False
    else:
        used_passwords.add(password)
        return True