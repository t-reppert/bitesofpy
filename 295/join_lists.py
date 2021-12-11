from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None
    new_list = []
    for idx, v in enumerate(lst_of_lst, start=1):
        for i in v:
            new_list.append(i)
        if idx != len(lst_of_lst):
            new_list.append(sep)
    return new_list