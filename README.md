<<<<<<< HEAD
[![Build Status](https://travis-ci.org/julienawilson/data-structures.svg?branch=master)](https://travis-ci.org/julienawilson/data-structures)

# Data Structures
=======
[![Build Status](https://travis-ci.org/julienawilson/data-structures.svg?branch=bst)](https://travis-ci.org/julienawilson/data-structures)

# data-structures
>>>>>>> 2f8af436a8271e1a77876030b065993c23274041
Patrick Saunders and Julien Wilson
<br>
Data Structures created in Python401

##Simple Graph
A directional weighted graph that supports breadth and depth first traversals.

##Binary heap:
binheap.py provides a binary heap class with push() and pop() methods.
both push() and pop() rely on a hidden _sort() method to keep the heap
properly structured.

##Priority Queue
Priority Queue: ordered by priority value and order of entry in to Queue.

##Deque
Double Ended Queue

##Doubly Linked List
A linked list that points in both directions

##Binary Search Tree
A tree of nodes sorted by values less than and greater than root branching to the left and right, respectively.

Methods include:
* insert(self, val): Insert value into tree; if value already exists, ignore it. Method autobalances after insertion, and tree size increments by one.
* search(self, val): Return node containing that value, else None.
* size(self): Return number of nodes/vertices in tree, 0 if empty.
* depth(self): Return number of levels in tree. Tree with one value has depth of 0.
* contains(self, val): Return True if value is in tree, False if not.
* balance(self): Return a positive or negative integer representing tree's balance.
    Trees that are higher on the left than the right should return a positive value;
    trees that are higher on the right than the left should return a negative value;
    an ideally-balanced tree should return 0.
* in_order(self): Return a generator that returns each node value from in-order traversal.
* pre_order(self): Return a generator that returns each node value from pre-order traversal.
* post_order(self): Return a generator that returns each node value from post_order traversal.
* breadth_first(self): Return a generator returns each node value from breadth-first traversal.
* delete(value): Delete a node's connections (edges), effectively deleting node. Method autobalances after deletion, and tree size decrements by one.



