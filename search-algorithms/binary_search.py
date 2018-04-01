# Recursive implementation
def recursive_binary_search(input_list, l, r, target):
    if not input_list:
        raise RuntimeError("List is empty")
    
    if l <= r:
        
        midpoint = l + (r - l)//2
        
        if input_list[midpoint] == target:
            return midpoint
        
        if input_list[midpoint] < target:
            print('a ', str(midpoint), ' l-',str(l),' r-',str(r))
            return recursive_binary_search(input_list, midpoint + 1, r, target)
        elif input_list[midpoint] > target:
            print('b ', str(midpoint), ' l-',str(l),' r-',str(r))
            return recursive_binary_search(input_list, l, midpoint - 1, target)
        
    else:
        return -1
    
print(recursive_binary_search(to_sort, 0, len(to_sort) - 1, 8))


# Loop implementation
def BinarySearch(array, target):
    lower_index = 0
    upper_index = len(array) - 1
    
    while lower_index <= upper_index:
        mid_index = lower_index + ( upper_index - lower_index ) //2
        value = array[mid_index]
        
        if value == target:
            return mid_index
        elif value < target:
            lower_index = mid_index + 1
        else:
            upper_index = mid_index - 1
    return False
