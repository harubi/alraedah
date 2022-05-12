from typing import *


def get_lists_from_json(json: Iterable[dict]) -> list:
    # BAD! We should iterate over json objects, never load them all info memory, we should leverage generator iterators and yield expressions here.
    try:
        return list(json)
    except Exception as e:
        return e


def generate_adjacency_list(nodes: Iterable[list]) -> dict:
    """
    A function to generate a linked-list representing a graph adjacency list from an array.
    For every item in the list, we add to the graph the node as a key,
    and we add an array as a value containing the node (aka edge) pointed at.
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


def dfs(graph: Iterable[dict], starting_node: int):
    """
    DFS (Depth-first search) is our method here, where we iteratively traverse
    out our graph, and save them into the visited list. I have extended the functionality here to
    check if the working node is already in the visited list and if that list is also the
    same length as the graph, actually proving that we have, in fact, a perfect cycle ;)
    """
    try:
        visited, stack = [], [starting_node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                # add all unexplored, adjacent nodes to stack by using the list.extend method
                stack.extend(set(graph[node]) - set(visited))
        if len(visited) == len(graph) and visited[-1] == visited[starting_node]:
            return True
    except Exception as e:
        return e

    return False


def is_cyclic(json: Iterable[dict]) -> dict:
    """
    A function that ties everything together.
    """
    results, lists = {}, get_lists_from_json(json)
    try:
        for list in lists:
            graph = generate_adjacency_list(json[list])
            first_graph_node = next(iter(graph))
            results[list] = dfs(graph, first_graph_node)
    except Exception as e:
        return e

    return results
