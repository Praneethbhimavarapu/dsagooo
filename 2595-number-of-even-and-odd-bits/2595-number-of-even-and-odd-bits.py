class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        even = 0
        odd = 0
        i = 0

        while n > 0:
            if n % 2 == 1:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1

            n //= 2
            i += 1

        return [even, odd]