import re

def strip_comments(code):
    line_regex = re.compile(r'^\s*#.*\n',re.M)
    midline_regex = re.compile(r'[^\:\)\'\n]\s*#[ a-zA-Z]*\n',re.M)
    multiline_regex = re.compile(r'^\s*"""[A-Za-z0-9\-\:\,\(\)\_\.\n\s]*"""\n',re.M)
    code = line_regex.sub('',code)
    code = midline_regex.sub('',code)
    code = multiline_regex.sub('',code)
    return code