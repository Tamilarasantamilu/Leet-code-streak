class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False

        for i in range(m):
            if target <= matrix[i][-1]:
                break

        return target in matrix[i]