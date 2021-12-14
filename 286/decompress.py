from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    s = ""
    for i in string:
        if i in table:
            s += decompress(table[i], table)
        else:
            s += i
    return s
