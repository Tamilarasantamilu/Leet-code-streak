class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            h_left, h_right = height[i], height[j]
            width = j - i
            area = min(h_left, h_right) * width
            max_area = max(max_area, area)
            if h_left > h_right:
                j -= 1
            else:
                i += 1
        return max_area
