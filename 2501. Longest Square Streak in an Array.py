class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            streak_length = 1
            current = num

            while current in num_set:
                current = current ** 2
                if current in num_set:
                    streak_length += 1

            if streak_length >= 2:
                longest_streak = max(longest_streak, streak_length)

        return longest_streak if longest_streak >= 2 else -1
