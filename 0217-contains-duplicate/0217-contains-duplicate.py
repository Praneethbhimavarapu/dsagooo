class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k={}
        for i in nums:
             k[i] = k.get(i, 0) + 1
        for key in k:
            if k[key]>1:
                return True
                break
        return False