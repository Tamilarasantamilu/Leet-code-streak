class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a DP array initialized to 0
        dp = [0] * (days[-1] + 1)
        
        # Convert travel days to a set for fast lookup
        days = set(days)

        # Compute the minimum cost for each day
        for d in range(len(dp)):
            # If it's a travel day
            if d in days: 
                dp[d] = min(
                dp[max(d-1, 0)] + costs[0], 
                dp[max(d-7, 0)] + costs[1], 
                dp[max(d-30, 0)] + costs[2]
            )
            # If it's not a travel day, cost remains the same as the previous day
            else:
                dp[d] = dp[d-1]
        return dp[-1]
