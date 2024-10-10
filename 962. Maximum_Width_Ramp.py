class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Step 1: Build a decreasing stack of indices
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        max_width = 0
        # Step 2: Traverse the array from the end
        for j in range(len(nums) - 1, -1, -1):
            # While the current element can form a valid ramp
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width
