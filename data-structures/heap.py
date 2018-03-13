class BinHeap:
    def __init__(self):
        self.heapList = [0]     # Initialize with 0 to help with a division function (later)
        self.currentSize = 0    # The size of the heap (# items)
    
    # Takes item at i and "percolates it up", repeatedly switching it with it's parent until it is larger than it's parent
    def percUp(self,i):
        while i // 2 > 0:                                   # While there are parent nodes above
            if self.heapList[i] < self.heapList[i // 2]:    # If the parent is smaller than the child then swap
               tmp = self.heapList[i // 2]
               self.heapList[i // 2] = self.heapList[i]
               self.heapList[i] = tmp
            i = i // 2                                      # Update position of percolating node
      
    # Add an item at 0 and then percolate it up
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
        
    # Takes item at i and "percolates it down", repeatedly switching it with a child until it is larger than it's parent
    def percDown(self,i):
        while (i * 2) <= self.currentSize:              # Only runs while there is at least one child
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    # Return the minimum child
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:       # If there is no child on the right, return the index of the left child
            return i * 2
        else:                                  # Otherwise return the smaller child
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    # Delete the top value (which is the min value) by...
    # Placing the last value where the top value is and percolating it down
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    
    
    # This function will build a heap from a list in O(n) operations
    # Note that if you inserted items one by one it would take O(n log n) operations
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]      # Create unordered heap equal to list
        while (i > 0):                      # Starting from the second last layer, percolate down and repeat for all higher layers
            self.percDown(i)
            i = i - 1
