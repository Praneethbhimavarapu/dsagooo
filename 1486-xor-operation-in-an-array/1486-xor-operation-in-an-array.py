class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        result = 0

        for i in range(n):
            num = start + 2 * i
            result=result^(num)

        return result        