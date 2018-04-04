
class SpecialStack():
    
    __init__(self, arr, n, capacity):
        self.min_element = None
        self.max_capacity = capacity
        self.size = 0
        self.arr = []
        self.current_mins = [] # if you want to track the minimum element
        
        if n > self.capacity:
            raise IndexError("your array has more elements than this stack's capacity")
        else:
            for x in arr:
                push(arr, x)
        

    # Your task is to complete all these function's
    # function should append an element on to the stack
    def push(arr, ele):
        if isFull
    # Function should pop an element from stack
    def pop(arr):
        # Code here
    # function should return 1/0 or True/False
    def isFull(n, arr):
        # Code here
    # function should return 1/0 or True/False
    def isEmpty(arr):
        #Code here
    # function should return minimum element from the stack
    def getMin(n, arr):
        # Code here
