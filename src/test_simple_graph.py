"""Test the Simple Graph functionality."""


import pytest

INPUT_VALUES = [
]


@pytest.fixture
def gr():
    """Simple fixture to save importing SimpleGraph in every test."""
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    return new_graph


def test_init(gr):
    """Test that the class initializes."""
    from simple_graph import SimpleGraph
    assert isinstance(gr, SimpleGraph)


def test_node_dict(gr):
    """Test that an empty class has a node dict."""
    assert isinstance(gr.node_dict, dict)


def test_edge_list(gr):
    """Test that an empty class has an edge list."""
    assert isinstance(gr.edges_list, list)


def test_add_node(gr):
    """Test that add node method works."""
    gr.add_node('value')
    assert 'value' in gr.node_dict


def test_nodes(gr):
    """Test that the graph knows which nodes it contains."""
    gr.add_node('val1')
    gr.add_node('val2')
    assert 'val1' in gr.node_dict and 'val2' in gr.node_dict


def test_number_nodes(gr):
    """Test that the graph has the expected number of nodes."""
    gr.add_node('val1')
    gr.add_node('val2')
    assert sorted(gr.nodes()) == ['val1', 'val2']


def test_add_edge_empty(gr):
    """Test that adding edge to empty graph creates nodes."""
    gr.add_edge('a', 'b')
    assert sorted(gr.nodes()) == ['a', 'b']


def test_add_edge_recorded(gr):
    """Test that adding an edge is properly recorded in a seperate list."""
    gr.add_edge('a', 'b')
    assert gr.edges_list == [('a', 'b')]


def test_add_edge_existing(gr):
    """Test adding an edge to existing nodes."""
    gr.add_node('val1')
    gr.add_node('val2')
    gr.add_edge('val1', 'val2')
    assert gr.node_dict['val1'] == ['val2']


def test_add_edge_existing_recorded(gr):
    """Test adding an edge to existing nodes is recorded sperately."""
    gr.add_node('val1')
    gr.add_node('val2')
    gr.add_edge('val1', 'val2')
    assert gr.edges_list == [('val1', 'val2')]


def test_del_nodes(gr):
    """Test that nodes are deleted."""
    gr.add_node('val1')
    gr.del_node('val1')
    assert 'val1' not in gr.node_dict


def test_del_node_cleanup(gr):
    """Test that edges without endpoints are deleted."""
    gr.add_edge('a', 'b')
    gr.del_node('b')
    assert len(gr.edges_list) == 0


def test_del_edge_list(gr):
    """Test that deleted edges are removed from the edge list."""
    gr.add_edge('a', 'b')
    gr.del_edge('a', 'b')
    assert len(gr.edges_list) == 0


def test_del_edge_dict(gr):
    """Test that deleted edges are remved from the graph dictionary."""
    gr.add_edge('a', 'b')
    gr.del_edge('a', 'b')
    assert 'b' not in gr.node_dict['a']


def test_has_node(gr):
    """Test that has_node() returns true when node exists."""
    gr.add_node('val1')
    assert gr.has_node('val1')


def test_has_node_neg(gr):
    """Test that has_node()returns negative when node doesn't exist."""
    gr.add_node('val1')
    assert not gr.has_node('val2')


def test_empty_has_node_neg(gr):
    """Test that has_node()returns negative on empty graph."""
    assert not gr.has_node('val2')


def test_neighbors_returns_list_of_neighbors(gr):
    """Test that neightbors() returns a list of the nodes neighbors."""
    gr.add_edge('a', 'b')
    gr.add_edge('a', 'c')
    gr.add_edge('a', 'd')
    assert gr.neighbors('a') == ['b', 'c', 'd']


def test_empty_neghbors(gr):
    """Test Neighbors returns empty list when node has no neighbors."""
    gr.add_node('a')
    assert gr.neighbors('a') == []


def test_neghbors_invalid_node(gr):
    """Test Neighbors returns error when node does not exist."""
    with pytest.raises(ValueError):
        gr.neighbors('a')


def test_adjacent_true(gr):
    """Test that adjacent returns true when first node points to second."""
    gr.add_edge('a', 'b')
    assert gr.adjacent('a', 'b')


def test_adjacent_false(gr):
    """Test that adjacent returns false if nodes not connected."""
    gr.add_node('d')
    gr.add_node('e')
    assert not gr.adjacent('d', 'e')


def test_adjacent_invalid_node(gr):
    """Test that adjacent raises ValueError if one node does not exist."""
    gr.add_node('c')
    with pytest.raises(ValueError):
        gr.adjacent('c', 'f')


def test_depth_first_trav(gr):
    """Test that depth first traversal returns proper list."""
    gr.add_edge(1, 2)
    gr.add_edge(1, 3)
    gr.add_edge(2, 4)
    gr.add_edge(2, 5)
    gr.add_edge(3, 6)
    gr.add_edge(3, 7)
    assert gr.depth_first_traversal(1) == [1, 2, 4, 5, 3, 6, 7]


def test_depth_first_trav_irregular(gr):
    """Test that depth first traversal returns proper list with irregular graph."""
    gr.add_edge(1, 2)
    gr.add_edge(1, 3)
    gr.add_edge(2, 4)
    gr.add_edge(2, 5)
    gr.add_edge(3, 6)
    gr.add_edge(3, 7)
    gr.add_edge(4, 3)
    assert gr.depth_first_traversal(1) == [1, 2, 4, 3, 6, 7, 5]


def test_depth_first_trav_error_empty(gr):
    """Test that depth first traversal returns error in empty graph."""
    with pytest.raises(KeyError):
        gr.depth_first_traversal(12)


def test_depth_first_trav_no_head(gr):
    """Test that depth first traversal returns error when head not there."""
    gr.add_edge(1, 2)
    gr.add_edge(1, 3)
    gr.add_edge(2, 4)
    gr.add_edge(2, 5)
    gr.add_edge(3, 6)
    gr.add_edge(3, 7)
    with pytest.raises(KeyError):
        gr.depth_first_traversal(12)


def test_breadth_first_trav(gr):
    """Test that breadth first traversal returns proper list."""
    gr.add_edge(1, 2)
    gr.add_edge(1, 3)
    gr.add_edge(2, 4)
    gr.add_edge(2, 5)
    gr.add_edge(3, 6)
    gr.add_edge(3, 7)
    assert gr.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]


def test_breadth_first_trav_irregular(gr):
    """Test that breadth first traversal returns proper list on irregular graph."""
    gr.add_edge(1, 2)
    gr.add_edge(1, 3)
    gr.add_edge(2, 4)
    gr.add_edge(2, 5)
    gr.add_edge(3, 6)
    gr.add_edge(3, 7)
    gr.add_edge(5, 3)
    assert gr.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]


def test_breadth_first_trav_error_empty(gr):
    """Test that breadth first traversal returns error in empty graph."""
    with pytest.raises(KeyError):
        gr.breadth_first_traversal(12)


def test_breadth_first_trav_no_head(gr):
    """Test that breadth first traversal returns error when head not there."""
    gr.add_edge(1, 2)
    gr.add_edge(1, 3)
    gr.add_edge(2, 4)
    gr.add_edge(2, 5)
    gr.add_edge(3, 6)
    gr.add_edge(3, 7)
    with pytest.raises(KeyError):
        gr.breadth_first_traversal(12)
