from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def largestRectangleArea(heights: List[int]) -> int:
            stack = []  # Stack to store indices of increasing heights
            max_area = 0
            heights.append(0)  # Append a sentinel value at the end

            for i, h in enumerate(heights):
                # If current height is less than the previous height
                while stack and h < heights[stack[-1]]:
                    # Calculate area for the popped height
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)  # Add the current index to the stack

            return max_area

        max_area = 0
        heights = [0] * len(matrix[0])  # Initialize heights array with 0s

        for row in matrix:
            # Update heights array for each row
            for i, val in enumerate(row):
                heights[i] = heights[i] + 1 if val == "1" else 0
            # Calculate maximal rectangle area for the updated heights
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
