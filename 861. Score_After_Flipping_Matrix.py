class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        #flip rows
        for r in range(rows):
            if grid[r][0]==0:
                for c in range(cols):
                    grid[r][c]=0 if grid[r][c] else 1
        #flip cols
        for c in range(cols):
            onescount=0
            for r in range(rows):
                onescount+=grid[r][c]
            if onescount<rows-onescount:
                for r in range(rows):
                    grid[r][c]=0 if grid[r][c] else 1
        
        res=0
        for r in range(rows):
            for c in range(cols):
                res+=grid[r][c]<<(cols-c-1)
        return res
