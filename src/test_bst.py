"""Tests for the Binary Search Tree."""

import pytest
from bst import Node
from bst import BinarySearchTree


def test_node_creation():
    """Test that instantiating new node creates instance."""
    a_node = Node(4)
    assert a_node


def test_new_node_val():
    """Test that new node has the correct value."""
    a_node = Node(67)
    assert a_node.value == 67


def test_default_node_no_children():
    """Test that a default node has no children."""
    a_node = Node(5)
    assert a_node.left is None
    assert a_node.right is None


def test_new_node_left_val():
    """Test the a node left value points to a node, if assigned."""
    a_node = Node(45)
    other_node = Node(67, left=a_node)
    assert other_node.left == a_node


def test_new_node_right_val():
    """Test the a node right value points to a node, if assigned."""
    a_node = Node(45)
    other_node = Node(4, right=a_node)
    assert other_node.right == a_node


def test_new_tree_has_no_root():
    """Test new binary search tree is empty."""
    b_tree = BinarySearchTree()
    assert  b_tree.size == 0


def test_insert_in_empty_tree_establishes_root():
    """Test inserting to empty BST assigns value as root."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    assert b_tree.root == 17


def test_insert_