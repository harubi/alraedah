from typing import *
# This is very unsafe, but I did at for testing purposes.
import sys
sys.setrecursionlimit(1500)


def get_lists_from_json(json: dict) -> list:
    # BAD! We should iterate over json objects, never load them all info memory, we should leverage generator iterators and yield expressions here.
    try:
        return list(json)
    except Exception as e:
        return e


def generate_adjacency_list(nodes: list) -> dict:
    """ 
    A function to generate a linked-list representing a graph adjacency list from an array.
    For every item in the expanded list, we add to the graph the node as a key,
    and we add an array as a value containing the node (thus edge) pointed at.
    """
    graph = {}
    try:
        for node in nodes:
            try:
                graph[node] = [nodes[node]]
            except IndexError:
                graph[node] = []
    except Exception as e:
        return e

    return graph


def dfs(visited: list, graph: dict, node: int):
    """ 
    DFS (Depth-first search) is our method here, where we recursively traverse 
    out our graph, and save them into the visited list. I have extended the function here to
    check if the working node is already in the visited list and if that list is also the 
    same length as the graph, actually proving that we have, in fact, a perfect cycle ;)
    """
    try:
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                return dfs(visited, graph, neighbour)
        elif node in visited and len(visited) == len(graph):
            return True
    except Exception as e:
        return e

    return False


def is_cyclic(json: dict) -> dict:
    """
    A function that ties everything together and return true if the any graph is cyclic,
    It goes every list, converts it to a graph and check.
    """
    results = {}
    lists = get_lists_from_json(json)
    try:
        for list in lists:
            visited = []
            graph = generate_adjacency_list(json[list])
            firstGraphNode = next(iter(graph))
            results[list] = dfs(visited, graph, firstGraphNode)
    except Exception as e:
        return (e)

    return results
