[![Build Status](https://travis-ci.org/julienawilson/data-structures.svg?branch=master)](https://travis-ci.org/julienawilson/data-structures)

# Data Structures
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
* insert(self, val): Insert value into tree; if value already exists, ignore it.
* search(self, val): Return node containing that value, else None.
* size(self): Return number of nodes/vertices in tree, 0 if empty.
* depth(self): Return number of levels in tree. Tree with one value has depth of 0.
* contains(self, val): Return True if value is in tree, False if not.
* balance(self): Return a positive or negative integer representing tree's balance.
    Trees that are higher on the left than the right should return a positive value;
    trees that are higher on the right than the left should return a negative value;
    an ideally-balanced tree should return 0.
