class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_tbl = collections.Counter(s)
        for idx, c in enumerate(s):
            if hash_tbl[c] == 1:
                return idx
        return -1
