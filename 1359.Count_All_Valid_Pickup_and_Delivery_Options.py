class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 1
        for i in range(1, n + 1):
            res *= i *((i - 1) * 2 + 1)
            res %= MOD
        return res