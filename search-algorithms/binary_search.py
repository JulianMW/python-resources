

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
