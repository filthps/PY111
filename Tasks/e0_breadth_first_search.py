from typing import Hashable, List
import networkx as nx
from collections import deque


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Поиск в ширину (горизонтально)
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    path_nodes = []
    visited_nodes = {node: False for node in g.nodes}
    wait_nodes = deque()  # "Горящие" ожидающие узлы
    wait_nodes.append(start_node)
    visited_nodes[start_node] = True
    while wait_nodes:
        curr_node = wait_nodes.popleft()
        for neibhour in g[curr_node]:
            if not visited_nodes[neibhour]:
                wait_nodes.append(neibhour)
                visited_nodes[neibhour] = True
        path_nodes.append(curr_node)

    return path_nodes

