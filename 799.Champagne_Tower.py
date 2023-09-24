class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        q = [poured]
        for r in range(query_row):
            q2 = [0] * (len(q) + 1)
            for i, amount in enumerate(q):
                if amount <= 1:
                    continue
                tmp = (amount - 1) / 2
                q2[i] += tmp
                q2[i + 1] += tmp
            q = q2
        return min(q[query_glass], 1)
