#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""Simple Graph Data Structure."""
from queue import Queue


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

    def add_edge(self, n1, n2, weight=1):
        """Add a new edge to the graph connecting ‘n1’ and ‘n2’, add 'n1' and 'n2' if necessary."""
        if n1 not in self.node_dict:
            self.add_node(n1)
        if n2 not in self.node_dict:
            self.add_node(n2)
        self.node_dict[n1].append((n2, weight))
        self.edges_list.append((n1, n2, weight))

    def del_node(self, n):
        """Delete the node ‘n’ from the graph, raises an error if no
        such node exists."""
        if n in self.node_dict.keys():
            del self.node_dict[n]
        for key in self.node_dict:
            for edge in self.node_dict[key]:
                if edge[0] == n:
                    self.node_dict[key].remove(edge)
        for edge in self.edges_list:
            if edge[0] == n or edge[1] == n:
                self.edges_list.remove(edge)

    def del_edge(self, n1, n2):
        """Delete the edge connecting ‘n1’ and ‘n2’ from the
        graph, raises an error if no such edge exists"""
        for edge in self.edges_list:
            if edge[0] == n1 and edge[1] == n2:
                self.edges_list.remove(edge)
                break
        else:
            raise ValueError('This edge does not exist.')
        if n1 in self.node_dict.keys():
            for edge in self.node_dict[n1]:
                if edge[0] == n2:
                    self.node_dict[n1].remove(edge)

    def has_node(self, n):
        """True if node ‘n’ is contained in the graph, False if not."""
        return n in self.node_dict.keys()

    def neighbors(self, n):
        """Return the list of all nodes connected to ‘n’ by edges,
        raises an error if n is not in g."""
        if n not in self.node_dict.keys():
            raise ValueError('You have chosen a node which does not exist')
        return [edge[0] for edge in self.node_dict[n]]

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 and n2,
        False if not, raises an error if either of the supplied nodes are not
        in g."""
        if n1 not in self.node_dict.keys() or n2 not in self.node_dict.keys():
            raise ValueError('You have chosen a node which does not exist')
        return n2 in [edge[0] for edge in self.node_dict[n1]]

    def depth_first_traversal(self, start):
        """Perform a depth first traversal from start."""
        try:
            trav_list = [start]
            path = []
            while trav_list:
                head = trav_list.pop()
                if head not in path:
                    path.append(head)
                    trav_list.extend([edge[0] for edge in self.node_dict[head]][::-1])
            return path
        except KeyError:
            raise KeyError('That node does not exist')

    def breadth_first_traversal(self, start):
        """Perform a breadth first graph traversal, return the path."""
        try:
            trav_list = Queue([start])  # make this a queue
            path = []
            while trav_list.peek():
                head = trav_list.dequeue()  # check this method name
                if head not in path:
                    path.append(head)
                    for item in [edge[0] for edge in self.node_dict[head]]:
                        trav_list.enqueue(item)
            return path
        except IndexError:
            raise KeyError('That node does not exist')


if __name__ == "__main__":

    import timeit

    def build_graph():
        """Build a randomly created graph to test."""
        import random
        test_graph = SimpleGraph()
        for i in range(100):
            test_graph.add_edge(random.randint(1, 50), random.randint(1, 50))
        return test_graph
    g = build_graph()

    print(timeit.repeat(stmt='g.depth_first_traversal(random.choice(list(g.node_dict.keys())))',
                        setup='from __main__ import SimpleGraph, g, random', repeat=3,
                        number=1000
                        )
          )

    print(timeit.repeat(stmt='g.breadth_first_traversal(random.choice(list(g.node_dict.keys())))',
                        setup='from __main__ import SimpleGraph, g, random', repeat=3,
                        number=1000
                        )
          )
