"""Shortest path between two nodes in a graph."""

import math


def dijkstra_path(graph, start, end):
    """Shortest path using Dijkstra's algorithm."""
    path_table = {}
    node_dict = {}
    # try:
    #     infinity = math.inf
    # except:
    infinity = float("inf")
    for node in graph.nodes():
        path_table[node] = [None, infinity]
        node_dict[node] = infinity
    path_table[start][1] = 0
    node_dict[start] = 0
    while node_dict:
        shortest_dist_node = min(node_dict, key=node_dict.get)
        current_node_val = shortest_dist_node
        if current_node_val == end:
            break
        node_dict.pop(current_node_val)

        for child in graph.neighbors(current_node_val):

            current_node_distance = path_table[current_node_val][1]
            for edge in graph.node_dict[current_node_val]:
                if edge[0] == child:
                    edge_length = edge[1]
            trial_distance = current_node_distance + edge_length
            if trial_distance < path_table[child][1]:
                path_table[child][1] = trial_distance
                node_dict[child] = trial_distance
                path_table[child][0] = current_node_val
    current = end
    total_length = path_table[end][1]
    path_list = [current]
    while current is not start:
        path_list.append(path_table[current][0])
        current = path_table[current][0]
    return "Total length: {}, Path: {}""".format(total_length, path_list[::-1])
