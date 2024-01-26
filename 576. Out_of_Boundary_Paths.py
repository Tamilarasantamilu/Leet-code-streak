class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 1000000007
        dp = dict()
        def memo(i,j,move):
            if move<0:
                return 0
            if i<0 or j<0 or i>=m or j>=n:
                #you just kicked the ball out of the court!!
                return 1
            #check cache
            if (i,j,move) in dp:
                return dp[(i,j,move)]
            #find all the ways and add them. 
            ways = (memo(i-1,j,move-1)+memo(i,j-1,move-1)+memo(i+1,j,move-1)+memo(i,j+1,move-1))%mod
            #update cache.
            dp[(i,j,move)] = ways
            return dp[(i,j,move)]
        
        return memo(startRow,startColumn,maxMove)
