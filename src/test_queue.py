"""Tests for queue.py."""

import pytest


@pytest.fixture
def sample_queue():
    """Create testing queue."""
    from queue import Queue
    new_queue = Queue([1, 2, 3, 4, 5])
    return new_queue


@pytest.fixture
def single_queue():
    """Create testing queues."""
    from queue import Queue
    one_queue = Queue(["one"])
    return one_queue


@pytest.fixture
def empty_queue():
    """Create testing queues."""
    from queue import Queue
    empty_queue = Queue()
    return empty_queue


def test_queue_empty_head_init(empty_queue):
    """Test for empty head after queue init."""
    assert empty_queue.dll.head_node is None


def test_queue_empty_tail_init(empty_queue):
    """Test for empty tail after queue init."""    
    assert empty_queue.dll.tail_node is None


def test_queue_one_head_init(single_queue):
    """Test for head on one item queue init."""
    assert single_queue.dll.head_node.contents == "one"


def test_queue_one_tail_init(single_queue):
    """Test for tail on one item queue init."""
    assert single_queue.dll.tail_node.contents == "one"


def test_queue_init_head(sample_queue):
    """Test for head on new queue init."""
    assert sample_queue.dll.head_node.contents == 5


def test_queue_init_tail(sample_queue):
    """Test for tail on new queue init."""
    assert sample_queue.dll.tail_node.contents == 1


def test_queue_enqueue(sample_queue):
    """Test for enqueue on new queue."""
    sample_queue.enqueue("hey")
    assert sample_queue.dll.head_node.contents == "hey"


def test_queue_enqueue_on_empty(empty_queue):
    """Test for enqueue on empty queue."""
    empty_queue.enqueue("hey")
    assert empty_queue.dll.head_node.contents == "hey"


def test_queue_dequeue(sample_queue):
    """Test for dequeue on new queue."""
    assert sample_queue.dequeue() == 1


def test_queue_multiple_dequeue(sample_queue):
    """Test for multiple dequeue on new queue."""
    sample_queue.dequeue()
    sample_queue.dequeue()
    assert sample_queue.dequeue() == 3


def test_queue_dequeue_on_empty(empty_queue):
    """Test for dequeue on empty queue."""
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_queue_one_dequeue(single_queue):
    """Test dequeue when queue has one item."""
    assert single_queue.dequeue() == "one"


def test_head_queue_one_dequeue(single_queue):
    """Test head after dequeue when queue has one item."""
    single_queue.dequeue()
    assert single_queue.dll.head_node is None


def test_tail_queue_one_dequeue(single_queue):
    """Test tail after dequeue when queue has one item."""
    single_queue.dequeue()
    assert single_queue.dll.tail_node is None


def test_queue_peek(sample_queue):
    """Test peek on new queue."""
    assert sample_queue.peek() == 1


def test_one_queue_peek(single_queue):
    """Test peek on queue with one item."""
    assert single_queue.peek() == "one"


def test_empty_queue_peek(empty_queue):
    """Test peek on empty queue."""
    assert empty_queue.peek() is None


def test_one_queue_size(single_queue):
    """Test size on queue with one item."""
    assert single_queue.size() == 1


def test_empty_queue_size(empty_queue):
    """Test size on empty queue."""
    assert empty_queue.size() == 0


def test_new_queue_size(sample_queue):
    """Test peek on new queue."""
    assert sample_queue.size() == 5
