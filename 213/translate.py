import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    code_regex = re.compile(r'(\<code\>.*?\<\/code\>)',re.M)
    pre_regex = re.compile(r'(\<pre\>[^\r]*?\</pre\>)',re.M)
    original_code = code_regex.findall(org_text)  
    original_pre = pre_regex.findall(org_text)
    code_count = 0
    code_trans = code_regex.findall(trans_text)
    for i in code_trans:
        trans_text = re.sub(re.escape(i), original_code[code_count], trans_text)
        code_count += 1
    pre_count = 0
    pre_trans = pre_regex.findall(trans_text)
    for i in pre_trans:
        trans_text = re.sub(re.escape(i), original_pre[pre_count], trans_text)
        pre_count += 1
    return trans_text