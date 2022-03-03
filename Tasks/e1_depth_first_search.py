from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    path_nodes = []
    visited_nodes = {node: False for node in g.nodes}
    wait_nodes = []  # "Горящие" ожидающие узлы
    wait_nodes.append(start_node)
    visited_nodes[start_node] = True
    curr_node = wait_nodes.pop(-1)
    if curr_node:
        dfs(g, start_node)
    for neibhour in g[curr_node]:
        if not visited_nodes[neibhour]:
            wait_nodes.append(neibhour)
            visited_nodes[neibhour] = True
    path_nodes.append(curr_node)

    return path_nodes
