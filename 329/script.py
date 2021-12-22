import re


def snake_case_keys(data):
    new_dict = {}
    for k,v in data.items():
        new_k = ''
        length = len(k)
        for idx, l in enumerate(k):
            if l.isupper() and idx != 0:
                new_k += '_' + l.lower()
            elif l == '-':
                new_k += '_'
            else:
                new_k += l.lower()
        if re.search(r'\d+', new_k):
            temp_k = [x for x in re.split(r'([0-9]+)', new_k) if x]
            new_k = '_'.join(temp_k)
        if isinstance(v, dict):
            new_v = snake_case_keys(v)
        elif isinstance(v, list):
            new_list = []
            for i in v:
                if isinstance(i, dict):
                    new_list.append(snake_case_keys(i))
                elif isinstance(i, list):
                    new_list_2 = []
                    for j in i:
                        if isinstance(j, dict):
                            new_list_2.append(snake_case_keys(j))
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