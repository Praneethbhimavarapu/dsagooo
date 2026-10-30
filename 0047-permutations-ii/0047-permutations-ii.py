class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resultList=[]
        tempList=[]
        freq={}
        for item in nums:
            freq[item] = freq.get(item, 0) + 1
        def backtrack():
            if len(tempList)==len(nums):
             resultList.append(tempList[:])
             return
            for number in freq:
                if freq[number]==0:
                    continue
                else:
                    tempList.append(number)
                    freq[number]-=1
                    backtrack()
                    tempList.pop()
                    freq[number]+=1
        backtrack()
        return resultList