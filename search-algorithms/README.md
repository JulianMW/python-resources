# A library of searching algorithms
include: big-O (min, average, max), resources/memory needed, data format requirements (ex. sorted, integer etc...)

## List Search Algorithms
### Sequential Search
Loop through entire sequence. Performance:

| Best | Worst | Average |
| ---- | ----- | ------- |
| O(1) | O(n) | O(n/2) |


### Binary Search

Requires that list is sorted. Compares item. Performance:

| Best | Worst | Average |
| ---- | ----- | ------- |
| O(1) | O(log n) | ? |



## BFS, DFS, Dijkstra's

### DFS for Binary Tree
.   A

.  / \

. B   C

where A := +

#### Pre-order:    Self, Left, Right

1. Process Node itself

2. Recursively call self on Left node

3. Recursively call self on Right node

##### This will: Hug Left, climbing down the tree

##### Use When: 
Duplicating nodes and values, making a complete duplicate of a binary tree. Or checking if trees are duplicates. Or creating a parse tree (B + C)

#### In-order:    Left, Self, Right

1. Recursively call self on Left node

2. Process Node itself

3. Recursively call self on Right node

##### This will: Hug Left, climbing up the tree

##### Use When: 
Need to return values from the underlying set in order, according to the comparator that set up the binary search tree

#### Post-order:    Left, Right, Self

1. Recursively call self on Left node

2. Recursively call self on Right node

3. Process Node itself

##### This will: Hug bottom of tree first

##### Use When: 
Deleting or freeing nodes and values; can delete or free an entire binary tree. Or creating a reverse parse notation (B C +)


### BFS for Binary Tree

1. Process Node itself

2. Add Left then Right nodes to a queue

3. Call the next node in the queue


#### DFS for Graph
Similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array. 

### Dijkstra's
Dijkstra's algorithm finds shortest paths from source to all vertices in the given graph



## Searchable Structures

### Binary Search
##### Data requirements:
Sorted
