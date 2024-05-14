
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0

        def greedy(x, y):
            # Base case: if not valid or already visited, return 0
            if not is_valid(x, y):
                return 0
            
            # Mark the current cell as visited
            gold = grid[x][y]
            original = gold
            grid[x][y] = 0
            
            # Explore all four directions
            max_gold = 0
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                max_gold = max(max_gold, greedy(new_x, new_y))
            
            # Restore the original value before returning
            grid[x][y] = original
            return gold + max_gold

        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, greedy(i, j))
        
        return max_gold
