class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=min(nums)
        total=sum(nums)
        return total-len(nums)*mini
        