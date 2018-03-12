"""
Count the number of appearances of a value in a list using binary search
"""

def binary_search_range(array, target):
    array_max_index = len(array) - 1
    lower_index = 0
    upper_index = array_max_index
    
    found_min = False
    found_max = False
    min_index = False
    max_index = False
    
    print("finding min index")
    
    # find value min index
    while lower_index <= upper_index:
        mid_index = lower_index + ( upper_index - lower_index ) //2
        value = array[mid_index]
        
        if value == target:
            if (mid_index > 0 and array[mid_index - 1] < value) or (mid_index == 0):
                min_index = mid_index
                found_min = True
                break
            else:
                upper_index = mid_index - 1
        elif value < target:
            lower_index = mid_index + 1
        else:
            upper_index = mid_index - 1
            
    print('min index is', min_index,'!')
            
    print("finding max index")
    # find value max index
    upper_index = array_max_index
    while lower_index <= upper_index:
        mid_index = lower_index + ( upper_index - lower_index ) //2
        value = array[mid_index]
        
        if value == target:
            if (mid_index < array_max_index and array[mid_index + 1] > value) or (mid_index == array_max_index):
                max_index = mid_index
                found_max = True
                break
            else:
                lower_index = mid_index + 1
        elif value < target:
            lower_index = mid_index + 1
        else:
            upper_index = mid_index - 1
            
    
    
    print('max index is', max_index,'!')
        
        
    if found_min and found_max:
        return (max_index - min_index + 1)
    else:
        return False
