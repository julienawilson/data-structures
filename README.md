[![Build Status](https://travis-ci.org/julienawilson/data-structures.svg?branch=bst)](https://travis-ci.org/julienawilson/data-structures)

# data-structures
Patrick Saunders and Julien Wilson
<br>
Data Structures created in Python401

##Simple Graph
A directional unweighted graph that supports breadth and depth first traversals.

##Binary heap:
binheap.py provides a binary heap class with push() and pop() methods.
both push() and pop() rely on a hidden _sort() method to keep the heap
properly structured.

##Deque
Double Ended Queue

##Doubly Linked List
A linked list that points in both directions

##Binary Search Tree
A tree of nodes sorted by values less than and greater than root branching to the left and right, respectively.

Methods include:
* insert(self, val): Insert value into tree; if value already exists, ignore it.
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

