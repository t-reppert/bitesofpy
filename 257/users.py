import re

def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    users = passwd.splitlines()
    user_dict = {}
    for x in users:
        if x:
            line = x.split(':')
            if line[4]:
                user_dict[line[0]] = re.sub(r'\,+',' ',line[4]).strip()
            else:
                user_dict[line[0]] = 'unknown'
    return user_dict