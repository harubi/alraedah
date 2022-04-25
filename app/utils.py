from typing import Any

def get_lists_from_json(json: dict) -> Any:
    return list(json)

def generate_adjacency_list(nodes):
    """ 
    A function to generate a linked-list representing a graph adjacency list from an array.
    For every item in the expanded list, we add to the graph the node as a key,
    and we add an array as a value containing the node (thus edge) pointed at.
    """
    graph = {}

    for node in nodes:
        try:
            graph[node] = [nodes[node]]
        except IndexError:
            graph[node] = []

    return graph


def dfs(visited, graph, node):
    """ 
    DFS (Depth-first search) is our method here, where we recursively traverse 
    out our graph, and save them into the visited list. I have extended the function here to
    check if the working node is already in the visited list and if that list is also the 
    length as the graph, thus actually proving that we have, in fact, a perfect cycle ;)
    """
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            return dfs(visited, graph, neighbour)
    elif node in visited and len(visited) == len(graph):
        return True
    
    return False


def is_cyclic(json):
    """
    A function that ties everything together and return true if the any graph is cyclic,
    It goes every list, converts it to a graph and check.
    """
    results = {}
    
    lists = get_lists_from_json(json)
    
    print(lists)
    
    for list in lists:
        visited = []
        graph = generate_adjacency_list(json[list])
        firstGraphNode = next(iter(graph))
        results[list] = dfs(visited, graph, firstGraphNode)
        
    return results
