from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # Create a 2D grid where each cell represents a 3x3 block of the original cell
        expanded_grid = [[0] * (n * 3) for _ in range(n * 3)]
        
        # Fill the expanded grid based on the slashes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    # Add slashes in the expanded grid
                    expanded_grid[i * 3][j * 3 + 2] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    # Add backslashes in the expanded grid
                    expanded_grid[i * 3][j * 3] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3 + 2] = 1
        
        def bfs(start_i, start_j):
            # BFS to mark all cells in the same region
            queue = [(start_i, start_j)]
            expanded_grid[start_i][start_j] = 2  # Mark as visited
            while queue:
                x, y = queue.pop(0)
                # Explore all 4 directions
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n * 3 and 0 <= ny < n * 3 and expanded_grid[nx][ny] == 0:
                        # Check if the movement is blocked by a slash or backslash
                        if (dx == -1 and expanded_grid[x - 1][y] == 0) or \
                           (dx == 1 and expanded_grid[x + 1][y] == 0) or \
                           (dy == -1 and expanded_grid[x][y - 1] == 0) or \
                           (dy == 1 and expanded_grid[x][y + 1] == 0):
                            queue.append((nx, ny))
                            expanded_grid[nx][ny] = 2  # Mark as visited
        
        # Count regions using BFS
        regions = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if expanded_grid[i][j] == 0:
                    bfs(i, j)
                    regions += 1
        
        return regions
