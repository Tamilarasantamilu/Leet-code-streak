class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set(s)
        count = 0
        for char in chars:
            left, right = s.index(char), s.rindex(char)
            inBetween = set()
            for k in range(left+1, right):
                inBetween.add(s[k])
            count += len(inBetween)
        return count
