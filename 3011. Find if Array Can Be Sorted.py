class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if sorted(nums) == nums:
            return True

        k, l = 0, 1
        res = []
        while(l < len(nums)):
            if bin(nums[k])[2:].count("1") != bin(nums[l])[2:].count("1"):
                res += sorted(nums[k:l])
                k = l
            l += 1
        res += sorted(nums[k:l])
        return res == sorted(nums)
