class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        missing = 0 
        pos = 0    
        for i in range(len(nums)):
            if nums[i]>0:
                if not pos and nums[i]>1: 
                    return 1
                pos = 1
                if (i!=len(nums)-1) and (nums[i+1] - nums[i] > 1):
                    missing = nums[i] + 1
                    return missing       
        if missing == 0 and pos:
            return nums[-1] + 1
        else:
            return 1
