class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            eve=0
            k=nums[i]
            while k!=0:
                k=k//10
                eve+=1
            if eve%2==0:
                count+=1
        return count
