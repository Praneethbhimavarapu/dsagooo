class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        mapp={}
        for i in nums:
            count+=mapp.get(i,0)
            mapp[i]=mapp.get(i,0)+1
        return count
