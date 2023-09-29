class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        tone = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if tone == -1:
                    return False
                tone = 1
            elif nums[i - 1] > nums[i]:
                if tone == 1:
                    return False
                tone = - 1
        return True
        
