class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        ansp=1
        ans=0
        while n>0:
            k=n%10
            n=n//10
            ansp*=k
            ans+=k
        return ansp-ans