
# Sorting
# ------------------------------------------------ #

# sorting a string 
#(because string.sort() doesn't work... can't sort immutable object)
''.join(sorted(a))
#'ENOVWZ'

# sorting a list
my_list = [2, 1, 3, 5, 4]
sorted(my_list)
# [1, 2, 3, 4, 5]

# sorting a list in-place
my_list.sort()

# sorting by a function
# key will be a modification of x, where our lambda value is some iterator... 
#...like it will evaluate to the items in our list one by one
#(ex. even numbers first)
my_list.sort(key = lambda x: x%2)

# sort by, then by
#(use a tuple to implement a hierarchy of sorts)
#ex. sort by even, then by value
my_list.sort(key = lambda x: (x%2,x))
#and
sorted_list = sorted(my_list, key = lambda x: (x%2,x))



# Input
# ------------------------------------------------ #

# takes in a line of input, converts to a list split on ' '
s = input().split()

# ensures that list consists of integers (uses the fact that list is iterable)
[int(z) for z in input().split()]


# Comparisons
# ------------------------------------------------ #

# check if a list is empty
if not my_list:
    #actionA
    pass
else:
    #actionB
    pass
    
    
# check type (ex. is it a list or a dict)
my_list = [1,2,3]
non_list = {'a':1}
if isinstance(my_list, (list,)):
    ## This code will execute
if isinstance(non_list, (list,)):
    ## This code will NOT execute




# Built-ins
# ------------------------------------------------ #

# enumerate()
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_start_value = 1
for counter, value in enumerate(my_list, counter_start_value):
    print(counter, value)
# Output:
# 1 apple
# 2 banana etc...




# Lists
# ------------------------------------------------ #

# 'mylist.remove(value)' removes the first matching value, not a specific index:
# 'del mylist[index]' removes the item by index

# unpacking
inputter = [[1,2,3],[4,5,6],[7,8,9]]
print(*inputter)
# [1,2,3],[4,5,6],[7,8,9]

# zip() - creates a generator which will return tuples for the item 
[x for x in zip([1,2,3],[4,5,6])]
# [(1, 4), (2, 5), (3, 6)]

# transposing an array as list of lists ( unpacking and zipping )
arr = [[1,2,3],[4,5,6]]
[x for x in zip(*arr)]
# [(1, 4), (2, 5), (3, 6)]
# USEFUL FOR ITERATING OVER COLUMNS OF AN ARRAY
# ex. 
for row in arr:
    <do something with that row>
for col in zip(*arr):
    <do something with that column>
