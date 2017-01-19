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
    """Test that inserting existing number doesn't change size."""
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


def test_contains_with_nonexistent_val_gt_root(small_tree):
    """Test contains returns False when value is greater than root but node nonexistent."""
    assert small_tree.contains(99) is False


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

def test_balance_w_no_left_nodes():
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    b_tree.insert(43)
    assert b_tree.balance() == 1


def test_inorder_no_nodes():
    """Test in-order traversal on empty tree returns empty path."""
    b_tree = BinarySearchTree()
    inorder_list = []
    for node in b_tree.in_order():
        inorder_list.append(node.value)
    assert inorder_list == []


def test_inorder_single_node_treee():
    """Test in-order traversal on single-node tree returns that one node."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    inorder_list = []
    for node in b_tree.in_order():
        inorder_list.append(node.value)
    assert inorder_list == [17]


def test_inorder_small_tree(small_tree):
    """Test that inorder works on small tree."""
    inorder_list = []
    for node in small_tree.in_order():
        inorder_list.append(node.value)
    assert inorder_list == [35, 40, 50, 60, 80, 90]


def test_inorder_weird_tree(weird_tree):
    """Test that inorder works on weird tree."""
    inorder_list = []
    for node in weird_tree.in_order():
        inorder_list.append(node.value)
    assert inorder_list == [2, 44, 48, 49, 50, 79, 80, 83, 90, 100, 102, 103]


def test_preorder_no_nodes():
    """Test pre-order traversal on empty tree returns empty path."""
    b_tree = BinarySearchTree()
    preorder_list = []
    for node in b_tree.in_order():
        preorder_list.append(node.value)
    assert preorder_list == []


def test_preorder_single_node_tree():
    """Test pre-order traversal on single-node tree returns that one node."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    preorder_list = []
    for node in b_tree.in_order():
        preorder_list.append(node.value)
    assert preorder_list == [17]


def test_preorder_small_tree(small_tree):
    """Test that preorder works on small tree."""
    preorder_list = []
    for node in small_tree.pre_order():
        preorder_list.append(node.value)
    assert preorder_list == [50, 40, 35, 80, 60, 90]


def test_preorder_weird_tree(weird_tree):
    """Test that preorder works on weird tree."""
    preorder_list = []
    for node in weird_tree.pre_order():
        preorder_list.append(node.value)
    assert preorder_list == [50, 44, 2, 48, 49, 79, 80, 83, 90, 100, 103, 102]


def test_postorder_no_nodes():
    """Test post-order traversal on empty tree returns empty path."""
    b_tree = BinarySearchTree()
    postorder_list = []
    for node in b_tree.in_order():
        postorder_list.append(node.value)
    assert postorder_list == []


def test_postorder_single_node_tree():
    """Test post-order traversal on single-node tree returns that one node."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    postorder_list = []
    for node in b_tree.in_order():
        postorder_list.append(node.value)
    assert postorder_list == [17]


def test_postorder_small_tree(small_tree):
    """Test that post-order traversal of small tree returns expected path."""
    postorder_list = []
    for node in small_tree.post_order():
        postorder_list.append(node.value)
    assert postorder_list == [35, 40, 60, 90, 80, 50]


def test_postorder_weird_tree(weird_tree):
    """Test that post-order traversal of weird tree returns expected path."""
    postorder_list = []
    for node in weird_tree.post_order():
        postorder_list.append(node.value)
    assert postorder_list == [2, 49, 48, 44, 102, 103, 100, 90, 83, 80, 79, 50]


def test_bfs_on_bst_no_nodes():
    """Test breadth-first-search traversal on empty tree returns empty path."""
    b_tree = BinarySearchTree()
    bfs_list = []
    for node in b_tree.breadth_first():
        bfs_list.append(node.value)
    assert bfs_list == []


def test_bfs_on_single_node_bst():
    """Test breadth-first-search traversal on one-node tree returns node."""
    b_tree = BinarySearchTree()
    b_tree.insert(17)
    bfs_list = []
    for node in b_tree.breadth_first():
        bfs_list.append(node.value)
    assert bfs_list == [17]


def test_bfs_small_tree(small_tree):
    """Test breadth-first-search traversal returns expected path."""
    bfs_list = []
    for node in small_tree.breadth_first():
        bfs_list.append(node.value)
    assert bfs_list == [50, 40, 80, 35, 60, 90]


def test_bfs_weird_tree(weird_tree):
    """Test that breadth-first-search traversal returns expected path."""
    bfs_list = []
    for node in weird_tree.breadth_first():
        bfs_list.append(node.value)
    assert bfs_list == [50, 44, 79, 2, 48, 80, 49, 83, 90, 100, 103, 102]


def test_delete_node_with_no_children(small_tree):
    """Test calling delete on node with no children."""
    small_tree.delete(35)
    assert small_tree.search(35) == None


def test_delete_node_with_no_children_update_size(small_tree):
    """Test calling delete on node with no children."""
    small_tree.delete(35)
    assert small_tree.size() == 5


def test_delete_node_with_no_children_annuls_parent_connection(small_tree):
    """Test calling delete on node with no children kills parent's connection."""
    small_tree.delete(35)
    assert small_tree.search(40).left is None
    with pytest.raises(AttributeError):
        assert small_tree.search(35).parent


def test_delete_node_with_no_children_annuls_own_connection(small_tree):
    """Test calling delete on node with no children kills parent's connection."""
    small_tree.delete(35)
    with pytest.raises(AttributeError):
        assert small_tree.search(35).parent


def test_delete_node_with_one_child_reassigns_connections(small_tree):
    """Test deleting a node reassigns its one child to expected new parent."""
    small_tree.delete(40)
    assert small_tree.search(35).parent.value == 50
    assert small_tree.search(50).left.value == 35



def test_delete_node_annuls_own_connections(small_tree):
    """Test calling delete on node kills parent and child connections."""
    small_tree.delete(40)
    with pytest.raises(AttributeError):
        assert small_tree.search(40).parent is None
    with pytest.raises(AttributeError):
        assert small_tree.search(40).left is None


def test_delete_updates_size(small_tree):
    """Test that deleting a node updates tree's size."""
    small_tree.delete(40)
    assert small_tree.size() ==  5


def test_delete_node_with_two_childs_updates_size(small_tree):
    """Test that delete node with two childs updates size."""
    small_tree.delete(80)
    assert small_tree.size() == 5


def test_rotate_left_small_tree_assign_child(small_tree):
    """Test that left rotation  on small tree reassigns children."""
    small_tree.rotate_left(small_tree.root)
    assert small_tree.search(80).left.value == 50


def test_rotate_left_small_tree_assign_parent(small_tree):
    """Test that left rotation  on small tree reassigns parent."""
    small_tree.rotate_left(small_tree.root)
    assert small_tree.search(50).parent.value == 80


def test_rotate_left_reassigns_root(small_tree):
    """Test the left rotation reassigns root."""
    small_tree.rotate_left(small_tree.root)
    assert small_tree.root.value == 80


def test_rotate_left_doesnt_reassign_root(small_tree):
    """Test the left rotation does not reassign root."""
    small_tree.rotate_left(small_tree.search(80))
    assert small_tree.root.value == 50


def test_rotate_left_small_tree_assign_parent_not_root(small_tree):
    """Test that left rotation  on small tree reassigns children."""
    small_tree.rotate_left(small_tree.search(80))
    assert small_tree.search(80).parent.value == 90


def test_rotate_left_small_tree_assign_child_not_root(small_tree):
    """Test that left rotation  on small tree reassigns children."""
    small_tree.rotate_left(small_tree.search(80))
    assert small_tree.search(80).right is None


def test_rotate_right_small_tree_assign_child(small_tree):
    """Test that right rotation  on small tree reassigns children."""
    small_tree.rotate_right(small_tree.root)
    assert small_tree.search(40).right.value == 50


def test_rotate_right_small_tree_assign_parent(small_tree):
    """Test that right rotation  on small tree reassigns parent."""
    small_tree.rotate_right(small_tree.root)
    assert small_tree.search(50).parent.value == 40


def test_rotate_right_small_tree_assign_parent_not_root(small_tree):
    """Test that right rotation  on small tree reassigns children."""
    small_tree.rotate_right(small_tree.search(40))
    assert small_tree.search(40).parent.value == 35


def test_rotate_right_small_tree_assign_child_not_root(small_tree):
    """Test that right rotation  on small tree reassigns children."""
    small_tree.rotate_right(small_tree.search(40))
    assert small_tree.search(40).left is None


def test_rotate_right_small_tree_assign_parent_child_not_root(small_tree):
    """Test that right rotation  on small tree reassigns children."""
    small_tree.rotate_right(small_tree.search(40))
    import pdb; pdb.set_trace()  # deleting 35 but no rotating anything 
    assert small_tree.search(50).left.value == 35


def test_rotate_right_small_tree_assign_right_child_not_root(small_tree):
    """Test that right rotation  on small tree reassigns children."""
    small_tree.rotate_right(small_tree.search(40))
    import pdb; pdb.set_trace()  #  deleting 35 but no rotating anything 
    assert small_tree.search(35).right is None
