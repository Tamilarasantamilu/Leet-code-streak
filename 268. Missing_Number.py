class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in range(n+1):
            if i not in nums:
                res.append(i)
        return res[0]
