import builtins
from typing import Dict, List
import keyword
import sys
import pkgutil


scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    total = 0
    builtins_list = dir(builtins)
    modules = [x.lstrip('_') for x in sys.builtin_module_names]
    modules2 = [x.name for x in pkgutil.iter_modules()]
    modules = modules + modules2
    for o in objects:
        if o in builtins_list:
            total += 1
        if o in keyword.kwlist:
            total += 2
        if o in modules:
            total += 3
    return total


score_objects(['any', 'all', 'max'])