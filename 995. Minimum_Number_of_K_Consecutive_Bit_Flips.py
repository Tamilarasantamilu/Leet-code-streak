from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = [0] * n
        flip_count = 0
        result = 0
        
        for i in range(n):
            if i >= k:
                flip_count ^= flip[i - k]
            if nums[i] ^ flip_count == 0:
                if i + k > n:
                    return -1
                flip_count ^= 1
                flip[i] = 1
                result += 1
        
        return result

# Example usage:
# sol = Solution()
# print(sol.minKBitFlips([0,1,0], 1)) # Output: 2
# print(sol.minKBitFlips([1,1,0], 2)) # Output: -1
# print(sol.minKBitFlips([0,0,0,1,0,1,1,0], 3)) # Output: 3
