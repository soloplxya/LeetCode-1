import math 

class Solution(object):
    def searchInsert(self, array, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.recursiveMutatedBinarySearch(array, target, 0, len(array)-1)
        
    def recursiveMutatedBinarySearch(self, array, target, start, end):
        mid = int(start + (end-start)/2)
        if end >= start: 
            if array[mid] == target: 
                return mid      
            if array[mid] > target: 
                return self.recursiveMutatedBinarySearch(array, target, start, mid - 1)
            if array[mid] < target: 
                return self.recursiveMutatedBinarySearch(array, target, mid + 1, end)
        else: 
            # not found 
            if array[mid] < target:
                return mid + 1 
            else: 
                return mid - 1 if mid > 0 else 0