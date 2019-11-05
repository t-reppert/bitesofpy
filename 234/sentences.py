import re

def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    sentences = (s.strip() for s in re.findall(r'[,\w\s]+[.?!]{1}\n*', text))
    cap_sentences = [ s[0].upper()+s[1:] for s in sentences ]
    return " ".join(cap_sentences)

