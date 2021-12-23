from typing import Dict, Any
import re

def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    new_dict = {}
    for k,v in data.items():
        if isinstance(k, str):
            new_k = k.lstrip('@')
        else:
            new_k = k
        if isinstance(v, dict):
            new_v = rename_keys(v)
        elif isinstance(v, list):
            new_list = []
            for i in v:
                if isinstance(i, dict):
                    new_list.append(rename_keys(i))
                elif isinstance(i, list):
                    new_list_2 = []
                    for j in i:
                        if isinstance(j, dict):
                            new_list_2.append(rename_keys(j))
                        else:
                            new_list_2.append(j)
                    new_list.append(new_list_2)
                else:
                    new_list.append(i)
            new_v = new_list
        else:
            new_v = v
        new_dict[new_k] = new_v
    return new_dict