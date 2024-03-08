class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        freq, count = 0, 0
        for value in c.values():
            freq = max(freq, value)

        for key, value in c.items():
            if value == freq:
                count += value
        
        return count
