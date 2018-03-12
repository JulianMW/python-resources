"""

Count the number of appearances of a value in a list using binary search

"""

def binary_search_range(array, target):
    array_max_index = len(array) -1
    lower = 0
    upper = array_max_index
    
    min_index = False
    max_index = False
    
    print("finding min index")
    
    # find lower range
    while lower < upper:
        x = lower + (upper - lower) // 2
        print(x)
        val = array[x]
        if target == val:
            if ( x > 0 and val > array[x-1] ) or ( x == 0 ):
                min_index = x
                break
            else:
                upper = x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif ( target < val):
            upper = x
            
    print('min index is', min_index,'!')
    
    print("finding max index")
    
    # find upper range
    # reset the max value and begin search again with same lower value
    upper = array_max_index
    while lower < upper:
        x = lower + (upper - lower) // 2
        print(x)
        val = array[x]
        if target == val:
            if ( x < array_max_index and val < array[x+1] ) or ( x == array_max_index ):
                max_index = x
                break
            else:
                lower = x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x
            
    print('max index is', max_index,'!')
        
        
    if min_index and not max_index:
        max_index == min_index
        return (max_index - min_index + 1)
    elif min_index and max_index:
        return (max_index - min_index + 1)
    else:
        return False
