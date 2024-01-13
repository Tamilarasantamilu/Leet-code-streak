class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        for i in t:
            if freq[i]:
                freq[i] -= 1
        return sum(freq.values())
