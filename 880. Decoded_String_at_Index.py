class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for i, c in enumerate(s):
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
            if k <= size:
                break
        for c in s[i::-1]:
            if c.isdigit():
                size /= int(c)
                k %= size
            else:
                if k % size == 0:
                    return c
                size -= 1
        
