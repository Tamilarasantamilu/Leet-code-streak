from collections import Counter
from itertools import accumulate
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Calculate remainders of subarray sums modulo k
        remainders = [0]  # Initialize with count of subarrays with sum divisible by k (remainder 0)
        res = 0

        # Perform prefix sum calculation and calculate remainders
        for num in accumulate(nums):
            remainder = num % k
            remainders.append(remainder)

        # Count combinations of subarrays with the same remainder
        for val in Counter(remainders).values():
            res += (val * (val - 1)) // 2

        return res
