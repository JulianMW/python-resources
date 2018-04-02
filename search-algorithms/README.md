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

### DFS
#### DFS for Binary Tree
Pre-order, in-order and post-order traversal

### BFS for Binary Tree
Pre-order, in-order and post-order traversal

#### DFS for Graph
Similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array. 

### Dijkstra's
Dijkstra's algorithm finds shortest paths from source to all vertices in the given graph



## Searchable Structures

### Binary Search
##### Data requirements:
Sorted
