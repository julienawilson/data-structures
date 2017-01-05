"""Test our implementation of Dijkstra's shortest path algorithim."""


import pytest


@pytest.fixture
def gr():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    return new_graph


# def test_wrong_start(gr):
#     from shortest_path import dijkstra_path
#     gr.add_node('val1')
#     gr.add_node('val2')
#     gr.add_edge('val1', 'val2', 4)
#     with pytest.raises(KeyError):
#         dijkstra_path(gr, 'val3', 'val2')


# def test_wrong_end(gr):
#     from shortest_path import dijkstra_path
#     gr.add_node('val1')
#     gr.add_node('val2')
#     gr.add_edge('val1', 'val2', 4)
#     with pytest.raises(KeyError):
#         dijkstra_path(gr, 'val2', 'val1')


# def test_valid_params(gr):
#     from shortest_path import dijkstra_path
#     gr.add_edge(1, 2, 1)
#     gr.add_edge(1, 3, 3)
#     gr.add_edge(2, 4, 5)
#     gr.add_edge(2, 5, 12)
#     gr.add_edge(3, 6, 2)
#     gr.add_edge(3, 7, 6)
#     simple_tree = dijkstra_path(gr, 1, 4)
#     assert simple_tree == "Total length: 6, Path: [1, 2, 4]"


def test_cycle_graph(gr):
    from shortest_path import dijkstra_path
    gr.add_edge(1, 2, 5)
    gr.add_edge(1, 3, 1)
    gr.add_edge(2, 1, 2)
    gr.add_edge(3, 2, 2)
    gr.add_edge(2, 4, 5)
    gr.add_edge(3, 5, 2)
    gr.add_edge(4, 6, 2)
    gr.add_edge(5, 6, 11)
    cycle_graph = dijkstra_path(gr, 1, 6)
    assert cycle_graph == "Total length: 10, Path: [1, 3, 2, 4, 6]"
