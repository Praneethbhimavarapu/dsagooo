class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxel=nums[0]
        k=0
        for i in range(1,len(nums)):
            if maxel<nums[i]:
                k=i
                maxel=nums[i]
        return k