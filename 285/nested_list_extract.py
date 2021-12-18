import re


def process_list(items):
    processed_list = []
    for idx, i in enumerate(items):
        if isinstance(i, list):
            processed_list.extend(process_list(i))
        else:
            processed_list.append(i)
    return processed_list


def extract_ipv4(data):
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """
    ip_regex = re.compile(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    items = process_list(data)
    if 'ip' not in items or 'mask' not in items:
        return []
    final_list = []
    temp_ip = ''
    temp_mask = ''
    for idx, i in enumerate(items):
        if '"' in i:
            i = i.replace('\"','')
        if i == 'ip':
            if not items[idx+1]:
                return []
            ip = items[idx+1].replace('\"','')
            if not ip_regex.match(ip):
                return []
            temp_ip = ip
        elif i == 'mask':
            if not items[idx+1] or not items[idx+1].isnumeric():
                return []
            temp_mask = items[idx+1].replace('\"','')
            final_list.append((temp_ip, temp_mask))
    return final_list
