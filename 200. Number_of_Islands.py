from typing import List

class Solution:
    
    def islandCheck(self,i,j,grid):
      grid[i][j] = "X"
      up = i-1
      down = i+1
      right = j+1
      left = j-1
      if up>=0:
        if grid[up][j] == "1":
          self.islandCheck(up,j,grid)
      if down<len(grid):
        if grid[down][j] == "1":
          self.islandCheck(down,j,grid)
      if right<len(grid[i]):
        if grid[i][right] == "1":
          self.islandCheck(i,right,grid)
      if left>=0:
        if grid[i][left] == "1":
            self.islandCheck(i,left,grid)
      return

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i,row in enumerate(grid):
            for j, element in enumerate(row):
              if grid[i][j] =="1":
                self.islandCheck(i,j,grid)
                islands = islands+1

        return islands

grid = [["1"]]
ob = Solution()
print(ob.numIslands(grid))
