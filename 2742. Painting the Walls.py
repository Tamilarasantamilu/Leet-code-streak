class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        C = len(cost)
        dp = [inf]* C  + [0]
        
        for row in range(C - 1, -1, -1):
            new_dp = [0] * (C + 1)
            for col in range(C - 1, -1, -1):
                painter = cost[row] +( dp[col + time[row] + 1] if col + time[row] < C else 0)
                new_dp[col] = min(dp[col], painter)
            dp = new_dp
        return dp[0]
