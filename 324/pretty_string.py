import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    return pprint.pformat(obj, depth=2, width=60, sort_dicts=True)
