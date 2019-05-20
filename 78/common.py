def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    setlist = [ set(v) for v in programmers.values() ]
    return list(set.intersection(*setlist))