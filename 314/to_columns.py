from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    s = ""
    for idx, n in enumerate(names, start=1):
        s += f"| {n:<10s}"
        if idx % cols == 0:
            print(s)
            s = ""
        if idx == len(names):
            print(s)