def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    data_transposed = []
    if type(data) == list:
        data_t = {}
        for j in range(len(data[0])):
            for i in range(len(data)):
                if j not in data_t:
                    data_t[j] = [data[i][j]]
                else:
                    data_t[j].append(data[i][j])
        for k,v in data_t.items():
            data_transposed.append(tuple(v))
    else:
        keys = []    
        values = []
        for k,v in data.items():
            keys.append(k)
            values.append(v)
        keys=tuple(keys)
        values=tuple(values)
        data_transposed = [keys,values]

    return data_transposed
