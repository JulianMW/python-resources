def _partition(arr, l, r):
    
    pivot = arr[r]
    
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i = i+1
            arr[j], arr[i] = arr[i], arr[j]
            
    
    i = i + 1
    arr[i], arr[r] = arr[r], arr[i]
    
    return i
        
    
    
def _quick_sort(arr, l, r):
    
    if l < r:
        
        pivot = _partition(arr, l, r)
        
        _quick_sort(arr, l, pivot - 1)
        _quick_sort(arr, pivot + 1, r)
        
        
def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)
    
quick_sort(to_sort)
to_sort
