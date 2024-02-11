class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * m for _ in range(m)] for _ in range(n)]
        
        # Initialize the DP array for the last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n - 1][j1][j2] = grid[n - 1][j1]
                else:
                    dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]
        
        # Dynamic Programming
        for i in range(n - 2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float('-inf')
                    
                    # Inner loops for 9 possible moves
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ans = 0
                            if j1 == j2:
                                ans = grid[i][j1]
                            else:
                                ans = grid[i][j1] + grid[i][j2]
                            
                            # Check if the move is valid
                            if j1 + di < 0 or j1 + di >= m or j2 + dj < 0 or j2 + dj >= m:
                                ans += float('-inf') # Invalid move
                            else:
                                ans += dp[i + 1][j1 + di][j2 + dj] # Include the DP result from the next row
                            
                            maxi = max(ans, maxi) # Update maximum result
                    dp[i][j1][j2] = maxi # Store the maximum result for this state in the DP array
        
        # Return the maximum cherries collected
        return dp[0][0][m - 1]
