class Solution:
    def minimumLength(self, s: str) -> int:
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                char = s[l]
                while l <= r and s[l] == char:
                    l += 1
                while r >= l and s[r] == char:
                    r -= 1
            else:
                return r - l + 1
        return 0 if l > r else 1
