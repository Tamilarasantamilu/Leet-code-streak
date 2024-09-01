class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        result = []
        for i in range(m):
            # Append a row to the result array
            result.append(original[i * n : (i + 1) * n])
        return result
            
