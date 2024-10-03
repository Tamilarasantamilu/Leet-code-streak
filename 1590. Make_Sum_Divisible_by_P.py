class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p
        if target == 0:
            return 0
        prefix_mod = {0: -1} 
        prefix_sum = 0
        min_length = float('inf')
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            desired_prefix = (prefix_sum - target) % p
            if desired_prefix in prefix_mod:
                min_length = min(min_length, i - prefix_mod[desired_prefix])
            prefix_mod[prefix_sum] = i
        return min_length if min_length != float('inf') and min_length != len(nums) else -1
