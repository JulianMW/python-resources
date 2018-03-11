# Cheatsheet and Implementation of Various Sorting Algos

### Bubble Sort
O(n**2)

Iterate through all sequential items repeatedly. Swap if first is larger than second.


### Selection Sort
O(n**2), but typically faster than bubble

Iterate through n times, and place the largest (/next largest etc..) item in it's correct spot


### Insertion Sort
O(n**2)

Makes one pass through data, inserting each item into it's correct spot in a growing sublist seeded from value at position 0


### Shell Sort
Between O(n) and O(n**2)

Calls the insertion sort repeatedly on sub-lists created by selecting every n'th item. Then combines all these and does a final insertion sort


### Merge Sort
O(n log n)

Splits the list into halves recursively until only one item per leaf. Then merges them upwards, incrementing through each sorted list pair to generate a new sorted list.
Requires extra storage.


### Quick Sort
Between O(n log n) and O(n**2)

Uses a pivot value. Any pair after the pivot value where one is greater and the other smaller will be switched. When the left and right marks cross, thats where the pivot value is placed. The list is divided in two at this point and quicksort is recursively called on those two sublists.


### Radix Sort
O(d*(n+b)), 
where d is the max # digits in input integers
and b is the base for representing numbers (ex. for decimal b=10)

Uses a pivot value. Any pair after the pivot value where one is greater and the other smaller will be switched. When the left and right marks cross, thats where the pivot value is placed. The list is divided in two at this point and quicksort is recursively called on those two sublists.
