class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder = {0: -1}  
        cur = 0 
        for i, n in enumerate(nums): 
            cur += n 
            r = cur % k 
            if r not in reminder: 
                reminder[r] = i 
            elif r in reminder and i - reminder[r] >= 2: 
                return True 
        return False 
