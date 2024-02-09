class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Sort the input array
        nums.sort()

        # Initialize two arrays: dp to store the length of the largest subset ending at each index,
        # and prev to store the previous index in the largest subset ending at each index.
        dp = [1] * len(nums)
        prev = [-1] * len(nums)

        # Iterate through the array
        for i in range(1, len(nums)):
            for j in range(i):
                # Check if nums[i] is divisible by nums[j]
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # Find the index of the maximum value in dp
        max_index = dp.index(max(dp))

        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result[::-1]
