class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = max(nums)
            if -a in nums:
                return a
            else:
                nums.remove(a)
        return -1
