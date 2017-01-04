"""Shortest path between two nodes in a graph."""

from simple_graph import SimpleGraph
import math


def dijkstra_path(graph, start, end):
    """Shortest path using Dijkstra's algorithm."""
    path_table = {}
    for node in graph.nodes():
        path_table[node] = [None, math.inf]
    node_list = graph.breadth_first_traversal(start)
    for node in node_list:
        for edge in graph.node_dict[node]:
            total_to_node = edge[1] + path_table[node][1]
            if total_to_node < path_table[edge[0]][1]:
                path_table[edge[0]][1] = total_to_node
                path_table[edge[0]][0] = node
    current = end
    total_length = path_table[end][1]
    path_list = [current]
    while current is not start:
        path_list.append(path_table[current][0])
        current = path_table[current][0]
    return "Total length: {{}}, Path: {{}}""".format(total_length, path_list.reverse())
