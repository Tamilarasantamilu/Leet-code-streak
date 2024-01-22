class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        a=sum(nums)
        b=sum(set(nums))
        s=n*(n+1)//2
        return [a-b,s-b]
