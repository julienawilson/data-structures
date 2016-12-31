"""Simple Graph Data Structure."""


class SimpleGraph(object):
    """A simple graph class.

    .nodes(): return a list of all nodes in the graph
    .edges(): return a list of all edges in the graph
    .add_node(n): adds a new node ‘n’ to the graph
    .add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’,
        if either n1 or n2 are not already present in the graph, they should
        be added.
    .del_node(n): deletes the node ‘n’ from the graph, raises an error if no
        such node exists
    .del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the
        graph, raises an error if no such edge exists
    .has_node(n): True if node ‘n’ is contained in the graph, False if not.
    .neighbors(n): returns the list of all nodes connected to ‘n’ by edges,
        raises an error if n is not in g
    .adjacent(n1, n2): returns True if there is an edge connecting n1 and n2,
        False if not, raises an error if either of the supplied nodes are not
        in g
    """

    def __init__(self):
        """Initialize the Graph Data Structure."""
        self.node_dict = {}
        self.edges_list = []

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return self.node_dict.keys()

    def edges(self):
        """Return a list of all edges in the graph."""
        return self.edges_list

    def add_node(self, n):
        """Add a new node ‘n’ to the graph."""
        self.node_dict[n] = []

    def add_edge(self, n1, n2):
        """Add a new edge to the graph connecting ‘n1’ and ‘n2’, add 'n1' and 'n2' if necessary."""
        if n1 not in self.node_dict:
            self.add_node(n1)
        if n2 not in self.node_dict:
            self.add_node(n2)
        self.node_dict[n1].append(n2)
        self.edges_list.append((n1, n2))

    def del_node(self, n):
        """Delete the node ‘n’ from the graph, raises an error if no
        such node exists."""
        if n in self.node_dict.keys:
            del self.node_dict[n]
        for key in self.node_dict:
            if n in self.node_dict[key]:
                self.node_dict[key].remove(n)
        for edge in self.edges_list:
            if edge[0] == n or edge[1] == n:
                self.edges_list.remove(edge)

    def del_edge(self, n1, n2):
        """deletes the edge connecting ‘n1’ and ‘n2’ from the
        graph, raises an error if no such edge exists"""

    def has_node(self, n):
        """True if node ‘n’ is contained in the graph, False if not."""

    def neighbors(self, n):
        """returns the list of all nodes connected to ‘n’ by edges,
        raises an error if n is not in g"""

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2,
        False if not, raises an error if either of the supplied nodes are not
        in g"""
