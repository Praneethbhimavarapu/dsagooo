class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resultList=[]
        tempList=[]
        def backtrack():
            if len(tempList)==len(nums):
             resultList.append(tempList[:])
             return
            for number in nums:
                if number in tempList:
                    continue
                else:
                    tempList.append(number)
                    backtrack()
                    tempList.pop()
        backtrack()
        return resultList
            