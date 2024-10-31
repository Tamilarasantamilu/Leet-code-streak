class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories based on positions
        robot.sort()
        factory.sort()
        
        num_robots = len(robot)
        num_factories = len(factory)
        
        # Initialize the DP table with infinity
        dp = [[float('inf')] * (num_robots + 1) for _ in range(num_factories + 1)]
        dp[0][0] = 0  # No robots, no factories, no cost
        
        # Populate the DP table
        for i in range(1, num_factories + 1):
            pos, limit = factory[i - 1]
            
            for j in range(num_robots + 1):
                # Case when we don't use the current factory
                dp[i][j] = dp[i - 1][j]
                
                # Try assigning up to `limit` robots to this factory
                total_dist = 0
                for k in range(1, min(j, limit) + 1):
                    total_dist += abs(robot[j - k] - pos)
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + total_dist)
                    
        return dp[num_factories][num_robots]
            
