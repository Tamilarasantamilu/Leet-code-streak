class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        count = 0
        n = len(nums)
        for mask in range(1 << n):
            subset_or = 0
            for i in range(n):
                if mask & (1 << i):
                    subset_or |= nums[i]
            if subset_or == max_or:
                count += 1
        
        return count
