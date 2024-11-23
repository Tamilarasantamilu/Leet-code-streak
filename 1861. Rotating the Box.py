from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Step 1: Apply gravity to each row
        for row in box:
            n = len(row)
            empty_pos = n - 1  # Start with the rightmost position
            for i in range(n - 1, -1, -1):
                if row[i] == '*':  # Obstacle
                    empty_pos = i - 1
                elif row[i] == '#':  # Stone
                    row[i], row[empty_pos] = row[empty_pos], row[i]
                    empty_pos -= 1

        # Step 2: Rotate the matrix 90 degrees clockwise
        m, n = len(box), len(box[0])
        rotated_box = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]
        
        return rotated_box
