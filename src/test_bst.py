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

@pytest.fixture()
def weird_tree():
    """Grow a small tree with five nodes."""
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(79)
    tree.insert(80)
    tree.insert(83)
    tree.insert(90)
    tree.insert(100)
    tree.insert(44)
    tree.insert(48)
    tree.insert(49)
    tree.insert(103)
    tree.insert(2)
    tree.insert(102)
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
    assert b_tree._size == 0


def test_insert_in_empty_tree_establishes_root():
    """Test inserting to empty BST assigns value as root."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    assert b_tree.root.value == 17


def test_insert_in_empty_tree_updates_size():
    """Test that insert on empty tree increments size."""
    b_tree = BinarySearchTree()
    b_tree.insert(43)
    assert b_tree._size == 1


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
    assert small_tree._size == 7


def test_insert_to_small_tree_existing_num(small_tree):
    """Test that inserting existing number on small tree doesn't change size."""
    small_tree.insert(40)
    assert small_tree.size() == 6


def test_search_on_root_value():
    """Test that searching for root value returns root."""
    b_tree = BinarySearchTree()
    b_tree.insert(43)
    assert b_tree.search(43).value == b_tree.root.value


def test_search_for_nonexistent_value(small_tree):
    """Test that search for value not in tree returns None."""
    assert small_tree.search(101) is None


def test_search_for_something_deep_in_the_tree(small_tree):
    """Test searching for a node value at bottom of tree."""
    assert small_tree.search(90).value == 90


def test_search_for_a_node_value_on_left(small_tree):
    """Test searching for a node value at bottom of tree."""
    assert small_tree.search(35).value == 35


def test_size_on_empty():
    """Test sizze method on empty tree returns 0."""
    b_tree = BinarySearchTree()
    assert b_tree.size() == 0


def test_size_on_populated_tree(small_tree):
    """Test the size on a populated tree."""
    assert small_tree.size() == 6


def test_contains_empty_tree():
    """Test that .contains() returns false on empty tree."""
    tree = BinarySearchTree()
    assert tree.contains(4) is False


def test_contains_true_small_tree(small_tree):
    """Test that small tree contains a node."""
    assert small_tree.contains(80) is True


def test_contains_true_small_tree_root(small_tree):
    """Test that small tree contains a node."""
    assert small_tree.contains(50) is True


def test_contains_false_small_tree(small_tree):
    """Test that small tree contains a node."""
    assert small_tree.contains(30) is False


def test_contains_true_weird_tree(weird_tree):
    """Test that small tree contains a node."""
    assert weird_tree.contains(103) is True


def test_contains_true_weird_tree_root(weird_tree):
    """Test that small tree contains a node."""
    assert weird_tree.contains(50) is True


def test_depth_on_small_tree(small_tree):
    """Test the size on a small Tree."""
    assert small_tree.depth() == 2


def test_depth_on_weird_tree(weird_tree):
    """Test the depth on a weird tree."""
    assert weird_tree.depth() == 7


def test_balance_on_small_tree(small_tree):
    """Test balance of smal tree fixture."""
    assert small_tree.balance() == 0


def test_balance_on_weird_tree(weird_tree):
    """Test balance of smal tree fixture."""
    assert weird_tree.balance() == 4


def test_inorder_small_tree(small_tree):
    """Test that inorder works on small tree."""
    inorder_list = []
    for x in small_tree.in_order():
        inorder_list.append(x.value)
    assert inorder_list == [35, 40, 50, 60, 80, 90]


def test_inorder_weird_tree(weird_tree):
    """Test that inorder works on weird tree."""
    inorder_list = []
    for x in weird_tree.in_order():
        inorder_list.append(x.value)
    assert inorder_list == [2, 44, 48, 49, 50, 79, 80, 83, 90, 100, 102, 103]
