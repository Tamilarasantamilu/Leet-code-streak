class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for left in range(n):
            sums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    sums[i] += matrix[i][right]
                d = {0: 1}
                curr_sum, cnt = 0, 0
                for s in sums:
                    curr_sum += s
                    if curr_sum - target in d:
                        cnt += d[curr_sum - target]
                    if curr_sum not in d:
                        d[curr_sum] = 0
                    d[curr_sum] += 1
                res += cnt
        return res
