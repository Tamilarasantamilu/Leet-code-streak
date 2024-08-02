class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        if ones == 0 or ones == n:
            return 0
        
        nums = nums + nums
        max_ones = curr_ones = sum(nums[:ones])
        
        for i in range(ones, len(nums)):
            curr_ones += nums[i] - nums[i - ones]
            max_ones = max(max_ones, curr_ones)
        
        return ones - max_ones
