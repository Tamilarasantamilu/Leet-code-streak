class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def get_bitmask(word):
            if len(set(word)) != len(word): return 0
            res = 0
            for char in word:
                res |= 1 << (ord(char) - ord('a'))
            return res
        masks = set()
        for word in arr:
            mask = get_bitmask(word)
            if mask:
                masks.add(mask)
        masks = list(masks)
        res = 0
        def backtrack(idx, mask):
            if idx == len(masks):
                nonlocal res
                res = max(res, mask.bit_count())
                return
            backtrack(idx + 1, mask)
            if mask & masks[idx] == 0:
                backtrack(idx + 1, mask | masks[idx])
        backtrack(0,0)
        return res
