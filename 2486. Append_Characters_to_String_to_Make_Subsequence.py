class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j != len(t):
            count = len(t[j:])
        return count
        
