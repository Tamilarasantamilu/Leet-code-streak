class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0

        maxi = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            ops = (nums[i] - 1) // maxi
            ans += ops
            maxi = nums[i] // (ops + 1)

        return ans