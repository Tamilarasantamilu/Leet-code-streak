class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        if m < n:
            return False

        idx2 = 0
        for idx1 in range(m):
            temp1 = ord(str1[idx1])
            temp2 = ord(str2[idx2]) if idx2 < n else 0
            if idx2 < n and (temp1 == temp2 or
                             temp1 + 1 == temp2 or
                             temp1 - 25 == temp2):
                idx2 += 1

        return idx2 == n
