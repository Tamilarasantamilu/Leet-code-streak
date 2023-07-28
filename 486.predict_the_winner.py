class Pair:
    def __init__(self):
        self.fir = 0
        self.sec = 0

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[Pair() for i in range(n)] for _ in range(n)]

        # Base case
        for i in range(n):
            dp[i][i].fir = nums[i]
            dp[i][i].sec = 0
        
        # State transition
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                left_res = nums[i] + dp[i+1][j].sec
                right_res = nums[j] + dp[i][j-1].sec
                if left_res > right_res:
                    dp[i][j].fir = left_res
                    dp[i][j].sec = dp[i+1][j].fir
                else:
                    dp[i][j].fir = right_res
                    dp[i][j].sec = dp[i][j-1].fir
        
        return dp[0][n-1].fir >= dp[0][n-1].sec