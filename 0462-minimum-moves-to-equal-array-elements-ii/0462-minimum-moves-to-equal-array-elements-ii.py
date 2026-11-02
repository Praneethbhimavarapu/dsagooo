class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median=nums[len(nums)//2]
        move=0
        for num in nums:
            move+=abs(num-median)
        return move