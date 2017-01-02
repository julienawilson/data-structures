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
