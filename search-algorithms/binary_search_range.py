"""

Count the number of appearances of a value in a list using binary search

"""

def binary_search_range(array, target):
    max_index = len(array)
    lower = 0
    upper = max_index
    
    min_index = False
    max_index = False
    
    # find lower range
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            if ( x > 0 and val > array[x-1] ) or ( x == 0 ):
                min_index = x
                break
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x
    
    
    # find upper range
    # reset the max value and begin search again with same lower value
    upper = max_index
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x
