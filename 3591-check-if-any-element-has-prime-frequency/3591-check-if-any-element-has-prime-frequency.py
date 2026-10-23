from collections import Counter
class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maap=Counter(nums)
        for count in maap.values():
            if count>1:
                prime=True
                for i in range(2,count):
                    if count%i==0:
                        prime=False
                        break
                if prime:
                    return True
        return False
