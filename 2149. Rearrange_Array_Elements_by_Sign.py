from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        result = []
        
        # Separate positive and negative integers
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        
        # Iterate through both lists alternatively and append to result
        for i in range(len(nums) // 2):
            p = positive.pop(0)
            result.append(p)
            n = negative.pop(0)
            result.append(n)
        
        return result
