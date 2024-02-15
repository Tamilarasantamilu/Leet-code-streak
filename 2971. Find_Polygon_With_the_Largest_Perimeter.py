class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        j = n-1

        while(sum(nums[:j]) <= nums[j] and j>=0):
            j -= 1
        
        if sum(nums[:j]) > nums[j]:
            return sum(nums[:j+1])
        else:
            return -1
