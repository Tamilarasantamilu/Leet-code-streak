class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n= len(matrix)
        if n==1:
            return matrix[0][0]

        dp = [[0] * n for _ in range(n)]

        dp[0]= matrix[0]

        for i in range(1, n):
            for j in range(0, n):
                l=j if j==0 else j-1
                r=j+1 if j==n-1 else j+2
                dp[i][j] = min(dp[i-1][l:r]) + matrix[i][j]

        print(dp)
        return min(dp[-1])

      
