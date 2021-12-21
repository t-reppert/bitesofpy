from typing import List


def split_once(text: str, separators: str = None) -> List[str]:
    if not text:
        return ['']
    def check_text(text):
        whitespace_seps = [' ', '\v', '\t', '\r', '\f', '\n']
        for w in whitespace_seps:
            if w in text:
                return True
        return False
    if not separators and not check_text(text):
        return [text]
    if not separators:
        separators = [' ','\t','\v','\r', '\f', '\n']
    try:
        i = {text.index(s): s for s in separators if s in text}
    except ValueError:
        return text
    separators_ordered = [i[k] for k in sorted(i.keys())]
    split_list = []
    temp_string = text
    for s in separators_ordered:
        temp_list = temp_string.split(s, 1)
        split_list.append(temp_list[0])
        temp_string = temp_list[1]
    split_list.append(temp_string)
    return split_list
