class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        solution =[-1,-1];
        start = 0
        end = len(A)-1
        while start<end:
            midpoint = (start + end )/2
            if A[midpoint] == target:
                end = midpoint
            elif A[midpoint] < target:
                start = midpoint+1
            else:
                end = midpoint -1
        if A[start]!= target:
            return solution
        solution[0] = start
        end = len(A)-1
        while start<end:
            midpoint = (start + end +1)/2
            if A[midpoint] == target:
                start = midpoint
            else:
                end = midpoint -1
        solution[1] = start
        return solution
