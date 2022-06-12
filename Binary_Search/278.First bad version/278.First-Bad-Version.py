# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n versions starting from 1 to n     
        if (n < 2): 
            return n 
        start = 1
        end = n
        while (start<=end):
            mid = int(start + (end-start)/2)
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif (isBadVersion(mid)):
                end = mid-1
            else: 
                start = mid + 1 

