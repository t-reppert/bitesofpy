def flatten(list_of_lists):
    new_list = []
    for i in list_of_lists:
        if type(i) == list:
            new_list.extend(i)
        elif type(i) == tuple:
            new_list.append(list(i))
        else:
            new_list.append(i)
    for i in new_list:
        if type(i) == list:
            return flatten(new_list)
    return new_list
