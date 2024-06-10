class Solution:
    def heightChecker(self, heights):
        n = len(heights)
        arr = sorted(heights)
        count = 0
        for i in range(n):
            if arr[i] == heights[i]:
                continue
            else:
                count += 1
        return count
