class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0: -1}
        length = 0
        val = 0
        for i, num in enumerate(nums):
            if num == 1:
                val += 1
            else:
                val -= 1
            if val in lookup:
                length = max(length, i - lookup[val])
            else:
                lookup[val] = i
        return length
