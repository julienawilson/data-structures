"""Tests for the Binary Search Tree."""

import pytest
from bst import Node
from bst import BinarySearchTree

@pytest.fixture()
def small_tree():
    """Grow a small tree with five nodes."""
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(40)
    tree.insert(80)
    tree.insert(35)
    tree.insert(60)
    tree.insert(90)
    return tree

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
    assert b_tree.size == 0


def test_insert_in_empty_tree_establishes_root():
    """Test inserting to empty BST assigns value as root."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    assert b_tree.root.value == 17


def test_insert_in_empty_tree_updates_size():
    """Test that insert on empty tree increments size."""
    b_tree = BinarySearchTree()
    b_tree.insert(43)
    assert b_tree.size == 1


def test_inserting_lower_val_pushes_left():
    """Test that inserting lower value creates left branch."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    b_tree.insert(10)
    assert b_tree.root.left.value == 10


def test_inserting_higher_val_pushes_right():
    """Test that inserting higher value creates right branch."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    b_tree.insert(20)
    assert b_tree.root.right.value == 20

def test_inserting_less_but_more_into_populated_tree(small_tree):
    """Test inserting lower value that would push left then right."""
    small_tree.insert(43)
    assert small_tree.root.left.right.value == 43


def test_inserting_lower_item_into_populated_tree(small_tree):
    """Test inserting value that pushes all the way left."""
    small_tree.insert(33)
    assert small_tree.root.left.left.left.value == 33


def test_insert_to_small_tree_updates_size(small_tree):
    """Test that insert on small tree increments size."""
    small_tree.insert(43)
    assert small_tree.size == 7
