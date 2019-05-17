IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    filtered_names = []
    for name in names:
        if name[0] == IGNORE_CHAR:
            continue
        elif name[0] == QUIT_CHAR:
            break
        elif any(digit in name for digit in '0123456789'):
            continue
        filtered_names.append(name)
        if len(filtered_names) == MAX_NAMES:
            break
    return filtered_names
    