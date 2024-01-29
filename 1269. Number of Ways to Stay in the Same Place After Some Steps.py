class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        
        # To avoid accessing indices out of bounds, we limit the range of `arrLen`.
        maxLen = min(steps//2 + 1, arrLen)
        
        # Initialize a 2D array with all zeros.
        dp = [[0] * maxLen for _ in range(steps+1)]
        
        # Base case: If steps is 0, there's only one way to be at index 0.
        dp[0][0] = 1
        
        for i in range(1, steps+1):
            for j in range(maxLen):
                # Stay in the same position
                dp[i][j] = dp[i-1][j]
                
               
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
                
                # Move one step to the right
                if j < maxLen - 1:
                    dp[i][j] += dp[i-1][j+1]
                
                dp[i][j] %= MOD
        
        return dp[steps][0]
