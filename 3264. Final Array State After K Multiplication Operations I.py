class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mini = nums.index(min(nums))
            nums[mini] *= multiplier
        return nums
