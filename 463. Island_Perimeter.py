class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        ans = 0
        for row in range(0,h):  
            for col in range(0,w): 
                if grid[row][col]==1:
                    if row == 0 or grid [row-1][col]==0:
                        ans += 1
                    if row == h-1 or grid [row+1][col]==0:
                        ans += 1
                    if col == 0 or grid [row][col-1]==0:
                        ans += 1
                    if col ==w-1  or grid [row][col+1]==0:
                        ans += 1
        return ans
