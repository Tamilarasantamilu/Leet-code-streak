class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        nums = [nums[i:i+3] for i in range(0,n,3)]
        for i in range(len(nums)):
            if max(nums[i])-min(nums[i])>k:
                return []
        return nums
