class Solution:
    def integerBreak(self, n: int) -> int:
        visited = {}
        def dp(number, broken):
            if number == 1:
                return 1
            if number in visited:
                return visited[number]
            res = 0
            if broken:
                res = number
            for i in range(1, number):
                res = max(res, i * dp(number - i, True))
            visited[number] = res
            return res
        return dp(n, False)
        
