from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Calculate the sums of all subarrays of size k
        n = len(nums)
        window_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sum[0] = current_sum
        
        for i in range(1, len(window_sum)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = current_sum
        
        # Step 2: Compute left and right arrays
        left = [0] * len(window_sum)
        best_left = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best_left]:
                best_left = i
            left[i] = best_left
        
        right = [0] * len(window_sum)
        best_right = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best_right]:
                best_right = i
            right[i] = best_right
        
        # Step 3: Find the best middle subarray
        max_sum = 0
        result = []
        for j in range(k, len(window_sum) - k):
            i, l = left[j - k], right[j + k]
            total = window_sum[i] + window_sum[j] + window_sum[l]
            if total > max_sum:
                max_sum = total
                result = [i, j, l]
        
        return result
