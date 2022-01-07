from numpy import inf
from copy import deepcopy

def shortest_path(graph, start, end):
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """
    result = {}
    sorted_graph = sorted(graph.items())
    original_graph = deepcopy(graph)
    costs = {sorted_graph[s][0]: inf for s in range(len(sorted_graph))}
    costs[sorted_graph[0][0]] = 0

    next_node = start
    while next_node != end:
        for neighbor in graph[next_node]:
            if graph[next_node][neighbor] + costs[next_node] < costs[neighbor]:
                costs[neighbor] = graph[next_node][neighbor] + costs[next_node]
                result[neighbor] = next_node
            del graph[neighbor][next_node]
        del costs[next_node]
        next_node = min(costs, key=costs.get)

    node = end
    reverse_path = [end]
    total_cost = 0
    while node != start:
        reverse_path.append(result[node])
        total_cost += original_graph[node][result[node]]
        node = result[node]
    
    path = list(reversed(reverse_path))
    return (total_cost, path)