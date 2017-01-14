"""Shortest Path using A*."""


def a_star(graph, start, end):
    """Shortest path using Dijkstra's algorithm."""
    path_table = {}
    node_dict = {}
    infinity = float("inf")
    fscore = infinity

    for node in graph.nodes():
        path_table[node] = [None, infinity, fscore]
        node_dict[node] = infinity
    path_table[start][1] = 0  # gscore value
    # fscore value
    path_table[start][2] = heuristic_cost_estimate(start, end)
    # fscore vlaue in open table
    node_dict[start] = heuristic_cost_estimate(start, end)

    while node_dict:

        # get the value for the shortedst distance node
        shortest_dist_node = min(node_dict, key=node_dict.get)
        current_node_val = shortest_dist_node

        if current_node_val == end:
            break
        node_dict.pop(current_node_val)

        # shortest total distance to current node
        current_node_distance = path_table[current_node_val][1]

        # find the shortest weight edge attached to the current node
        for child in graph.neighbors(current_node_val):
            for edge in graph.node_dict[current_node_val]:
                if edge[0] == child:
                    edge_length = edge[1]

            # Test that the next path segment is the shortest total path so far
            trial_distance = current_node_distance + edge_length
            if trial_distance < path_table[child][1]:
                path_table[child][1] = trial_distance
                node_dict[child] = trial_distance + heuristic_cost_estimate(start, end)
                path_table[child][0] = current_node_val
                path_table[child][2] = node_dict[child]

    current = end
    total_length = path_table[end][1]
    path_list = [current]
    while current is not start:
        path_list.append(path_table[current][0])
        current = path_table[current][0]
    return "Total length: {}, Path: {}""".format(total_length, path_list[::-1])


def heuristic_cost_estimate(start, end):
    """Hold problem-specific heuristic."""
    return 1
