class Solution:
    def tribonacci(self, n: int) -> int:

        dp  = []


        for i in range(n+1):

            if i==0:
                dp.append(0)
            elif i==1:
                dp.append(1)
            elif i==2:
                dp.append(1)

            else:
                current = dp[i-3] + dp[i-2] + dp[i-1]
                dp.append(current)

        return dp[-1]         
