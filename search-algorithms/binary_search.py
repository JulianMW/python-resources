

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:     # exit when our indicies cross
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # exit if x (our midpoint) == lower
                break        # because no further iterations will make lower == upper
            lower = x
        elif target < val:
            upper = x
