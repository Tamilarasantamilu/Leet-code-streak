class Solution:
    def countSquares(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        totalSquares = sum(grid[0])
        
        for row in range(1, rows):
            totalSquares += grid[row][0]
            for col in range(1, cols):
                if grid[row][col]:
                    grid[row][col] += min(grid[row-1][col-1], grid[row][col-1], grid[row-1][col])
                    totalSquares += grid[row][col]
        
        return totalSquares
