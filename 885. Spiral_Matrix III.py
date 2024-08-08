class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        directions = [
            (0, 1),  # EAST
            (1, 0),  # SOUTH
            (0, -1), # WEST
            (-1, 0)  # NORTH
        ]
        
        result = [[rStart, cStart]]
        step = 0
        dir = 0
        
        while len(result) < rows * cols:
            if dir == 0 or dir == 2:
                step += 1
            
            for _ in range(step):
                rStart += directions[dir][0]
                cStart += directions[dir][1]
                
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
            
            dir = (dir + 1) % 4
        
        return result
