class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        num_elements = len(nums)
        if num_elements == 1:
            if nums[0] == target:
                return [0,0]
        
        return [self.binaryRangeSearchLeft(nums, target, 0, num_elements-1),
                self.binaryRangeSearchRight(nums, target, 0, num_elements-1)]
        
    def binaryRangeSearchLeft(self, nums, target, l, r):
        if l <= r:
            
            midpoint = l + (r - l)//2
            
            if nums[0] == target:
                return 0
            
            # if we've found our index, return it
            if midpoint > 0 and nums[midpoint] == target and nums[midpoint-1] < target:
                return midpoint
            
            # condition for searching right half next
            if nums[midpoint] < target:
                return self.binaryRangeSearchLeft(nums, target, midpoint+1, r)
            
            # condition for searching left half next
            if nums[midpoint] > target or (nums[midpoint] == target and nums[midpoint-1] == target):
                return self.binaryRangeSearchLeft(nums, target, l, midpoint-1)
            
            
        else:
            return -1
        
        
    def binaryRangeSearchRight(self, nums, target, l, r):
        if l <= r:
            
            midpoint = l + (r - l)//2
            
            if midpoint == len(nums) - 1:
                if nums[-1] == target:
                    return len(nums) - 1
                else:
                    return -1
            
            # if we've found our index, return it
            if nums[midpoint] == target and nums[midpoint+1] > target:
                return midpoint
            
            # condition for searching right half next
            if nums[midpoint] < target or (nums[midpoint] == target and nums[midpoint+1] == target):
                return self.binaryRangeSearchRight(nums, target, midpoint+1, r)
            
            # condition for searching left half next
            if nums[midpoint] > target:
                return self.binaryRangeSearchRight(nums, target, l, midpoint-1)
            
        else:
            return -1
