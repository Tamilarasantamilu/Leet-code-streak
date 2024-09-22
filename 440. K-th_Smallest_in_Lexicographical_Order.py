class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            step = 0
            first = current
            last = current + 1
            while first <= n:
                step += min(n + 1, last) - first
                first *= 10
                last *= 10

            if k >= step:
                current += 1
                k -= step
            else:
                current *= 10
                k -= 1

        return current
