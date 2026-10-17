class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(target)}
        visited = [False] * len(nums)
        swaps = 0
        for i in range(len(nums)):
            if visited[i]:
                continue
            j = i
            cycle = 0
            while not visited[j]:
                visited[j] = True
                cycle += 1
                j = pos[nums[j]]
            swaps += cycle - 1
        return swaps        
            