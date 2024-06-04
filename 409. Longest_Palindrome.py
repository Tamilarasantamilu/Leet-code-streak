class Solution:
    def longestPalindrome(self, s: str) -> int:
        num = Counter(s)
        si = 0
        do = 0
        for key, val in num.items():
            if val % 2 == 0:
                do += val
            elif val > 1 and val % 2 == 1:
                do += val - 1
                si += 1
            elif val == 1:
                si += 1

        if si:
            do += 1

        return do
